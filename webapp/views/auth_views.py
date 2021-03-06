from .req import *

class RegisterAPI(generics.GenericAPIView):
    serializer_class = AuthSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": AuthSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = [AllowAny]
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        # print(request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # print("\n\n\ntest\n",(request.__dict__),"\n\n\n")
        login(request, user)
        result = super(LoginAPI, self).post(request, format=None)
        # print(result)
        return result

