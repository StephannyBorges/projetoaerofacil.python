from django.contrib import admin
from django.urls import path
from core import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rota Raiz (Página Inicial)
    path('', views.index_view, name='index'),

    # Rotas das outras páginas
    path('resultados/', views.resultados_view, name='resultados'),
    path('selecionar-assento/', views.selecionar_assento_view, name='selecionar_assento'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]