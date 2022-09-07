from django.contrib import admin
from .models import PlanModel, MemoModel, PlaceModel,ReviewModel

#, whereModel

# Register your models here.

admin.site.register(PlanModel)
admin.site.register(MemoModel)
admin.site.register(PlaceModel)
admin.site.register(ReviewModel)

#admin.site.register(whereModel)