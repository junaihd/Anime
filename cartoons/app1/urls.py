from.import views
from django.urls import path,include

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('login',views.loginpage,name='loginpage'),
    path('register',views.registerpage,name='registerpage'),
    path('indexx',views.indexpage,name='indexpage'),
    path('anime',views.animepage,name='ani'),
    path('contact',views.contactpage,name='con'),
    path('about',views.aboutpage,name='aboutt'),
    path('movie',views.moviepage,name='moviee'),
    path('api/v1/movie',views.movieapi,name='movieapi'),
    path('api/v2/film',views.filmapi,name='filmapi')
]