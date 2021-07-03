from .req import *
class QuestionApi(APIView):
    serializer_class = QuestionSerializer

    def get(self,request,id=None):
        if id==None:
            question_data = Question.objects.all()
            serializer = QuestionSerializer(question_data,many = True)
            return Response(serializer.data)
        else:
            question_data = Question.objects.get(id=id)
            serializer = QuestionSerializer(question_data)
            return Response(serializer.data)
        
    
    def post(self,request,format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Question Posted'},status=status.HTTP_201_CREATED)
        return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)



    def put(self,request,id,format=None):
        pk=id
        oldData=Question.objects.get(id=pk)
        serializer=QuestionSerializer(oldData,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Question Updated'},status=status.HTTP_201_CREATED)
        return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id,format=None):
        pk=id
        data=Question.objects.get(id=pk)
        serializer=QuestionSerializer(data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Question Patched'},status=status.HTTP_201_CREATED)
        return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
        pk=id
        data=Question.objects.get(id=pk)
        data.delete()
        return Response({'msg':'Question Removed.'})



