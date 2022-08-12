from django.shortcuts import redirect, render
# from .forms import HomeForm
from django.views.generic.edit import FormView
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'home/home.html', {})

# class HomeView(FormView):
#     form_class = HomeForm
#     form_method = 'post'
#     template_name = 'home/home.html'
    
#     def form_valid(self, request):
#         u = request
#         print(u)
        # self.u = request.POST['username']
        # self.p = request.POST['password1']
        
        # user = authenticate(request,username=self.u,password=self.p)
        # if user is not None:
        #     login(request, user)
        #     return redirect('user:home')