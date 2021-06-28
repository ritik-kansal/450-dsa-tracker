# from webapp.serializers import QuestionUserMarkSerializer
# from webapp.models import Question_user_mark
from .req import *

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer

class QuestionUserMarkViewSet(viewsets.ModelViewSet):
    queryset = Question_user_mark.objects.all()
    serializer_class = QuestionUserMarkSerializer

class PairProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Pair_programmer.objects.all()
    serializer_class = PairProgrammerSerializer

class UserAskedForPairProgrammingViewSet(viewsets.ModelViewSet):
    queryset = User_asked_for_pair_programming.objects.all()
    serializer_class = UserAskedForPairProgrammingSerializer
    
class MarkUpdateViewSet(viewsets.ModelViewSet):
    queryset = Mark_update.objects.all()
    serializer_class = MarkUpdateSerializer