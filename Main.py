import tkinter as tk
from tkinter import ttk
import tkcalendar as tkc
import datetime as dt
#from NewRefVals import customer



#-------------------------------------------------------  
BG = 'white'
FG = 'black'
DGR = 'dark goldenrod'

#BG =  '#0C1021'
#FG = 'white'
#DGR = 'dark goldenrod'




#-------------------------------------------------------  
class Foundation(object):
    
    def __init__(self, master):
        """
        
        """
        
        self.master = master        
        self.create_frame_grid()
        self.widget_creator()
    
    
    
    
    
    #-------------------------------------------------------   
    def create_frame_grid(self):
        """
        Grid Layout:
        
        1,1 | 1.2 | 1.3
        2.1 | 2.2 | 2.3
        3.1 | 3.2 | 3.3
           
        """
        
        self.f11 = tk.Frame(self.master)
        self.f11.grid(row = 0, column = 0, padx = 2, pady = 2)
        
        self.f12 = tk.Frame(self.master)
        self.f12.grid(row = 0, column = 1, padx = 2, pady = 2)
        
        self.f13 = tk.Frame(self.master)
        self.f13.grid(row = 0, column = 2, padx = 2, pady = 2)
        
        self.f21 = tk.Frame(self.master)
        self.f21.grid(row = 2, column = 0, padx = 2, pady = 2)
        
        self.f22_23 = tk.Frame(self.master)
        self.f22_23.grid(row = 2, column = 1, columnspan = 2, padx = 2, pady = 2)
        
        self.f_row_3 = tk.Frame(self.master)
        self.f_row_3.grid(row = 3, column = 0, columnspan =3, padx = 2, pady = 2)  


    
    
    
    
    #-------------------------------------------------------       
    def widget_creator(self):
        """
        
        """
        
        self.add_widgets_grid11()           #Label (date), Checklist, Accounts combobox
        self.add_widgets_grid12()           #Calendar widget_creato
        self.add_widgets_grid13()           #Todo's, Reminder, Call Logs
        
        self.add_widgets_grid21()           #Contacts
        self.add_widgets_grid22_23()        #2,2 and 2,3 combine for notebook widget   
        
        self.add_widgets_row3()             #Goals tracker labels all of row 3 frame
        
        return
        
    
    
    
    
    
    #-------------------------------------------------------    
    def add_widgets_grid11(self):
        """
        Create 3 total Widgets:
        
        1.
        2.
        3.
        
        """
        
        #TODAYS DATE LABEL ----------------------------------------------
        self.todays_date = tk.Label(self.f11, text = "Todays Date: {}".format(dt.date.today()), font = 'verdana 10 bold')
        self.todays_date.grid(row = 0, column = 0, padx = 3, pady = 3, sticky = tk.EW)
        
        #LISTBOX CHECKLIST ----------------------------------------------
        self.chklist = """Check Emails\nRespond Emails\nTEST\n""".split('\n')
        
        self.lbox_checklist = tk.Listbox(self.f11, selectbackground = DGR, selectforeground = FG, selectmode = tk.BROWSE)
        self.lbox_checklist.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = tk.EW)
        
        for i in self.chklist:
            self.lbox_checklist.insert(tk.END, i)
        
        #COMBOBOX ACCOUNTS ---------------------------------------------
        self.cbox_accounts = ttk.Combobox(self.f11, values = ['test1', 'test2', 'test3'])
        self.cbox_accounts.grid(row = 2, column = 0, padx = 3, pady = 3, sticky = tk.EW)
        
        return
    
    
    
    
    
    #-------------------------------------------------------   
    def add_widgets_grid12(self):
        """
        Create tkCalendar widget to utilize calendar type function
        
        """
        today = dt.date.today()
        mindate = dt.date(year=(int(2020)-1), month = int(today.month), day = int(today.day))
        maxdate = today + dt.timedelta(days=365)
        
        self.cal = tkc.Calendar(self.f12, font="Arial 14", selectmode='day', locale='en_US',
                            background = BG, foreground = FG, headersbackground = BG, headersforeground = DGR,
                            bordercolor = DGR,normalbackground = BG, normalforeground = FG, 
                            weekendbackground = BG, weekendforeground = FG,
                            selectbackground = DGR, selectforeground = 'black',
                            othermonthforeground = 'dim gray', othermonthbackground = BG, 
                            othermonthweforeground = 'dim gray', othermonthwebackground = BG, 
                            mindate=mindate, maxdate=maxdate, disabledforeground='red',
                            tooltipbackground = BG, tooltipforeground = DGR,
                            cursor="hand1", year = int(today.year), month = int(today.month), day = int(today.day))
        
        self.cal.grid(row = 0, padx = 25, pady = 25., sticky = tk.NSEW)
        self.cal.bind('<<CalendarMonthChanged>>', None) 
    
    
    
    #-------------------------------------------------------   
    def add_widgets_grid13(self):
        """
        
        """    
        
        #LISTBOX CHECKLIST ----------------------------------------------
        self.lbox_contacts = tk.Listbox(self.f21)
        self.lbox_contacts.grid(row = 0, column = 0, padx = 3, pady = 3, sticky = tk.EW)
        
    
    
    
    
    #-------------------------------------------------------   
    def add_widgets_grid21(self):
        """
        
        """    
        pass    
    
    
    
    
    
    
    #-------------------------------------------------------   
    def add_widgets_grid22_23(self):
        """
        
        """    
        pass    
    
    
    
    
    
    #-------------------------------------------------------     
    def add_widgets_row3(self):
        """
        
        """
        
        self.lframe_goals = tk.LabelFrame(self.f_row_3, text = 'Goals Tracker')
        self.lframe_goals.grid(row = 0, column = 0, columnspan = 3, padx = 5, pady = 5, sticky = tk.EW)
        
        self.goal_1 = tk.Label(self.lframe_goals, text = 'Goal 1:')
        self.goal_1.grid(row = 0, column = 0, padx = 3, pady = 3, sticky = tk.EW)
    
        self.goal_2 = tk.Label(self.lframe_goals, text = 'Goal 2:')
        self.goal_2.grid(row = 0, column = 1, padx = 3, pady = 3, sticky = tk.EW)
        
        self.goal_3 = tk.Label(self.lframe_goals, text = 'Goal 3:')
        self.goal_3.grid(row = 0, column = 2, padx = 3, pady = 3, sticky = tk.EW)
        
    





#-------------------------------------------------------   
if __name__ == '__main__':
    root = tk.Tk()
    root.title("quod erat demonstrandum")
    Foundation(root)
    root.mainloop()
