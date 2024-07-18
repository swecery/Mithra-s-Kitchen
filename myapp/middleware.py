# myapp/middleware.py

from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class LoginRedirectMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            if request.path in [reverse('login'), reverse('register')]:
                return redirect('home')
        
        if not request.user.is_authenticated:
            if request.path == reverse('reservation'):
                return redirect('login')
        return None