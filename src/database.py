from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from src.models import Base

# Conexão com o banco de dados PostgreSQL
DATABASE_URL = "postgresql+asyncpg://username:password@localhost:5432/main_service_db"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def init_db():
    async with engine.begin() as conn:
        # Criação das tabelas, caso não existam
        await conn.run_sync(Base.metadata.create_all)

# Dependência para obter uma sessão
async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
