while True:
print("--- Hotel Room Booking System---")
print("1. Check Available Rooms")
print("2. Book Room")
print("3. Cancel Booking")
print("4. Exit")
ch = int(input("Enter choice: "))
if ch == 1:
print("Available Rooms:", rooms)
elif ch == 2:
n =int(input("Enter number of rooms to book: "))
if n > 0 and n <=rooms:
rooms = rooms- n
print("Room Booked Successfully")
else:
print("Rooms NotAvailable")
elif ch == 3:
n =int(input("Enter number of rooms to cancel: "))
rooms = rooms + n
print("Booking Cancelled Successfully")
elif ch == 4:
print("Thank You")
break
else:
print("Invalid Choice”
