from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path(r'', views.first_app_index, name="index"),
    path(r'models', views.model_page, name="models"),
    path(r'formpage', views.form_page, name="form_page"),
    path(r'userform', views.new_user_form, name="new_user_form"),

    # User Models
    path('register', views.register, name="register"),
    path('user_login', views.user_login, name="user_login"),
]