""" 2) Crie uma função que receba qualquer número e retorne o fatorial deste número """
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Calcula o fatorial de um número.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Digite um número para calcular seu fatorial:'))
        while True:
            try:
                numero = int(input())
                calculo, numero_fatorial = self.calcular_fatorial(numero)
                print("\033[92m", "\nComo é feito o cálculo: ")
                print(calculo, "\033[94m", numero_fatorial)
                self.stdout.write(self.style.SUCCESS(str(numero_fatorial)))
                break
            except ValueError:
                print("\033[91m", "Opção Inválida!!!", "\033[93m")

    def calcular_fatorial(self, numero):
        calculo = str(numero) + "! = "
        fatorial = 1

        for i in range(numero, 0, -1):
            fatorial *= i
            calculo += str(i) + " x " if i != 1 else str(i) + " ="

        return calculo, fatorial
