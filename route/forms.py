from django import forms

from route.models import ResultModel


class ResultForm(forms.ModelForm):
    day = forms.IntegerField()
    where = forms.IntegerField()

    class Meta:
        model = ResultModel
        fields = ("day", "where")
