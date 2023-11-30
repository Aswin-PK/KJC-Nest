from django import forms
from Hostel.models import Hostel_Details 


class Hostel_DetailsForm(forms.ModelForm):
    class Meta:
        model = Hostel_Details
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Hostel_DetailsForm, self).__init__(*args, **kwargs)
        

        # Set required attribute to False for all fields except 'hostel_name', 'hostel_warden', and 'hostel_address'
        for field_name, field in self.fields.items():
            if field_name not in ['hostel_name', 'hostel_warden', 'hostel_address']:
                field.required = False
                