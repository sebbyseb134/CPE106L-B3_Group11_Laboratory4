# PERSON IN CHARGE: SOMERA
# GROUP 11 | CPE106L-B3
from validation import validate_id,validate_date,validate_time,validate_reason
class Appointment:
    VALID_STATUSES={'Scheduled','Completed','Cancelled'}
    def __init__(self,appointment_id,owner_id,pet_id,date,time,reason):
        self.appointment_id=validate_id(appointment_id,'Appointment ID'); self.owner_id=validate_id(owner_id,'Owner ID'); self.pet_id=validate_id(pet_id,'Pet ID'); self.date=validate_date(date); self.time=validate_time(time); self.reason=validate_reason(reason); self.status='Scheduled'
    def update_status(self,status):
        if status not in self.VALID_STATUSES: raise ValueError('Appointment status is invalid. Choose Scheduled, Completed, or Cancelled.')
        if self.status=='Cancelled' and status!='Cancelled': raise ValueError('A cancelled appointment cannot be reopened.')
        if self.status=='Completed' and status=='Scheduled': raise ValueError('A completed appointment cannot return to Scheduled.')
        self.status=status
    def cancel(self):
        if self.status=='Completed': raise ValueError('A completed appointment cannot be cancelled.')
        if self.status=='Cancelled': raise ValueError('This appointment is already cancelled.')
        self.status='Cancelled'
    def __str__(self): return f'Appointment ID: {self.appointment_id} | Owner ID: {self.owner_id} | Pet ID: {self.pet_id} | Date: {self.date.isoformat()} | Time: {self.time.strftime("%H:%M")} | Reason: {self.reason} | Status: {self.status}'
