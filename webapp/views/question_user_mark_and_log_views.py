from enum import unique
from .req import *

class Log(APIView):
    serializer_class = MarkUpdateSerializer

    def maintainLog(self,data,format=None):
        # print(data.id,data.mark)
        data = ({"question_user_mark_id":data.id,"previous_mark":data.mark})
        serializer = MarkUpdateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(True)
        return Response(False)
        


class QuestionUserMarkAndLogApi(APIView):
    serializer_class = QuestionUserMarkSerializer
    

    # To-DO
    # unique constraint on combination of question_id and user_id in question_user_mark table

    # question id and user id can identify the question_mark uniquely
    def __patch(self,request,data,format=None):
        # user can update only his marks
        data_fetched = data.first()
        serializer=QuestionUserMarkSerializer(data.first(),data=request.data,partial=True)
        if serializer.is_valid():
            obj = Log()
            if obj.maintainLog(data_fetched):
                serializer.save()
                return Response({'msg':'Mark Patched'},status=status.HTTP_201_CREATED)
                

            # maintain record of previous marks
        return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    # if calling first time then it will create new mark else it will call patch internally and updates the previous record
    def post(self,request,format=None):
        if 'question_id' not in request.data:
            return Response({
                "question_id":["question_id is required field"]
            })

        data=Question_user_mark.objects.filter(question_id=request.data['question_id'],user_id=self.request.user.id)

        if data.exists():  # if marking the question first time
            return self.__patch(request,data)
        else:
            serializer = QuestionUserMarkSerializer(data=request.data)
            if serializer.is_valid():
                # user can only mark question for himself
                serializer.save(user_id=self.request.user)
                return Response({'msg':'Marked'},status=status.HTTP_201_CREATED)
            return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

