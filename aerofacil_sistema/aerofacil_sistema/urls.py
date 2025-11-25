from django.contrib import admin
from django.urls import path
from core import views  # <--- ESSA LINHA ERA A QUE FALTAVA!

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rota para a página de Login/Busca (Página inicial)
    path('', views.login_view, name='login'),

    # Rota para a página de Confirmação
    path('confirmacao/', views.confirmacao_view, name='confirmacao'),
]