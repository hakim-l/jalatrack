from django.views.generic import (
ListView,
CreateView,
UpdateView,
TemplateView
)

from django.urls import reverse_lazy
from .models import ActivityModel


class ActivityListView(ListView):
    model = ActivityModel
    template_name = "templates/reports/individualReports.html"
    context_object_name = 'activity'

class ActivityCreateView(CreateView):
    model= ActivityModel
    fields = (
              'division',
              'name','end_at','plans',
              'activity','activity_type',
              'attachment'
    )
# Create your views here.
