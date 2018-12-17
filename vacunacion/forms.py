from django import forms
from .models import Vaccination, Vaccine, Dose, Carnet


class VaccinationAddForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(VaccinationAddForm, self).__init__()
        try:
            self.fields['carnet'] = forms.ModelChoiceField(queryset=kwargs.pop('queryset'))
        except:
            pass

    vaccine = forms.ModelChoiceField(queryset=Vaccine.objects.all(), required=True)
    type = forms.ChoiceField(choices=Dose.TYPE_CHOICES, required=True)
    date = forms.DateField(widget=forms.SelectDateWidget(years=range(1980, 2050)), required=True, help_text='Required. Format: YYYY-MM-DD')
    next_dose = forms.DateField(widget=forms.SelectDateWidget(years=range(1980, 2050)), help_text='Optional. Format: YYYY-MM-DD')
    batch_number = forms.CharField(max_length=15, required=True)
    verification_code = forms.CharField(max_length=6, required=True, help_text='No "-" or "/"')

    class Meta:
        fields = ('vaccine', 'type', 'batch_number', 'date', 'next_dose', 'verification_code',)

class CreateCarnetForm(forms.ModelForm):

    class Meta:
        model = Carnet
        fields = ('dni', 'name', 'last_name', 'born_date',)