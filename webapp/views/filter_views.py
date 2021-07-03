from .req import *

class LevelFilterAPI(APIView):
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]
    def get(self,request,id,Format=None):
        data = Question.filter(level=id)
        serializer = QuestionSerializer(data,many=True)
        return Response(serializer.data)

class StatusFilterAPI(APIView):
    serializer_class = QuestionUserMarkSerializer
    def get(self,request,id,Format=None):
        data = Question_user_mark.objects.filter(mark=id)
        serializer = QuestionUserMarkSerializer(data,many=True)
        return Response(serializer.data)    

class TopicFilterAPI(APIView):
    serializer_class = TopicSerializer
    def get(self,request,id,Format=None):
        data = Question.objects.filter(topic_id=id)
        serializer=QuestionSerializer(data,many=True)
        return Response(serializer.data)

class QuestionSearchFilterAPI(APIView):
    serializer_class=QuestionSerializer
    def post(self,request,Format=None):
        str=json.dumps(request.data)
        dict=json.loads(str)
        data = Question.objects.filter(link=dict['link'])
        serializer=QuestionSerializer(data)
        return Response(serializer.data)
