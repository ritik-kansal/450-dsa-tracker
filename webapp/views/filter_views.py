from .req import *

class LevelFilterAPI(APIView):
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]
    def get(self,request):
        data = Question.objects.all()
        serializer = QuestionSerializer(data,many=True)
        return Response(serializer.data)
    def post(self,request,Format=None):
        str=json.dumps(request.data)
        dict=json.loads(str)
        data = Question.objects.all().filter(level=dict['level'])
        serializer = QuestionSerializer(data,many=True)
        return Response(serializer.data)

class StatusFilterAPI(APIView):
    serializer_class = QuestionUserMarkSerializer
    def get(self,request):
        data = Question_user_mark.objects.all()
        serializer = QuestionUserMarkSerializer(data,many=True)
        return Response(serializer.data)
    def post(self,request,Format=None):
        str=json.dumps(request.data)
        dict=json.loads(str)
        data = Question_user_mark.objects.all().filter(mark=dict['mark'])
        serializer = QuestionUserMarkSerializer(data,many=True)
        return Response(serializer.data)    

class TopicFilterAPI(APIView):
    serializer_class = TopicSerializer
    def post(self,request,Format=None):
        str=json.dumps(request.data)
        dict=json.loads(str)
        data = Topic.objects.all().filter(name=dict['name']).values('id')
        serializer = TopicSerializer(data)
        id=serializer['id']
        data = Question.objects.all().filter(topic_id=id)
        serializer=QuestionSerializer(data,many=True)
        return Response(serializer.data)

class QuestionSearchFilterAPI(APIView):
    serializer_class=QuestionSerializer
    def get(self,request,Format=None):
        data = Question.objects.all()
        serializer=QuestionSerializer(data)
        return Response(serializer.data)
    def post(self,request,Format=None):
        str=json.dumps(request.data)
        dict=json.loads(str)
        data = Question.objects.all().filter(link=dict['link'])
        serializer=QuestionSerializer(data)
        return Response(serializer.data)
