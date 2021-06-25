from .req import *
# Create your views here.

# get user
def getUser(request,id):
    user_data = User.objects.get(id=id)  
    serializer = UserSerializer(user_data)
    return JsonResponse(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type="application/json")

def getAllUsers(request):
    user_data = User.objects.all()  
    serializer = UserSerializer(user_data, many=True)
    return JsonResponse(serializer.data, safe=False)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type="application/json")
# get user


# # create user with auth 
# @csrf_exempt
# def createUser(request):
#     if request.method == "POST":
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data = JSONParser().parse(stream)
#         serializer = UserSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'user created'}
#             return JsonResponse(res)
#             # json_data = JSONRenderer().render(res)
#             # return HttpResponse(json_data,content_type='application/json')
#         return JsonResponse(serializer.errors)
#     res = {'msg':'error occured'}
#     return JsonResponse(res)
# create user
