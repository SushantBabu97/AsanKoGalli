from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm


class SignUpView(View):
    def get(self, request):
        context = {
            'form': UserCreationForm(),
        }
        return render(request, 'registration/signup.html', context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        context = {
            'form': form,
        }
        return render(request, 'registration/signup.html', context)


# from django.views import View
# from .models import *
#
#
# class HomepageView(View):
#
#     def get(self, request):
#         context = {
#             'latest_blog': Blog.objects.order_by('-id').all(),
#
#         }
#         return render(request, 'index.html', context)
