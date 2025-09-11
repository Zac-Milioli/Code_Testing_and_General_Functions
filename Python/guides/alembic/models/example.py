from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func, JSON
from sqlalchemy.dialects.postgresql import JSONB
from .table_registry import table_registry

@table_registry.mapped_as_dataclass
class ExampleModel:
    __tablename__                   = "example"
    id: Mapped[int]                 = mapped_column(init=False, primary_key=True)
    numero: Mapped[str]             = mapped_column(init=True)
    tipoNumero: Mapped[str]         = mapped_column(init=True)
    data: Mapped[dict]              = mapped_column(JSON, init=True)
    dataBinary: Mapped[dict]        = mapped_column(JSONB, init=True)
    dataAdicao: Mapped[datetime]    = mapped_column(init=True, default=func.now())
