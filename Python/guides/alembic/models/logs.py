from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func
from .table_registry import table_registry
from pydantic import BaseModel
from typing import ClassVar

@table_registry.mapped_as_dataclass
class LogModel:
    __tablename__                   = "logs"
    id: Mapped[int]                 = mapped_column(init=False, primary_key=True)
    log_type: Mapped[str]           = mapped_column(init=True)
    description: Mapped[str]        = mapped_column(init=True)
    user: Mapped[str]               = mapped_column(init=True, nullable=True, default=None)
    dataAdicao: Mapped[datetime]    = mapped_column(init=True, default=func.now())

class LogType(BaseModel):
    TEST: ClassVar[str]             = "TEST"
    REPORT: ClassVar[str]           = "REPORT"
    ERROR: ClassVar[str]            = "ERROR"
    REQUEST_ERROR: ClassVar[str]    = "REQUEST_ERROR"
    INFO: ClassVar[str]             = "INFO"
    WARNING: ClassVar[str]          = "WARNING"

    @classmethod
    def get_all_types(cls):
        types = [
            attr_name
            for attr_name, attr_value in cls.__dict__.items()
            if isinstance(attr_value, str) and attr_name.isupper()
        ]
        return types
