from tkinter import *

window = Tk()
window.title('Calculator')
window.iconbitmap('calc.ico')
window.geometry('355x475')
window.configure(bg='#97AFB9')
window.resizable(False, False)

#Functions goes here
expression = ''
def click(num):
    global expression
    if num == '%':
        num = '*0.01'
    expression += str(num)
    equation.set(expression)

def equal_to():
    global expression
    try:
        answer = str(eval(expression))
        equation.set(answer)
        expression = answer
    except:
        expression = 'Error'
        equation.set(expression)
        expression = ''

def clear():
    global expression
    expression = ''
    equation.set('0')

def delete():
    global expression
    if expression == '':
        equation.set('0')
    else:
        expression = expression[0:-1]
        equation.set(expression)

#Functions End's Here --->


main_frame = Frame(window, bg='#97AFB9')
main_frame.pack()

equation = StringVar()
equation.set('0')
entry_field = Entry(main_frame, textvariable=equation, font=('arial', 20, 'bold'), justify='right')


#Creating Buttons ---->
#first row -->
clear_button = Button(main_frame, text='C', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=clear)
division = Button(main_frame, text='/', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click('/'))
multiply = Button(main_frame, text='*', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click('*'))
delete = Button(main_frame, text='del', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=delete)

#second row -->
button_7 = Button(main_frame, text='7', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click(7))
button_8 = Button(main_frame, text='8', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click(8))
button_9 = Button(main_frame, text='9', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click(9))
subtract = Button(main_frame, text='-', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click('-'))

#Third row -->
button_4 = Button(main_frame, text='4', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click(4))
button_5 = Button(main_frame, text='5', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click(5))
button_6 = Button(main_frame, text='6', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click(6))
addition = Button(main_frame, text='+', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click('+'))

#Fourth row -->
button_1 = Button(main_frame, text='1', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click(1))
button_2 = Button(main_frame, text='2', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click(2))
button_3 = Button(main_frame, text='3', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click(3))

#Fifth row -->
percent = Button(main_frame, text='%', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click('%'))
zero = Button(main_frame, text='0', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click(0))
decimal = Button(main_frame, text='.', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=lambda:click('.'))

#Span fourth and fifth row -->
equals = Button(main_frame, text='=', font=('times new roman', 12), relief='ridge',
                     bg='#7ddcff', bd=1, width=8, height=3, command=equal_to)

#Button Creation End's Here --->


#Positioning Buttons Using Grid Method --->
entry_field.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=25, pady=15)

clear_button.grid(row=1, column=0)
division.grid(row=1, column=1)
multiply.grid(row=1, column=2)
delete.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
subtract.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
addition.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

percent.grid(row=5, column=0)
zero.grid(row=5, column=1)
decimal.grid(row=5, column=2)

equals.grid(row=4, column=3, rowspan=2, sticky=N+S)

#Positioning End's Here -->


window.mainloop()