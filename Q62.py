#The author's name is Julia Bub
class Ambulance:
    """Represents the qualities of an ambulance with attributes: priority, speed, and capacity"""

myAmbulance = Ambulance()
myAmbulance.priority = 1
#"0 if there is no patient in the ambulance, 1 if there is"
myAmbulance.speed = 80
#"maximum speed of the ambulance"
myAmbulance.capacity = 3
#"number of patients inside the ambulance"

def drive(t):
    controlled_velocity = -10*(1 - t.priority) + 2.37*(t.speed/10)**3.98 + 30*(t.capacity + 1.2)
    return controlled_velocity
print(drive(myAmbulance))
