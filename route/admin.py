from django.contrib import admin
from .models import PlanModel, MemoModel, PlaceModel

#, whereModel

# Register your models here.

admin.site.register(PlanModel)
admin.site.register(MemoModel)
admin.site.register(PlaceModel)

#admin.site.register(whereModel)