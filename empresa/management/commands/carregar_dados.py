from django.core.management.base import BaseCommand
import csv
import datetime
from empresa.models import Pessoas, Cargos


class Command(BaseCommand):
    help = 'Carrega dados dos arquivos CSV para o banco de dados'

    def handle(self, *args, **kwargs):
        self.carregar_cargos()
        self.carregar_pessoas()
        self.stdout.write(self.style.SUCCESS('Dados carregados com sucesso!'))

    def carregar_cargos(self):
        with open('cargos.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cargo = Cargos(id=row['id'], nome_cargo=row['nome_cargo'])
                cargo.save()

    def carregar_pessoas(self):
        with open('pessoas.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cargo = Cargos.objects.get(id=row['id_cargo'])
                pessoa = Pessoas(
                    nome=row['nome'],
                    id_cargo=cargo,
                    admissao=datetime.datetime.strptime(row['admissao'], '%Y-%m-%d').date()
                )
                pessoa.save()
