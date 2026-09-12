class ClinicDatabase:
    _instance=None
def __new__(cls):
        if cls._instance is None:
            cls._instance=super().__new__(cls); cls._instance._initialized=False
        return cls._instance
def __init__(self):
        if self._initialized: return
        self.owners={}; self.pets={}; self.appointments={}; self._initialized=True
def add_owner(self,owner):
        if owner.owner_id in self.owners: raise ValueError('Owner ID already exists. Use a different Owner ID.')
        self.owners[owner.owner_id]=owner
def get_owner(self,owner_id): return self.owners.get(owner_id)
def add_pet(self,pet):
        if pet.pet_id in self.pets: raise ValueError('Pet ID already exists. Use a different Pet ID.')
        if pet.owner_id not in self.owners: raise ValueError('Pet cannot be added because the selected Owner ID does not exist.')
        self.pets[pet.pet_id]=pet; self.owners[pet.owner_id].add_pet(pet)
def get_pet(self,pet_id): return self.pets.get(pet_id)
def add_appointment(self,a):
        if a.appointment_id in self.appointments: raise ValueError('Appointment ID already exists. Use a different Appointment ID.')
        if a.owner_id not in self.owners: raise ValueError('Appointment cannot be scheduled because the Owner ID does not exist.')
        if a.pet_id not in self.pets: raise ValueError('Appointment cannot be scheduled because the Pet ID does not exist.')
        if self.pets[a.pet_id].owner_id != a.owner_id: raise ValueError('Appointment is invalid. The selected pet does not belong to the selected owner.')
        for e in self.appointments.values():
            if e.status=='Scheduled' and e.pet_id==a.pet_id and e.date==a.date and e.time==a.time: raise ValueError('Appointment conflicts with another scheduled appointment for this pet.')
        self.appointments[a.appointment_id]=a
def get_appointment(self,appointment_id): return self.appointments.get(appointment_id)
def clear(self): self.owners.clear(); self.pets.clear(); self.appointments.clear()