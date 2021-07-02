from .req import *

class AnalyticsAPI(APIView):
    def get(self,request,id=None):
        if id == None: #for current user
            id = self.request.user.id
        else:
            # ToDo 
            # validate
            pass

        # 2 = done
        data = Question_user_mark.objects.filter(mark=2).select_related('question_id').select_related('question_id__topic_id')
        question_solved = len(data)
        # percentage of question solved
        percentage = (question_solved)/450 * 100

        topic_wise_count = dict()
        level = [0 for i in range(3)]
        # difficulty wise percentage
        # and topic count
        for question_user_mark in data:
            # each question_user_mark object has a pre-fetched 'question_id' attribute, and accessing it won't hit the db again. 
            
            topic = question_user_mark.question_id.topic_id.name
            topic_wise_count[topic] = topic_wise_count.get(topic,0)+1

            level[question_user_mark.question_id.level]+=1 # 0 easy --- 2 hard

        easy_per = level[0]/question_solved *100
        medium_per = level[1]/question_solved *100
        hard_per = level[2]/question_solved *100

        return Response({
            "percentage":percentage,
            "difficulty_based_info":{
                "easy_per":easy_per,
                "medium_per":medium_per,
                "hard_per":hard_per,
            },
            "topic_wise_count":topic_wise_count
        })
