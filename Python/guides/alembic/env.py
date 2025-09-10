## No arquivo env.py das migrations, adicionar as seguintes configurações:

# IMPORTAR TABLE_REGISTRY E MODELS
# from src.models.table_registry import table_registry
# from src.models import X

# IMPORTAR DOTENV PARA CARREGAR URL DO BANCO
from dotenv import load_dotenv
import os

from alembic import context

load_dotenv()

config = context.config

# ADICIONAR A URL DO BANCO COMO A PADRÃO
DB_URL = os.getenv("DATABASE_URL")
config.set_main_option("sqlalchemy.url", DB_URL)

# ADICIONAR METADADOS
# target_metadata = table_registry.metadata
