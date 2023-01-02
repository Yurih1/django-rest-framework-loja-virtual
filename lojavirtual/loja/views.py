from django.http import JsonResponse

def itens_loja(request):
    
    if request.method == 'GET':
        roupas = {
            "tipo": "calça",
            "preco": 50,
            "descrição": "jeans"
        }
    return JsonResponse(roupas)
