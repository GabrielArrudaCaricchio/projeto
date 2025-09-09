from django.shortcuts import render

def home(request): 
    return render(request, 'site/index.html')
#se quiser alterar qual arquivo será a home basta trocar o index.html pelo nome do arquivo (fazer isso dentro da função)