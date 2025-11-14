from fastapi import APIRouter

from api.datatypes import Pet, Pop, get_random_pet, get_random_pop

router = APIRouter()


type ReturnPet = dict[str, int | str | list[dict[str, int | dict[str, int | str]]]]


def get_random_pet_output(pet: Pet) -> ReturnPet:
    pet_dict: ReturnPet = {
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


type ReturnPop = dict[str, int | str | list[dict[str, int | dict[str, int | str]]]]


def get_random_pop_output(pop: Pop) -> ReturnPop:
    pop_dict: ReturnPop = {
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
def get_pet(name: str) -> ReturnPet:
    pet = get_random_pet(name)
    return get_random_pet_output(pet)


@router.get("/pops/{name}")
def get_pop(name: str) -> ReturnPop:
    pet = get_random_pop(name)
    return get_random_pop_output(pet)
