# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:01:43 2020

@author: tamanna
"""


import Tkinter
import random
import time
import tkMessageBox

root=Tkinter.Tk()
root.title("dreamy creamy bar login system")
root.geometry("1300x550")
root.configure(bg="powder blue")
def loginhere():
    
    u=username.get()
    p=password.get()
    if(u=="tamanna" and p=="aggarwal12345"):
        
#-------------------------------------------------------------------------------------------
        newwindow=Tkinter.Toplevel(root)
           
        localtime=time.asctime(time.localtime(time.time()))
        global operator
        operator=""


        newwindow.geometry("1500x800+0+0")
        newwindow.title("restuarant management system")
        newwindow.configure(bg="Cadet Blue")
        def btnclick(number):
              global operator
              operator=operator+str(number)
              txt_input.set(operator)
    
        def btnclear():
              global operator
              operator=operator[0:-1]
              txt_input.set(operator)
    
  
        def btnequal():
              global operator
    
              txt_input.set(str(eval(operator)))
              operator=str(eval(operator))
    
        def total():
               x=random.randint(1,10000)
               rand.set(str(x))
               costofmeal=((float(fries.get())*50)+(float(burger.get())*40)+(float(chick.get())*100)+
               (float(waff.get())*150)+(float(sandwich.get())*50)+(float(drinks.get())*120)+
               (float(donut.get())*150))
               paytax=float((costofmeal*20)/100)
               dis=float((5*costofmeal)/100)
               servicetax=float(costofmeal/99)
               com.set("RS"+str(costofmeal))
               servicechr.set("RS"+str(servicetax))
               statetax.set("RS"+str(paytax))
               subtotal.set("RS"+str(costofmeal))
               discount.set("RS"+str(dis))
               tc=float(costofmeal+paytax+servicetax-dis)
               totalcost.set("RS"+str(tc))
               txtrecipt.delete("1.0",Tkinter.END)
               txtrecipt.insert(Tkinter.END,"Receipt Ref:\t\t\t"+rand.get()+"\n")
               txtrecipt.insert(Tkinter.END,'Item:\t\t\t'+"Cost of items\n")
               if(fries.get()!="0"):
                   txtrecipt.insert(Tkinter.END,"french fries:\t\t\t"+fries.get()+"\n")
               if(drinks.get()!="0"):
                    txtrecipt.insert(Tkinter.END,"drinks:\t\t\t"+drinks.get()+"\n")
               if(burger.get()!="0"):
                    txtrecipt.insert(Tkinter.END,"burger:\t\t\t"+burger.get()+"\n")
               if(chick.get()!="0"):
                    txtrecipt.insert(Tkinter.END,"chick:\t\t\t"+chick.get()+"\n")
               if(waff.get()!="0"):
                    txtrecipt.insert(Tkinter.END,"waff:\t\t\t"+waff.get()+"\n")
               if(sandwich.get()!="0"):
                    txtrecipt.insert(Tkinter.END,"sandwich:\t\t\t"+sandwich.get()+"\n")
               if(donut.get()!="0"):
                    txtrecipt.insert(Tkinter.END,"donuts:\t\t\t"+donut.get()+"\n")
               txtrecipt.insert(Tkinter.END,"Cost of meal:\t\t\t"+com.get()+"\n")
               txtrecipt.insert(Tkinter.END,"Paytax:\t\t\t"+statetax.get()+"\n")
               txtrecipt.insert(Tkinter.END,"Service charge:\t\t\t"+servicechr.get()+"\n") 
               txtrecipt.insert(Tkinter.END,"Discount:\t\t\t"+discount.get()+"\n")
               txtrecipt.insert(Tkinter.END,"Total cost of meal:\t\t\t"+totalcost.get()+"\n")
                
                        
        def reset():
                rand.set("")  
                fries.set("0")
                burger.set("0")  
                chick.set("0") 
                waff.set("0") 
                sandwich.set("0") 
                drinks.set("0")
                donut.set("0")
                com.set("0")
                servicechr.set("0")
                statetax.set("0")
                subtotal.set("0")
                totalcost.set("0")
                discount.set("0")
                txtrecipt.delete(1.0,Tkinter.END)
                txt_input.set("")
                #txtrecipt.delete(1.0,10.0)  for deleting at some limit where we want to delete

        def qexit():
                  iexit=tkMessageBox.askyesno("dreamy cremy bar","Confirm if you want to exit")
                  if(iexit>0):
                        root.destroy()
                  else:
                        return 
 
        Topf=Tkinter.Frame(newwindow,bg="Cadet Blue",bd=20,relief=Tkinter.RIDGE)
        Topf.pack(side=Tkinter.TOP,fill=Tkinter.X,pady=0)
        
        leftf=Tkinter.Frame(newwindow,bg="Cadet Blue",bd=10,width=600,height=400,relief=Tkinter.RIDGE)
        leftf.pack(side=Tkinter.LEFT)
        
        rightf=Tkinter.Frame(newwindow,bg="Cadet Blue",bd=10,width=700,height=400,relief=Tkinter.RIDGE)
        rightf.pack(side=Tkinter.RIGHT)
        
        labelinfo=Tkinter.Label(Topf,font=('arial',50,'bold'),text="DREAMY CREAMY BAR",fg='darkred',justify="center",bg="cadet blue",bd=21).pack()
        labelinfo=Tkinter.Label(Topf,font=('arial',20,'bold'),text=localtime,fg='darkred',bg="cadet blue",justify="center").pack()
        
        rightftop=Tkinter.Frame(rightf,bg="cadet blue",bd=15,relief=Tkinter.RIDGE)
        rightftop.pack(side=Tkinter.TOP)
        rightfbottom=Tkinter.Frame(rightf,bg="cadet blue",bd=15,relief=Tkinter.RIDGE)
        rightfbottom.pack(side=Tkinter.BOTTOM)
        
        
        #---------------------------------------------
        rand=Tkinter.StringVar()  
        fries=Tkinter.StringVar()  
        burger=Tkinter.StringVar()  
        chick=Tkinter.StringVar()  
        waff=Tkinter.StringVar()  
        sandwich=Tkinter.StringVar()  
        drinks=Tkinter.StringVar() 
        donut=Tkinter.StringVar() 
        com=Tkinter.StringVar() 
        servicechr=Tkinter.StringVar() 
        statetax=Tkinter.StringVar() 
        subtotal=Tkinter.StringVar() 
        totalcost=Tkinter.StringVar()  
        discount=Tkinter.StringVar() 
        
        #column 0 and 1
                   
        labelref=Tkinter.Label(leftf,font=("arial",15,"bold"),fg="black",
                                text="REFERENCE",bd=16,bg="Cadet Blue").grid(row=0,column=0,pady=5)
        txtref=Tkinter.Entry(leftf,font=("arial",15,"bold"),
                             textvariable=rand,bd=10,insertwidth=4,bg="pink",justify="left",fg="black").grid(row=0,column=1) 
        #insertwidth means width of insertion cursor
         
        labelfries=Tkinter.Label(leftf,font=("arial",15,"bold"),fg="black",
                                text="FRENCH FRIES",bd=16,bg="Cadet Blue").grid(row=1,column=0,pady=5)
        txtfries=Tkinter.Entry(leftf,font=("arial",15,"bold"),
                               textvariable=fries,bd=10,insertwidth=4,bg="pink",justify="left",fg="black").grid(row=1,column=1)
        fries.set("0")
        labelburger=Tkinter.Label(leftf,font=("arial",15,"bold"),fg="black",
                                text="BURGERS MEAL",bd=16,bg="Cadet Blue").grid(row=2,column=0,pady=5)
        txtburger=Tkinter.Entry(leftf,font=("arial",15,"bold"),
                             textvariable=burger,bd=10,insertwidth=4,bg="pink",justify="left",fg="black").grid(row=2,column=1)
        burger.set("0")
        labelchicken=Tkinter.Label(leftf,font=("arial",15,"bold"),fg="black",
                                text="CHICKEN MEAL",bd=16,bg="Cadet Blue").grid(row=3,column=0,pady=5)
        txtchicken=Tkinter.Entry(leftf,font=("arial",15,"bold"),
                             textvariable=chick,bd=10,insertwidth=4,bg="pink",justify="left",fg="black").grid(row=3,column=1)
        chick.set("0")
        labelwaffle=Tkinter.Label(leftf,font=("arial",15,"bold"),fg="black",
                                text="WAFFLES",bd=16,bg="Cadet Blue").grid(row=4,column=0,pady=5)
        txtfwaffle=Tkinter.Entry(leftf,font=("arial",15,"bold"),
                             textvariable=waff,bd=10,insertwidth=4,bg="pink",justify="left",fg="black").grid(row=4,column=1)
        waff.set("0")
        labelsandwich=Tkinter.Label(leftf,font=("arial",15,"bold"),fg="black",
                                text="SANDWICHES",bd=16,bg="Cadet Blue").grid(row=5,column=0,pady=5)
        txtsandwich=Tkinter.Entry(leftf,font=("arial",15,"bold"),
                             textvariable=sandwich,bd=10,insertwidth=4,bg="pink",justify="left",fg="black").grid(row=5,column=1)
        sandwich.set("0")
        labeldrinks=Tkinter.Label(leftf,font=("arial",15,"bold"),fg="black",
                                text="DRINKS",bd=16,bg="Cadet Blue").grid(row=6,column=0,pady=5)
        txtdrinks=Tkinter.Entry(leftf,font=("arial",15,"bold"),
                             textvariable=drinks,bd=10,insertwidth=4,bg="pink",justify="left",fg="black").grid(row=6,column=1)
        drinks.set("0")                   
        #-------------------------
        
        #column 2 and 3 
        labeldonut=Tkinter.Label(leftf,font=("arial",15,"bold"),fg="black",
                                text="DONUTS",bd=16,bg="Cadet Blue").grid(row=0,column=2,pady=5)
        txtdonut=Tkinter.Entry(leftf,font=("arial",15,"bold"),
                             textvariable=donut,bd=10,insertwidth=4,bg="pink",justify="left",fg="black").grid(row=0,column=3) 
        #insertwidth means width of insertion cursor
        donut.set("0")
        labelcom=Tkinter.Label(leftf,font=("arial",15,"bold"),fg="black",
                                text="COST OF MEAL",bd=16,bg="Cadet Blue").grid(row=1,column=2,pady=5)
        txtcom=Tkinter.Entry(leftf,font=("arial",15,"bold"),
                             textvariable=com,bd=10,insertwidth=4,bg="pink",justify="left",fg="black").grid(row=1,column=3)
        
        labelservicechr=Tkinter.Label(leftf,font=("arial",15,"bold"),fg="black",
                                text="SERVICE CHARGES",bd=16,bg="Cadet Blue").grid(row=2,column=2,pady=5)
        txtservicechr=Tkinter.Entry(leftf,font=("arial",15,"bold"),
                             textvariable=servicechr,bd=10,insertwidth=4,bg="pink",justify="left",fg="black").grid(row=2,column=3)
        
        labelstatetax=Tkinter.Label(leftf,font=("arial",15,"bold"),fg="black",
                                text="STATE TAX",bd=16,bg="Cadet Blue").grid(row=3,column=2,pady=5)
        txtstatetax=Tkinter.Entry(leftf,font=("arial",15,"bold"),
                             textvariable=statetax,bd=10,insertwidth=4,bg="pink",justify="left",fg="black").grid(row=3,column=3)
                         
        labelsubtotal=Tkinter.Label(leftf,font=("arial",15,"bold"),fg="black",
                                text="SUB TOTAL",bd=16,bg="Cadet Blue").grid(row=4,column=2,pady=5)
        txtfsubtotal=Tkinter.Entry(leftf,font=("arial",15,"bold"),
                             textvariable=subtotal,bd=10,insertwidth=4,bg="pink",justify="left",fg="black").grid(row=4,column=3)
        
        labeltotalcost=Tkinter.Label(leftf,font=("arial",15,"bold"),fg="black",
                                text="TOTAL COST",bd=16,bg="Cadet Blue").grid(row=5,column=2,pady=5)
        txttotalcost=Tkinter.Entry(leftf,font=("arial",15,"bold"),
                             textvariable=totalcost,bd=10,insertwidth=4,bg="pink",justify="left",fg="black").grid(row=5,column=3)
        
        labeldiscount=Tkinter.Label(leftf,font=("arial",15,"bold"),fg="black",
                                text="DISCOUNT",bd=16,bg="Cadet Blue").grid(row=6,column=2,pady=5)
        txtdiscount=Tkinter.Entry(leftf,font=("arial",15,"bold"),
                             textvariable=discount,bd=10,insertwidth=4,bg="pink",justify="left",fg="black").grid(row=6,column=3)
                        
        #-------------------------------
        #BTTONS FOR TOTAL,RESET,QUIT
        
        
        btntotal=Tkinter.Button(leftf,padx=16,pady=16,fg="white",font=("arial",17,"bold"),bd=10,width=4,
                                text="TOTAL",bg="darkred",command=total).grid(row=7,column=0,pady=5)
        btnreset=Tkinter.Button(leftf,padx=16,pady=16,fg="white",font=("arial",17,"bold"),bd=10,width=4,
                                text="RESET",bg="darkred",command=reset).grid(row=7,column=1,pady=5)
        btnquit=Tkinter.Button(leftf,padx=16,pady=16,fg="white",font=("arial",17,"bold"),bd=10,width=4,
                                text="QUIT",bg="darkred",command=qexit).grid(row=7,column=2,pady=5)
        
        #----------------------------------------------------
        #input--
        txt_input=Tkinter.StringVar()
        #-----
        
        txtdisplay=Tkinter.Entry(rightftop,width=33,font=('arial',20,'bold'),bg="pink",
                                 textvariable=txt_input,insertwidth=4,justify='right',bd=10,).grid(row=0,column=0,columnspan=4,pady=1)
        
        #-------------------------
        btn7=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="7",command=lambda:btnclick(7)).grid(row=1,column=0)
        btn8=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="8",command=lambda:btnclick(8)).grid(row=1,column=1)
        btn9=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="9",command=lambda:btnclick(9)).grid(row=1,column=2)
        add=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="+",command=lambda:btnclick("+")).grid(row=1,column=3)
        #----------------------------
        btn4=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="4",command=lambda:btnclick(4)).grid(row=2,column=0)
        btn5=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="5",command=lambda:btnclick(5)).grid(row=2,column=1)
        btn6=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="6",command=lambda:btnclick(6)).grid(row=2,column=2)
        sub=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="-",command=lambda:btnclick("-")).grid(row=2,column=3)
        #-------------------------
        btn1=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="1",command=lambda:btnclick(1)).grid(row=3,column=0)
        btn2=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="2",command=lambda:btnclick(2)).grid(row=3,column=1)
        btn3=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="3",command=lambda:btnclick(3)).grid(row=3,column=2)
        mul=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="*",command=lambda:btnclick("*")).grid(row=3,column=3)
        #-------------------
        btn0=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="0",command=lambda:btnclick(0)).grid(row=4,column=0)
        div=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="/",command=lambda:btnclick("/")).grid(row=4,column=1)
        equal=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="=",command=btnequal).grid(row=4,column=2)
        C=Tkinter.Button(rightftop,bd=8,padx=16,pady=0,fg="black",font=("arial",16,"bold"),bg="powder blue",width=6,
                            text="C",command=btnclear).grid(row=4,column=3)
        
        
        txtrecipt=Tkinter.Text(rightfbottom,bg="white",width=40,height=9,bd=4,font=("arial",17,"bold"),
                               relief=Tkinter.RIDGE)
        txtrecipt.insert(6.0,"HELLO TAMANNA")
        txtrecipt.grid(row=0,column=0)
        
#-----------------------------------------------------------------------------------
                        
            
    else:
            tkMessageBox.askyesno("Login System","Too Bad,invalid login detail")
            username.set("")
            password.set("")
            
def resethere():
    username.set("")
    password.set("")
            
def exithere():
    iexit=tkMessageBox.askyesno("login system","Confirm if you want to exit")
    if(iexit>0):
            root.destroy()
    else:
            return    
Topf=Tkinter.Frame(root,bg="Cadet Blue",bd=20,relief=Tkinter.RIDGE)
Topf.pack(side=Tkinter.TOP,fill=Tkinter.X)

Bottomf=Tkinter.Frame(root,bg="Cadet Blue",bd=20,relief=Tkinter.RIDGE)
Bottomf.pack(side=Tkinter.BOTTOM)

bf1=Tkinter.Frame(Bottomf,bg="Cadet Blue",bd=20,relief=Tkinter.RIDGE)
bf1.pack(side=Tkinter.TOP)
    
bf2=Tkinter.Frame(Bottomf,bg="Cadet Blue",bd=20,relief=Tkinter.RIDGE)
bf2.pack(side=Tkinter.BOTTOM)

lbltitle=Tkinter.Label(Topf,text="Dreamy Creamy Bar Login System",font=('arial',50,'bold'),
                           fg='Black',bg="Cadet Blue",bd=20)
lbltitle.pack()

username=Tkinter.StringVar()

password=Tkinter.StringVar()

lbluser=Tkinter.Label(bf1,text="USERNAME",font=('arial',20,'bold'),bd=22,bg="cadet blue",fg="cornsilk")
lbluser.grid(row=0,column=0)
textuser=Tkinter.Entry(bf1,font=('arial',20,'bold'),textvariable=username)
textuser.grid(row=0,column=1)
    
lblpass=Tkinter.Label(bf1,text="PASSWORD",font=('arial',20,'bold'),bd=22,bg="cadet blue",fg="cornsilk")
lblpass.grid(row=1,column=0)
textpass=Tkinter.Entry(bf1,font=('arial',20,'bold'),textvariable=password,show="*")
textpass.grid(row=1,column=1)    

btnlogin=Tkinter.Button(bf2,text="LOGIN HERE",width=17,command=loginhere,font=('arial',20,'bold'))
btnlogin.grid(row=0,column=0,padx=20,pady=20)
btnreset=Tkinter.Button(bf2,text="RESET HERE",width=17,command=resethere,font=('arial',20,'bold'))
btnreset.grid(row=0,column=1,padx=20,pady=20)
btnexit=Tkinter.Button(bf2,text="EXIT HERE",width=17,command=exithere,font=('arial',20,'bold'))
btnexit.grid(row=0,column=2,padx=20,pady=20)


root.mainloop()