
from .req import *

class QuestionUserMarkApi(APIView):
    serializer_class = QuestionUserMarkSerializer

    def get(self,request,id):
        mark= Question_user_mark.objects.get(id=id)
        serializer=QuestionUserMarkSerializer(mark)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = QuestionUserMarkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Marked'},status=status.HTTP_201_CREATED)
        return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    # def put(self,request,id,format=None):
    #     pk=id
    #     oldData=Pair_programmer.objects.get(id=pk)
    #     serializer=PairProgrammerSerializer(oldData,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Pairing Updated'},status=status.HTTP_201_CREATED)
    #     return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    # def patch(self,request,id,format:None):
    #     pk=id
    #     data=Pair_programmer.objects.get(id=pk)
    #     serializer=PairProgrammerSerializer(data,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({'msg':'Pairing Patched'},status=status.HTTP_201_CREATED)
    #     return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    # def delete(self,request,id,format=None):
    #     pk=id
    #     data=Pair_programmer.objects.get(id=pk)
    #     data.delete()
    #     return Response({'msg':'Unpaired.'})
