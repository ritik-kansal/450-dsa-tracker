from .req import *

class AnalyticsAPI(APIView):
    def get(self,request,id=None):
        if id == None: #for current user
            id = self.request.user.id
            
        # 2 = done
        # 1 = revise
        # 0 = pending
        question_pending = Question_user_mark.objects.filter(mark=0,user_id=id)
        number_question_pending = len(question_pending)

        question_revise = Question_user_mark.objects.filter(mark=1,user_id=id)
        number_question_revise = len(question_revise)

        # data = Question_user_mark.objects.filter(mark=2,user_id=id).select_related('question_id').select_related('question_id__topic_id')
        question_done = Question_user_mark.objects.filter(mark=2,user_id=id)
        number_question_done = len(question_done)

        number_question_solved = number_question_done+number_question_revise
        # percentage of question solved
        percentage = (number_question_solved)/450 * 100

        topic_wise_count = dict()
        level = [0 for i in range(3)] # 0(index) easy --- 2 hard
        # question = set()
        # difficulty wise percentage and topic count
        for question_user_mark in question_done | question_revise:
            # each question_user_mark object has a pre-fetched 'question_id' attribute, and accessing it won't hit the db again. 
            
            topic = question_user_mark.question_id.topic_id.name
            topic_wise_count[topic] = topic_wise_count.get(topic,0)+1
            # question.add(question_user_mark.question_id)
            level[question_user_mark.question_id.level]+=1 

        easy_per = level[0]/number_question_solved *100
        medium_per = level[1]/number_question_solved *100
        hard_per = level[2]/number_question_solved *100

        # serializer = QuestionSerializer(question,many = True)
        serializer = QuestionUserMarkSerializer(question_done | question_revise,many = True)

        return Response({
            "questions_mark" : serializer.data,
            "percentage":percentage,
            "difficulty_based_info":{
                "easy_per":easy_per,
                "medium_per":medium_per,
                "hard_per":hard_per,
            },
            "topic_wise_count":topic_wise_count,
            "user_based":{
                "total_attempted":number_question_solved+number_question_revise+number_question_pending,
                "question_solved":number_question_solved,
                "question_revise":number_question_revise,
                "question_pending":number_question_pending,
            }
        })
