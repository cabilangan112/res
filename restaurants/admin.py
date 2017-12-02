# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Restaurants, Dish,  RestaurantReview






admin.site.register	(Restaurants)
admin.site.register	(Dish)
admin.site.register	(RestaurantReview)


