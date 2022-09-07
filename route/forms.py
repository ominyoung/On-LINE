from django import forms

from route.models import MemoModel, PlanModel, ReviewModel


class PlanForm(forms.ModelForm):
    username = forms.CharField()

    class Meta:
        model = PlanModel
        fields = ("username", )


class MemoForm(forms.ModelForm):
    title = forms.CharField()
    content = forms.CharField()
    count = forms.IntegerField()

    class Meta:
        model = MemoModel
        fields = ("title", "content", "count")

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewModel
        fields = '__all__'