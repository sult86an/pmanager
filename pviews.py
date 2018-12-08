from django.views import generic
from django.views.generic import View
from .models import Leaders
from initiatives.models import Initi,  Reports, Goals, Supports, Stages, Risks, Challenges, MainStage
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.shortcuts import  get_object_or_404,  render_to_response
from django.conf import settings
from global_login_required import login_not_required
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import GoalsForm
from initiatives.forms import UpdateStage, UpdateChallenge, UpdateRisks, StageForm, UpdateStageForm
from django.urls import reverse, reverse_lazy, resolve
from django.utils import timezone
from datetime import datetime
from django.forms import modelformset_factory
from django.views.generic.edit import ModelFormMixin

from django.core.exceptions import ImproperlyConfigured
from django.forms import models as model_forms
from django.http import HttpResponseRedirect
from django.utils.encoding import force_text
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View
from django.views.generic.detail import (
    BaseDetailView, SingleObjectMixin, SingleObjectTemplateResponseMixin,
)
from django.contrib.sessions.models import Session


@login_not_required
def userindex(request):
    return render(request, 'pmanager/index.html')


@login_not_required
def user_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('pmanager:home'))
    else:
        return render(request, 'pmanager/index.html', {})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse(userindex))


class IndexView(generic.ListView):
    template_name = 'pmanager/home.html'
    context_object_name = 'mub'

    def get_queryset(self):
        user = self.request.user
        return Initi.objects.filter(leader__first_name=user)


# #class IndexView(generic.ListView):
#    # template_name = 'pmanager/home.html'
#     context_object_name = 'mub'
#
#     def get_queryset(self):
#         #return Initi.objects.filter(leader__id=1)
#         return Initi.mub_name
class LeadersView(generic.ListView):
    template_name = 'pmanager/leaders.html'
    context_object_name = 'leaders'

    def get_queryset(self):
        return User.objects.all()


class InitiativesView(generic.ListView):
    template_name = 'pmanager/my_initiative.html'
    context_object_name = 'detail'

    def get_queryset(self):
        user = self.request.user
        return Initi.objects.filter(leader__first_name=user)


class GoalsView(generic.ListView):
    template_name = 'pmanager/goals.html'
    context_object_name = 'goals'

    def get_queryset(self):
        user = self.request.user
        return Goals.objects.filter(mub__leader__first_name=user)


class SupportsView(generic.ListView):
    template_name = 'pmanager/supports.html'
    context_object_name = 'supports'

    def get_queryset(self):
        user = self.request.user
        return Supports.objects.filter(mub__leader__first_name=user)


class RisksView(generic.ListView):
    template_name = 'pmanager/risks.html'
    context_object_name = 'risks'

    def get_queryset(self):
        user = self.request.user
        return Risks.objects.filter(mub_risk__leader__first_name=user)


class ChallengesView(generic.ListView):
    template_name = 'pmanager/challenge.html'
    context_object_name = 'challenges'

    def get_queryset(self):
        user = self.request.user
        return Challenges.objects.filter(mub__leader__first_name=user)


class StagesView(generic.ListView):
    template_name = 'pmanager/stages.html'
    context_object_name = 'stages'

    def get_queryset(self):
        user = self.request.user
        return Stages.objects.filter(mub__leader__first_name=user)


class WeekReportView(generic.DetailView):
    template_name = 'pmanager/weekly_report.html'
    model = Initi


class ListWeek(generic.ListView):
    template_name = 'pmanager/weekly_report.html'
    context_object_name = 'reports'

    def get_queryset(self):
        user = self.request.user
        return Reports.objects.filter(mub_r__leader__first_name=user)


class DetailView(generic.DetailView):
    template_name = 'pmanager/detail.html'
    model = Reports

    def get_queryset(self):
        user = self.request.user
        return Reports.objects.filter(mub_r__leader__first_name=user)


class EnquiryView(View):
    template_name = 'pmanager/enquiry.html'

    def get(self, request):
        return render(request, self.template_name)


class GoalsFormView(CreateView):
    model = Goals
    fields = ['goal', 'mub']
    template_name = 'pmanager/add-form.html'
    success_url = reverse_lazy('pmanager:goals')

    def get_context_data(self, **kwargs):
        user = self.request.user
        mub = Initi.objects.filter(leader__first_name=user)
        ctx = super().get_context_data(**kwargs)
        ctx['mub'] = self.request.GET.get('id=', mub)
        return ctx


class GoalDelete(DeleteView):
    model = Goals
    success_url = reverse_lazy('pmanager:goals')


class SupportsFormView(CreateView):
    model = Supports
    fields = ['support', 'mub']
    template_name = 'pmanager/add-support.html'
    success_url = reverse_lazy('pmanager:supports')

    def get_context_data(self, **kwargs):
        user = self.request.user
        mub = Initi.objects.filter(leader__first_name=user)
        ctx = super().get_context_data(**kwargs)
        ctx['mub'] = self.request.GET.get('id=', mub)
        return ctx


class SupportDelete(DeleteView):
    model = Supports
    success_url = reverse_lazy('pmanager:supports')


class StageFormView(CreateView):
    model = Stages
    fields = ['mub', 'stage', 'ratio', 'end_date']
    template_name = 'pmanager/add-stage.html'
    success_url = reverse_lazy('pmanager:stages')

    def get_context_data(self, **kwargs):
        user = self.request.user
        mub = Initi.objects.filter(leader__first_name=user)
        ctx = super().get_context_data(**kwargs)
        ctx['mub'] = self.request.GET.get('id=', mub)
        return ctx


class StageUpdate(UpdateView):
    form_class = UpdateStage
    template_name = 'pmanager/update-form.html'
    success_url = reverse_lazy('pmanager:stages')

    def get_queryset(self):
        user = self.request.user
        mub = Initi.objects.filter(leader__first_name=user)
        return Stages.objects.filter(mub__leader__first_name=user)


class StageDelete(DeleteView):
    model = Stages
    success_url = reverse_lazy('pmanager:stages')


class RisksFormView(CreateView):
    model = Risks
    fields = ['risk', 'mub_risk', 'owner_risk', 'probability', 'influence', 'plan']
    template_name = 'pmanager/add-risk.html'
    success_url = reverse_lazy('pmanager:risks')

    def get_context_data(self, **kwargs):
        user = self.request.user
        mub = Initi.objects.filter(leader__first_name=user)
        ctx = super().get_context_data(**kwargs)
        ctx['mub_risk'] = self.request.GET.get('id=', mub)
        return ctx


class RiskeUpdate(UpdateView):
    form_class = UpdateRisks
    template_name = 'pmanager/update-form.html'
    success_url = reverse_lazy('pmanager:risks')

    def get_queryset(self):
        user = self.request.user
        mub = Initi.objects.filter(leader__first_name=user)
        return Risks.objects.filter(mub_risk__leader__first_name=user)


class RiskDelete(DeleteView):
    model = Risks
    success_url = reverse_lazy('pmanager:risks')


class ChallengesFormView(CreateView):
    model = Challenges
    fields = ['challenge', 'mub', 'owner', 'status', 'info']
    template_name = 'pmanager/add-challenge.html'
    success_url = reverse_lazy('pmanager:challenges')

    def get_context_data(self, **kwargs):
        user = self.request.user
        mub = Initi.objects.filter(leader__first_name=user)
        ctx = super().get_context_data(**kwargs)
        ctx['mub'] = self.request.GET.get('id=', mub)
        return ctx


class ChallengeUpdate(UpdateView):
    form_class = UpdateChallenge
    template_name = 'pmanager/update-form.html'
    success_url = reverse_lazy('pmanager:challenges')

    def get_queryset(self):
        user = self.request.user
        mub = Initi.objects.filter(leader__first_name=user)
        return Challenges.objects.filter(mub__leader__first_name=user)


class ChallengeDelete(DeleteView):
    model = Challenges
    success_url = reverse_lazy('pmanager:challenges')


class CreateReport(CreateView):
    model = Reports
    fields = ['week_ar', 'week_no', 'mub_r', 'ready']
    template_name = 'pmanager/create-report.html'
    success_url = reverse_lazy('pmanager:reports')

    def get_context_data(self, **kwargs):
        user = self.request.user
        mub = Initi.objects.filter(leader__first_name=user)
        ctx = super().get_context_data(**kwargs)
        ctx['mub_r'] = self.request.GET.get('id=', mub)
        return ctx


class ReportsPrerpare(generic.CreateView):
    template_name = 'pmanager/report-prepare.html'
    model = Reports
    fields = ['week_ar', 'week_no', 'mub_r', 'ready']

    def get_context_data(self, *args,  **kwargs):
            pk = self.request.POST.get("week_id")
            mub = Reports.objects.filter(pk=pk)
            ctx = super().get_context_data(**kwargs)
            ctx['week_ar'] = self.request.GET.get('id=', mub)
            return ctx

    def packOrders(request):
        # your code
        return HttpResponseRedirect(reverse('pmanager:insert-stage'))


class InsertStage(generic.CreateView):
    form_class = StageForm
    template_name = 'pmanager/report_stage.html'
    success_url = reverse_lazy('pmanager:reports')

    def get_queryset(self, *request):
        stage = self.request.GET.get('stage')
        report = self.request.GET.get('report')
        return MainStage.objects.filter(report=report, stage=stage)


class StageReportUpdate(UpdateView):
    form_class = UpdateStageForm
    success_url = reverse_lazy('pmanager:reports')
    template_name = 'pmanager/update-form.html'

    def get_queryset(self):
        stage = self.request.GET.get('stage')
        report = self.request.GET.get('report')
        ratio = self.request.GET.get('ratio')
        return MainStage.objects.filter(report=report, stage=stage)


class ReportReadyUpdate(UpdateView):
    model = Reports
    fields = ['ready']
    success_url = reverse_lazy('pmanager:home')
    template_name = 'pmanager/report-prepare.html'

    def get_queryset(self):
        week = self.request.POST.get('week')
        return Reports.objects.filter(id=week)
