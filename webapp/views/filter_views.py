from django.http import response
from .req import *
from django.db import connection

class GeneralFilterAPI(APIView):
    def __dictfetchall(self,cursor):
    # "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def helper(self,request,page_number=1,format=None):
        friends = Pair_programmer.objects.filter(user_1=request.user.id).select_related("user_2")

        friends = [str(friend.user_2.id) for friend in friends]
        if len(friends) == 0:
            friends.append('-1') # to avoid error with in keyword as friend is autoincrement value so -1 is as good as empty
        sql_friends = ",".join(friends)
         
        arguments = []
        select = (f"SELECT q.*,t.name as topic_name,qm.mark,(SELECT COUNT(*) FROM webapp_question_user_mark as qm WHERE qm.question_id = q.id AND qm.mark IN (0,1,2) AND user_id IN ({sql_friends})) AS friends")
        select_count = (f"SELECT COUNT(*)")
        
        table  = (" FROM webapp_question as q" 
                  " JOIN webapp_topic as t ON q.topic_id = t.id"
                  f" LEFT JOIN webapp_question_user_mark as qm ON q.id=qm.question_id AND user_id = {request.user.id}")
        
        query_str = f" WHERE (user_id = {request.user.id} OR user_id IS NULL)"
        for query in request.data:
            if query!="search":
                data = (request.data[query])
                if len(data) == 0 or (len(data)==1 and "null" in data):
                    data.append(-1)
                if "null" in data:
                    arguments+= [d for d in data if d!="null"]
                    query_str += f" AND ({query} IN ({','.join(['%s'] * (len(data)-1))}) OR {query} IS NULL)"
                else:
                    arguments+=data
                    query_str += f" AND {query} IN ({','.join(['%s'] * len(data))})"
            else:
                for search in request.data[query]:
                    # arguments.append(request.data[query][search])
                    query_str+=f" AND q.{search} LIKE '%%{request.data[query][search]}%%'"    
        try:
            cursor = connection.cursor()
            
            cursor.execute(select_count+table+query_str,arguments)
            result_count = cursor.fetchone()

            query_str+=" ORDER BY q.id LIMIT 10 OFFSET %s"
            arguments.append((page_number-1)*10)
            cursor.execute(select+table+query_str,arguments)
            result = self.__dictfetchall(cursor)            
            cursor.close()
            return {
                "length":len(result),
                "total_length":result_count[0],
                "questions":result
            }

        except Exception as e:
            return {"msg":str(e)}

    def post(self,request,page_number=1,format=None):
        response = self.helper(request,page_number,format)
        return Response(response)