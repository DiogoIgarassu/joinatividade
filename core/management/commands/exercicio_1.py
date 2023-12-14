"""
1) Crie uma função que receba uma lista com dados numéricos e strings de números misturados. Retorne
ela ordenada de forma decrescente considerando as strings como valores numéricos. Retorne também o
menor e o maior valor da lista. Considere a melhor performance em sua solução.
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Ordena uma lista mista de números e retorna o maior e o menor valor.'

    def handle(self, *args, **kwargs):
        lista = [9, 2, 95, 28, 0, 73, 81, 91, 71, '22', 6, 21, 1, 47, "52", 35, 68, 29, 66, 91, 81, "99", 40]
        lista_ordenada, menor_valor, maior_valor = self.ordenar_lista_mista(lista)

        print("Lista ordenada:", "\033[94m", lista_ordenada, "\033[00m")
        print("Menor valor:", "\033[91m", menor_valor, "\033[00m")
        print("Maior valor:", "\033[92m", maior_valor, "\033[00m")

    def ordenar_lista_mista(self, lista):
        lista_numerica = [int(item) for item in lista]
        lista_ordenada = sorted(lista_numerica, reverse=True)
        menor_valor = min(lista_ordenada)
        maior_valor = max(lista_ordenada)
        return lista_ordenada, menor_valor, maior_valor





