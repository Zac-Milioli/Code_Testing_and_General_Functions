# Utilização do alembic

## Necessidade
- Ter a URL de um banco de dados em um arquivo .env
- Instalar SQLAlchemy

## Comandos principais
`alembic init nome_da_pasta` <- Inicializar a pasta

`alembic revision --autogenerate -m "nome-do-commit"` <- Efetuar commit

`alembic upgrade head` <- Enviar ao banco as atualizações

## Para usar
É necessário abrir uma sessão para interagir com o banco de dados. Para isso basta reproduzir o arquivo em utils/session.py.
Com ela, é só realizar as operações usando `with get_session() as session:`
