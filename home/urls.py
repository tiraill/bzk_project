from django.urls import path, include
import home.views as view

urlpatterns = [
    path('account/', include('allauth.urls')),
    path('settings/', include('profiles.urls')),
    path('', view.index_page, name='home'),
]