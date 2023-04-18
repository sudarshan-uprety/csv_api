from django import forms
from .models import MyModel

class MyModelForm(forms.ModelForm):
    csv_files = forms.FileField()

    class Meta:
        model = MyModel
        fields = ['csv_files']