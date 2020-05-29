import tkinter as tk
from tkinter import ttk
import tkcalendar as tkc
import datetime as dt
#from NewRefVals import customer, single_list
import calendar as cal
import collections as clc


#-------------------------------------------------------  
BG = 'white'
FG = 'black'
DGR = 'dark goldenrod'

#BG =  '#0C1021'
#FG = 'white'
#DGR = 'dark goldenrod'


customer = ['AZ_Canning', 'Abrams_Airborne', 'Air_Liquide_Bagdad', 'Air_Products_and_Chemicals', 'Apache_Nitrogen', 'Arizona_Electric_Power', 'Arizona_LNG_Applied_LNG',
            'Arizona_Mining_Company', 'Arizona_Pacific_Wood', 'Asarco_Mission', 'Avondale', 'BE_Aerospace', 'Biosphere', 'Black_&_Veatch', 'Botanicare', 'Brown_and_Caldwell',
            'Bull_Moose', 'Bullhead_City', 'CCA', 'Camp_Dresser_McGhee', 'Carefree', 'Casa_Grande', 'Casa_Grande_Area', 'Cave_Creek', 'Chandler', 'Chino_Valley_',
            'City_of_Casa_Grande_WWTP', 'City_of_Henderson', 'City_of_Las_Vegas', 'Clark_County_Water_Reclamation_District', 'Clarkdale_Metals', 'Coolidge_Land_Acquition_Wes_Emulsions',
            'Cottonwood', 'Daisy_Sour_Cream', 'Davis_Monthan_AFB', 'Drake_Materials_Paulden', 'Ehrmanns_Dairy', 'Envirogen', 'Environmental_Biomass', 'Epcor_Bullhead_City',
            'Euclid_Chemical', 'FMI_Ajo', 'FMI_Bagdad', 'FMI_Bisbee', 'FMI_Sieritta', 'Fann_Environmental', 'Florence', 'Fluid_Solutions', 'Fountain_Hills', 'Franklin_Foods_Cream_Cheese',
            'Frito_Lay', 'Ft_Huachuca', 'Ft_Mohave', 'GCW', 'Glendale', 'Goodyear', 'Greeley_and_Hansen', 'Green_Valley_Pecans', 'Griffith_Energy_New_Star_Energy', 'Henderson_Electric',
            'Hexcel', 'Honeywell', 'Hydro_Geo_Chem', 'IBM', 'IDG', 'JDS_Engineering', 'Jones_Lang_LaSalle', 'Kinder_Morgan', 'Kingman', 'Kingman_all_Accounts', 'LPC_Contstruction',
            'Las_Vegas_Valley_Water_District', 'Laughlin', 'Lhoist_North_America', 'MGC', 'Mesa_NOT_Riverview', 'Mingus_Associates_Construction', 'Mohave_Valley', 'Morrison_Maierle',
            'Needles', 'Neltec', 'Nexus_Energy_calpine', 'Nord_Copper', 'Nucor', 'Oceanspray', 'Olin_Chlor', 'Paragon', 'Peoria', 'Phoenix_', 'Pima_County_WW', 'Poggemeyer_Engineers',
            'Praxair_Electronics', 'Prescott', 'Pro_Petroleum', 'Queen_Creek', 'Rain_Bird', 'Raytheon_Hagemeyer', 'Renewable_Algal_Energy', 'Sasol_Inc', 'Scottsdale', 'Severn_Trent_Environmental_Services',
            'Sierra_Vista_Regional_Health_Center', 'Slater_Hannifan_Group', 'Sletten', 'Southern_Nevada_Water_Authority', 'Sun_Mechanical', 'Sundt_', 'Surprise', 'Swissport_Fueling_',
            'TEP_Irvington', 'Timet_HOLD_OFF', 'Tolin_Mechanical', 'Tolleson', 'Topock', 'Trans_Canada_Power_Plant_Coolidge', 'United_Metals', 'Wilson_Engineers']


caldates_dict = clc.OrderedDict()
#-------------------------------------------------------



#-------------------------------------------------------  
class Foundation(object):
    
    
    #------------------------------------------------------- 
    def __init__(self, master):
        """
        
        """
        
        self.master = master
        self.master.config(bg = BG)
        
        self.parse_cal_dates()
        self.create_frame_grid()
        self.widget_creator()
    
    
    
    #-------------------------------------------------------   
    def parse_cal_dates(self):
        """
        
        """
        
        calobj = cal.Calendar()
        yearcal = calobj.yeardatescalendar(2020, width = 1)
        days_itr = 0
        
        for a in yearcal:
            for b in a:
                for c in b:
                    for d in c:
                        caldates_dict[days_itr] = dt.datetime.strftime(d, '%Y %m %d')
                        days_itr += 1
        
        return
    
    
    
    
    #-------------------------------------------------------   
    def create_frame_grid(self):
        """
        Grid Layout:
        
        1,1 | 1.2 | 1.3
        2.1 | 2.2 | 2.3
        3.1 | 3.2 | 3.3
           
        """
        
        
        self.f11 = tk.Frame(self.master, bg = BG)
        self.f11.grid(row = 0, column = 0, padx = 2, pady = 2)
        
        self.f12 = tk.Frame(self.master, bg = BG)
        self.f12.grid(row = 0, column = 1, padx = 2, pady = 2)
        
        self.f13 = tk.Frame(self.master, bg = BG)
        self.f13.grid(row = 0, column = 2, padx = 2, pady = 2)
        
        self.f21 = tk.Frame(self.master, bg = BG)
        self.f21.grid(row = 2, column = 0, padx = 2, pady = 2)
        
        self.f22_23 = tk.Frame(self.master, bg = BG)
        self.f22_23.grid(row = 2, column = 1, columnspan = 2, padx = 2, pady = 2)
        
        self.f_row_3 = tk.Frame(self.master, bg = BG)
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
        self.todays_date = tk.Label(self.f11, text = "Todays Date: {}".format(dt.date.today()), font = 'verdana 10 bold', bg = BG)
        self.todays_date.grid(row = 0, column = 0, padx = 3, pady = 3, sticky = tk.EW)
        
        #LISTBOX CHECKLIST ----------------------------------------------
        self.chklist = """Check Emails\nRespond Emails\nTEST\n""".split('\n')
        
        self.check_scroll = tk.Scrollbar(self.f11, orient = tk.VERTICAL)
        self.check_scroll.grid(row = 1, column = 1, sticky = tk.NS)
        self.lbox_checklist = tk.Listbox(self.f11, selectbackground = DGR, selectforeground = FG,
                                         selectmode = tk.BROWSE, bg = BG, width = 40,
                                         yscrollcommand = self.check_scroll.set)
        self.lbox_checklist.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = tk.EW)
        self.check_scroll.config(command = self.lbox_checklist.yview)
        
        
        for i in self.chklist:
            self.lbox_checklist.insert(tk.END, i)
        
        #COMBOBOX ACCOUNTS ---------------------------------------------
        self.cbox_accounts = ttk.Combobox(self.f11, values = customer)# ['test1', 'test2', 'test3'])
        self.cbox_accounts.grid(row = 2, column = 0, padx = 3, pady = 3, sticky = tk.EW)
        
        return
    
    
    
    
    
    #-------------------------------------------------------   
    def add_widgets_grid12(self):
        """
        Create tkCalendar widget to utilize calendar type function
        
        Calendar Events:
        <<CalendarSelected>> event is generated each time the user selects a day with the mouse.
        <<CalendarMonthChanged>> event is generated each time the user changes the displayed month.
        
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
        
        self.cal.grid(row = 0, column = 0, columnspan = 2, padx = 3, pady = 3, sticky = tk.NSEW)
        
        self.cal.bind('<<CalendarMonthChanged>>', None)
        self.cal.bind('<<CalendarSelected>>', self.cal_on_selection)
        self.cal.bind('<<Double-Button-1>>', self.call_on_doubleclick)
    



    #-------------------------------------------------------   
    def call_on_doubleclick(self, event):
        """
        Event handle identif 
        """
        
        print('Double Click')       
    
    #-------------------------------------------------------     
    def cal_on_selection(self, event):
        """
        
        """
        
        pass
        
    
    
    #-------------------------------------------------------   
    def add_widgets_grid13(self):
        """
        
        """
        
        
        #LISTBOX CHECKLIST ----------------------------------------------
        self.cont_scroll = tk.Scrollbar(self.f21, orient = tk.VERTICAL)
        self.cont_scroll.grid(row = 0, column = 1, sticky = tk.NS)
        
        self.lbox_contacts = tk.Listbox(self.f21, bg = BG, width = 40, 
                                        selectbackground = DGR, selectforeground = FG, yscrollcommand = self.cont_scroll.set)
        self.lbox_contacts.grid(row = 0, column = 0, padx = 3, pady = 3, sticky = tk.EW)
        
        self.cont_scroll.config(command = self.lbox_contacts.yview)
        
        for k,v in caldates_dict.items():
            self.lbox_contacts.insert(tk.END, repr(v))

    
    
    
    
    #-------------------------------------------------------   
    def add_widgets_grid21(self):
        """
        
        """    
        
        self.dateent = tkc.DateEntry(self.f21, date_pattern='MM/dd/yyyy').grid()
        #self.npad_widget = tk.Listbox(self)
        pass
    
    
    
    
    ##--------------------------------------------------------
    #def single_list(self, list,ignore_types=(str)):
        #""" 
        
        #"""
        
        
        #for item in list:
            
            #if isinstance(item, Iterable) and not isinstance(item, ignore_types):
                #yield from single_list(item,ignore_types=(str))
            #else:
                #yield item
    
        #items_single=single_list(z)
        
        #for item in items_single:
            #print(item)
            
        #return
    
    
    
    
    #-------------------------------------------------------   
    def add_widgets_grid22_23(self):
        """
        
        """
        
        self.npad_scroll = tk.Scrollbar(self.f22_23, orient = tk.VERTICAL)
        self.npad_scroll.grid(row = 0, column = 1, sticky = tk.NS)
        
        self.npad_widget = tk.Listbox(self.f22_23, width = 80, yscrollcommand = self.npad_scroll.set)
        self.npad_widget.grid(row = 0, column = 0, padx = 3, pady = 3, sticky = tk.EW)
        
        self.npad_scroll.config(command = self.npad_widget.yview)
        
        #items_single=single_list(z)
        
        for item in customer: #items_single:
            print(item)
            
        return
    
    
    
    
    
    #-------------------------------------------------------     
    def add_widgets_row3(self):
        """
        
        """
        
        
        self.lframe_goals = tk.LabelFrame(self.f_row_3, text = 'Goals Tracker', bg = BG)
        self.lframe_goals.grid(row = 0, column = 0, columnspan = 3, padx = 5, pady = 5, sticky = tk.EW)
        
        self.goal_1 = tk.Label(self.lframe_goals, text = 'Goal 1:', bg = BG)
        self.goal_1.grid(row = 0, column = 0, padx = 3, pady = 3, sticky = tk.EW)
    
        self.goal_2 = tk.Label(self.lframe_goals, text = 'Goal 2:', bg = BG)
        self.goal_2.grid(row = 0, column = 1, padx = 3, pady = 3, sticky = tk.EW)
        
        self.goal_3 = tk.Label(self.lframe_goals, text = 'Goal 3:', bg = BG)
        self.goal_3.grid(row = 0, column = 2, padx = 3, pady = 3, sticky = tk.EW)
        
    





#-------------------------------------------------------   
if __name__ == '__main__':
    """ 
    
    """
    
    root = tk.Tk()
    root.title("DXP Q.E.D - quod erat demonstrandum")
    Foundation(root)
    root.mainloop()
