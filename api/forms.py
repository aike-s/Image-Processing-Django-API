from django import forms
from .models import Job, History

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = '__all__'

class HistoryForm(forms.ModelForm):

    class Meta:
        model = History
        fields = ('step', 'job_id')