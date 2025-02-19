from  tkinter import *
from tkinter import ttk


class todo:
    def __init__(self,root):
        self.root = root
        self.root.title ('To-Do-List')
        self.root.geometry ("650x410+300+150")

        self.label = Label(self.root, text='T0-Do-List-App',font='ariel,35,bold',width=10,bd=5,bg='orange',fg='black')
        self.label.pack(side='top',fill=BOTH)

        self.label2 = Label(self.root, text='Add Task',font='ariel,18,bold',width=10,bd=5,bg='orange',fg='black')
        self.label2.place(x=40 , y=54)

        self.label3 = Label(self.root, text='TASKS',font='ariel,18,bold',width=10,bd=5,bg='orange',fg='black')
        self.label3.place(x=380 , y=54)

        self.main_text=Listbox(self.root , height=15,bd=13,width=40,font='ariel,20,bold')
        self.main_text.place(x=250,y=100)

        self.text =Text(self.root , height=3,bd=5,width=20,font='ariel,20,bold')
        self.text.place(x=20 , y=120)


        #********************************addtask*******************#
        

        def add():
            content = self.text.get(1.0,END)
            self.main_text.insert(END , content)
            with open('data.txt','a') as file:
                file.write(content)
                file.seek(0)
                file.close()
            self.text.delete(1.0,END)
        

        def delete():
            delete_ = self.main_text.curselection()
            look=self.main_text.get(delete_)
            with open('data.txt','r+')as f:
                new_f = f.readlines()
                f.seek(0)
                for line in new_f:
                    item = str(look)
                    if item not in line:
                        f.write(line)
                f.truncate()
            self.main_text.delete(delete_)

        with open('data.txt','r') as file:
            read = file.readlines()
            for i in read:
                ready = i.split()
                self.main_text.insert(END, ready)
            file.close()

        self.button = Button(self.root,text="ADD",font='ariel,25,bold', width=10,bd=5,bg='Green',fg='black',command=add)
        self.button.place(x=50,y=200)

        self.button = Button(self.root,text="DELETE",font='ariel,25,bold', width=10,bd=5,bg='red',fg='black',command=delete)

        self.button.place(x=50,y=280)



        


def main():
    root = Tk()
    ui =todo(root)
    root.mainloop()

    
if __name__ == "__main__":
    main()
