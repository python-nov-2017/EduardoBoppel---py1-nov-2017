from django import forms
from .models import Lead

class LeadCreationForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'email']