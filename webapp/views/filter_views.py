from .req import *

class LevelFilterAPI(APIView):
    permission_classes = [AllowAny]
    def get(self,request,id,Format=None):
        data = Question.filter(level=id)
        serializer = QuestionSerializer(data,many=True)
        return Response(serializer.data)

class StatusFilterAPI(APIView):
    def get(self,request,id,Format=None):
        data = Question_user_mark.objects.filter(mark=id)
        serializer = QuestionUserMarkSerializer(data,many=True)
        return Response(serializer.data)    

class TopicFilterAPI(APIView):
    permission_classes = [AllowAny]
    def get(self,request,id,Format=None):
        data = Question.objects.filter(topic_id=id)
        serializer=QuestionSerializer(data,many=True)
        return Response(serializer.data)

class QuestionSearchFilterAPI(APIView):
    permission_classes = [AllowAny]
    def get(self,request,Format=None):
        data = Question.objects.all()
        serializer=QuestionSerializer(data,many=True)
        return Response(serializer.data)

    def post(self,request,Format=None):
        str=json.dumps(request.data)
        dict=json.loads(str)
        data = Question.objects.filter(link__contains=dict['name'])
        serializer=QuestionSerializer(data)
        return Response(serializer.data)
