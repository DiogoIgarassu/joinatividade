# JoinAtividade

Descrição do seu projeto aqui.

## Pré-requisitos

- **Docker**
- **Docker Compose**

## Configuração e Execução

### Configurando o Ambiente

1. **Clonar o Repositório**
   ```bash
   git clone https://github.com/DiogoIgarassu/joinatividade.git
   cd joinatividade

Construir e Executar com Docker Compose
```docker-compose up --build

Este comando constrói a imagem Docker do projeto (se ainda não foi construída) e inicia os containers definidos no docker-compose.yml.
Executando Migrações do Django
Para aplicar as migrações do Django, abra um novo terminal e execute:

```docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate```


Certamente! Aqui está o texto formatado com as tags de Markdown apropriadas para o arquivo README.md do seu projeto Django "JoinAtividade". Você pode copiar este texto diretamente para o seu README.md:

markdown
Copy code
# JoinAtividade

Descrição do seu projeto aqui.

## Pré-requisitos

- **Docker**
- **Docker Compose**

## Configuração e Execução

### Configurando o Ambiente

1. **Clonar o Repositório**
   ```bash
   git clone https://github.com/DiogoIgarassu/joinatividade.git
   cd joinatividade```

2. **Construir e Executar com Docker Compose**

```bash
docker-compose up --build```

Este comando constrói a imagem Docker do projeto (se ainda não foi construída) e inicia os containers definidos no docker-compose.yml.

3. **Executando Migrações do Django**

Para aplicar as migrações do Django, abra um novo terminal e execute:

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate```

web é o nome do serviço do seu aplicativo Django no docker-compose.yml.

4. **Acesso**
Após iniciar os containers, o aplicativo estará disponível em:

Aplicativo Django: http://localhost:8000
Administração do PostgreSQL (se aplicável): http://localhost:9090 (ou a porta configurada para o PgAdmin no docker-compose.yml)

**Comandos Úteis**
Parar os Containers: docker-compose down
Visualizar Logs: docker-compose logs
Acessar o Shell do Django: docker-compose exec web python manage.py shell
