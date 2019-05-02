from .import_libs import *
from .models import *
from django import forms
''' Forms '''

class RecallForm(forms.Form):
    date_next = forms.DateField(required=False)
