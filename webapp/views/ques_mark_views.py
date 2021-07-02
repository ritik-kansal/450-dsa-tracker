
from .req import *

class QuestionUserMarkApi(APIView):
    serializer_class = QuestionUserMarkSerializer

    def get(self,request,id=None):
        if id==None:
            data = Question_user_mark.objects.all()
            serializer = QuestionUserMarkSerializer(data,many = True)
            return Response(serializer.data)
        else:
            data = Question_user_mark.objects.get(id=id)
            serializer = QuestionUserMarkSerializer(data)
            return Response(serializer.data)

    
    def post(self,request,format=None):
        serializer = QuestionUserMarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=self.request.user)
            return Response({'msg':'Marked'},status=status.HTTP_201_CREATED)
        return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id,format=None):
        pk=id
        oldData=Question_user_mark.objects.get(id=pk)
        serializer=QuestionUserMarkSerializer(oldData,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Mark Updated'},status=status.HTTP_201_CREATED)
        return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id,format=None):
        pk=id
        data=Question_user_mark.objects.get(id=pk)
        serializer=QuestionUserMarkSerializer(data,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Mark Patched'},status=status.HTTP_201_CREATED)
        return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
        pk=id
        data=Question_user_mark.objects.get(id=pk)
        data.delete()
        return Response({'msg':'Deleted'})
