from typing import Any

from fastapi import APIRouter

from api.datatypes import Pet, Pop, get_random_pet, get_random_pop

router = APIRouter()


@router.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict[str, Any]:
    return {"item_id": item_id, "q": q}


def get_random_pet_output(pet: Pet) -> dict:
    pet_dict = {
        "id": pet.id,
        "name": pet.name,
        "pats": [],
    }
    for pat in pet.pats:
        pat_dict = {
            "id": pat.id,
            "pop": {
                "id": pat.pop.id,
                "name": pat.pop.name,
            },
            "quality": pat.quality,
        }
        pet_dict["pats"].append(pat_dict)  # type:ignore

    return pet_dict


def get_random_pop_output(pop: Pop) -> dict:
    pop_dict = {
        "id": pop.id,
        "name": pop.name,
        "pats": [],
    }
    for pat in pop.pats:
        pat_dict = {
            "id": pat.id,
            "pet": {
                "id": pat.pet.id,
                "name": pat.pet.name,
            },
            "quality": pat.quality,
        }
        pop_dict["pats"].append(pat_dict)  # type:ignore

    return pop_dict


@router.get("/pets/{name}")
def get_pet(name: str) -> dict:
    pet = get_random_pet(name)
    return get_random_pet_output(pet)


@router.get("/pops/{name}")
def get_pop(name: str) -> dict:
    pet = get_random_pop(name)
    return get_random_pop_output(pet)
