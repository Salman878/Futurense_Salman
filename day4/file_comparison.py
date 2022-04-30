from tabulate import tabulate
from tkinter import *
from tkinter import filedialog

base = Tk()
# Create a canvas
base.geometry('250x250')

from tkinter import *
root = Tk()
root.withdraw()

f1_list=[]
def file_opener1():
    global f1_list
    f1=[]
    input1 = filedialog.askopenfile(initialdir="/")
    l1=input1.readlines()
    for word in range(len(l1)):
        q=l1[word]
        f1=q.split()
        f1_list.extend(f1)
    print(f1)


f2_list = []

def file_opener2():
   global f2_list
   f2=[]
   input2 = filedialog.askopenfile(initialdir="/")
   l2=input2.readlines()
   for j in range(len(l2)):
       q=l2[j]
       f2=q.split()
       f2_list.extend(f2)
   print(f2)





res=[['file1','file2']]

def comparing():
    temp=['-','-']
    global res
    for i in range(len(f1_list)):
        if f1_list[i]==f2list[i]:
            res.append(temp)
        else:
            li_to=[]
            li_to.append(f1_list[i])
            li_to.append(f2_list[i])
            res.append(li_to)
            li_to=[]
    print(tabulate(res, headers='firstrow'))

x = Button(base, text ='Select a file1',command=lambda:file_opener1())
x.pack()
y = Button(base, text ='Select a file2',command=lambda:file_opener2())
y.pack()

compute = Button(base,text = "compare",command=lambda:comparing())
compute.pack()

# z = Button(base, text ='evalute', command = lambda:file_reader())
# z.pack()
mainloop()







