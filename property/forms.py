from django import forms
from .models import PropertyBook


class PropertyBookForm(forms.ModelForm):
   class Meta:
       model =PropertyBook
       fields =['date_form','date_to','childern','guest']

