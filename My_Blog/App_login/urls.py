from django.urls import path
from . import views

app_name = 'APP_Login'

urlpatterns = [
    path('sign_up/',views.sign_up,name="sign_up"),
    path('signin/',views.login_page,name="signin"),
    path('logout/',views.logout_user, name="logout"),  
    path('profile/',views.profile,name="ViewProfile"),
    path('change/',views.user_change,name="user_change"),
    path('password/',views.password_change,name="pass_change"),
    path('changeimage/',views.add_pro_pic,name="add_pro_pic"),
    path('changeprofileimage/',views.change_pro_pic,name="change_pro_pic"),
   
]
