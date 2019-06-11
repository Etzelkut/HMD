# accounts/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render

from .forms import CustomUserCreationForm
# from .models import CustomUser

# def terms_of_use(request):
#     if request.user.is_authenticated:
#         user = CustomUser.objects.get(username=request.user.username)
#         if user.first_login:
#             user.first_login=False
#             user.save()
#             return render(request, '../templates/terms_of_use.html')
#         else:
#             return render(request, '../templates/home.html')
#     else: 
#         return render(request, '../templates/home.html')

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'