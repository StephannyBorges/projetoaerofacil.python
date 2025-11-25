from django.shortcuts import render

# 1. Página Inicial (index.html)
def index_view(request):
    return render(request, 'index.html')

# 2. Página de Resultados (resultados.html)
def resultados_view(request):
    # Aqui futuramente filtraremos os voos reais
    return render(request, 'resultados.html')

# 3. Página de Seleção de Assento (selecionar-assento.html)
def selecionar_assento_view(request):
    return render(request, 'selecionar-assento.html')

# 4. Dashboard (dashboard.html)
def dashboard_view(request):
    return render(request, 'dashboard.html')