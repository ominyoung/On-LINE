from django.db import models


# Create your models here.
class ResultModel(models.Model):
    day = models.IntegerField("day")
    where = models.IntegerField("where", null = True)
    #where = models.ForeignKey('whereModel', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)

    def as_dict(self):
        return {'day': self.day, 'where': self.where}


#class whereModel(models.Model):
#    where_id = models.IntegerField("where", primary_key=True)
#    where_name = models.CharField(max_length=45)
#
#    def __str__(self):
#        return str(self.id)
