from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
import json
import datetime
from .models import * 
from .forms import CreateUserForm
from .utils import cookieCart, cartData, guestOrder
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def homepage(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/homepage.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')

def LoginPage(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			messages.error(request, 'Invalid username or password')

	context = {}
	return render(request, 'store/login.html', context)

def RegisterPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, '! Account was created for	' + user + ' !')
				return redirect('login')

		context = {'form':form}
		return render(request, 'store/register.html', context)

def store(request):
	pastry = Product.objects.filter(category='pastry')
	drink = Product.objects.filter(category='drink')
	combo = Product.objects.filter(category="combo")
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems, 
			'merch': merch, 
			'pastry': pastry, 
			'drink': drink, 
			'combo': combo
			}
	return render(request, 'store/store.html', context)


def cart(request):
	
	data = cartData(request)
	
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	merch = Product.objects.filter(category="merch")
	context = {'items':items, 
			'order':order, 
			'cartItems':cartItems,}
	return render(request, 'store/cart.html', context)


def merch(request):
    data = cartData(request)
    merch = Product.objects.filter(category='merch')
    context = {'merch': merch, 'cartItems': data['cartItems']}
    return render(request, 'store/merch.html', context)


def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)

	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

def gallery(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/gallery.html', context)

def contact(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/contact.html', context)

def submit_form(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f"Name: {name}, Email: {email}, Message: {message}")

        return JsonResponse({'message': 'Form submitted successfully!'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def findcafe(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/findcafe.html', context)

def aboutus(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/aboutus.html', context)
