from django.urls import path, include

captcha_urlpatterns = [
    path('captcha/',include('captcha.urls')),

]