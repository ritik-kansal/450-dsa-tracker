from .req import *
from django.db import connection

class QuestionDataApi(APIView):
    def __dictfetchall(self,cursor):
    # "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def helper(self,request,page_number=1):
        friends = Pair_programmer.objects.filter(user_1=request.user.id).select_related("user_2")

        sql_friends = ""
        for friend in friends[:len(friends)-1]:
            sql_friends += str(friend.user_2.id)+","
        sql_friends += str(friends[len(friends)-1].user_2.id)

        # each page will hold 10 questions
        
        #can use string formating as sql_friends variable cant be altered
        select = (f"SELECT q.*,t.name as topic_name,qm.mark,(SELECT COUNT(*) FROM webapp_question_user_mark as qm WHERE qm.question_id = q.id AND qm.mark IN (0,1,2) AND user_id IN ({sql_friends})) AS friends" )
        select_count = "SELECT COUNT(*)"
        
        table = (" FROM webapp_question as q"
                 " JOIN webapp_topic as t ON q.topic_id = t.id" 
                 " LEFT JOIN webapp_question_user_mark as qm ON q.id = qm.question_id AND qm.user_id = %s" )
                #  " WHERE q.id >= %s AND q.id <= %s")
        query_str = " LIMIT 10 OFFSET %s"
        cursor = connection.cursor()
        try:
            cursor.execute(select_count+table,[request.user.id])
            result_count = cursor.fetchone()
            
            cursor.execute(select+table+query_str,[request.user.id,(page_number-1)*10])
            result = self.__dictfetchall(cursor)
            
            cursor.close()
            
            return {
                "length":len(result),
                "total_length":result_count[0],
                "questions":result,
            }
        
        except:
            cursor.close()
            return {
                "msg":"error occured"
            }

    def get(self,request,page_number=1):
        return Response(self.helper(request,page_number))

