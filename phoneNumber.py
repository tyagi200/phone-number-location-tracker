import phonenumbers


from phonenumbers import geocoder,timezone,carrier

number=input("Enter your phone number with +__")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_geographical_number(phone)
car=carrier.name_for_number(phone,'en')
reg=geocoder.description_for_number(phone,"en")
print(phone)
print(time)
print(car)
print(reg)