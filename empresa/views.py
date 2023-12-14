from django.shortcuts import render


def hide_box_view(request):
    return render(request, 'empresa/hide_box.html')


def conteudo_view(request):
    return render(request, 'empresa/conteudo.html')
