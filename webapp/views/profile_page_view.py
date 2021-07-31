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
        questions_marked = Question_user_mark.objects.all()
        for question_mark in questions_marked:
            print(question_mark.mark)
            mark[question_mark.mark] += 1
        mark[3] = 450-len(questions_marked)
        return {
            "marks": mark
        }

    def get(self, request, id=None):
        questions_solved = QuestionSolvedAPI().helper(request, 1)
        question_marked = self.helper_mark(request, id)
        today = datetime.date.today()
        idx = (today.weekday())

        mon = (today - datetime.timedelta(idx))
        mon_sql = mon.strftime('%Y-%m-%d')
        sun = (today - datetime.timedelta(idx-6))
        sun_sql = sun.strftime('%Y-%m-%d')

        query = (f"SELECT strftime('%Y-%m-%d',created_at) AS day, COUNT(*) as count FROM webapp_question_user_mark"
                 f" WHERE created_at>='{mon_sql}' AND created_at<='{sun_sql}'"
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
                    r['day'], '%Y-%m-%d').strftime('%a')
                week_data[week_day] = r['count']

            for i in range(7):
                days[i] = week_data[days[i]]

            print(days)
            cursor.close()
            return Response({
                "questions_solved": questions_solved,
                "question_marked": question_marked,
                "week_data": days
            })

        except:
            return Response({
                "msg": "error occured"
            })
