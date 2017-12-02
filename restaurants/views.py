# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from models import RestaurantReview,Restaurants,Dish
from forms import RestaurantForm, DishForm
from django.views.generic import View 



		
class RestaurantDetail(DetailView):
	model = Restaurants
	template_name = 'myrestaurants/restaurant_detail.html'

	def get_context_data(self, **kwargs):
		context = super(RestaurantDetail, self).get_context_data(**kwargs)
		context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
		return context
	
class RestaurantsCreate(CreateView):
	model = Restaurants
	template_name = 'form.html'
	form_class = RestaurantForm
	
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super (RestaurantsCreate, self).form_valid(form)
		
class DishCreate(CreateView):
	model = Dish 
	template_name = 'form,html'
	form_class = DishForm
	
	def form_valid(self,form):
		form.instance.user = self.request.user
		form.instancde.restaurants = Restaurants.object.get(id=self.kwargs['pk'])
		return super (DishCreate, self).form_valid(form)
		
def review(request, pk):
	restaurants = get_object_or_404(Restaurans, pk=pk)
	review = RestaurantReview(rating=request.POST['rating'], comment=request.POST['comment'],user=request.user,restaurants=restaurants)
	review.save()
	return HttpResponseRedirect(reverse('restaurant_detail', args(restaurants.id)))
	