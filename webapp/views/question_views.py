from .req import *

class QuestionApi(APIView):
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]

    def get(self, request,id=None, format=None):
        if id == None:
            question_data = Question.objects.all()
            serializer = QuestionSerializer(question_data,many=True)
        else:
            question_data = Question.objects.get(id=id)
            serializer=QuestionSerializer(question_data)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Question Created'},status=status.HTTP_201_CREATED)
        return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


