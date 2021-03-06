"""dsa_450_tracker_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from webapp import views
from webapp.views import *
from knox import views as knox_views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register('questions',QuestionViewSet,basename='question')
# router.register('topics',TopicViewSet,basename='topic')
# router.register('question-user-marks',QuestionUserMarkViewSet,basename='question_user_mark')
# router.register('pair-programmers',PairProgrammerViewSet,basename='pair_programmer')
# router.register('user-asked-for-pair-programming',UserAskedForPairProgrammingViewSet,basename='user_asked_for_pair_programming')
# router.register('mark-updates',MarkUpdateViewSet,basename='mark_update')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/users/', UserApi.as_view()),
    path('api/users/<int:id>/', UserApi.as_view()),
        
    path('api/topics', TopicApi.as_view()),
    path('api/topics/<int:id>', TopicApi.as_view()),

    path('api/questions', QuestionApi.as_view()),
    path('api/questions/<int:id>', QuestionApi.as_view()),

    
    path('api/pairing', PairApi.as_view()),
    path('api/pairing/<int:id>', PairApi.as_view()),

    path('api/question-user-mark', QuestionUserMarkApi.as_view()),
    path('api/question-user-mark/<int:id>',QuestionUserMarkApi.as_view()),
    

    path('api/register', RegisterAPI.as_view(), name='register'),
    path('api/isauth', IsAuthenticated.as_view(), name='isAuthenticated'),
    path('api/login', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    path('api/analytics', AnalyticsAPI.as_view()),
    path('api/analytics/<int:id>', AnalyticsAPI.as_view()),
    path('api/questions_solved', QuestionSolvedAPI.as_view()),
    
    # path('api/filter/level/<int:level>', LevelFilterAPI.as_view()),
    # path('api/filter/status/<int:status>', StatusFilterAPI.as_view()),
    # path('api/filter/topic/<int:topic_id>', TopicFilterAPI.as_view()),
    # path('api/filter/search', QuestionSearchFilterAPI.as_view()),
    # path('api/filter/search/<str:query>', QuestionSearchFilterAPI.as_view()),
    
    path('api/filter/general/<int:page_number>', GeneralFilterAPI.as_view()),
    path('api/filter/general', GeneralFilterAPI.as_view()),

    path('api/test_question_user_mark_public', QuestionUserMarkAndLogApi.as_view()),
    
    # path('api/get_question/<int:page_number>', QuestionDataApi.as_view()),
    
    # pages
    path('api/pages/index', IndexPageAPI.as_view()),
    path('api/pages/profile', ProfilePageAPI.as_view()),
    

]
