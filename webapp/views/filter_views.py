from .req import *
from django.db import connection
# filter question level based
# class LevelFilterAPI(APIView):
#     # permission_classes = [AllowAny]
#     def get(self,request,level,format=None):
#         data = Question.objects.filter(level=level)
#         serializer = QuestionSerializer(data,many=True)
#         return Response(serializer.data)


# filter question on topic based
# class TopicFilterAPI(APIView):
#     # permission_classes = [AllowAny]
#     def get(self,request,topic_id,format=None):
#         data = Question.objects.filter(topic_id=topic_id)
#         serializer=QuestionSerializer(data,many=True)
#         return Response(serializer.data)

# search
# class QuestionSearchFilterAPI(APIView):
#     def get(self,request,query=None,format=None):
#         if query == None:
#             data = Question.objects.all()
#         else:
#             data = Question.objects.filter(name__contains=query)
#         serializer=QuestionSerializer(data,many=True)
#         return Response(serializer.data)

# filter question on status based
# class StatusFilterAPI(APIView):
#     def get(self,request,status,format=None):
#         data = Question_user_mark.objects.filter(mark=status,user_id=self.request.user.id)
#         serializer = QuestionUserMarkSerializer(data,many=True)
#         return Response(serializer.data)    

# class GeneralFilterAPI(APIView):
#     permission_classes = [AllowAny]
#     def post(self,request,format=None):
        
#         data = Question.objects.filter(**request.data)
#         serializer=QuestionSerializer(data,many=True)
#         return Response(serializer.data)



class GeneralFilterAPI(APIView):
    # permission_classes = [AllowAny]
    def __dictfetchall(self,cursor):
    # "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def helper(self,request,page_number=1,format=None):
        friends = Pair_programmer.objects.filter(user_1=request.user.id).select_related("user_2")

        sql_friends = ""
        for friend in friends[:len(friends)-1]:
            sql_friends += str(friend.user_2.id)+","
        sql_friends += str(friends[len(friends)-1].user_2.id)

         
        arguments = []
        select = (f"SELECT q.*,t.name as topic_name,qm.mark,(SELECT COUNT(*) FROM webapp_question_user_mark as qm WHERE qm.question_id = q.id AND qm.mark IN (0,1,2) AND user_id IN ({sql_friends})) AS friends")
        select_count = (f"SELECT COUNT(*)")
        
        table  = (" FROM webapp_question as q" 
                  " JOIN webapp_topic as t ON q.topic_id = t.id"
                  " LEFT JOIN webapp_question_user_mark as qm ON q.id=qm.question_id")
        
        query_str = f" WHERE (user_id = {request.user.id} OR user_id IS NULL)"
        for query in request.data:
            if query!="search":
                data = (request.data[query])
                if "null" in data:
                    arguments+= [d for d in data if d!="null"]
                    query_str += f" AND ({query} IN ({','.join(['%s'] * (len(data)-1))}) OR {query} IS NULL)"
                else:
                    arguments+=data
                    query_str += f" AND {query} IN ({','.join(['%s'] * len(data))})"
            else:
                for search in request.data[query]:
                    arguments.append(request.data[query][search])
                    query_str+=f" AND {search} LIKE '%%s%'"   
        try:
            cursor = connection.cursor()
            
            cursor.execute(select_count+table+query_str,arguments)
            result_count = cursor.fetchone()
            # result_count = self.__dictfetchall(cursor)

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
        except:
            return Response({
                "msg":"error occured"
            })

    def post(self,request,page_number=1,format=None):
        # get friends for current user
        return Response(self.helper(request,page_number,format))

        # error handling
