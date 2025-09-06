##
#  Manage student grades.
#

# Use a dictionary named 'grades' to track student grades.
 
  # Loop until the user chooses to quit.
  # Check user input for the following "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? "
  # Prevent unexected inputs by converting input to upper-case
 

   # Use a condition to handle adding a new student.
   # Convert grade into integer
   # Gather user input for "Enter the name of the student: "
   # Check if student name already exists "Sorry, that student is already present."
   # Gather user input for student grade "Enter the student's grade: "
 

   # Handle removing a student if user inputs 'R'
   # Check input for "What student do you want to remove? "
   # use pop to remove key/value form grades
   # Check if student doesn't exist - "Sorry, that student doesn't exist and couldn't be removed."
   

   # Handle modifying a student grade if user inputs 'M'
   # "Enter the name of the student to modify: "
   # Convert grade into integer
   # If student is in grades dictionary, show existing grade "The old grade is"
   # Gather input for new grade "Enter the new grade: "
   # If student doesn't exist "Sorry, that student doesn't exist and couldn't be modified."
 
   # Handle printing grade average as a string if user input is 'P'
   # Use "The average grade is "
   # Handle printing all of the student names with associated grade
   # Display explictly as strings

   # Handle the case for quiting if user inputs 'Q' "Goodbye!"

   # Handle the case of invalid input. "Sorry, that wasn't a valid choice."
