# python-review2-cw

Create a task list. A user is presented with the text below. Let them select an option to list all of their tasks, add a task to their list, delete a task, or quit the program. Make each option a different function in your program. Do <strong>NOT</strong> use Google. Do <strong>NOT</strong> use other students. Try to do this on your own.

```
Congratulations! You're running [YOUR NAME]'s Task List program.

What would you like to do next?
1. List all tasks.
2. Add a task to the list.
3. Delete a task.
0. To quit the program
```

#### Extra Credit. Once a task is Output the data to a text file. When the program is run again, input that text file.

Use the links below to get started on file io:
- https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
- https://thepythonguru.com/python-file-handling/
- https://pythonbasics.org/read-file/
- https://pythonbasics.org/write-file/

___

#### Only use the information below if necessary

To list all items in an array:
```python
for itemInArray in arrayOfTasks:
```
To add an item to an array
```python
arrayOfTasks.append(newTask)
```
To check if an item is in an array
```python
if deleteTask in arrayOfTasks:
```
To delete a task
```python
arrayOfTasks.remove(deleteTask)
```
