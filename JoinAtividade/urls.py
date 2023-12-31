"""
URL configuration for JoinAtividade project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from empresa.views import hide_box_view, conteudo_view
from geomaps.views import mapa_view, excluir_alvo

urlpatterns = [
    path('hide-box/', hide_box_view, name='hide-box'),
    path('conteudo/', conteudo_view, name='conteudo'),
    path('', mapa_view, name='mapa'),
    path('excluir-alvo/<int:alvo_id>/', excluir_alvo, name='excluir_alvo'),
    path('admin/', admin.site.urls),
]
