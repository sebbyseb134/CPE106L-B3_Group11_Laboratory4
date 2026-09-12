# PERSON IN CHARGE: SOMERA
# GROUP 11 | CPE106L-B3
import unittest
from datetime import date,timedelta
from appointment import Appointment
from clinic_database import ClinicDatabase
from owner import PetOwner
from pet_factory import PetFactory
class TestClinicSystem(unittest.TestCase):
    def setUp(self): self.database=ClinicDatabase(); self.database.clear(); self.future=(date.today()+timedelta(days=1)).isoformat()
    def add_owner_pet(self,owner='O001',pet='P001',ptype='Dog'):
        self.database.add_owner(PetOwner(owner,'Juan Dela Cruz','09123456789')); self.database.add_pet(PetFactory.create_pet(ptype,pet,'Buddy',3,owner))
    def test_register_pet_owner(self):
        self.database.add_owner(PetOwner('O001','Juan Dela Cruz','09123456789')); self.assertEqual(self.database.get_owner('O001').name,'Juan Dela Cruz')
    def test_add_pet_record(self):
        self.add_owner_pet(); self.assertEqual(self.database.get_pet('P001').pet_type,'Dog')
    def test_schedule_appointment(self):
        self.add_owner_pet(); self.database.add_appointment(Appointment('A001','O001','P001',self.future,'10:00','General Check-up')); self.assertEqual(self.database.get_appointment('A001').status,'Scheduled')
    def test_cancel_appointment(self):
        self.add_owner_pet(); a=Appointment('A001','O001','P001',self.future,'14:00','Check-up'); self.database.add_appointment(a); a.cancel(); self.assertEqual(a.status,'Cancelled')
    def test_singleton_instance(self): self.assertIs(ClinicDatabase(),ClinicDatabase())
    def test_invalid_pet_type(self):
        with self.assertRaises(ValueError): PetFactory.create_pet('Fish','P001','Nemo',2,'O001')
    def test_invalid_negative_age(self):
        with self.assertRaises(ValueError): PetFactory.create_pet('Dog','P001','Buddy',-1,'O001')
    def test_invalid_contact(self):
        with self.assertRaises(ValueError): PetOwner('O001','Juan Dela Cruz','12345')
    def test_missing_owner(self):
        with self.assertRaises(ValueError): self.database.add_pet(PetFactory.create_pet('Dog','P001','Buddy',3,'O999'))
    def test_duplicate_owner(self):
        self.database.add_owner(PetOwner('O001','Juan Dela Cruz','09123456789'))
        with self.assertRaises(ValueError): self.database.add_owner(PetOwner('O001','Maria Santos','09987654321'))
    def test_owner_pet_mismatch(self):
        self.database.add_owner(PetOwner('O001','Juan Dela Cruz','09123456789')); self.database.add_owner(PetOwner('O002','Maria Santos','09987654321')); self.database.add_pet(PetFactory.create_pet('Cat','P001','Ming',2,'O001'))
        with self.assertRaises(ValueError): self.database.add_appointment(Appointment('A001','O002','P001',self.future,'10:00','Check-up'))
    def test_duplicate_appointment_id(self):
        self.add_owner_pet(); self.database.add_appointment(Appointment('A001','O001','P001',self.future,'10:00','Check-up'))
        with self.assertRaises(ValueError): self.database.add_appointment(Appointment('A001','O001','P001',self.future,'11:00','Vaccination'))
    def test_conflicting_pet_appointment(self):
        self.add_owner_pet(); self.database.add_appointment(Appointment('A001','O001','P001',self.future,'10:00','Check-up'))
        with self.assertRaises(ValueError): self.database.add_appointment(Appointment('A002','O001','P001',self.future,'10:00','Vaccination'))
if __name__=='__main__': unittest.main()
