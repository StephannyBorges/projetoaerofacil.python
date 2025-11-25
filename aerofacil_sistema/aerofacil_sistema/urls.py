from django.contrib import admin
from django.urls import path
from core import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rota para a página de Login/Busca (Página inicial)
    path('', views.login_view, name='login'),

    # Rota para a página de Confirmação
    path('confirmacao/', views.confirmacao_view, name='confirmacao'),
    path('detalhes/', views.detalhes_view, name='detalhes'),
]
# aerofacil_sistema/aerofacil_sistema/urls.py
from django.contrib import admin
from django.urls import path
from core import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('confirmacao/', views.confirmacao_view, name='confirmacao'),
    
    # --- NOVA ROTA AQUI ---
    path('detalhes/', views.detalhes_view, name='detalhes'),
]