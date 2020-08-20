"""Smanagment middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse


class UserisAuthentication:
    """UserisAuthentication middleware.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            if request.path in [reverse('login')]:
                return redirect('feed')

        response = self.get_response(request)
        return response
