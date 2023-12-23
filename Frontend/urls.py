from django.urls import path
from Frontend import views

urlpatterns = [

    path('index_pagee/',views.index_pagee,name="index_pagee"),
    path('product_page/',views.product_page,name="product_page"),
    path('catagory_pro/<cat_name>/',views.catagory_pro,name="catagory_pro"),
    path('single_product/<int:pro_id>/',views.single_product,name="single_product"),
    path('contact_us/',views.contact_us,name="contact_us"),
    path('about_us/',views.about_us,name="about_us"),
    path('service/',views.service,name="service"),
    path('contactdata/',views.contactdata,name="contactdata"),

    path('signup_user/',views.signup_user,name="signup_user"),
    path('login_user/',views.login_user,name="login_user"),
    path('signupdata/',views.signupdata,name="signupdata"),
    path('Userlogin/',views.Userlogin,name="Userlogin"),
    path('Userlogout/',views.Userlogout,name="Userlogout"),


    path('cart_page/',views.cart_page,name="cart_page"),
    path('cartdata/',views.cartdata,name="cartdata"),
    path('cart_delete/<int:pro_id>/',views.cart_delete,name="cart_delete"),

    path('checkout_page/',views.checkout_page,name="checkout_page"),
    path('product_search/',views.product_search,name="product_search"),
    path('bookingdata/',views.bookingdata,name="bookingdata"),
    path('payment_product/',views.payment_product,name="payment_product"),



]