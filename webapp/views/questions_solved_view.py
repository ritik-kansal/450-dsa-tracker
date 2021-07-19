from .req import *

class QuestionSolvedAPI(APIView):
    def helper(self,request,id=None):
        if id == None: #for current user
            id = self.request.user.id

        level = [0 for i in range(4)] #easy, medium, hard, notsolved
        questions_marked = Question_user_mark.objects.filter(mark__range=(1,3),user_id=id).select_related('question_id')
        for question_mark in questions_marked:
            # print(question_mark.mark)
            level[question_mark.question_id.level]+=1 
        level[3] = 450-len(questions_marked)

        return {
            "count":len(questions_marked),
            "difficulty_levels":level
        }

    def get(self,request,id = None):
        # questions solved
        
        return Response({
            "questions_solved": self.helper(request,id)
        })