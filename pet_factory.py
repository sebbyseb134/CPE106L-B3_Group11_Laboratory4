# PERSON IN CHARGE: PONCE
# GROUP 11 | CPE106L-B3
from pets import Dog,Cat,Bird,Rabbit
class PetFactory:
    _pet_classes={'dog':Dog,'cat':Cat,'bird':Bird,'rabbit':Rabbit}
    @staticmethod
    def create_pet(pet_type,pet_id,name,age,owner_id):
        key=pet_type.strip().lower()
        if key not in PetFactory._pet_classes: raise ValueError('Pet Type is invalid. Choose only Dog, Cat, Bird, or Rabbit.')
        return PetFactory._pet_classes[key](pet_id,name,age,owner_id)
