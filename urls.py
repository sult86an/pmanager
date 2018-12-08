from django.urls import path
from . import pviews
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

app_name = 'pmanager'
urlpatterns = [
    # /initiatives/

    path('user_login/', pviews.user_login, name='user'),
    path('logout/', pviews.user_logout, name='logout'),
    path('home/', pviews.IndexView.as_view(), name='home'),
    path('initiative/', pviews.InitiativesView.as_view(), name='initiative'),
    path('goals/', pviews.GoalsView.as_view(), name='goals'),
    path('goals/add/', pviews.GoalsFormView.as_view(), name='add-goal'),
    path('goals/delete/<int:pk>/', pviews.GoalDelete.as_view(), name='goal-delete'),
    path('supports/', pviews.SupportsView.as_view(), name='supports'),
    path('supports/add/', pviews.SupportsFormView.as_view(), name='add-support'),
    path('supports/delete/<int:pk>/', pviews.SupportDelete.as_view(), name='support-delete'),
    path('risks/', pviews.RisksView.as_view(), name='risks'),
    path('risks/add/', pviews.RisksFormView.as_view(), name='add-risk'),
    path('risks/update/<int:pk>/', pviews.RiskeUpdate.as_view(), name='update-risk'),
    path('risks/delete/<int:pk>/', pviews.RiskDelete.as_view(), name='risk-delete'),
    path('challenges/', pviews.ChallengesView.as_view(), name='challenges'),
    path('challenges/add/', pviews.ChallengesFormView.as_view(), name='add-challenge'),
    path('challenges/update/<int:pk>/', pviews.ChallengeUpdate.as_view(), name='update-challenge'),
    path('challenges/delete/<int:pk>/', pviews.ChallengeDelete.as_view(), name='challenge-delete'),
    path('stages/', pviews.StagesView.as_view(), name='stages'),
    path('stages/add/', pviews.StageFormView.as_view(), name='add-stage'),
    path('stages/update/<int:pk>/', pviews.StageUpdate.as_view(), name='update-stage'),
    path('stages/delete/<int:pk>/', pviews.StageDelete.as_view(), name='stage-delete'),
    path('reports/', pviews.ListWeek.as_view(), name='reports'),
    path('reports/add/', pviews.CreateReport.as_view(), name='create-report'),
    path('reports/prepare/', pviews.ReportsPrerpare.as_view(), name='report-prepare'),
    path('reports/prepare/add/<int:id>/', pviews.InsertStage.as_view(), name='insert-stage'),
    path('reports/prepare/update/<int:pk>/', pviews.StageReportUpdate.as_view(), name='stageUpdate'),
    path('reports/prepare/send/<int:pk>/', pviews.ReportReadyUpdate.as_view(), name='ReportReadyUpdate'),
    path('leaders/', pviews.LeadersView.as_view(), name='leaders'),
    path('messages/', pviews.EnquiryView.as_view(), name='messages'),
]
