from django.conf.urls import url
from django.utils import timezone
from . import views
from django.views.generic import DetailView, ListView, UpdateView
from models import Restaurants, Dish
from forms import RestaurantForm, DishForm
from views import RestaurantsCreate, DishCreate,RestaurantDetail


urlpatterns = [
	url(r'\^\$',ListView.as_view(queryset=Restaurants.objects.filter(date__lte=timezone.now()).order_by('date')[:5],context_object_name='latest_restaurant_list', template_name=' restaurant_list.html'), name='restaurant_list'),	
	
	url(r'^restaurants/(?P<pk>\d+)/\$',RestaurantDetail.as_view(), name='restaurant_detail'),
		
	url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/\$',DetailView.as_view(model=Dish, template_name='myrestaurants/dish_detail.html'),name='dish_detail'),
	
	url(r'^restaurants/create/\$',RestaurantsCreate.as_view(),name='restaurant_create'),
	
	url(r'^restaurants/(?P<pk>\d+)/edit/\$',UpdateView.as_view(model = Restaurants, template_name = 'myrestaurants/form.html',form_class = RestaurantForm),
        name='restaurant_edit'),

	url(r'^restaurants/(?P<pk>\\d+)/dishes/create/\$',
    	DishCreate.as_view(),
        name='dish_create'),		
	
]