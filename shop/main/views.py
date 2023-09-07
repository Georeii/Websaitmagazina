from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .models import *
from .forms import  *
from django.contrib.auth import login, authenticate

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			# -----------------
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			# register user---------^
			new_profil = Profil()
			new_profil.telephone = request.POST.get("telephone")
			new_profil.Date_of_Birth = request.POST.get("Date_of_Birth")
			new_profil.Address_pep = request.POST.get("Address")
			new_profil.gender = request.POST.get("gender")
			new_profil.user=new_user
			new_profil.save()
			# -----------------
			hopping_cart = Shopping_cart()
			hopping_cart.user = new_user
			hopping_cart.save()
			return HttpResponseRedirect("/",{"sms":"Вы зарегистрировались"})
		else:
			user_form = UserRegistrationForm()
			return render(request, 'main/register.html', {'user_form': user_form,"sms":"такое имя пользователя уже есть"})
	else:
		user_form = UserRegistrationForm()
		return render(request, 'main/register.html', {'user_form': user_form})



def Login_sing(request):
	if request.method == "POST":
		form = UserSingForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect("/")
				else:
					form = UserSingForm()
					return render(request, "main/login.html",{"form":form,"sms":"Акаунт не найден"})
			else:
				form = UserSingForm()
				return render(request, "main/login.html",{"form":form,"sms":"пароль или логин введен не правильно"})	
	else:
		form = UserSingForm()
		return render(request, "main/login.html",{"form":form})

def catalog(request):
	catolog = Catolog.objects.all()
	return render(request, "main/catalog.html",{'catolog': catolog})


def products(request,id):
	product = Product.objects.filter(id_catolog = id)
	return render(request, "main/products.html",{'product': product})


def product_car(request,ids):
	product_osn = Product.objects.get(id = ids)
	try:
		dop_img = dop_img_product.objects.filter(product=product_osn)
		kol = []
		for i in range(0, dop_img.count()):
			kol.append(i+1)
		return render(request, "main/product.html",{'product_osn': product_osn,"dop_img":dop_img,"kol":kol})
	except:
		return render(request, "main/product.html",{'product_osn': product_osn})

def add_shopping_cart(request,ids):
	# if request.method == "POST":

	hopping_cart = Shopping_cart.objects.filter(user = request.user)
	for i in hopping_cart:
		shopping_cart_add = i
	col = request.POST.get("col")
	products = Product.objects.get(id = ids)

	product_block_sc = Product_Block_SC()
	product_block_sc.product = products
	product_block_sc.col_product = col
	product_block_sc.shopping_cart = shopping_cart_add
	product_block_sc.save()
	return HttpResponseRedirect(f"/product/{ids}")


def shopping_cart(request):
	dictionary = {}
	if request.user.is_authenticated == True:
		shopping_cart = Shopping_cart.objects.get(user = request.user)
		product_block_sc = Product_Block_SC.objects.filter(shopping_cart = shopping_cart)
		if product_block_sc.count() != 0:
			product_price = 0
			product = []
			for i in product_block_sc:
				product_price += i.product.price * i.col_product
				product.append(i.product)
				dictionary["price"] = product_price
				dictionary["products"] =  product
		else:
			dictionary["sms"] = "Добавьте товаров в корзину"
		orders = Order.objects.filter(user = request.user)
		if orders != 0:
			# print(orders)
			product_block_o = []
			for j in orders:
				s = Product_Block_O.objects.filter(order = j)
				if s.count() != 0:
					product_block_o.append( s)
		product_order = []
		price_order = 0
		print(product_block_o)
		for i in product_block_o:
			for j in i:
			
				print(j)
				product_order.append(j.product)
		dictionary["product_order"] = product_order
		dictionary["orders"] = orders
	else:
		dictionary["sms"] = "Войдите в акаунт"
		# return render(request, "main/shopping_cart.html",{"sms":"Войдите в акаунт"})
	# try:
	


		# return render(request, "main/shopping_cart.html",{"price":product_price,"products":product,"price_order":price_order,"product_order":product_order,"orders":orders})
	# except:
	print(dictionary)
	return render(request, "main/shopping_cart.html",dictionary)
	

def personal_area(request):
	try:
		profils = Profil.objects.filter(user = request.user)
		for profil in profils:
			return render(request, "main/personal_area.html",{"profil":profil})
	except:
		return render(request, "main/personal_area.html")


def changing_user_data(request):
	if request.method == 'POST':
		# -----------------
		user = User.objects.get(id = request.user.id)
		user.username = request.POST.get("username")
		user.first_name = request.POST.get("first_name")
		user.last_name = request.POST.get("last_name")
		user.email = request.POST.get("email")
		user.save()
		# user---------^
		profil = Profil.objects.filter(user = user)
		for i in profil:
			i.telephone = request.POST.get("telephone")
			i.Date_of_Birth = request.POST.get("Date_of_Birth")
			i.Address_pep = request.POST.get("Address")
			i.gender = request.POST.get("gender")
			i.save()
		return HttpResponseRedirect("/")

def order_user_data(request):
	if request.user.is_authenticated == True and request.method == 'POST':
		shopping_cart = Shopping_cart.objects.get(user = request.user)
		product_block_sc = Product_Block_SC.objects.filter(shopping_cart = shopping_cart)
		order = Order()
		order.user = request.user
		order.city = request.POST.get("city")
		order.street = request.POST.get("street")
		order.home = request.POST.get("home")
		order.order_status = 2
		order.payment_status = 1
		order.save()
		for product_block_s in product_block_sc:
			product_block_o = Product_Block_O()
			product_block_o.product = product_block_s.product
			product_block_o.col_product = product_block_s.col_product
			product_block_o.order = order
			product_block_o.save()
			product_block_s.delete()
		return HttpResponseRedirect("/shopping_cart",{"sms":"заказ зарегистрирован"})
