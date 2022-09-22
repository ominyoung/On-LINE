from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class PlanModel(models.Model):
    username = models.CharField(max_length=100)
    startdate = models.DateField()
    enddate = models.DateField()

    def __str__(self):
        return f'[{self.pk}] :: {self.username}'


class MemoModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    count = models.IntegerField("count")

    plan_pk = models.ForeignKey(PlanModel, null=True, blank=True, on_delete=models.SET_NULL)
    username = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pk}] :: {self.title}'


class PlaceModel(models.Model):
    place_name = models.CharField(max_length=50)
    place_address = models.CharField(max_length=150)
    latitude = models.CharField(max_length=50)
    longtitude = models.CharField(max_length=50)
    count = models.IntegerField("count")

    plan_pk = models.ForeignKey(PlanModel, null=True, blank=True, on_delete=models.SET_NULL)
    username = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pk}] :: {self.place_name}'

# 나의 여행 일기
class ReviewModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='author_review')
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    # 사진
    photo = models.ImageField(blank=True, null=True)
    # 추천수
    voter = models.ManyToManyField(User, related_name='voter_review')