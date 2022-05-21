from django.contrib import admin
from .models import ResultModel, PlanModel, MemoModel

#, whereModel

# Register your models here.

admin.site.register(ResultModel)
admin.site.register(PlanModel)
admin.site.register(MemoModel)

#admin.site.register(whereModel)