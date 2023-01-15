from django import forms
from charityorganization.models import Charityorg

class charityForm(forms.ModelForm):


    class Meta:
        model = Charityorg
        fields = "__all__"