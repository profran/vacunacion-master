from django import forms
from accounts.models import User
from .models import Vaccination, Vaccine, Dose, Carnet
from django.db.models import Q
import datetime


class VaccinationAddForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(VaccinationAddForm, self).__init__()
        try:
            self.fields['carnet'] = forms.ModelChoiceField(queryset=kwargs.pop('queryset'))
        except:
            pass

    vaccine = forms.ModelChoiceField(queryset=Vaccine.objects.all(), required=True)
    type = forms.ChoiceField(choices=Dose.TYPE_CHOICES, required=True)
    date = forms.DateField(widget=forms.SelectDateWidget(years=range(1980, 2050)), initial=datetime.date.today(), required=True, help_text='Required. Format: YYYY-MM-DD')
    next_dose = forms.DateField(widget=forms.SelectDateWidget(years=range(1980, 2050)), initial=datetime.date.today(), help_text='Optional. Format: YYYY-MM-DD')
    batch_number = forms.CharField(max_length=15, required=True)
    token = forms.CharField(max_length=6, required=True, help_text='No "-" or "/"')

    class Meta:
        fields = ('vaccine', 'type', 'batch_number', 'date', 'next_dose', 'token',)

class CreateCarnetForm(forms.ModelForm):

    dni = forms.CharField(max_length=15, required=False)

    class Meta:
        model = Carnet
        fields = ('dni', 'name', 'last_name', 'born_date',)

class GetCarnetForm(forms.Form):
    dni = forms.CharField(max_length=15, required=True, help_text='Obligatorio. Nombre de usuario o DNI')

    def clean(self):
        cleaned_data = super().clean()
        dni = cleaned_data.get('dni')

        try:
            User.objects.get(Q(dni=dni) | Q(username=dni))
        except:
            self._errors["dni"] = self.error_class(['Usuario con este dni o nombre de usuario no fue encontrado.'])

            del cleaned_data["dni"]

        return cleaned_data

    class Meta:
        fields = ('dni')