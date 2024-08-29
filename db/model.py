from sqlalchemy.orm import registry,Mapped,mapped_column
from db.connection import engine

table_registry = registry()

@table_registry.mapped_as_dataclass
class User():
    __tablename__="User"
    
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True,init=False)    
    name:Mapped[str] = mapped_column(nullable=False)
    email:Mapped[str] = mapped_column(nullable=False)
    password:Mapped[str] = mapped_column(nullable=False)
    cpf_cnpj:Mapped[str] = mapped_column(nullable=True)
    is_active:Mapped[bool] = mapped_column(nullable=False,default=True)


table_registry.metadata.create_all(engine)
