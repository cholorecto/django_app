from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import LoginForm
from django.contrib import messages


class LoginView(TemplateView):
    template_name = 'accounts/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            user = authenticate(request, username=self.request.POST.get('username'),
                                password=self.request.POST.get('password'))
            if user is not None:
                login(request, user)
                return redirect('dashboard')

        context = {'form':form}
        messages.warning(request, 'Invalid credentials.')
        return render(request, self.template_name, context)


class LogoutView(View):
    def get(self, request):
        if self.request.user.is_authenticated:
            logout(self.request)
            return redirect('login')