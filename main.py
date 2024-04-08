
# to do list application 

class Task:
    def __init__(self, name, state = 'todo') -> None:
        self.name = name    
        self.state = state
    
    def change_state(self, new_state):
        self.state = new_state

class TaskList:
    
    def __init__(self) -> None:
        self.tasks = {}

    def add_task(self, task):
        if self.task_exists(task.name):
            print('Task already exists')
            return
        elif type(task) != Task:
            print('Invalid task')
            return
        else:
            self.tasks[task.name] = task
            print('Task added')

    def remove_task(self, task):
        if not self.task_exists(task.name):
            print('Task does not exist')
            return
        else:
            del self.tasks[task.name]

    def list_tasks(self):
        if len(self.tasks) == 0:
            print('No tasks')
            return

        else:
            print('Tasks \tStates')
            for task in self.tasks.values():
                print(f"{task.name} \t{task.state}")
        

    def task_exists(self, task_name):
        for tasks in self.tasks.values():
            if task_name in tasks.name:
                return True

    def get_task(self, task_name):
        if not self.task_exists(task_name):
            print('Task does not exist')
            return
        else:
            return self.tasks[task_name]
    
task_list = TaskList()


while True:
    states = ['todo', 'doing', 'done']
    print('1. Add task')
    print('2. Remove task')
    print('3. List tasks')
    print('4. Change state ')
    print('5. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        task_name = input('Enter task name: ')
        task = Task(task_name)
        task_list.add_task(task)
    elif choice == '2':
        task_name = input('Enter task name: ')
        task = Task(task_name)
        task_list.remove_task(task)
        print('Task removed')
    elif choice == '3':
        task_list.list_tasks()
    elif choice == '4':
        task_name = input('Enter task name: ')
        new_state = input('Enter new state (todo, doing, done): ')
        if new_state not in states :
            print('Invalid state')
            continue
        elif task_list.get_task(task_name) == None:
            print('Task does not exist')
            continue
        else:
            task = task_list.get_task(task_name)
            task.change_state(new_state)
            print('State changed')
    elif choice == '5':
        print('Goodbye!')
        break
    else:
        print('Invalid choice')








