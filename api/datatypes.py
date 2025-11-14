import random

from pydantic import BaseModel


class Pet(BaseModel):
    """Pets which are Patted by Pops"""

    id: int
    name: str
    pats: list[Pat]


class Pop(BaseModel):
    """Pops who Pat Pets"""

    id: int
    name: str
    pats: list[Pat]


class Pat(BaseModel):
    """Pats patted on Pets by Pops"""

    id: int
    pet: Pet
    pop: Pop
    quality: int


pets = [
    Pet(id=1001, name="Scruffy", pats=[]),
    Pet(id=1002, name="Bubbles", pats=[]),
    Pet(id=1003, name="Bosco", pats=[]),
    Pet(id=1004, name="Rex", pats=[]),
    Pet(id=1005, name="Kitty", pats=[]),
    Pet(id=1006, name="Pup", pats=[]),
]

pops = [
    Pop(id=2001, name="Pedro", pats=[]),
    Pop(id=2002, name="Lucy", pats=[]),
    Pop(id=2003, name="Mike", pats=[]),
    Pop(id=2004, name="Angela", pats=[]),
    Pop(id=2005, name="Lucas", pats=[]),
    Pop(id=2006, name="Barbara", pats=[]),
]


def get_random_pet(name: str) -> Pet:
    pet = Pet(id=1007, name=name, pats=[])

    for x in range(random.randint(0, 3)):
        pop = pops[x]

        for y in range(random.randint(1, 2)):
            pat = Pat(id=3000 + y + (x * 10), pet=pet, pop=pop, quality=random.randint(0, 5))
            pet.pats.append(pat)
            pop.pats.append(pat)
    return pet


def get_random_pop(name: str) -> Pop:
    pop = Pop(id=2007, name=name, pats=[])

    for x in range(random.randint(0, 3)):
        pet = pets[x]

        for y in range(random.randint(1, 2)):
            pat = Pat(id=3000 + y + (x * 10), pet=pet, pop=pop, quality=random.randint(0, 5))
            pet.pats.append(pat)
            pop.pats.append(pat)
    return pop
