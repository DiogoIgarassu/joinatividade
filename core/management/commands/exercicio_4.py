from empresa.models import Pessoas, Cargos
from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Responde atividade número 4.'

    def handle(self, *args, **kwargs):
        resposta = input("Deseja a resposta de qual alternativa da questão 4 (A/B/C)? ").lower()

        if resposta == 'a':
            self.resposta_a()
        elif resposta == 'b':
            self.resposta_b()
        elif resposta == 'c':
            self.resposta_c()
        else:
            self.stdout.write(self.style.ERROR('Digite uma opção correta (A/B/C).'))

        self.stdout.write(self.style.SUCCESS('\nExecução concluída com sucesso!'))

    def resposta_a(self):

        print("\033[91m", "\nCOM SQL", "\033[00m")
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT empresa_pessoas.nome, empresa_cargos.nome_cargo
                FROM empresa_pessoas
                INNER JOIN empresa_cargos ON empresa_pessoas.id_cargo_id = empresa_cargos.id
                ORDER BY empresa_pessoas.admissao ASC;
            """)
            resultados = cursor.fetchall()
            print(resultados)

        print("\nDados organizados:")
        for resultado in resultados:
            print("\033[92m Nome: \033[94m", resultado[0], "\033[92m Cargo \033[94m", resultado[1])


        resultados = (Pessoas.objects.all().select_related('id_cargo').order_by('admissao')
                      .values('nome', 'id_cargo__nome_cargo'))


        print("\033[91m", "\nCOM ORM - Saída de dados:", "\033[00m", "\n\n", resultados)
        print("\nDados organizados:")

        for resultado in resultados:
            print("\033[92m", "Nome:", "\033[94m",resultado['nome'], "\033[92m", "Cargo", "\033[94m",
                  resultado['id_cargo__nome_cargo'])

    def resposta_b(self):
        print("\033[91m", "\nCOM SQL", "\033[00m")
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT empresa_pessoas.nome, empresa_cargos.nome_cargo
                FROM empresa_pessoas
                INNER JOIN empresa_cargos ON empresa_pessoas.id_cargo_id = empresa_cargos.id
                ORDER BY empresa_pessoas.admissao ASC
                LIMIT 1;
            """)
            resultado = cursor.fetchone()
            print("\nFuncionário mais antigo:")
            print("\033[92m Nome: \033[94m", resultado[0], "\033[92m Cargo \033[94m", resultado[1])

            print("\033[91m", "\nCOM ORM", "\033[00m")
            resultado = (Pessoas.objects.all().select_related('id_cargo')
                         .order_by('admissao').values('nome', 'id_cargo__nome_cargo').first())

            if resultado:
                print("\nFuncionário mais antigo:")
                print("\033[92m", "Nome:", "\033[94m", resultado['nome'], "\033[92m", "Cargo", "\033[94m",
                      resultado['id_cargo__nome_cargo'])
            else:
                print("Não há funcionários registrados.")

    def resposta_c(self):
        print("\033[91m", "\nCOM SQL", "\033[00m")
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT empresa_cargos.nome_cargo, COUNT(empresa_pessoas.id) AS quantidade_funcionarios
                FROM empresa_cargos
                LEFT JOIN empresa_pessoas ON empresa_cargos.id = empresa_pessoas.id_cargo_id
                GROUP BY empresa_cargos.nome_cargo
                ORDER BY empresa_cargos.nome_cargo;
            """)
            resultados = cursor.fetchall()
            print("\nQuantidade de funcionários por cargo:")
            for resultado in resultados:
                print("\033[92m Cargo: \033[94m", resultado[0], "\033[92m Quantidade: \033[94m", resultado[1])

        from django.db.models import Count
        print("\033[91m", "\nCOM ORM", "\033[00m")
        resultados = (Cargos.objects.annotate(quantidade_funcionarios=Count('pessoas'))
                      .values('nome_cargo', 'quantidade_funcionarios')
                      .order_by('nome_cargo'))

        print("\nQuantidade de funcionários por cargo:")
        for resultado in resultados:
            print("\033[92m", "Cargo:", "\033[94m", resultado['nome_cargo'], "\033[92m", "Quantidade", "\033[94m",
                  resultado['quantidade_funcionarios'])


