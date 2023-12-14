from django.core.management.base import BaseCommand
import csv
import datetime
from empresa.models import Pessoas, Cargos
from geomaps.models import Alvo


class Command(BaseCommand):
    help = 'Carrega dados dos arquivos CSV para o banco de dados'

    def handle(self, *args, **kwargs):
        self.carregar_cargos()
        self.carregar_pessoas()
        self.carregar_alvos()
        self.stdout.write(self.style.SUCCESS('Dados carregados com sucesso!'))

    def carregar_cargos(self):
        with open('cargos.csv', newline='') as csvfile:
            print("\033[94m", "Carregando cargos...", "\033[00m")
            reader = csv.DictReader(csvfile)
            for row in reader:
                cargo = Cargos(id=row['id'], nome_cargo=row['nome_cargo'])
                cargo.save()

    def carregar_pessoas(self):
        with open('pessoas.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            print("\033[93m", "Carregando Pessoas...", "\033[00m")
            for row in reader:
                cargo = Cargos.objects.get(id=row['id_cargo'])
                pessoa = Pessoas(
                    nome=row['nome'],
                    id_cargo=cargo,
                    admissao=datetime.datetime.strptime(row['admissao'], '%Y-%m-%d').date()
                )
                pessoa.save()

    def carregar_alvos(self):
        with open('alvos.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            print("\033[92m", "Carregando Alvos...", "\033[00m")
            for row in reader:
                alvo = Alvo(
                    nome=row['nome'],
                    latitude=float(row['latitude']),
                    longitude=float(row['longitude']),
                    data_expiracao=datetime.datetime.strptime(row['data_expiracao'], '%Y-%m-%d').date()
                )
                alvo.save()
