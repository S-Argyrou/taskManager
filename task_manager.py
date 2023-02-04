#=====importing libraries===========
# Import date from datetime library to get today's date.
from datetime import datetime, date


#=====Defining Functions===========


def reg_user():
    """ When admin logged in, allow to register a new user,
    if it does not exist already.

    Keyword arguments:
    None
    
    Returns:
    Confirmation message if user added successfully.
    """ 
    
    # Check if user_name is equal to 'admin'
    if usr_name == 'admin':
            
        # If it is, Request input of a new username, of a new password and of password confirmation.             
        new_usr_name = input('Please enter a new username: ')
        
        # Check if user has already been added.
        # If so, prompt for a different username
        while new_usr_name in name_list:
            print('\nThe user has already been added.\n')
            new_usr_name = input('Please enter a new username: ')
        
        # If the user has never been added, prompt for a password and confirm password.
        else:    
            new_password = input('Please enter a new password: ')
            confirm_password = input('Please confimr your password again: ')
            
        # Check if the data stored in 'new_password' and 'confirm_password' are the same.
        # If they are not, the while loop will carry on requesting to input the right match for password.
        while confirm_password != new_password:
                
            # Print a message, if the data stored in 'new_password' and 'confirm_password' are NOT the same
            confirm_password = input('The passwords do not match. Please try again: ')
             
        # If 'new_password' and 'confirm_password' store the same data, we add the new logins at the end of 'user.txt'.
        else:
            with open('user.txt','a') as f:
                f.write('\n' +new_usr_name + ', ' + confirm_password )
                print('\nNew user added!\n')
                

    # Print a relevant message, if user_name is NOT equal to 'admin'.      
    else:
        print('\nYou need admin privileges to register new users!\n')




def add_task():
    """ Allow to add a task and assign it to a user,
    
    Keyword arguments:
    None
    
    Returns:
    Confirmation message if task added successfully.
    """ 
    
    # Request user input of a new username, task, tile, task description and due date..
    person_usr = input('Please enter the username of the person whom the task is assigned to: ')
    task_title = input('Please enter the task title: ')
    task_descrip = input('Please enter a description: ')
    due_date = input('Please enter the due date in the following format yyyy-mm-dd: ')
    task_completed = 'No'
    
    # Assign to the variable 'today' the current date 
    today = date.today()
    
    
    # Open the file in append mode.
    with open('tasks.txt','a') as file2:
        
        # Add at the end of the file a new line displaying the inputs.
        file2.write(f'\n{person_usr}, {task_title}, {task_descrip}, {today}, {due_date}, {task_completed}')
    
    # Print success message.
    print('\nTask successfully adde!\n')




def view_all():
    """ Allow to view all the tasks assigned to each user,
    
    Keyword arguments:
    None
    
    Returns:
    Tasks specifications for each user in a user friendly way.
    """ 
    
    # Open the file in read mode.
    with open('tasks.txt','r') as file2:
        
        # Assign to a variable 'data' the file split in single lines.
        data = file2.readlines()
        
        # For loop to split the line into words.
        # Enumerate function to assign a number to each task (start value 1).
        # This makes reading the output more user-friendly.
        for index, line in enumerate(data, 1):
            split_data = line.split(', ')
            
            # Create a variable 'output' to display the output.            
            output = f'''
\n_________Task number: {index}_____________\n\n        
Assigned to:\t\t{split_data[0]}\n
Task:\t\t\t{split_data[1]}\n
Task description:\t{split_data[2]}\n
Date assigned:\t\t{split_data[3]}\n
Due date:\t\t{split_data[4]}\n
Task complete?\t\t{split_data[5]}\n
\n____________________________________\n\n'''
            
            # Print the output in a user-friendly way.
            print(output)



  
def view_mine():
    """ Allow to see all task assigned to a particular user and
    change username and due date if task is still incomplete.
    
    Keyword arguments:
    None
        
    """ 
        
    # Open the file in read mode.
    with open('tasks.txt','r') as file2:
        
        # Assign to a variable 'content' the file split in single lines.
        content = file2.readlines()

        # Read every line from 'content'.
        # Enumerate function to assign a number to each task (start value 1).
        for index, line in enumerate(content, 1):
                         
            # Split the line where there is comma and space. 
            split_data = line.split(', ')
            
            # Assign to the variable 'user' the value stored in the variable 'split_data[0]'
            # (i.e  the first field in the file)
            user = split_data[0]
            
            # Check if the username of the person logged in is the same as the username
            # If they are, print it in a user-friendly format.
            if usr_name == user:
               
                output = f'''\n_________Task number: {index}_____________\n\n
Task:\t\t\t{split_data[1]}\n
Assigned to:\t\t{split_data[0]}\n
Date assigned:\t\t{split_data[3]}n
Due date:\t\t{split_data[4]}\n
Task complete?\t\t{split_data[5]}\n
Task description:\n\t{split_data[2]}\n
\n\n____________________________________\n'''
                
                print(output)
               
                # Set the task number equal to the index used in the enumerate function.
                task_number = index
                
                # Request an integer input from the user
                task_selection = int(input("Select a task number or press '-1' to go back to the main menu: "))
                
                # Checks the user input.
                # If the input is the same as the task number, prompt for marking or editing the task.                
                if task_selection == task_number:
                    
                    choice = input("Would you like to mark or edit the task? Type mark or edit : ").lower()
                    
                    # If user chooses to mark the task as complete, change the last piece of data from 'No' to 'Yes'.
                    # Print a success message to inform the user.
                    if choice == 'mark':
                        
                        split_data[5] = 'Yes\n'
                        print(f'\nThe task assigned to {user} has been marked as complete\n')
                                     
                    # If user chooses to edit the task, prompt for change username or due date..                   
                    elif choice == 'edit':
                        
                        # If task is already complete, display a relevant message.
                        if split_data[5] =='Yes\n':
                                print('\nYou cannot edit a task anymore when it is completed\n')
                        
                        # Request user input.
                        else:        
                            option = input("Do you want edit the username or the due date? Type 'u' or 'dd'").lower()
                           
                            # Depending on the input, allow change in either username or due date.
                            # Display a success message when the changes have been done.
                            if option == 'u':
                                split_data[0] = input('Please edit the username: ')
                                print('\nUsername has been successfully changed\n')                        
                                                
                            elif option == 'dd':
                                split_data[4] = input('Please edit the due date. Write the date in the following format: yyyy-mm-dd ')
                                print('\nDue date has been successfully changed\n')                              
                            
                            # Display an error message if the input is wrong.
                            else:
                                print('\nInvalid input\n')
                    
                    # Display an error message if input is different from 'mark' or 'edit'.
                    else:
                        print('Invalid input')
                    
                
                # If task selection is equal to -1 print a relevant message.
                # Send the user back to main menu.
                elif task_selection == -1:
                    print('\nBack to the main menu\n')
                    exit
                
                # Inform the user, if no tasks are assigned to him/her.
                else:
                    print(f'\nNo task numbered {task_selection} is assigned to this user.\n')
                
            # Convert the line where the changes have been done in a string    
            line_as_string = ', '.join(split_data)
            
            # Assign the line to that particular index position of the content of the file.
            # As index position starts from 1, we need to take 1 away to make sure index assignment is correct..
            content[index-1] = line_as_string
                                     
            # Open the file in write and read mode.
            with open('tasks.txt','w+') as file2:
                
                # Loop through every line in the file and update the content.
                # Write in the file the new content.
                for line in content:
                    file2.write(line)
   
   
        
    

def user_overview():
    """ Generate statistics on individual users,
    
    Keyword arguments:
    None
    
    """ 
    
    # Open first file in read mode.
    # Open the second file in write and read mode.
    with open('tasks.txt','r') as file2, open('user_overview.txt','w+') as f:
        
       
                
        # Assign to a variable 'content' the file split in single lines.
        content = file2.readlines()
                           
        # Create two empty lists to store all the usernames extracted from the file.
        # We wiil use them to check if there are more tasks assigned to the same person
        users_from_tasks = []
        duplicate_names = []

        # Create empty dictionaries for later.
        assigned_tasks_dict = {}
        assigned_tasks_perc_dict = {}
        complete_tasks_perc_dict = {}
        incomplete_tasks_perc_dict = {} 
        overdue_tasks_perc_dict = {}
        
                  
        # Read every line from 'content' 
        for line in content:
                        
            # Assign to a variable 'total_tasks' the number of lines found in 'content'
            total_tasks = len(content)
            
            # Split the line where there is comma and space.               
            split_data = line.strip().split(', ')
                        
            # Assign to the variable 'user' the value stored in the variable 'split_data[0]'
            # (representing the first field in the file)
            user = split_data[0]
            
            # Add all the usernames to the 'duplicate_names' list
            duplicate_names.append(user)
            
            # Loop through every name in the list.
            for name in duplicate_names:
                                
                # If the word is NOT in 'users_from_tasks' list, add it to it.
                if name not in users_from_tasks:
                                        
                    users_from_tasks.append(name)
                                                                             
            # Set the variable num_of_users equal to the lenght of the list 'users_from_tasks'.
            # This will tell exactly how many user there are.
            num_of_users = len(users_from_tasks)
            
            # Create counter variables to store the number of complete, incomplete and overdue tasks and their percentages.
            # Set their initial value equal to 0.
            complete_tasks = 0
            incomplete_tasks = 0
            overdue_tasks = 0
            incomplete_tasks_perc = 0
            complete_tasks_perc = 0
                   
            
            # Check if task is complete.
            # If it is add one to the counter variable.
            if split_data[5] == 'Yes': 
                complete_tasks += 1
            
            # Check if task is incomplete.
            # If it is add one to the counter variable.
            elif split_data[5] == 'No':
                incomplete_tasks +=1
            
           
            # Set the variable 'due_date' equal to the data stored in the fifth field in the document.
            due_date = split_data[4]
            
            # Use date format to convert the data from a simple text string in a date.
            # This will allow to compare it with our present date down below.
            due_date = datetime.strptime(due_date, "%Y-%m-%d")
            
            # Check if task is overdue and incomplete.
            # If it is add one to the counter variable.
            if due_date < datetime.now() and split_data[5] == 'No':
                 
                overdue_tasks +=1
                 
            # Create a list storing tuples of usernames and number of tasks assigned to each user.
            # Set function removes duplicates.
            users_tasks_count = list((name, duplicate_names.count(name)) for name in set(duplicate_names))

    
            # Loop through every tuple.
            # Store the user as a key and the number of tasks as the value into 'assigned_tasks_dict'
            for toople in users_tasks_count:
                if toople[0] == user:
                    assigned_tasks_dict[user] = toople[1]
                       
            # Find percentages of complete, incomplete and overdue tasks.            
            assigned_tasks_perc = assigned_tasks_dict[user] / total_tasks * 100
            complete_tasks_perc = complete_tasks / assigned_tasks_dict[user] * 100
            incomplete_tasks_perc = 100 - complete_tasks_perc
            overdue_tasks_perc = overdue_tasks / assigned_tasks_dict[user] * 100
            
            # Assign to each dictionary a key and a value.
            assigned_tasks_perc_dict[user] = assigned_tasks_perc
            complete_tasks_perc_dict[user] = complete_tasks_perc
            incomplete_tasks_perc_dict[user] = incomplete_tasks_perc
            overdue_tasks_perc_dict[user] = overdue_tasks_perc
            
        # Loop through every user in 'users_from_tasks' list.
        for user in users_from_tasks:
            
            # Write in the file a user friendly message showing statistics for each user.
            f.write(f'''

            User: \t\t\t\t\t{user}
            
                tasks assigned\t\t\t\t{assigned_tasks_dict[user]}
                % tasks assigned\t\t\t{round(assigned_tasks_perc_dict[user])}%
                                                
                % complete tasks\t\t\t{round(complete_tasks_perc_dict[user])}%
                % incomplete tasks\t\t\t{round(incomplete_tasks_perc_dict[user])}%
                % overdue tasks\t\t\t\t{round(overdue_tasks_perc_dict[user])}%''')
              
    # Exit the loop, open the file again but in append mode.
    # Add at the end of the file a last message showing info about total number of users and tasks.
    with open('user_overview.txt','a') as f:
                f.write(f'''
                
                __________________________________________

                Total number of tasks: \t\t\t{total_tasks}
                Total number of users: \t\t\t{num_of_users}''')
                       
    
    
def task_overview():
    """ Generate statistics on tasks and their completion.
    
    Keyword arguments:
    None
    
    Return:
    Parameters on tasks completition that will be  displayed on the console in a readable
    format, since txt files and console treat tabs differently.
    """ 
    
    # Open the file in read mode.    
    with open('tasks.txt','r') as file2:
        
        # Create some counter variables, with an initial value of 0.
        tasks_overdue = 0
        complete_tasks = 0
        incomplete_tasks = 0        
        incomplete_tasks_perc = 0
        overdue_tasks_perc = 0
                
        # Assign to a variable 'content' the file split in single lines.
        content = file2.readlines()
                            
        # Read every line from 'content' 
        for line in content:          
           
            # Assign to a variable 'total_tasks' the number of lines found in 'content'
            total_tasks = len(content)
            
            # Split the line where there is comma and space.               
            split_data = line.strip().split(', ')
            
            # Set the variable 'due_date' equal to the data stored in the fifth field in the document.      
            due_date = split_data[4]
        
            # Use date format to convert the data from a simple text string in a date.
            # This will allow to compare it with our present date down below.
            due_date = datetime.strptime(due_date, "%Y-%m-%d")
                       
            # Check if task is complete.
            # If it is add one to the counter variable.
            if split_data[5] == 'Yes':
                complete_tasks += 1            
                                         
            # Check if task is incomplete.
            # If it is add one to the counter variable.        
            elif split_data[5] == 'No':
                
                incomplete_tasks += 1
                incomplete_tasks_perc = incomplete_tasks / total_tasks * 100
                
                # Check if task is overdue and incomplete.
                # If it is add one to the counter variable.
                if due_date < datetime.now() and split_data[5] == 'No':
                 
                    tasks_overdue +=1   
                   
                   # Create a variable to store the percentage of tasks overdue.
                    overdue_tasks_perc = tasks_overdue / total_tasks * 100
                       
            # Display a message if no task has been assigne to the user.
            else:
                print('Not found')
                

        #Open the file in write mode.
        with open('task_overview.txt','w') as f:
            
        # Create a variable 'output' to display the output in a user-friednly format.        
            output = f'''
\t\t\t\t\t\tTASKS OVERVIEW

The total number of tasks is:\t\t\t\t\t\t {total_tasks}
The number of completed tasks is:\t\t\t\t\t {complete_tasks}
The number of incompleted tasks is:\t\t\t\t\t {incomplete_tasks}
The number of overdue and incompleted tasks is:\t\t {tasks_overdue}
The % of incompleted tasks is:\t\t\t\t\t\t{round(incomplete_tasks_perc)}%
The % of overdue tasks is:\t\t\t\t\t\t\t {round(overdue_tasks_perc)}%'''
           
            # Write the output in the file 
            f.write(output)
    
    # Return different values that will be used to print the message in a user friendly way in the console.
    return total_tasks, complete_tasks, incomplete_tasks, incomplete_tasks_perc, tasks_overdue, overdue_tasks_perc
        
  

def gen_reports():      
    """ If admin logged in, allow to generate reports on tasks completition and users.
    
    Keyword arguments:
    None
    
    Returns:
    Confirmation message if reports successfully generated.
    """ 
    
    # Check if username logged in is equal to 'admin'
    if usr_name == 'admin':
        
        # Print a relevant message.
        print('''\nReports generated.
It is recommended to generate reports once some changes are made.\n''')
        
        # Create two variables to store data returned from the functions.
        task_results = task_overview()
        user_results = user_overview()
    
    # If the username is not the admin, print a relevant message.
    else:
        print('\nYou need admin privileges to perform this action!\n')
        
        
        
def display_stats():
    """ If admin logged in, allow to generate reports, read from them and display them on the console.
    
    Keyword arguments:
    None
    
    Returns:
    Statistics displayed in a user friendly way..
    """         
    # Call the function to generate reports, in case the file have not been generated yet.    
    gen_reports()
    
    # Create variables to store data returned from function.
    # This has been done as console and txt have different ways of formatting tabs.
    total_tasks, complete_tasks, incomplete_tasks, incomplete_tasks_perc, tasks_overdue, overdue_tasks_perc = task_overview()
    
    # Check if username logged in is equal to 'admin'
    if usr_name == 'admin':
        
        # If it is, open both files in read mode.
        with open('user_overview.txt', 'r') as u, open('task_overview.txt', 'r') as t:
            
            # Print in the console a user friendly message with statistics about the users.
            print('\t\t\t\tUSERS OVERVIEW')
            print(u.read())
            print('\n\n\n\t\t\t\tTASKS OVERVIEW\n')
            print(f'''The total number of tasks is:\t\t\t\t\t\t {total_tasks}
The number of completed tasks is:\t\t\t\t\t {complete_tasks}
The number of incompleted tasks is:\t\t\t\t\t {incomplete_tasks}
The number of overdue and incompleted tasks is:\t\t\t\t {tasks_overdue}
The % of incompleted tasks is:\t\t\t\t\t\t{round(incomplete_tasks_perc)}%
The % of overdue tasks is:\t\t\t\t\t\t {round(overdue_tasks_perc)}%''')
            print('\n\n\n\t\t\t\tEND OF STATISTICS\n')
            print('_______________________________________________________________________________\n')


#====Login Section====

# Set some variables and assign them empty lists.
name_list = []
pwd_list = []


# Open the file in read mode
with open('user.txt', 'r') as f:

    # We are going through every line of the file.
    for line in f:
        
        # Remove the leading spaces and newline character with .strip() method
        # Use split() method to split every line in single words.
        # The separator is a commma followed by a space 
        name, pwd = line.strip(',\n').split(', ')
        
        # Add every gotten name in 'name_list'
        name_list.append(name)
        
        # Add every gotten password in 'pwd_list'
        pwd_list.append(pwd)
        
        
    # Request user input
    usr_name = input('Enter a username: ')
    
    # This loop will carry on requesting user input until it matches any one items in 'name_list'  
    while usr_name not in name_list:
        usr_name = input('Please, enter a valid username: ')
    
    
    # Declare a variable 'pos_usr' to store the index position of the usr input in the usr_name list
    pos_usr = name_list.index(usr_name)
    
    # Request user input
    password = input('Enter a password: ')
    
    
    # This loop will carry on requesting user input until it matches any one items in the pwd_list.
    # Also it checks if pwd input has the same index position of the usr pos in 'name_list'.
    while password != pwd_list[pos_usr]:        
        password = input('Please, enter a valid password: ')


#====Choose Option Section====
        
# This loop will carry on executing once usr_name and password are correct. 
while True:
    
    # Presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gn - generate reports
vs - view statistics
e - Exit
: ''').lower()

    
     # Check if user input is equal to 'r'
    if menu == 'r':
        
        # Call the function.
        reg_user()
    
    # Check if user input is equal to 'a'
    elif menu == 'a':
        
        # Call the function.
        add_task()
        
    
    # Check if user input is equal to 'va'
    elif menu == 'va':
        
        # Call the function.
        view_all()
    
    
    # Check if user input is equal to 'vm'
    elif menu == 'vm':
        
        # Call the function.
        view_mine()   
      
    # Check if user input is equal to 'gn'    
    elif menu == 'gn':
        
        # Call the function.
        gen_reports()
        
    # Check if user input is equal to 'vs'    
    elif menu == 'vs':
        
        # Call the function.
        display_stats()
    
    # Check if user input is equal to 'e'               
    elif menu == 'e':
        
        # If it is, print a relevant message.
        print('Goodbye!!!')
        
        # Exit() function ends the program.
        exit()
        
    # This code displays an error message if the user input is not correct.
    else:
        print("\nYou have made a wrong choice, Please Try again\n")
        

        
