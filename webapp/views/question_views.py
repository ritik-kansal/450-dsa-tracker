from .req import *
def getQuestion(request,id):
    question_data = Question.objects.get(id=id)
    serializer = QuestionSerializer(question_data)
    return JsonResponse(serializer.data)
def getAllQuestions(request):
    question_data = Question.objects.all()
    serializer = QuestionSerializer(question_data,many = True)
    return JsonResponse(serializer.data,safe = False)

# create
@csrf_exempt
def createQuestion(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = QuestionSerializer(data=python_data)
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

