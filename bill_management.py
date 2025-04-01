import pyttsx3
from tkinter import *
 
# Initialize root window
root = Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False, False)
 
# Initialize pyttsx3 engine for text-to-speech
def text_to_speech(text):
     engine = pyttsx3.init()
     engine.say(text)
     engine.runAndWait()

# Reset function
def Reset():
     for entry in entry_list:
         entry.delete(0, END)
     Total_bill.set("")  # Reset the total
 
# Total function
def Total():
     try:
         quantities = [int(var.get()) if var.get() else 0 for var in variables]
     except ValueError:
         quantities = [0 for _ in variables]
 
     prices = [80, 70, 50, 60, 20, 40, 20, 40]
     total_cost = sum(q * p for q, p in zip(quantities, prices))
     
     Total_bill.set(f"Rs. {total_cost:.2f}")  # Set total cost in entry
     
     # Call text-to-speech
     text_to_speech(f"Total bill is Rs. {total_cost:.2f}")
 
# Title Label
Label(text="BILL MANAGEMENT", bg="black", fg="white", font=("Times New Roman", 28, "bold"), width=300, height=2).pack()
 
# Menu Card Frame
f = Frame(root, bg="Crimson", highlightbackground="black", highlightthickness=1, width=300, height=370)
f.place(x=10, y=118)
 
Label(f, text="Menu", font=("Veranda", 24, "bold"), fg="black", bg="Crimson").place(x=90, y=10)
 
menu_items = [
    "Butter Chicken..............Rs.280",
    "Biryani.....................Rs.170",
    "Palak Paneer................Rs.150",
    "Tandoori Chicken............Rs.260",
    "Chole Bhature...............Rs.120",
    "Masala Dosa.................Rs.100",
    "Rogan Josh..................Rs.120",
    "Gulab Jamun.................Rs.40"
]

for i, item in enumerate(menu_items):
    Label(f, font=("Veranda", 12,"bold"), text=item, fg="black", bg="Crimson").place(x=10, y=60 + i * 20)

# Bill Frame
f2 = Frame(root, bg="Crimson", highlightbackground="black", highlightthickness=1, width=300, height=370)
f2.place(x=690, y=118)

Label(f2, text="Bill", font=("Veranda", 17, "bold"), bg="Crimson").place(x=120, y=10)

lbl_total = Label(f2, font=("Veranda", 17,"bold"), text="Total", fg="black", bg="crimson")
lbl_total.place(x=30, y=70)

Total_bill = StringVar()

entry_total = Label(f2, font=("veranda", 18), textvariable=Total_bill, bd=5, width=15, bg="lightgoldenrodyellow")
entry_total.place(x=30, y=110)

# Entry Work Frame
f1 = Frame(root, bd=5, width=300, height=370, relief=RAISED)
f1.place(x=340, y=118)

variables = [StringVar() for _ in range(len(menu_items))]

labels = [
    "Butter Chicken",
    "Biryani",
    "Palak Paneer",
    "Tandoori Chicken",
    "Chole Bhature",
    "Masala Dosa",
    "Rogan Josh",
    "Gulab Jamun"
]

entry_list = []

for i, label in enumerate(labels):
    lbl = Label(f1, font=("Times new roman", 12,"italic","bold"), text=label, fg="black")
    lbl.grid(row=i, column=0, pady=5, padx=5, sticky="w")
    entry = Entry(f1, font=("Times new roman", 12), textvariable=variables[i], bd=3, width=10, bg="peachpuff")
    entry.grid(row=i, column=1, pady=5, padx=5)
    entry_list.append(entry)

# Buttons
btn_reset = Button(f1, bd=3, fg="black", bg="cadetblue", font=("Veranda", 12,"bold"), width=10, text="Reset", command=Reset)
btn_reset.grid(row=len(labels), column=0, pady=20, padx=10)

btn_total = Button(f1, bd=3, fg="black", bg="cadetblue", font=("Veranda", 12,"bold"), width=10, text="Total", command=Total)
btn_total.grid(row=len(labels), column=1, pady=20, padx=10)

# Run the application
root.mainloop()