# PERSON IN CHARGE: PONCE
# GROUP 11 | CPE106L-B3
from validation import validate_id, require_text, validate_age
class Pet:
    pet_type='Pet'
    def __init__(self,pet_id,name,age,owner_id):
        self.pet_id=validate_id(pet_id,'Pet ID'); self.name=require_text(name,'Pet Name')
        if len(self.name)>40: raise ValueError('Pet Name is invalid. It cannot exceed 40 characters.')
        self.age=validate_age(str(age)); self.owner_id=validate_id(owner_id,'Owner ID')
    def __str__(self): return f'Pet ID: {self.pet_id} | Name: {self.name} | Type: {self.pet_type} | Age: {self.age} | Owner ID: {self.owner_id}'
class Dog(Pet): pet_type='Dog'
class Cat(Pet): pet_type='Cat'
class Bird(Pet): pet_type='Bird'
class Rabbit(Pet): pet_type='Rabbit'
