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

    def post(self,request,format=None):
        
        table = "SELECT *,q.id as id,qm.id as qm_id FROM webapp_question as q LEFT JOIN webapp_question_user_mark as qm ON q.id=qm.question_id"
        query_str = f" WHERE (user_id = {self.request.user.id} OR user_id IS NULL)"
        for query in request.data:
            if query!="search":
                query_str += f" AND {query} = {request.data[query]}"

            else:
                for search in request.data[query]:
                    query_str+=f" AND {search} LIKE '%{request.data[query][search]}%'"   

        cursor = connection.cursor()
        try:
        
            cursor.execute(table+query_str)
            result = self.__dictfetchall(cursor)
            cursor.close()
            return Response({
                "length":len(result),
                "questions":result
            })
        except:
            cursor.close()
            return Response({
                "msg":"error occured"
            })

        # error handling
