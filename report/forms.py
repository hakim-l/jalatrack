# from django.contrib.contenttypes.forms import ModelForm
# from activity.models import ActivityModel
# from division.models import DivisionModel
# from plan.models import PlanModel
#
# class IndividualReportForm(ModelForm):
#     class Meta:
#         model= EmployeeModel
#         fields= ('username','email','first_name','last_name',
#        'division', 'is_supervisor',)
#         division= forms.ModelChoiceField(queryset=DivisionModel.objects.all()
#                                          )
#
#
#
#
# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = EmployeeModel
#         fields = ("email",)
# #