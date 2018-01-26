from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .forms import LoginForm


class LoginView(TemplateView):
    template_name = 'accounts/login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            import pdb;pdb.set_trace()
            user = authenticate(request, username=self.request.POST.get('username'),
                                password=self.request.POST.get('password'))
            if user is not None:
                login(request, user)
                import pdb;pdb.set_trace()