import re
from datetime import datetime, date

def require_text(value, field):
    value=value.strip()
    if not value: raise ValueError(f'{field} cannot be empty.')
    return value

def validate_id(value, field):
    value=require_text(value, field)
    if not re.fullmatch(r'[A-Za-z0-9_-]+', value): raise ValueError(f'{field} is invalid. Use only letters, numbers, hyphens, or underscores.')
    return value

def validate_name(value):
    value=require_text(value,'Name')
    if len(value)<2: raise ValueError('Name is invalid. It must contain at least 2 characters.')
    if len(value)>60: raise ValueError('Name is invalid. It cannot exceed 60 characters.')
    if not re.fullmatch(r"[A-Za-zÀ-ÿ .'-]+",value): raise ValueError('Name is invalid. Do not use numbers or special symbols.')
    return value

def validate_contact(value):
    value=require_text(value,'Contact Number')
    if not re.fullmatch(r'(?:\+63|0)9\d{9}',value): raise ValueError('Contact Number is invalid. Use 09123456789 or +639123456789.')
    return value

def validate_age(value):
    try: age=int(value)
    except ValueError: raise ValueError('Age is invalid. Enter a whole number.')
    if age<0: raise ValueError('Age is invalid. It cannot be negative.')
    if age>100: raise ValueError('Age is invalid. Enter an age from 0 to 100.')
    return age

def validate_date(value):
    value=require_text(value,'Appointment Date')
    try: d=datetime.strptime(value,'%Y-%m-%d').date()
    except ValueError: raise ValueError('Appointment Date is invalid. Use YYYY-MM-DD, for example 2026-09-15.')
    if d<date.today(): raise ValueError('Appointment Date is invalid. You cannot schedule a past date.')
    return d

def validate_time(value):
    value=require_text(value,'Appointment Time')
    try: return datetime.strptime(value,'%H:%M').time()
    except ValueError: raise ValueError('Appointment Time is invalid. Use 24-hour HH:MM format, for example 10:30.')

def validate_reason(value):
    value=require_text(value,'Reason')
    if len(value)<3: raise ValueError('Reason is invalid. It must contain at least 3 characters.')
    if len(value)>100: raise ValueError('Reason is invalid. It cannot exceed 100 characters.')
    return value