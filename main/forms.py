from django import forms
from .models import participant

class partiform(forms.ModelForm):
    class Meta:
        model = participant
        fields = ['f_name','l_name','email','num_tel','school','first_participant','second_participant',
        'third_participant','project_name','theme','description']