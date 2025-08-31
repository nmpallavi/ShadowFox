distance = 490  
time_minutes = float(input("Enter time taken to cross the street (in minutes): "))
time_seconds = time_minutes * 60
speed = distance / time_seconds
print("Speed:", int(speed), "m/s")
