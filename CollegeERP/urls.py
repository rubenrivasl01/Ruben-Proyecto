from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

class LogoutThenRedirectView(LogoutView):
    http_method_names = ['get', 'post', 'options']
    next_page = '/accounts/login/'

    def get(self, request, *args, **kwargs):
        # Ejecuta la acción de logout y redirige
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('info.urls')),
    path('info/', include('info.urls')),
    path('api/', include('apis.urls')),
    path('accounts/logout/', 
         LogoutThenRedirectView.as_view(), name='logout'),
    path('accounts/login/',
         auth_views.LoginView.as_view(template_name='info/login.html'), name='login'),
]
