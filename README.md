This Python program is a simple hotel room booking system that works using a menu-driven approach. It allows the user to check available rooms, book rooms, cancel bookings, and exit the program. The system runs continuously until the user chooses to exit.

The program starts by setting rooms = 25, which represents the total number of available rooms in the hotel. A while True loop is used to repeatedly display the menu and take user input so that multiple operations can be performed without restarting the program.

Inside the loop, the program prints a menu with four options: check available rooms, book rooms, cancel booking, and exit. The user enters a choice, which is stored in the variable ch.

If the user selects option 1, the program displays the current number of available rooms.

If the user selects option 2, the program asks how many rooms the user wants to book. It checks whether the requested number is valid (greater than zero and less than or equal to available rooms). If valid, it subtracts that number from the available rooms and confirms the booking. Otherwise, it shows that rooms are not available.

If the user selects option 3, the program asks how many rooms to cancel and adds that number back to the available rooms, then prints a cancellation success message.

If the user selects option 4, the program prints a thank you message and stops execution using the break statement.

If any other number is entered, the program displays an “Invalid Choice” message.

Overall, this code demonstrates the use of loops, conditional statements, user input, and variable updates to simulate a basic booking system.
