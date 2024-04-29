# One to Many #
from classes.models import Car, Garage

# Many to Many #
from classes.models import Doctor, Patient, Appointment

# HARD MODE # (You may need to make more models to make this work!)
from classes.models import Student, Enrollment, Course

# SEED DATA GOES BELOW




#doctors and patients

d1 = Doctor(name = "Dre", specialty = "beats")
d2 = Doctor (name="Lee", specialty = "dentist")

p1 = Patient(first_name= "Scooby", last_name="Doo")
p2 = Patient (first_name = "Scrappy", last_name= "Doo")

a1= Appointment(doctor=d1, patient= p1)
a2 = Appointment(doctor=d1, patient= p2)
a3 = Appointment(doctor=d2, patient= p1)
a3 = Appointment(doctor=d2, patient= p2)