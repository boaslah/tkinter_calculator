import tkinter as tk

root = tk.Tk()
root.geometry("650x500")
root.title("Calculator")
text_area = tk.Text(root, height=2, width=100, font=('Arial', 24))

text_area.grid(columnspan=100)
operator = ""
num1 = 0
num2 = 0

def calculate(num1, num2, operator):
    if(operator == "*"):
        result = num1 * num2
    elif(operator == "+"):
        result = num1 + num2
    elif(operator == "-"):
        result = num1 - num2
    elif(operator == "/"):
        result = num1 / num2
    return num1, operator, num2, "=", result

def displayInput(symbol):
    text_area.insert(3.0, str(symbol))



def getNum2():
    content = text_area.get(1.0, "end")
    global num2
    num2 = int(content)

    result = calculate(num1, num2, operator)
    text_area.delete(1.0, "end")
    text_area.insert(3.0, result)

def getNum1():
    global num1
    global operator
    content = text_area.get(1.0, "end")
    operator = content[len(content) -2]
    num1 = int(content.replace(operator, ""))
    text_area.delete(1.0, "end")

def clear():
    text_area.delete(1.0, "end")



btn1 = tk.Button(root, text="1", command=lambda: displayInput("1"), height=4, width=10)
btn1.grid(row=2, column=1)
btn2 = tk.Button(root, text="2", command=lambda: displayInput("2"), height=4, width=10)
btn2.grid(row=2, column=2)
btn3 = tk.Button(root, text="3", command=lambda: displayInput("3"), height=4, width=10)
btn3.grid(row=2, column=3)  
btn4 = tk.Button(root, text="4", command=lambda: displayInput("4"), height=4, width=10)
btn4.grid(row=3, column=1)
btn5 = tk.Button(root, text="5", command=lambda: displayInput("5"), height=4, width=10)
btn5.grid(row=3, column=2)
btn6 = tk.Button(root, text="6", command=lambda: displayInput("6"), height=4, width=10)
btn6.grid(row=3, column=3)
btn7 = tk.Button(root, text="7", command=lambda: displayInput("7"), height=4, width=10)
btn7.grid(row=4, column=1)
btn8 = tk.Button(root, text="8", command=lambda: displayInput("8"), height=4, width=10)
btn8.grid(row=4, column=2)
btn9 = tk.Button(root, text="9", command=lambda: displayInput("9"), height=4, width=10)
btn9.grid(row=4,  column=3)
btnplus = tk.Button(root, text="+", command=lambda: [displayInput("+"), getNum1()], height=4, width=10)
btnplus.grid(row=2, column=4)
btnsubtract = tk.Button(root, text="-", command=lambda: [displayInput("-"), getNum1()], height=4, width=10)
btnsubtract.grid(row=3, column=4)
btndivid = tk.Button(root, text="/", command=lambda: [displayInput("/"), getNum1()], height=4, width=10)
btndivid.grid(row=4, column=4)
btn0 = tk.Button(root, text="0", command=lambda: displayInput("0"), height=4, width=10)
btn0.grid(row=5, column=2)
btnmultiply = tk.Button(root, text="*", command=lambda: [displayInput("*"), getNum1()], height=4, width=10)
btnmultiply.grid(row=5, column=4)
btnclear = tk.Button(root, text="Clear", command=lambda: clear(), height=4, width=10)
btnclear.grid(row=5, column=1)
btnequal = tk.Button(root, text="=", command=lambda: getNum2(), height=4, width=10)
btnequal.grid(row=5, column=3)

root.mainloop()
