from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# vue.js 단 결과를 json으로, 나중에 drf로 바꿀 예정
class ResultModel(models.Model):
    day = models.IntegerField("day")
    where = models.CharField(max_length=100)
    #where = models.ForeignKey('whereModel', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)

    #def as_dict(self):
    #    return {'day': self.day, 'where': self.where}


#class whereModel(models.Model):
#    where_id = models.IntegerField("where", primary_key=True)
#    where_name = models.CharField(max_length=45)
#
#    def __str__(self):
#        return str(self.id)

class PlanModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    """
    def __str__(self):
        return f'[{self.pk}] :: {self.username}'
    """

class MemoModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    count = models.IntegerField("count")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    plan_pk = models.ForeignKey(PlanModel, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}] :: {self.title}'