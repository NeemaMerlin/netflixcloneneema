from django.urls import path
from . import views

app_name='main'
urlpatterns =[
    path('home',views.main_home,name='main_home'),
    path('about',views.main_about,name='main_about'),
    path('blog',views.main_blog,name='main_blog'),
    path('portfolio',views.main_portfolio,name='main_portfolio'),
    path('contact',views.main_contact,name='main_contact'),
]
