import tkinter as tk
from tkinter import messagebox
import re
import sqlite3
import datetime as dt
from tkcalendar import *
from tkinter import ttk

__auther__ = 'Sorina Ivan'
__maintainer__ = 'Sorina Ivan'
__email__ = 'sorina.cizer@gmail.com'

__all__ = []


class Task:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('1000x600')
        self.root.configure(bg='#70d6ff')
        self.root.title("TO DO APP")

        self.frame_start_page = tk.Frame(self.root, bg='white', width=800, height=300, highlightbackground="blue",
                                         highlightthickness=2)
        self.frame_start_page.grid(padx=400, pady=10)

        self.label_app_name = tk.Label(self.frame_start_page, text='TO DO', font=('Caveat bold', 45), fg='black',
                                       bg='white')
        self.label_app_name.grid(column=1, row=0, padx=45, pady=40)

        self.register_button = tk.Button(self.frame_start_page, text='Register', font=('Arial', 15), bg='blue',
                                         fg='white',
                                         activeforeground='gray', width=10, command=self.register)
        self.register_button.grid(column=1, row=1, pady=40)

        self.login_button = tk.Button(self.frame_start_page, text="Login", font=('Arial', 15), bg='blue', fg='white',
                                      activeforeground='gray', width=10, command=self.login)
        self.login_button.grid(column=1, row=2, pady=40)

        self.root.mainloop()

    def register(self):
        self.register_page = tk.Toplevel(self.root)
        self.register_page.geometry('1000x600')
        self.register_page.configure(bg='#70d6ff')
        self.register_page.title('Register')

        self.frame_register = tk.Frame(self.register_page, bg='white', highlightbackground="blue", highlightthickness=2)
        self.frame_register.grid(padx=350, pady=40)

        self.label_title = tk.Label(self.frame_register, text='Register', font=('Arial', 25), bg='white')
        self.label_title.grid(column=1, row=0)

        self.label_user = tk.Label(self.frame_register, text='Username:', font=('Arial', 15), bg='white')
        self.label_user.grid(column=0, row=2, padx=10)

        self.user_var = tk.StringVar()
        self.entry_user = tk.Entry(self.frame_register, textvariable=self.user_var, font=('Arial', 15))
        self.entry_user.grid(column=1, row=2, padx=20)

        self.label_pass = tk.Label(self.frame_register, text='Password:', font=('Arial', 15), bg='white')
        self.label_pass.grid(column=0, row=3)

        self.pass_var = tk.StringVar()
        self.entry_pass = tk.Entry(self.frame_register, textvariable=self.pass_var, show='*', font=('Arial', 15))
        self.entry_pass.grid(column=1, row=3)

        self.label_email = tk.Label(self.frame_register, text='Email:', font=('Arial', 15), bg='white')
        self.label_email.grid(column=0, row=4)

        self.email_var = tk.StringVar()
        self.entry_email = tk.Entry(self.frame_register, textvariable=self.email_var, font=('Arial', 15))
        self.entry_email.grid(column=1, row=4)

        self.label_last_name = tk.Label(self.frame_register, text='Last Name:', font=('Arial', 15), bg='white')
        self.label_last_name.grid(column=0, row=5)

        self.last_var = tk.StringVar()
        self.entry_last = tk.Entry(self.frame_register, textvariable=self.last_var, font=('Arial', 15))
        self.entry_last.grid(column=1, row=5)

        self.label_first_name = tk.Label(self.frame_register, text='First Name:', font=('Arial', 15), bg='white')
        self.label_first_name.grid(column=0, row=6)

        self.first_var = tk.StringVar()
        self.entry_first = tk.Entry(self.frame_register, textvariable=self.first_var, font=('Arial', 15))
        self.entry_first.grid(column=1, row=6)

        self.register_button = tk.Button(self.frame_register, text="Register", font=('Arial', 15), bg='dark blue',
                                         fg='white',
                                         activeforeground='gray', width=10,
                                         command=lambda: [self.validation(), self.register_in_db()])
        self.register_button.grid(column=1, row=7, pady=20)

    def validation(self):
        last_name = self.entry_last.get()
        first_name = self.entry_first.get()
        passwd = self.entry_pass.get()
        email = self.entry_email.get()
        msg = ''
        symb = ['!', '#', '@', '%']
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if len(last_name) & len(first_name) == 0:
            msg = 'Last name/First name can\'t be empty!'
        else:
            try:
                if any(i.isdigit() for i in last_name) & any(j.isdigit() for j in first_name):
                    msg = 'Last/First name can\'t have numbers!'
                elif len(last_name) & len(first_name) <= 2:
                    msg = 'Last/First name is too short!'
                elif len(last_name) & len(first_name) > 100:
                    msg = 'Last/First name is too long!'
                elif len(passwd) < 6:
                    msg = 'Password length should be at least 6 characters!'
                elif not any(s in symb for s in passwd):
                    msg = 'Password should have at least one of the symbols: !, #, @, %'
                elif not re.fullmatch(pattern, email):
                    msg = 'Email is not valid!'
                else:
                    msg = 'You registered with success!'
            except Exception as e:
                messagebox.showinfo('ERROR', e)
        messagebox.showinfo("Message", msg)

    def register_in_db(self):
        usr_name = self.entry_user.get()
        passwd = self.entry_pass.get()
        email = self.entry_email.get()
        lst_name = self.entry_last.get()
        fst_name = self.entry_first.get()

        if passwd:
            # Create DB or connect to DB
            conn = sqlite3.connect('users.db')

            # Create cursor
            cur = conn.cursor()

            # Create table
            cur.execute('''CREATE TABLE IF NOT EXISTS Users_Data
                     (id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                     user_name TEXT, 
                     password TEXT, 
                     email TEXT, 
                     last_name TEXT, 
                     first_name TEXT)''')

            cur.execute(
                f'INSERT INTO Users_Data(user_name, password, email, last_name, first_name) VALUES (?, ?, ?, ?, ?)',
                (usr_name, passwd, email, lst_name, fst_name))

            conn.commit()

            conn.close()

    def login(self):
        self.login_page = tk.Toplevel(self.root)
        self.login_page.geometry('1000x600')
        self.login_page.configure(bg='#70d6ff')
        self.login_page.title('Login')

        self.frame_login = tk.Frame(self.login_page, bg='white', highlightbackground="blue", highlightthickness=2)
        self.frame_login.grid(padx=350, pady=40)

        self.label_title = tk.Label(self.frame_login, text='Login', font=('Arial', 25), bg='white')
        self.label_title.grid(column=1, row=0)

        self.label_user = tk.Label(self.frame_login, text='Username:', font=('Arial', 15), bg='white')
        self.label_user.grid(column=0, row=2)

        self.user_var = tk.StringVar()
        self.entry_user = tk.Entry(self.frame_login, textvariable=self.user_var, font=('Arial', 15))
        self.entry_user.grid(column=1, row=2, padx=20)

        self.label_pass = tk.Label(self.frame_login, text='Password:', font=('Arial', 15), bg='white')
        self.label_pass.grid(column=0, row=3)

        self.pass_var = tk.StringVar()
        self.entry_pass = tk.Entry(self.frame_login, textvariable=self.pass_var, show='*', font=('Arial', 15))
        self.entry_pass.grid(column=1, row=3)

        self.login_button = tk.Button(self.frame_login, text="Login", font=('Arial', 15), bg='dark blue',
                                      fg='white',
                                      activeforeground='gray', width=10,
                                      command=self.login_in_app)
        self.login_button.grid(column=1, row=4, pady=20)

    def login_in_app(self):
        conn = sqlite3.connect('users.db')

        # Create cursor
        cur = conn.cursor()

        find_user = 'SELECT * from Users_Data WHERE user_name = ? and password = ?'
        cur.execute(find_user, [(self.entry_user.get()), (self.entry_pass.get())])

        result = cur.fetchall()
        for rez in result:
            tk.messagebox.showinfo('Congratulations! You\'re logged in!')
            self.login_page.after(2, self.task)

        conn.commit()

        conn.close()

    def task(self):
        self.task_page = tk.Toplevel(self.root)
        self.task_page.geometry('1000x600')
        self.task_page.configure(bg='#70d6ff')
        self.task_page.title("TO DO APP")

        self.label_app_name = tk.Label(self.task_page, text='TO DO', font=('Caveat bold', 18), fg='black', bg='#70d6ff')
        self.label_app_name.grid(column=1, row=0, padx=230, pady=40)

        self.photo_app = tk.PhotoImage(
            file=r'C:\Users\I351631\OneDrive - SAP SE\Desktop\IT School\ToDo app\data\checklist1.png')
        self.label_image = tk.Label(image=self.photo_app, width=100, height=100, bg='#70d6ff')
        self.label_image.grid(column=1, row=0, sticky='e', padx=110)

        self.date = dt.datetime.now()
        self.label_date = tk.Label(self.task_page, text=f"Today: {self.date:%A, %B %d, %Y}",
                                   font=("Caveat", 17, 'underline'), bg='#70d6ff')
        self.label_date.grid(column=0, row=0, pady=10, padx=5)

        self.label_task = tk.Label(self.task_page, text='Task:', font=("Caveat", 17), bg='#70d6ff')
        self.label_task.grid(column=0, row=1, sticky='w', padx=20)

        self.task_var = tk.StringVar()
        self.entry_task = tk.Entry(self.task_page, textvariable=self.task_var, font=('calibre', 10))
        self.entry_task.grid(column=0, row=1, sticky='e')

        self.label_deadline = tk.Label(self.task_page, text='Deadline:', font=("Caveat", 17), bg='#70d6ff')
        self.label_deadline.grid(column=1, row=1, sticky='w', padx=50)

        self.cal = Calendar(self.task_page,
                            selectmode='day',
                            background='RoyalBlue',
                            foreground="MediumBlue",
                            selectbackground="RoyalBlue",
                            normalbackground="DeepSkyBlue",
                            weekendbackground="DodgerBlue")
        self.cal.grid(column=1, row=1)

        self.radio_frame = tk.Frame(self.task_page, bg='#70d6ff')
        self.radio_frame.grid(column=1, row=1, sticky='e', padx=20)
        self.var = tk.StringVar()
        self.R1 = tk.Radiobutton(self.radio_frame, text="Not Started", font=("Caveat", 17), variable=self.var,
                                 value="Not Started", bg='#70d6ff')
        self.R1.grid(column=1, row=1, sticky='w')

        self.R2 = tk.Radiobutton(self.radio_frame, text="In Progress", font=("Caveat", 17), variable=self.var,
                                 value="In Progress", bg='#70d6ff')
        self.R2.grid(column=1, row=2, sticky='w')

        self.R3 = tk.Radiobutton(self.radio_frame, text="Done", font=("Caveat", 17), variable=self.var, value="Done",
                                 bg='#70d6ff')
        self.R3.grid(column=1, row=3, sticky='w')
        self.var.set("Not Started")

        self.button_add = tk.Button(self.task_page, text="Add", font=("Caveat", 15), bg='dark blue', fg='white',
                                    activeforeground='gray', width=10, command=self.add_task_deadline)
        self.button_add.grid(column=2, row=1, sticky='e')

        self.tree_view = ttk.Treeview(self.task_page, selectmode="browse", show='headings', height=5)

        self.tree_view.grid(column=1, row=2, pady=20)
        self.scrbar = ttk.Scrollbar(self.task_page, orient='vertical', command=self.tree_view.yview)
        self.scrbar.grid(column=1, row=2, sticky='nse', pady=21)
        self.tree_view.configure(yscrollcommand=self.scrbar.set)

        self.tree_view['columns'] = ('1', '2', '3')
        self.tree_view.column("1", anchor='c')
        self.tree_view.column("2", anchor='c')
        self.tree_view.column("3", anchor='c')
        self.tree_view.heading("1", text="Tasks")
        self.tree_view.heading("2", text="Deadlines")
        self.tree_view.heading("3", text="Status")

        self.tree_view.bind("<Double-1>", self.on_double_click)

        self.button_sort = tk.Button(self.task_page, text="Sort by date", font=("Caveat", 15), bg='dark blue',
                                     fg='white',
                                     activeforeground='gray', width=10, command=self.sort_tree_view)
        self.button_sort.grid(column=2, row=2, sticky='n', pady=20)

        self.button_remove = tk.Button(self.task_page, text="Remove", font=("Caveat", 15), bg='dark blue', fg='white',
                                       activeforeground='gray', width=10, command=self.remove_task)
        self.button_remove.grid(column=2, row=2, sticky='s', pady=60)

        self.button_save = tk.Button(self.task_page, text='Save', font=("Caveat", 15), bg='dark blue', fg='white',
                                     activeforeground='gray', width=10, command=self.save_task)
        self.button_save.grid(column=2, row=2, sticky='s', pady=20)

    def add_task_deadline(self):
        task = self.entry_task.get()
        selected_date = self.cal.get_date()
        var = self.var.get()
        self.tree_view.insert('', 'end', values=(task, selected_date, var))

        self.entry_task.delete(first='0', last='-1')
        self.entry_task.focus()
        self.entry_task.after(1000, lambda: self.task_var.set(''))

    def remove_task(self):
        selected_item = self.tree_view.selection()[0]
        self.tree_view.delete(selected_item)

    def on_double_click(self, event):
        region_clicked = ttk.Treeview.identify_region(self.tree_view, event.x, event.y)
        column = ttk.Treeview.identify_column(self.tree_view, event.x)
        selected_id = self.tree_view.focus()
        selected_values = self.tree_view.item(selected_id)
        column_index = int(column[1:]) - 1
        if region_clicked not in ("tree", "cell"):
            return
        selected_text = selected_values.get("values")[column_index]

        column_box = ttk.Treeview.bbox(self.tree_view, selected_id, column)

        entry_edit = ttk.Entry(self.tree_view)

        # Record the column index and item id
        entry_edit.editing_column_index = column_index
        entry_edit.editing_item_id = selected_id

        entry_edit.insert(0, selected_text)
        entry_edit.select_range(0, tk.END)

        entry_edit.focus()

        entry_edit.bind("<FocusOut>", self.on_focus_out)

        entry_edit.bind("<Return>", self.on_enter_pressed)

        entry_edit.place(x=column_box[0], y=column_box[1], w=column_box[2])

    def on_focus_out(self, event):
        event.widget.destroy()

    def on_enter_pressed(self, event):
        new_text = event.widget.get()
        selected_id = event.widget.editing_item_id
        column_index = event.widget.editing_column_index
        current_values = self.tree_view.item(selected_id).get("values")
        current_values[column_index] = new_text
        self.tree_view.item(selected_id, values=current_values)

        event.widget.destroy()

    def sort_tree_view(self):
        # Create DB or connect to DB
        conn = sqlite3.connect('users.db')

        # Create cursor
        cur = conn.cursor()

        # Create table
        cur.execute('SELECT task_name, deadline, status FROM Users_Tasks ORDER BY deadline;')
        all_tasks = cur.fetchall()
        print(all_tasks)
        for item in self.tree_view.get_children():
            self.tree_view.delete(item)
        for i in all_tasks:
            self.tree_view.insert(parent='', index='end', values=(i[0], i[1], i[2]))

        conn.commit()
        conn.close()

    def get_all_tasks(self):
        conn = sqlite3.connect('users.db')

        # Create cursor
        cur = conn.cursor()
        id_user = cur.execute('SELECT id_user FROM Users_Data WHERE user_name = ?;', [self.entry_user.get()])
        rez = id_user.fetchall()
        conn.close()

        all_tasks = []

        for line in self.tree_view.get_children():
            values = self.tree_view.item(line)["values"]
            values.append(rez[0][0])
            all_tasks.append(tuple(values))

        return all_tasks

    def save_task(self):
        all_tasks = self.get_all_tasks()

        # Create DB or connect to DB
        conn = sqlite3.connect('users.db')

        # Create cursor
        cur = conn.cursor()

        # Create table
        cur.execute('''CREATE TABLE IF NOT EXISTS Users_Tasks
                                   (task_name TEXT, 
                                   deadline TEXT, 
                                   status TEXT, 
                                   id_user INTEGER,
                                   FOREIGN KEY(id_user) REFERENCES Users_Data (id_user));''')

        cur.execute('DELETE FROM Users_Tasks')
        cur.executemany(f'INSERT INTO Users_Tasks(task_name, deadline, status, id_user) VALUES(?, ?, ?, ?);', all_tasks)

        conn.commit()

        x = cur.execute('SELECT * FROM Users_Tasks;')
        print(x.fetchall())

        conn.close()


if __name__ == '__main__':
    task = Task()
