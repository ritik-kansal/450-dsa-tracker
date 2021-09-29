from typing import final
from .req import *
from .questions_solved_view import QuestionSolvedAPI
from .filter_views import GeneralFilterAPI
from django.db import connection

import datetime
import calendar


class ProfilePageAPI(APIView):
    def __dictfetchall(self, cursor):
        # "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def helper_mark(self, request, id=None):
        if id == None:  # for current user
            id = self.request.user.id

        mark = [0 for i in range(4)]
        questions_marked = Question_user_mark.objects.filter(user_id=id)
        for question_mark in questions_marked:
            # print(question_mark.mark)
            mark[2-question_mark.mark] += 1
        # mark[3] = len(questions_marked)
        return {
            "count" : len(questions_marked),
            "marks": mark
        }
    def topic_wise(self, request, id=None):
        if id == None:  # for current user
            id = self.request.user.id

        # mark = [0 for i in range(4)]
        topics = Topic.objects.all()
        

        count_for_topic = {topic.name:0 for topic in topics}
        questions_marked = Question_user_mark.objects.filter(user_id=id).select_related('question_id__topic_id')
        for question_mark in questions_marked:
            # print(question_mark.mark)
            if question_mark.mark > 0:
                count_for_topic[question_mark.question_id.topic_id.name] = count_for_topic.get(question_mark.question_id.topic_id.name,0) +1
        # mark[3] = len(questions_marked)

        labels = []
        values = []
        for topic in count_for_topic:
            labels.append((topic[:8]+('..' if len(topic)>=8 else "")))
            values.append(count_for_topic[topic])

        return {
            "labels": labels,
            "values": values
        }

    def post(self, request, id=None):
        if id == None:  # for current user
            id = self.request.user.id
        

        questions_solved = QuestionSolvedAPI().helper(request, id)
        question_marked = self.helper_mark(request, id)
        topic_wise_freq = self.topic_wise(request, id)
        if request.data['day'] == None:
            day = datetime.date.today()
        else:
            day = datetime.datetime.strptime(request.data['day'], '%Y-%m-%d')
        # print(request.data['day'])
        # print(day)
        idx = (day.weekday())
        # print(idx)
        mon = (day - datetime.timedelta(idx))
        mon_sql = mon.strftime('%Y-%m-%d')
        sun = (day - datetime.timedelta(idx-6))
        sun_sql = sun.strftime('%Y-%m-%d')
        # print("mon=",mon,"sun=",sun)
        query = (f"SELECT to_date(created_at::TEXT,'YYYY-MM-DD') AS day, COUNT(*) as count FROM webapp_question_user_mark"
                 f" WHERE created_at>='{mon_sql}' AND created_at<='{sun_sql}' AND user_id = {id}"
                 " GROUP BY day")

        try:
            cursor = connection.cursor()

            # cursor.execute(query,[mon,sun])
            cursor.execute(query)
            result = self.__dictfetchall(cursor)
            # print("before final")
            # print(result)
            days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            week_data = {days[i]: 0 for i in range(7)}
            # print(final_week_data)

            for r in result:
                week_day = datetime.datetime.strptime(
                    str(r['day']), '%Y-%m-%d').strftime('%a')
                week_data[week_day] = r['count']

            for i in range(7):
                days[i] = week_data[days[i]]

            # print(days)

            # for query in connection.queries:
                # print(query)

            cursor.close()
            return Response({
                "questions_solved": questions_solved,
                "question_marked": question_marked,
                "topic_wise_freq":topic_wise_freq,
                "week_data": days
            })

        except Exception as e:
            return Response({
                "msg": str(e)
            })
