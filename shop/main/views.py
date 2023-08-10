from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect 
from .models import Catolog, Product,dop_img_product, Profil
from .forms import  UserRegistrationForm,UserSingForm
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
			return render(request, 'main/register_done.html', {'new_user': new_user})
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
					return HttpResponseRedirect("personal_area")
				else:
					return HttpResponse('Disabled account')
			else:
				return HttpResponse('Invalid login')
	else:
		return HttpResponseRedirect("personal_area")

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


def shopping_cart():
	pass


def personal_area(request):
	profils = Profil.objects.filter(user = request.user)
	for profil in profils:
		return render(request, "main/personal_area.html",{"profil":profil})

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
		return HttpResponseRedirect("/personal_area")
