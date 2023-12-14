from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .forms import AlvoForm
from .models import Alvo
from django.core import serializers
import json


def mapa_view(request):
    if request.method == 'POST':
        form = AlvoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mapa')
    else:
        form = AlvoForm()

    alvos = Alvo.objects.all()
    alvos_json = serializers.serialize('json', alvos)
    return render(request, 'geomaps/maps.html', {'alvos': alvos_json, 'fomr': form})


def excluir_alvo(request, alvo_id):
    # Certifique-se de que somente requisições POST sejam aceitas
    if request.method == 'POST':
        alvo = get_object_or_404(Alvo, id=alvo_id)
        alvo.delete()
        return JsonResponse({'status': 'success', 'message': 'Alvo excluído com sucesso.'})

    return JsonResponse({'status': 'error', 'message': 'Método inválido.'})
