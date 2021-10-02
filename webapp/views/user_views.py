from .req import *

class UserApi(APIView):
    serializer_class = UserSerializer

    def get(self, request,id=None, format=None):
        if id == None:
            user_data = User.objects.all()
            serializer = UserSerializer(user_data,many=True)
        else:
            user_data = User.objects.get(id=id)
            serializer=UserSerializer(user_data)
        return Response(serializer.data)
    
