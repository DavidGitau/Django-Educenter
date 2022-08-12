from django.urls import path, include
from .views import home
from django.contrib.auth.views import LoginView

app_name = 'main'
urlpatterns = [
    path('', home, name='home'), 
    # path('', LoginView.as_view(template_name='home/home.html'))
]