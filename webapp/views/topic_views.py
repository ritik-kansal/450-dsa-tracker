from .req import *
def getTopic(request,id):
    topic_data = Topic.objects.get(id=id)
    serializer = TopicSerializer(topic_data)
    return JsonResponse(serializer.data)
def getAllTopics(request):
    topic_data = Topic.objects.all()
    serializer = TopicSerializer(topic_data,many = True)
    return JsonResponse(serializer.data,safe = False)

# create
@csrf_exempt
def createTopic(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = TopicSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'question created'}
            return JsonResponse(res)
            # json_data = JSONRenderer().render(res)
            # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(serializer.errors)
    res = {'msg':'error occured'}
    return JsonResponse(res)
# create