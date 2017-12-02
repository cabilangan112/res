from django.forms import ModelForm
from models import Restaurants, Dish

class RestaurantForm(ModelForm):
  class Meta:
    model = Restaurants
    exclude = ('user', 'date',)

class DishForm(ModelForm):
  class Meta:
    model = Dish
    exclude = ('user', 'date', 'restaurant',)