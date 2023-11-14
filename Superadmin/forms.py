from django import forms
from Hostel.models import Hostel_Details


class Hostel_DetailsForm(forms.ModelForm):
    class Meta:
        model = Hostel_Details
        fields = '__all__'
    
    