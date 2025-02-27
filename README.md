# PetClinicApp

Pet care management system 
Project description: 
I have developed an application that is useful for pet clinics and hospitals. This application 
includes features where the user can create a pet profile that contains general information 
about the pet. The application can schedule tasks, as well as their details. This project employs 
OOP, file handing using text files and Tkinter for GUI. 
Features  
➢ Pet Class 
1. Firstly, I created the pet class with the following attributes and initialized them. 
• Pet name 
• Animal 
• Age 
• Medical History 
• Care Instructions  
2. I created a method that turns the created pet object into a string so it can easily be 
stored in the pets.txt file. 
3. I created a static method that takes data from the pet.txt file, strips it from spaces 
and other characters used to organize the data in the file, and returns a Pet object. 
➢ Task Class 
1. Firstly, I created the task class with the following attributes and initialized them. 
• Pet name 
• Task type 
• Date 
• Time 
• Status 
2. I created a method that turns the created task object into a string so it can easily be 
stored in the tasks.txt file. 
3. I created a static method that takes data from the tasks.txt file, strips it from spaces 
and other characters used to organize the data in the file, and returns a Task object. 
➢ FileHandling class 
1. I created a static method that gets data from a file and turns it into an object. 
2. I created a static method that saves data into a file. 
➢ PetsManager class 
1. I created the class and its’ following attributes and initialized it: 
• Root -> main application window 
• Pets -> a list of pets 
• App -> main app object 
2. I created a new pop-up window where I created: 
a.  I created a frame and inside that frame, I created a “Pet profile” label. 
b. I created a list box and populated it with existing pet data 
c. I created the buttons: 
i. 
Add a pet -> adds a new pet to the list 
ii. 
iii. 
Edit a pet -> edits an existing pet (the pet must be selected to edit) 
Delete a pet -> deletes an existing pet (the pet must be selected to 
delete) 
iv. Display pet details -> shows all the details of a pet (the pet must  
v. Display total number of pets -> shows the total number of registered 
pets in the list box 
vi. Quit -> exits window 
3. Next, I created the methods needed to perform those actions along with a method 
to load the data to ensure that the list gets updated properly. 
4. When the first two are clicked I created a form to fill in the fields with the needed 
information. 
5. The Display pet details button shows a messagebox with the pet’s information and 
the Display total number of pets displays the information in a messagebox 
➢ TasksManager class 
1. I created the class and its’ following attributes and initialized it: 
• Root -> main application window 
• Tasks -> a list of tasks 
• Pets -> a list of pets 
• App -> main app object 
2. I created a new pop-up window where I created: 
a. I created a frame and inside that frame, I created a “Tasks” label. 
b. I created a list box and populated it with existing tasks data 
c. I created the buttons: 
i. 
ii. 
iii. 
Add a task -> adds a new task to the list 
Edit a task -> edits an existing task (the task must be selected to edit) 
Delete a task -> deletes an existing task (the task must be selected to 
delete) 
iv. Mark as completed -> marks a task as completed (the task must be 
selected to mark as completed) 
v. Tasks report -> displays the number of the total tasks, the completed 
tasks and the pending tasks. 
vi. Quit -> exits window 
3. Next, I created the methods needed to perform those actions along with a method 
to load the data to ensure that the list gets updated properly. 
4. When the first two are clicked I created a form to fill in the fields with the needed 
information. 
5. The Task report button shows a messagebox with the report information. 
➢ PetClinicApp class 
1. Imported everything I needed for the code to work. 
2. I created the class with its attributes and initialized it: 
• Root -> main application window 
3. I read data from both files and populate the lists. 
4. I created the main window where I created a frame, a label and three buttons: 
• Manage pets -> opens the pop-up window created for pets 
• Manage tasks -> opens the pop-up window created for tasks 
• Quit -> exits application 
5. I created the methods needed for the button to work so that when pressed an 
instance of PetsManager and TasksManager is created. 
6. Then I create two methods to save the data into their respective files. 
7. In the end, I created the main window and passed it down as an argument to the 
PetClinicApp to get the application started. 
Additional information 
Apart from the needed functionalities the code handles errors like empty fields or not selected 
item when selection is necessary. When they occur a messagebox appears informing the user of 
the error.
