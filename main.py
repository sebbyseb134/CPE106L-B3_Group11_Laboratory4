# PERSON IN CHARGE: MARQUEZ
# GROUP 11 | CPE106L-B3
from clinic_database import ClinicDatabase
from owner import PetOwner
from pet_factory import PetFactory
from appointment import Appointment
database=ClinicDatabase()
def register_owner():
    print('\n--- REGISTER PET OWNER ---')
    try: database.add_owner(PetOwner(input('Enter Owner ID: '),input('Enter Owner Name: '),input('Enter Contact Number: '))); print('Pet owner registered successfully.')
    except ValueError as e: print(f'Invalid input: {e}')
def view_owners():
    print('\n--- REGISTERED PET OWNERS ---')
    if not database.owners: print('No registered pet owners.'); return
    for x in database.owners.values(): print(x)
def add_pet():
    print('\n--- ADD PET RECORD ---')
    try:
        p=PetFactory.create_pet(input('Enter Pet Type (Dog/Cat/Bird/Rabbit): '),input('Enter Pet ID: '),input('Enter Pet Name: '),input('Enter Pet Age: '),input('Enter Owner ID: ')); database.add_pet(p); print('Pet record added successfully.')
    except ValueError as e: print(f'Invalid input: {e}')
def view_pets():
    print('\n--- REGISTERED PETS ---')
    if not database.pets: print('No pet records.'); return
    for x in database.pets.values(): print(x)
def schedule_appointment():
    print('\n--- SCHEDULE APPOINTMENT ---')
    try:
        a=Appointment(input('Enter Appointment ID: '),input('Enter Owner ID: '),input('Enter Pet ID: '),input('Enter Appointment Date (YYYY-MM-DD): '),input('Enter Appointment Time (HH:MM): '),input('Enter Reason: ')); database.add_appointment(a); print('Appointment scheduled successfully.')
    except ValueError as e: print(f'Invalid input: {e}')
def view_appointments():
    print('\n--- APPOINTMENT SCHEDULE ---')
    if not database.appointments: print('No appointments.'); return
    for x in database.appointments.values(): print(x)
def cancel_appointment():
    print('\n--- CANCEL APPOINTMENT ---'); a=database.get_appointment(input('Enter Appointment ID: '))
    if a is None: print('Invalid input: Appointment ID was not found.'); return
    try: a.cancel(); print('Appointment cancelled successfully.')
    except ValueError as e: print(f'Invalid action: {e}')
def update_appointment_status():
    print('\n--- UPDATE APPOINTMENT STATUS ---'); a=database.get_appointment(input('Enter Appointment ID: '))
    if a is None: print('Invalid input: Appointment ID was not found.'); return
    print('1. Scheduled\n2. Completed\n3. Cancelled'); choice=input('Choose status: ').strip(); statuses={'1':'Scheduled','2':'Completed','3':'Cancelled'}
    if choice not in statuses: print('Invalid input: Choose only 1, 2, or 3.'); return
    try: a.update_status(statuses[choice]); print('Appointment status updated successfully.')
    except ValueError as e: print(f'Invalid action: {e}')
def main():
    while True:
        print('\n'+'='*55+'\nPAWS AND CARE VETERINARY CLINIC\nAPPOINTMENT MANAGEMENT SYSTEM\n'+'='*55+'\n1. Register Pet Owner\n2. View Pet Owners\n3. Add Pet\n4. View Pets\n5. Schedule Appointment\n6. View Appointments\n7. Cancel Appointment\n8. Update Appointment Status\n9. Exit')
        choice=input('Enter your choice (1-9): ').strip()
        actions={'1':register_owner,'2':view_owners,'3':add_pet,'4':view_pets,'5':schedule_appointment,'6':view_appointments,'7':cancel_appointment,'8':update_appointment_status}
        if choice=='9': print('Thank you for using Paws and Care Veterinary Clinic.'); break
        if choice in actions: actions[choice]()
        else: print('Invalid input: Choose a number from 1 to 9.')
if __name__=='__main__': main()
