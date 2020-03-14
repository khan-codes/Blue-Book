from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import os
import random




import sqlite3
with sqlite3.connect('test_01.db') as db:
    pass

class Timer:
    def __init__(self, master):
        self.master = master
        master.title("Blue Book")

        self.state = False
        self.minutes = 1
        self.seconds = 1

        self.mins = 1
        self.secs = 1


        self.countdown()
        self.display = tk.Label(master, height=5, width=5, textvariable="")
        self.display.config(text="00:00")
        self.display.config(font=('Times New Roman', 15, 'bold'))
        self.display.grid(row=23, column=27, columnspan=2, rowspan=2)

        self.start_button = tk.Button(master, bg="SpringGreen2", activebackground="SpringGreen2", fg='black', text="Start", width=5, height=2, command=self.start)
        self.start_button.grid(row=24, column=26, columnspan=2, rowspan=2)

        self.pause_button = tk.Button(master, bg="IndianRed1", activebackground="IndianRed1", fg='black', text="Pause", width=5, height=2, command=self.pause)
        self.pause_button.grid(row=24, column=28, columnspan=2, rowspan=2)

        self.stop_button = tk.Button(master, bg='red', activebackground='red', fg='white', text='Stop', width=5, height=2, command=self.stop)
        self.stop_button.grid(row=24, column=27, columnspan=2, rowspan=2)


    def countdown(self):
        if self.state == True:
            if self.secs < 10:
                if self.mins < 10:
                    self.display.config(text="0%d : 0%d" % (self.mins, self.secs))
                else:
                    self.display.config(text="%d : 0%d" % (self.mins, self.secs))
            else:
                if self.mins < 10:
                    self.display.config(text="0%d : %d" % (self.mins, self.secs))
                else:
                    self.display.config(text="%d : %d" % (self.mins, self.secs))

            if (self.mins == 0) and (self.secs == 0):
                global time_taken
                time_taken = (self.minutes*60) + self.seconds
                print('Time taken: ', time_taken)
                global score
                print('Score:', score)
                self.display.config(text="Done!")
                self.master.destroy()
            else:
                if self.secs == 0:
                    self.mins -= 1
                    self.secs = 59
                else:
                    self.secs -= 1

                self.master.after(1000, self.countdown)
        else:
            self.master.after(100, self.countdown)

    def start(self):
        if self.state == False:
            self.state = True
            self.mins = self.minutes
            self.secs = self.seconds

    def pause(self):
        if self.state == True:
            self.state = False

    def stop(self):
        global time_taken
        global score
        if self.state == True:
            self.state = False
            time_taken = ((self.minutes * 60) + self.seconds) - ((self.mins * 60) + self.secs)
            print('Time taken:', time_taken)
            print('Score:', score)
            self.master.destroy()

def doNothing():
    x = 0



def proceed(root, selected_category_in, selected_scientist_in):
    if selected_scientist_in != 'None':
        global selected_scientist
        global selected_category
        selected_scientist = selected_scientist_in
        selected_category = selected_category_in
        #print('You have selected ' + selected_scientist + ' of ' + selected_category)
        root.destroy()

    else:
        not_none = Label(root, text="You can't select none!")
        not_none.config(font=('Helvetica', 12, 'bold'), fg='red')
        not_none.grid(row=1, column=8, columnspan=2, sticky=E)

#DEFINING THE WINDOW
root = Tk()
root.title('Blue Book')
root.minsize(300, 100)
root.geometry('600x500')
sp = 'C:/Users/az/Desktop/PiON'
imgicon = PhotoImage(file=os.path.join(sp, 'blue-book-reading-hi.png'))
root.tk.call('wm', 'iconphoto', root._w, imgicon)


def clear_widget(event):
    # will clear out any entry boxes defined below when the user shifts
    # focus to the widgets defined below
    if entry_name == root.focus_get() and entry_name.get() == 'Enter Username':
        entry_name.config(fg='black')
        entry_name.delete(0, END)
    elif entry_password == entry_password.focus_get() and entry_password.get() == '     ':
        entry_password.config(fg='black')
        entry_password.delete(0, END)


def repopulate_defaults(event):
    # will repopulate the default text previously inside the entry boxes defined below if
    # the user does not put anything in while focused and changes focus to another widget
    if entry_name != root.focus_get() and entry_name.get() == '':
        entry_name.insert(0, 'Enter Username')
        entry_name.config(fg='gray50')
    elif entry_password != root.focus_get() and entry_password.get() == '':
        entry_password.insert(0, '     ')
        entry_password.config(fg='gray50')

def login(*event):
    #this event is supposed to happen when thw user hit the ok button as a messag ein displayed. the message box widget is very importanr here
    username = 'bscs1627@pieas.edu.pk'
    password = '72784'
    answer = 'Yes'
    if entry_password.get() == password and entry_name.get() == username:
        root.destroy()
        print('Logged in')
        selecting_window()
        main_game_window()
        final_window()


    else:
        wrong = Label(root, text="Incorrect Username or Password")
        wrong.config(font=('Helvetica', 12, 'bold'), fg='red')
        wrong.grid(row=1, column=5, sticky=W)
        entry_password.delete(0, END)
        entry_name.delete(0, END)

def menu_bar(root):
    # MAKING THE MENU OBJECT
    menu_bar = Menu(root)

    # MAKING MENU SUB HEADINGS/OBJECTS/PARTS
    PiON_menu = Menu(menu_bar, tearoff=0)
    PiON_menu.add_command(label='What is it?', command=doNothing())
    PiON_menu.add_separator()
    PiON_menu.add_command(label='Previous', command=doNothing())
    menu_bar.add_cascade(label='PiON', menu=PiON_menu)

    rules_menu = Menu(menu_bar, tearoff=0)
    rules_menu.add_command(label='Blue Book rules', command=doNothing())
    rules_menu.add_separator()
    rules_menu.add_command(label='PiON rules', command=doNothing())
    menu_bar.add_cascade(label='Rules', menu=rules_menu)

    help_menu = Menu(menu_bar, tearoff=0)
    help_menu.add_command(label='Hint', command=doNothing())
    help_menu.add_separator()
    help_menu.add_command(label='Feedback', command=doNothing())
    menu_bar.add_cascade(label='Help', menu=help_menu)

    about_menu = Menu(menu_bar, tearoff=0)
    about_menu.add_command(label='Blue Book Team', command=doNothing())
    about_menu.add_separator()
    about_menu.add_command(label='Module head', command=doNothing())
    about_menu.add_separator()
    about_menu.add_command(label='Developer', command=doNothing())
    menu_bar.add_cascade(label='About', menu=about_menu)

    # CONFIGURING THESE ALL SUB PARTS
    root.config(menu=menu_bar)


def statusbar(root):
    status = Label(root, text='Activity Executed    Code:00x7A', bd=1, relief=SUNKEN, anchor=W)
    status.grid(row=25, column=0, sticky='ew')
    root.columnconfigure(0, weight=1)


def selecting_window():
    #DEFINING THE NEW MAIN WINDOW
    root = Tk()
    root.title('Blue Book by Dawood Sher Jan')
    root.minsize(300, 100)
    root.geometry('600x500')

    sp = 'C:/Users/az/Desktop/PiON'
    imgicon = PhotoImage(file=os.path.join(sp, 'blue-book-reading-hi.png'))
    root.tk.call('wm', 'iconphoto', root._w, imgicon)

    #DEFINING 50 ROWS
    rows = 0
    while rows < 25:
        root.rowconfigure(rows, weight=1)
        root.columnconfigure(rows, weight=1)
        rows += 1

    menu_bar(root)
    #statusbar(root)


    #LABELS OF CATEGORIES
    label_text_01 = 'NineteenthCentury'
    label_text_02 = 'Early20thCentury'
    label_text_03 = 'Late20thCentury'

    label_category01 = Label(root, text=label_text_01)
    label_category01.config(font=('Times New Roman', 13, 'bold'))
    label_category01.grid(row=6, column=5)


    label_category02 = Label(root, text=label_text_02)
    label_category02.config(font=('Times New Roman', 13, 'bold'))
    label_category02.grid(row=6, column=14, columnspan=2)

    label_category03 = Label(root, text=label_text_03)
    label_category03.config(font=('Times New Roman', 13, 'bold'))
    label_category03.grid(row=12, column=8, columnspan=2)


    #MAKING A COMBOBOX
    cat01_text = tk.StringVar()
    cat02_text = tk.StringVar()
    cat03_text = tk.StringVar()


    combo = ttk.Combobox(root, width=25, textvariable = cat01_text, state='readonly')
    combo_2 = ttk.Combobox(root, width=25, textvariable = cat02_text, state='readonly')
    combo_3 = ttk.Combobox(root, width=25, textvariable = cat03_text, state='readonly')

    #COMBO NUMBER 01
    combo['values'] = ['None', '01', '02', '03', '04', '05', '06', '07', '08']
    combo.current(0)
    combo.grid(row=7, column=5)

    #COMBO NUMBER 02
    combo_2['values'] = ['None', '01', '02', '03', '04', '05', '06', '07', '08']
    combo_2.current(0)
    combo_2.grid(row=7, column=14, columnspan=2)

    #COMBO NUMBER 03
    combo_3['values'] = ['None', '01', '02', '03', '04', '05', '06', '07', '08']
    combo_3.current(0)
    combo_3.grid(row=13, column=8, columnspan=2)


    #SELECTION BUTTON ICON
    img_icon_proceed = PhotoImage(file='right-arrow.png')
    label_icon_proceed = Label(root, image=img_icon_proceed)
    label_icon_proceed.image = img_icon_proceed

    #SELECTION BUTTONS
    selection_button_01 = Button(root, image=img_icon_proceed, text='Proceed  ', fg='navy', bg='sienna1', command=lambda : proceed(root, label_text_01, combo.get()), compound=RIGHT)
    selection_button_01.config(font=('Times New Roman', 13, 'bold'))
    selection_button_01.grid(row=8, column=5, columnspan=2, ipadx=15)

    selection_button_02 = Button(root, image=img_icon_proceed, text='Proceed  ', fg='navy', bg='sienna1', command=lambda : proceed(root, label_text_02, combo_2.get()), compound=RIGHT)

    selection_button_02.config(font=('Times New Roman', 13, 'bold'))
    selection_button_02.grid(row=8, column=14, columnspan=2, ipadx=15)

    selection_button_03 = Button(root, image=img_icon_proceed, text='Proceed  ', fg='navy', bg='sienna1', command=lambda : proceed(root, label_text_03, combo_3.get()), compound=RIGHT)
    selection_button_03.config(font=('Times New Roman', 13, 'bold'))
    selection_button_03.grid(row=14, column=8, columnspan=2, ipadx=15)

    root.mainloop()


selected_scientist = ''
selected_category = ''
selected_scientist_name = ''

#ID'S FOR HINTS
hints_i = random.sample(range(1,6), 5)
index = 0

def big_hints(root, button, row_no, column_no):
    #ADD A MESSAGE BOX TO GET CONFIRMATION
    answer = tkinter.messagebox.askquestion('Blue Book', 'Do you really want a big hint?')
    global selected_category
    global selected_scientist_name

    if answer == 'yes':
        #QUERY FROM DATA BASE
        global hints_i
        global index
        global selected_scientist

        hint = 'Question0' + str(hints_i[index])
        index = index + 1
        id = selected_scientist

        connection = sqlite3.connect('test_01.db')
        cursor = connection.cursor()

        cursor.execute('SELECT ({coi}) FROM {tn} WHERE {cn}={my_id}'. \
                format(coi=hint, tn=selected_category, cn='ID', my_id=str(id)))

        all_rows = cursor.fetchall()

        #TO GET THE NAME OF THE SCIENTIST
        cursor.execute('SELECT ({coi}) FROM {tn} WHERE {cn}={my_id}'. \
                       format(coi='Name', tn=selected_category, cn='ID', my_id=str(id)))
        selected_scientist_name = cursor.fetchall()
        #print(selected_scientist_name)
        connection.close()

        hint = all_rows
        label_hint = Label(root, text=hint, fg='IndianRed2')
        label_hint.config(font=('Times New Roman', 12, 'italic'))
        label_hint.grid(row=row_no, column=column_no, columnspan=15, sticky=W+E)

        global score
        score = score - 10
        label_score = Label(root, text='Total= ' + str(score), fg='red2')
        label_score.config(font=('Times New Roman', 15, 'bold'))
        label_score.grid(row=24, column=0, columnspan=3, rowspan=2)
        button.config(state=DISABLED)

    elif answer == 'No':
        doNothing()



def small_hints(root, button, row_no, column_no):
    #ADD A MESSAGE BOX TO GET CONFIRMATION
    answer = tkinter.messagebox.askquestion('Blue Book', 'Do you really want a small hint?')
    global selected_category

    if answer == 'yes':
        #QUERY FROM DATA BASE
        global hints_i
        global index
        global selected_scientist

        hint = 'Question0' + str(hints_i[index])
        index = index + 1
        id = selected_scientist
        connection = sqlite3.connect('test_01.db')
        cursor = connection.cursor()

        cursor.execute('SELECT ({coi}) FROM {tn} WHERE {cn}={my_id}'. \
                       format(coi=hint, tn=selected_category, cn='ID', my_id=str(id)))

        all_rows = cursor.fetchall()
        connection.close()

        hint = all_rows
        label_hint = Label(root, text=hint, fg='IndianRed2')
        label_hint.config(font=('Times New Roman', 12, 'italic'))
        label_hint.grid(row=row_no, column=column_no, columnspan=15, sticky=W+E)

        global score
        score = score - 5
        label_score = Label(root, text='Total= ' + str(score), fg='red2')
        label_score.config(font=('Times New Roman', 15, 'bold'))
        label_score.grid(row=24, column=0, columnspan=3, rowspan=2)
        button.config(state=DISABLED)

    elif answer == 'No':
        doNothing()

score = 50
time_taken = 0
final_score = 0

def main_game_window():
    global selected_category
    global selected_scientist
    #DEFINING THE NEW MAIN WINDOW
    root = Tk()
    root.title('Blue Book by Dawood Sher Jan')
    root.minsize(300, 100)
    root.geometry('800x600')

    sp = 'C:/Users/az/Desktop/PiON'
    imgicon = PhotoImage(file=os.path.join(sp, 'blue-book-reading-hi.png'))
    root.tk.call('wm', 'iconphoto', root._w, imgicon)

    #DEFINING 50 ROWS
    rows = 0
    while rows < 25:
        root.rowconfigure(rows, weight=1)
        root.columnconfigure(rows, weight=1)
        rows += 1


    scientist_selected = 'No one'

    #SORE lABEL
    global score
    label_score = Label(root, text='Total= ' + str(score), fg='red2')
    label_score.config(font=('Times New Roman', 15, 'bold'))
    label_score.grid(row=24, column=0, columnspan=3, rowspan=2)

    #LOADING UNKNOWN LOGO
    img = PhotoImage(file='Businessman_2-2-256.png')
    displayimage = img.subsample(3, 3)
    panel = Label(root, image=displayimage)
    panel.image = displayimage
    panel.grid(row=0, column=2, columnspan=3, rowspan=2, sticky=W+E)

    #LABEL TO DISPLAY BASIC RULES
    img_icon = PhotoImage(file='minus.png')
    label_icon = Label(root, image=img_icon)
    label_icon.image = img_icon
    label_icon.grid(row=0, column=24, rowspan=2, sticky=E)
    label_rules = Label(root, text='Big hint subtracts ten points\n    Small hint subtracts five points')
    label_rules.config(font=('Times New Roman', 10, 'bold'))
    label_rules.grid(row=0, column=25, columnspan=3, rowspan=2, ipadx=10, ipady=10)

    #INITIAL HINT LABEL
    initial_hint = 'Here Goes The Initial Hint'
    label_initial_hint = Label(root, text=initial_hint, fg='firebrick1')
    label_initial_hint.config(font=('Times New Roman', 12, 'bold'))
    label_initial_hint.grid(row=0, column=12, columnspan=4)


    menu_bar(root)


    #LOADING BULB LOGO
    img_icon_bulb = PhotoImage(file='light-bulb.png')
    label_icon_bulb = Label(root, image=img_icon_bulb)
    label_icon_bulb.image = img_icon_bulb

    #HINT BUTTONS
    #TO CHECK THAT A BUTTON GETS PRESSED NO MORE THAN ONCE
    #FIRST BIG
    global double_check
    big01 = Button(root, image=img_icon_bulb, text='  Big Hint', fg='black', bg='light steel blue',command=lambda: big_hints(root, big01, 4, 2), compound=LEFT)
    big01.config(font=('Helvetica', 10, 'bold'))

    #SECOND BIG
    big02 = Button(root, image=img_icon_bulb, text='  Big Hint', fg='black', bg='light steel blue', command=lambda: big_hints(root, big02, 6, 2), compound=LEFT)
    big02.config(font=('Helvetica', 10, 'bold'))

    small01 = Button(root, image=img_icon_bulb, text='  Small Hint', fg='black', bg='SpringGreen2', command=lambda: small_hints(root, small01, 8, 2), compound=LEFT)
    small01.config(font=('Helvetica', 10, 'bold'))

    small02 = Button(root, image=img_icon_bulb, text='  Small Hint', fg='black', bg='SpringGreen2', command=lambda: small_hints(root, small02, 10, 2), compound=LEFT)
    small02.config(font=('Helvetica', 10, 'bold'))

    small03 = Button(root, image=img_icon_bulb, text='  Small Hint', fg='black', bg='SpringGreen2', command=lambda: small_hints(root, small03, 12, 2), compound=LEFT)
    small03.config(font=('Helvetica', 10, 'bold'))


    #GRID THE BUTTONS
    big01.grid(row=3, column=2, columnspan=1, ipadx=13, pady=10, sticky=E)
    big02.grid(row=5, column=2, columnspan=1, ipadx=13, pady=10, sticky=E)
    small01.grid(row=7, column=2, columnspan=2, ipadx=13, pady=10)
    small02.grid(row=9, column=2, columnspan=2, ipadx=13, pady=10)
    small03.grid(row=11, column=2, columnspan=2, ipadx=13, pady=10)

    my_timer = Timer(root)
    root.mainloop()


def final_window():
    # DEFINING THE NEW MAIN WINDOW
    root = Tk()
    root.title('Blue Book by Dawood Sher Jan')
    root.minsize(300, 100)
    root.geometry('500x300')

    sp = 'C:/Users/az/Desktop/PiON'
    imgicon = PhotoImage(file=os.path.join(sp, 'blue-book-reading-hi.png'))
    root.tk.call('wm', 'iconphoto', root._w, imgicon)

    # DEFINING 50 ROWS
    rows = 0
    while rows < 15:
        root.rowconfigure(rows, weight=1)
        root.columnconfigure(rows, weight=1)
        rows += 1

    menu_bar(root)

    answer = tkinter.messagebox.askquestion('Blue Book', 'Was the answer correct?')
    if answer == 'yes':
        #CORRECT ANSWER LABEL
        global selected_scientist_name
        label_score = Label(root, text='Correct Answer: %s' % (selected_scientist_name), fg='OrangeRed2')
        label_score.config(font=('Times New Roman', 20, 'bold'))
        label_score.grid(row=2, column=3, columnspan=2, rowspan=3, sticky=W+E)

        #SCORE LABEL
        global score
        label_score = Label(root, text='Final Score: %d Points' % (score), fg='OrangeRed2')
        label_score.config(font=('Times New Roman', 14, 'bold'))
        label_score.grid(row=6, column=3, columnspan=2, rowspan=3, sticky=W+E)

        #TIME TAKEN LABEL
        global time_taken
        label_time_taken = Label(root, text='Total Time Taken: %d Seconds' % (time_taken), fg='OrangeRed2')
        label_time_taken.config(font=('Times New Roman', 14, 'bold'))
        label_time_taken.grid(row=10, column=3, columnspan=2, rowspan=3)
    else:
        root.destroy()


    #input('Press enter to exit')

    root.mainloop()



#   ******************************  BAKWAS!!!!!!  *** THE FIRST/LOGIN WINDOW  *****************************

#DEFINING 50 ROWS
rows = 0
while rows < 10:
    root.rowconfigure(rows, weight=1)
    root.columnconfigure(rows, weight=1)
    rows += 1


#LOADING SIGNIN LOGO
img_icon = PhotoImage(file='key.png')
label_icon = Label(root, image=img_icon)
label_icon.image = img_icon


#LOGIN BUTTON
button_login = Button(root, image=img_icon, text='  LOGIN', fg='black', bg='lavender', command=login, compound=LEFT)
button_login.config(font=('impact', 13))
button_login.bind('<Return>', login)
button_login.grid(row=4, column=5, columnspan=2, ipadx=20, ipady=4, sticky=W)


#LOGIN LABELS DEFINATION
label_name = Label(root, text="User Name")
label_name.config(font=('Helvetica', 12, 'bold'))
label_password = Label(root, text="Password")
label_password.config(font=('Helvetica', 12, 'bold'))


#PUTTING LOGIN LABELS IN A GRID
label_name.grid(row=2, column=4, pady=6, sticky=E)
label_password.grid(row=3, column=4, pady=6, sticky=E)

#LOGIN ENTRY WIDGET DEFINATION
entry_name = Entry(root, width=30)
entry_name.config(fg='gray50')
entry_name.insert(0, 'Enter Username')
entry_name.bind("<FocusIn>", clear_widget)
entry_name.bind('<FocusOut>', repopulate_defaults)
entry_name.config(font=(12))
#   ****************   FOCUS   ****************
entry_name.focus()

entry_password = Entry(root, width=30, fg='gray50')
bullet = "\u2022"
entry_password.insert(0, '     ')
entry_password.bind("<FocusIn>", clear_widget)
entry_password.bind('<FocusOut>', repopulate_defaults)
#CHECKS WHETHER THE PASSWORD IS CORRECT OR NOT BY PRESSING THE      **** ENTER KEY ****
entry_password.bind('<Return>', login)

entry_password.config(font=(12), show=bullet)

#PUTTING LOGIN ENTRY WIDGET IN GRID
entry_name.grid(row=2, column=5, pady=10, ipady=6, sticky=W)
entry_password.grid(row=3, column=5, pady=10, ipady=6, sticky=W)

menu_bar(root)

#LOADING PIEAS LOGO
img = PhotoImage(file='pieas-pic.png')
panel = Label(root, image=img)
panel.grid(row=0, column=4, columnspan=2, pady=10, sticky=E)


root.mainloop()
