from webapp.views.questions_data_view import QuestionDataApi
from .req import *
from .questions_data_view import QuestionDataApi

class IndexPageAPI(APIView):
    def get(self,request,id=None):
        # topics
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics,many=True)
        topics_data = serializer.data

        # questions solved
        if id == None: #for current user
            id = self.request.user.id

        level = [0 for i in range(4)] #easy, medium, hard, notsolved
        questions_marked = Question_user_mark.objects.filter(mark__range=(1,3),user_id=id).select_related('question_id')
        for question_mark in questions_marked:
            level[question_mark.question_id.level]+=1 
        level[3] = 450-len(questions_marked)
        questions_data = QuestionDataApi().helper(request,1)

        return Response({
            "topics":topics_data,
            "questions_data":questions_data,
            "questions_solved": {
                "count":len(questions_marked),
                "difficulty_levels":level
            }
        })