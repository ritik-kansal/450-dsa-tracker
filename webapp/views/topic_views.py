from .req import *

class TopicApi(APIView):
    serializer_class = TopicSerializer

    def get(self, request,id=None, format=None):
        if id == None:
            topic_data = Topic.objects.all()
            serializer = TopicSerializer(topic_data,many=True)
        else:
            topic_data = Topic.objects.get(id=id)
            serializer=TopicSerializer(topic_data)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Topic Created'},status=status.HTTP_201_CREATED)
        return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id,format=None):
        pk=id
        oldData=Topic.objects.get(id=pk)
        serializer = TopicSerializer(oldData,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Topic Updated'},status=status.HTTP_201_CREATED)
        return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id,format=None):
        pk=id
        data=Topic.objects.get(id=pk)
        data.delete()
        return Response({'msg':'Topic Deleted.'})