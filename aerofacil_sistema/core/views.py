from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')
from django.shortcuts import render
# --- ADICIONE ESSA NOVA PARTE ---
def confirmacao_view(request):
    # Aqui futuramente você pode pegar os dados do formulário
    return render(request, 'confirmacao.html')