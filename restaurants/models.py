from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

class Restaurants(models.Model):
	name 	  		=  models.CharField(max_length=200)
	street    	    =  models.CharField(max_length=200, blank=True, null=True)
	number      	=  models.IntegerField(blank=True, null=True)
	city			=  models.CharField(max_length=200, default="")
	ZipCode 		=  models.CharField(max_length=200, blank=True, null=True)
	StateOrProvince =  models.CharField(max_length=200, blank=True, null=True)
	Country 		=  models.CharField(max_length=200, blank=True, null=True)
	Telephone 		=  models.CharField(max_length=200, blank=True, null=True)
	url				=  models.URLField(blank=True, null=True)
	user			=  models.ForeignKey(User, default=1)
	Date 			=  models.DateField(default=date.today)
	
	def __unicode__(self):
		return u"%s" % self.name
		
class Dish(models.Model):
    name 			= models.CharField(max_length=200)
    description 	= models.CharField(max_length=200, blank=True, null=True)
    price 			= models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True, null=True)
    user		 	= models.ForeignKey(User, default=1)
    date			= models.DateField(default=date.today)
    image 			= models.ImageField(upload_to="Dish", blank=True, null=True)
    restaurant 		= models.ForeignKey(Restaurants, null=True, related_name='dishes')

    def __unicode__(self):
        return u"%s" % self.name

class Review(models.Model):
    RATING_CHOICES 	= ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating 			= models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment 		= models.TextField(blank=True, null=True)
    user 			= models.ForeignKey(User, default=1)
    date 			= models.DateField(default=date.today)

    class Meta:
        abstract = True

class RestaurantReview(Review):
    restaurant = models.ForeignKey(Restaurants)