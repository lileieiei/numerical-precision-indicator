from tkinter import *
from tkinter import filedialog,messagebox
from tkinter.ttk import Scrollbar,Checkbutton,Label,Button


from decimal import *

class NotePad(Tk):
    def __init__(self):
        super().__init__()
        self.set_window()
        self.create_body()
        self.res=[]



    def set_window(self):
        self.title(r"数据精度")
        max_width,max_height=self.maxsize()
        align_center="350x300+%d+%d"%((max_width-1200)/2,(max_height-900)/2)
        self.geometry(align_center)
    #界面操作主体
    def create_body(self):
        frame1 = Frame (self, relief=RAISED, borderwidth=2)
        frame1.pack(side=LEFT, fill=BOTH, ipadx=2, ipady=2, expand=0)
        frame2 = Frame (self, relief=RAISED, borderwidth=2)
        frame2 . pack (side=RIGHT, fill=BOTH, ipadx=2, ipady=2, expand=1)
        Label(frame1,text="开始数字").pack(side=TOP, padx=2, pady=2)
        self.start=Entry(frame1)
        self.start.pack(side=TOP, padx=2, pady=2)
        Label(frame1,text="结束数字").pack(side=TOP, padx=2, pady=2)        
             
        self.end=Entry(frame1) 
        self.end.pack(side=TOP, padx=2, pady=2)

        Label(frame1,text="步长").pack(side=TOP, padx=2, pady=2)  
        self.step=Entry(frame1) 
        self.step.pack(side=TOP, padx=2, pady=2)

        Label(frame1,text="运算，x为待确定数值，例如x+1").pack(side=TOP, padx=2, pady=2)  
        self.func=Entry(frame1) 
        self.func.pack(side=TOP, padx=2, pady=2)
        btn_run=Button(frame1,text="运行",command=self.run).pack(side=TOP, padx=2, pady=2)

        self.res_text=Text(frame2,wrap="word",border=1,width=20,undo=True,)
        self.res_text.pack(side="left",fill='x')

        scrollbar = Scrollbar (frame2, command=self.res_text.yview)
        scrollbar.pack (side=RIGHT, fill=Y)
        self.res_text.config (yscrollcommand=scrollbar.set)


    

    def run(self):
        self.res=[]
        start_num=self.start.get()
        end_num=self.end.get()
        step_num=self.step.get()
        self.find_dem(start_num,end_num,step_num,self.func.get())
        print(self.res)
        res_text="\n".join([str(self.res[i]) for i in range(1,len(self.res))])
        self.res_text.config(state="normal")
        self.res_text.delete("1.0",END)
        self.res_text.insert("1.0",res_text)
    def find_dem(self,start,end,step,func1):
        
        print(start,end,step,func1)
        start=float(start)
        end=float(end)
        step=float(step)
        now=start
        now_dem=Decimal(str(start))
        step_dem=Decimal(str(step))
        end_dem=Decimal(str(end))
        c=func1
        while now_dem<=end_dem:
            c=func1
            d=func1
            c=c.replace('x',"Decimal('%s')"%str(now_dem))
            d=d.replace('x','%s'%str(now_dem))
            
            res=eval(str(c))
            
            if float(res)-eval(d)!=0:
                print(res,eval(d))
                self.res.append(str(now_dem))
                
            now_dem=now_dem+step_dem
           


if __name__=="__main__":
    app=NotePad()
    #app.print_tree()
    app.mainloop()