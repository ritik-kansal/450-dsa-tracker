from .req import *

class registerAPI(generics.GenericAPIView):
    serializer_class = AuthSerializer
    # authentication_classes = [BasicAuthentication]
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": AuthSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

    def get(self,request,*args, **kwargs):
        user_data = User.objects.all()
        serializer = UserSerializer(user_data,many=True)

        return Response(serializer.data)