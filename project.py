def main():
    # project()
    extracredit()
# Create a task list.
# A user is presented with the text below.
# Let them select an option to list all of their tasks,
# add a task to their list,
# delete a task,
# or quit the program.
# Make each option a different function in your program.
# Do NOT use Google. Do NOT use other students. Try to do this on your own.
#
# Congratulations! You're running [YOUR NAME]'s Task List program.
#
# What would you like to do next?
# 1. List all tasks.
# 2. Add a task to the list.
# 3. Delete a task.
# 0. To quit the program

class taskmanager:
    def __init__(self,name,tasklist =[]):
        self.name = name
        self.tasklist = tasklist
    def tasklist(self):
        for x in self.tasklist():
            print(x)

outsidefile = open("tasklist1.txt","a")
# the most dangerous thing i learned today,
# you can COMPLETELY CHANGE EVERYTHING IN THE FILE
# HOW DO YOU ADD WITHOUT REPLACING?
def project():
    userlist =["Thomas","Kenn","Person"]
    tasklist = [{"name":"Thomas","taskList": ["task1","task2","task3"]},
                {"name":"Kenn","taskList": ["task1","task2","task3"]},
                {"name":"person","taskList": ["task1","task2","task3"]}]
    print("are you a new user?\n Y/n")
    for user in userlist:
        print(user)
    newUser = input("")
    # if(newUser == )
    if(newUser.upper() == "Y"):
        userInputName = input("please enter name\n")
        userlist.append(userInputName)
        tasklist.append({"name":userInputName,"taskList":[]})
        for person in userlist:
            if(userInputName.lower() == person.lower()):
                user = person
                entry = True
                break
    if(newUser.lower() == "n"):
        userInputName = input("please enter name")
        if userInputName.capitalize() not in userlist:
            print('user not in list')
            entry = False
        else:
            for person in userlist:
                if(userInputName.lower() == person.lower()):
                    user = person
                    entry = True
                    break


    #         for adding new user
    if(entry == True):
        print(f" welcome {user} what would you like to do?")
        while(True):
            command = input("View\tAdd\tRemove\tquit\n")
            if(command.lower() == "quit"):
                print("Have a good day")
                break
            elif(command.lower() == "view"):
                print(open("tasklist","r"))
                print("Tasklist:")
                for person in tasklist:
                    if person["name"] == user:
                        for x in (person["taskList"]):
                            print(f"task:{x}\n")
                    elif(person["taskList"] == []):
                        print("no tasks")
            elif(command.lower() == "add"):
                    newTask = input("What new task do you want to add?\n")
                    for person in tasklist:
                        if person["name"] == user:
                            person["taskList"].append(newTask)
            elif(command.lower() == "remove"):
                taskToRemove = input("What task do you want to remove?\n")
                for person in tasklist:
                    if person["name"] == user:
                        if(taskToRemove not in person["taskList"]):
                            print("No task found")
                            break
                        else:
                            person["taskList"].remove(taskToRemove)
            else:
                print("Invalid command please reinput command\nView task list\tAdd task to list\tRemove task\tquit\n")
    else:
        print("goodbye")



def extracredit():
    Input = input("what do i put in there?")
    outsidefile.write(f"\n{Input}")



if __name__ == '__main__':
    main()
