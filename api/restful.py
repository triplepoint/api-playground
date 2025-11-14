from fastapi import APIRouter

from api.datatypes import (
    ReturnPet,
    ReturnPop,
    get_random_pet,
    get_random_pet_output,
    get_random_pop,
    get_random_pop_output,
)

router = APIRouter()


@router.get("/pets/{name}")
def get_pet(name: str) -> ReturnPet:
    pet = get_random_pet(name)
    return get_random_pet_output(pet)


@router.get("/pops/{name}")
def get_pop(name: str) -> ReturnPop:
    pet = get_random_pop(name)
    return get_random_pop_output(pet)
