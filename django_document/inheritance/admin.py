from django.contrib import admin

# Register your models here.
from .models.proxy import Champion
from .models import (
    Place,
    Restaurant,
)
from .models.abstract_base_class import (
    Student,
    Teacher,
    School,
)

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(School)

admin.site.register(Place)
admin.site.register(Restaurant)

admin.site.register(Champion)