from django import forms

from route.models import ResultModel, MemoModel


class ResultForm(forms.ModelForm):
    day = forms.IntegerField()  # 여행 기간, 의미상 date가 가까움
    where = forms.IntegerField()

    class Meta:
        model = ResultModel
        fields = ("day", "where")


class MemoForm(forms.ModelForm):
    class Meta:
        model = MemoModel
        fields = '__all__'