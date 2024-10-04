from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response
from sqlalchemy.ext.asyncio import AsyncSession
from core.deps import get_session
from sqlmodel import select
from models.zoo_model import Zoo

router = APIRouter()

# POST /animais/
# Rota para criar um novo animal
@router.post("/animais", status_code=status.HTTP_201_CREATED, response_model=Zoo)
async def post_animal(animal: Zoo, db: AsyncSession = Depends(get_session)):
    novo_animal = Zoo(
        nome=animal.nome,
        especie=animal.especie,
        idade=animal.idade,
        habitat=animal.habitat
    )
    db.add(novo_animal)
    await db.commit()
    await db.refresh(novo_animal)
    return novo_animal

# GET /animais/
# Rota para buscar todas os animais
@router.get("/", response_model=List[Zoo])
async def get_animais(db: AsyncSession = Depends(get_session)):
    query = select(Zoo)
    result = await db.execute(query)
    animais: List[Zoo] = result.scalars().all()
    return animais

# GET /animais/{animal_id}
# Rota para buscar um animal específico pelo ID
@router.get("/animais/{animal_id}", response_model=Zoo)
async def get_animal(animal_id: int, db: AsyncSession = Depends(get_session)):
    query = select(Zoo).where(Zoo.id == animal_id)
    result = await db.execute(query)
    animal = result.scalar_one_or_none()
    if animal is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")
    return animal

# PUT /animais/{animal_id}
# Rota para atualizar um animal específico pelo ID
@router.put("/animais/{animal_id}", response_model=Zoo)
async def update_animal(animal_id: int, animal: Zoo, db: AsyncSession = Depends(get_session)):
    query = select(Zoo).where(Zoo.id == animal_id)
    result = await db.execute(query)
    animal_db = result.scalar_one_or_none()
    if animal_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")
    
    animal_db.nome = animal.nome
    animal_db.especie = animal.especie
    animal_db.idade = animal.idade
    animal_db.habitat = animal.habitat

    await db.commit()
    await db.refresh(animal_db)
    return animal_db

# DELETE /animais/{animal_id}
# Rota para deletar um animal específico pelo ID
@router.delete("/animais/{animal_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_animal(animal_id: int, db: AsyncSession = Depends(get_session)):
    query = select(Zoo).where(Zoo.id == animal_id)
    result = await db.execute(query)
    animal = result.scalar_one_or_none()
    if animal is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")
    
    await db.delete(animal)
    await db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)