from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
    path('', views.homepage, name="home"),
	path('menu/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('gallery/', views.gallery, name="gallery"),
    path('login/', views.LoginPage, name="login"),
    path('register/', views.RegisterPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('contact/', views.contact, name="contact"),
    path('contact/submit_form/', views.submit_form, name='submit_form'),
    path('findcafe/', views.findcafe, name="findcafe"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('merch/', views.merch, name="merch"),
    

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),

]