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

    def get(self,request,page_number=1):
        # each page will hold 10 questions
        start_id = 10*(page_number-1) + 1 # lets say page_number == 2 then start_id = 11
        table = f"SELECT q.*,t.name,qm.mark FROM webapp_question as q JOIN webapp_topic as t ON q.topic_id = t.id LEFT JOIN webapp_question_user_mark as qm ON qm.question_id = q.id WHERE q.id >= %s AND q.id <= %s AND (qm.user_id = %s OR qm.user_id IS NULL)"

        # return Response(start_id+9)
        cursor = connection.cursor()
        cursor.execute(table,[start_id,start_id+9,request.user.id])
        result = self.__dictfetchall(cursor)
        cursor.close()


        
        return Response({
            "length":len(result),
            "questions":result
        })
        # try:
        
        # except:
        #     cursor.close()
        #     return Response({
        #         "msg":"error occured"
        #     })

