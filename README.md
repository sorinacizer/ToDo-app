# TO DO app

### This is a ToDo app that records all the daily tasks. 
In this application you can register tasks with specific deadlines and also the status of them.
This tasks are saved in DataBase(SQLite3). With the button "Sort by date", you can see the tasks in chronological order.

#### GitHub url: 
> https://github.com/sorinacizer/ToDo-app

### Grafic Interface:
![img.png](./data/img.png)

### How to record your tasks:
1. Register, if you are a new user;
2. Login
3. Add your tasks

This is a code example:
```commandline
      def add_task_deadline(self):
        task = self.entry_task.get()
        selected_date = self.cal.get_date()
        var = self.var.get()
        self.tree_view.insert('', 'end', values=(task, selected_date, var))

        self.entry_task.delete(first='0', last='-1')
        self.entry_task.focus()
        self.entry_task.after(1000, lambda: self.task_var.set(''))
```

#### Register:
![img_4.png](./data/img_2.png)

#### Login:
![img.png](./data/img3.png)
