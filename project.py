def main():
    project()
    # extracredit()
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

outsidefile = open("tasklist1","a")
# the most dangerous thing i learned today,
# you can COMPLETELY CHANGE EVERYTHING IN THE FILE
# HOW DO YOU ADD WITHOUT REPLACING?
def project():
    userlist =["Thomas"]
    tasklist = [{"name":"Thomas","taskList": "tasklist1"}]
    print("are you a new user?\n Y/n")
    for user in userlist:
        print(user)
    newUser = input("")
    # if(newUser == )
    if(newUser.upper() == "Y"):
        userInputName = input("please enter name\n")
        userlist.append(userInputName)
        tasklist.append({"name":userInputName,"taskList":(f"tasklist{len(userlist)}")})
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
                print("have a good day")
                break
            elif(command.lower() == "view"):
                for person in tasklist:
                    if person["name"] == user:
                        print("taskList")
                        file = open(person["taskList"],"r")
                        print(file.read())
                        file.close()
                    elif(person["taskList"] == []):
                        print("no tasks")
            elif(command.lower() == "add"):
                    newTask = input("What new task do you want to add?\n")
                    for person in tasklist:
                        file = open(person["taskList"],"a")
                        file.write(f"{newTask}\n")
            elif(command.lower() == "remove"):

                taskToRemove = input("What task do you want to remove?\n")
                for person in tasklist:
                    if person["name"] == user:
                        readfile = open(person["taskList"],"r")
                        lines = readfile.readlines()
                        print(lines)
                        readfile.close()
                        editfiles = open(person["taskList"],"w")
                        for task in lines:
                            if(task != taskToRemove + "\n"):
                                editfiles.write(task)
                        editfiles.close()
            else:
                print("Invalid command please reinput command\nView\tAdd\tRemove\tquit\n")
    else:
        print("goodbye")



def extracredit():
    Input = input("what do i put in there?")
    outsidefile.write(f"\n{Input}")



if __name__ == '__main__':
    main()
