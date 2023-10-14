from django.views.generic import (
ListView,
CreateView,
UpdateView,
TemplateView
)

from django.urls import reverse_lazy
from .models import PlanModel


class PlanListView(ListView):
    model = PlanModel
    template_name = "templates/reports/individualReports.html"
    context_object_name = 'activity'

class ActivityCreateView(CreateView):
    model= PlanModel
    fields = (
              'division',
              'name','end_at','plans',
              'activity','activity_type',
              'attachment'
    )