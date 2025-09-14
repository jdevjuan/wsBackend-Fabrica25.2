# wsBackend-Fabrica25.2
# Lista de Tarefas (Django)

Este é um projeto de uma Lista de Tarefas, feito com Django e Django REST Framework.  
Aqui você consegue criar sua conta, adicionar tarefas, marcar como concluídas, editar ou excluir.  
Também tem uma API para manipular tarefas, caso queira usar com outro app ou fazer testes.

---

## Funcionalidades

- Criar conta e fazer login
- Adicionar, editar e excluir tarefas
- Marcar tarefas como concluídas
- Página inicial simples com HTML e CSS
- API para listar, criar, atualizar e excluir tarefas

## Como rodar o projeto

1. (Clone o repositório:)

2. Entre na pasta do projeto:
cd projeto

3. Crie um ambiente virtual (para não bagunçar o Python do sistema):
python -m venv venv

4. Ative o ambiente virtual:
Windows:
venv\Scripts\activate

5. Instale as dependências:
pip install django djangorestframework

6. Rode as migrações para criar o banco de dados:
python manage.py migrate

7. Crie um superusuário (opcional, para acessar o admin):
python manage.py createsuperuser

8. Inicie o servidor:
python manage.py runserver

9. Abra no navegador:
http://127.0.0.1:8000/

Como usar:
Faça signup e crie sua conta
Faça login
Adicione tarefas com título e status
Edite ou exclua tarefas quando quiser
Veja todas as tarefas na página inicial


API REST:
Todas as rotas exigem login. Aqui estão:
Método	       Endpoint              	O que faz
GET	         /api/tasks/	            Lista todas as suas tarefas
POST	     /api/tasks/create/	         Cria uma tarefa nova
PUT	   /api/tasks/update/<id>/	   Atualiza uma tarefa existente
DELETE	/api/tasks/delete/<id>/   	Deleta uma tarefa


Exemplo de JSON para criar ou atualizar uma tarefa:
{
    "title": "Nova tarefa",
    "completed": false
}
