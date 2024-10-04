from sqlmodel import SQLModel
from core.database import engine

# Função para criar as tabelas no banco de dados
async def create_tables() -> None:
    # Importa todos os modelos
    import models.__all_models
    print('Criando as tabelas')

    # Cria as tabelas
    async with engine.begin() as conn:
        # Dropar as tabelas, se já existirem (cuidado em produção)
        await conn.run_sync(SQLModel.metadata.drop_all)
        # Criar as tabelas
        await conn.run_sync(SQLModel.metadata.create_all)
    print('Tabelas criadas')

# Ponto de entrada quando o script for executado diretamente
if __name__ == '__main__':
    import asyncio
    # Executa a função create_tables com o asyncio
    asyncio.run(create_tables())