from django.contrib import admin

from model.models.many2many.intermediate import Idol, Group, Membership
from model.models.many2many.self_asymmetric import InstagramUser
from model.models.many2many.self_symmetric import FacebookUser
from model.models.many2many.basic import Pizza, Topping
from model.models.one_to_one import Restaurant, Place
from .models import (
    Manufacturer,
    Car,
    User)

admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(User)

admin.site.register(Pizza)
admin.site.register(Topping)

admin.site.register(FacebookUser)
admin.site.register(InstagramUser)

admin.site.register(Idol)
admin.site.register(Group)
admin.site.register(Membership)

admin.site.register(Place)
admin.site.register(Restaurant)