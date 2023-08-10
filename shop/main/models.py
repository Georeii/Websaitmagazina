from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class Product(models.Model):
	name = models.CharField(max_length = 200)
	description = models.TextField()
	description_small = models.CharField(max_length = 400) 
	price = models.FloatField()
	img = models.ImageField( upload_to='images')
	id_catolog = models.IntegerField()
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "товар"
		verbose_name_plural = "товары"

class dop_img_product(models.Model):
	img = models.ImageField( upload_to='images')
	product = models.ForeignKey(Product,on_delete = models.CASCADE)
	def __str__(self):
		return self.product.name
	class Meta:
		verbose_name = "дополнительная фотография"
		verbose_name_plural = "дополнительные фотографии"

class Profil(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,primary_key = True)
	telephone = models.CharField(max_length = 50)
	Date_of_Birth = models.DateField(null=True, blank=True)
	Address_pep = models.CharField(max_length = 100)
	gender = models.CharField(max_length = 10)
	def __str__(self):
		return self.user.first_name
	class Meta:
		verbose_name = "профиль"
		verbose_name_plural = "профили"


class Viewed(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
	product = models.ForeignKey('Product', on_delete = models.CASCADE)
	class Meta:
		verbose_name = "просмотр товара"
		verbose_name_plural = 'просмортры товаров'


class Catolog(models.Model):
	id_catolog = models.IntegerField()
	name = models.TextField()
	img = models.ImageField( upload_to='images/cat')
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "католог"
		verbose_name_plural = "катологи"


class shopping_cart(models.Model):
	product = models.ForeignKey('Product', on_delete = models.CASCADE)
	user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
	class Meta:
		verbose_name = "корзина"
		verbose_name_plural = "корзины"

class order(models.Model):
	product = models.ForeignKey('Product', on_delete = models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
	city = models.TextField()
	street = models.CharField(max_length = 200)
	home = models.CharField(max_length = 200)
	order_status = models.CharField(max_length = 40)
	payment_status = models.CharField(max_length = 50)
	class Meta:
		verbose_name = "Заказ"
		verbose_name_plural = "заказы"