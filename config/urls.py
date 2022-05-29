from django.contrib import admin
from django.urls import path
from django.urls import include
from dj_rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path('admin/', admin.site.urls),
    # rest auth jwt urls 
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     path('list/', include('api.urls')),

]
