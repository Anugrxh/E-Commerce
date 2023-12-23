from django.urls import path
from AdminApp import views
urlpatterns = [
    path('indexx/',views.indexx,name="indexx"),
    path('add_cat/',views.add_cat,name="add_cat"),
    path('catdata/',views.catdata,name="catdata"),
    path('display_cat/',views.display_cat,name="display_cat"),
    path('edit_catagory/<int:dataid>/',views.edit_catagory,name="edit_catagory"),
    path('update_catagory/<int:dataid>/',views.update_catagory,name="update_catagory"),
    path('delete_catagory/<int:dataid>/',views.delete_catagory,name="delete_catagory"),

    path('add_product/',views.add_product,name="add_product"),
    path('productdata/',views.productdata,name="productdata"),
    path('product_display/',views.product_display,name="product_display"),
    path('product_delete/<int:dataid>/',views.product_delete,name="product_delete"),
    path('Product_edit/<int:pro_id>/',views.Product_edit,name="Product_edit"),
    path('product_update/<int:pro_id>/',views.product_update,name="product_update"),

    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),

    path('contact_suggestion/',views.contact_suggestion,name="contact_suggestion"),
    path('bookingsss/',views.bookingsss,name="bookingsss"),
    path('delete_contact_suggestion/<int:dataid>/',views.delete_contact_suggestion,name="delete_contact_suggestion"),

]