# JoinAtividade

Projeto destinado a testar habilidades em python, prostgreSQL e Javascript pela empresa Join Tecnologia

## Pré-requisitos

- **Docker**
- **Docker Compose**

## Configuração e Execução

### Configurando o Ambiente

1. **Clonar o Repositório**
   ```bash
   git clone https://github.com/DiogoIgarassu/joinatividade.git
   cd joinatividade
   ```

2. **Construir e Executar com Docker Compose**

```bash
docker-compose up --build
```

Este comando constrói a imagem Docker do projeto (se ainda não foi construída) e inicia os containers definidos no docker-compose.yml.

3. **Executando Migrações do Django**

Para aplicar as migrações do Django, abra um novo terminal e execute:

```bash
python manage.py makemigrations
python manage.py migrate
```
**Carregar Dados**
- Para carregar os dados iniciais no banco de dados, execute:

```bash
python manage.py carregar_dados
```

web é o nome do serviço do seu aplicativo Django no docker-compose.yml.

4. **Acesso**
Após iniciar os containers, o aplicativo estará disponível em:

Aplicativo Django: http://localhost:8000
Administração do PostgreSQL (se aplicável): http://localhost:9090 (ou a porta configurada para o PgAdmin no docker-compose.yml)

**Comandos Úteis**
- Parar os Containers: docker-compose down
- Visualizar Logs: docker-compose logs
- Acessar o Shell do Django: docker-compose exec web python manage.py shell

### Visualizando os Resultados dos Exercícios

* **Exercícios 1-4:** Para visualizar as respostas dos exercícios do 1 ao 4, execute os seguintes comandos:

```bash
python manage.py exercicio_1
python manage.py exercicio_2
python manage.py exercicio_3
python manage.py exercicio_4
```

* **Exercício 7:** Para visualizar o resultado do exercício 7, abra o navegador em http://localhost:8000/hide-box/.
* **Exercício 9:** Para visualizar o resultado do exercício 9, abra o navegador em http://localhost:8000/conteudo/.

