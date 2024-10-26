from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre', views.sobre, name="sobre"),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sobre', views.sobre, name="sobre"),
    path('contato', views.contato, name="contato"),
    path('ajuda', views.ajuda, name="ajuda"),
]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('contato/', views.contato, name='contato'),
]

