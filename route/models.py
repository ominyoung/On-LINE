from django.db import models

# Create your models here.

# class Privacy(models.Model):
#     id = models.CharField(primary_key=True, max_length=45)
#     password = models.CharField(max_length=45, blank=True, null=True)
#     name = models.CharField(max_length=45, blank=True, null=True)
#     phone_num = models.IntegerField(blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)

#         managed = False
#         db_table = 'privacy'


# class Route(models.Model):
#     id = models.IntegerField(primary_key=True)
#     line_number = models.IntegerField(blank=True, null=True)
#     start_point = models.IntegerField(blank=True, null=True)
#     end_point = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'route'