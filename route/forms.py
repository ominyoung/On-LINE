from django import forms

from route.models import ResultModel, MemoModel, PlanModel


class PlanForm(forms.ModelForm):
    username = forms.CharField()

    class Meta:
        model = PlanModel
        fields = ("username", )


class ResultForm(forms.ModelForm):
    day = forms.IntegerField()  # 여행 기간, 의미상 date가 가까움
    where = forms.CharField()

    class Meta:
        model = ResultModel
        fields = ("day", "where")


class MemoForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField()
    count = forms.IntegerField()

    class Meta:
        model = MemoModel
        fields = ("title", "content", "count")