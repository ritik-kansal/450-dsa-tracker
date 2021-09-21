from .req import *
from .questions_solved_view import QuestionSolvedAPI
from .filter_views import GeneralFilterAPI

class IndexPageAPI(APIView):
    def get(self,request,id=None):
        # topics
        if id == None:
            id = self.request.user.id
        topics = Topic.objects.all()
        serializer = TopicSerializer(topics,many=True)
        topics_data = serializer.data

        # questions solved
        questions_solved = QuestionSolvedAPI().helper(request,id)
        
        questions_data = GeneralFilterAPI().helper(request,1) # 1 is for page number

        return Response({
            "topics":topics_data,
            "questions_data":questions_data,
            "questions_solved": questions_solved
        })