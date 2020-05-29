import tkinter as tk
from tkinter import ttk



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



#------------------------------------------------------------------
class maker_notebook(ttk.Notebook):
    
    count = 0
    
    def __init__(self, parent, *args, **kwargs):
        """ 
        
        """
        
        ttk.Notebook.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.bind('<3>', self.undo_disable)
                  
        s = ttk.Style()
        default_vals = ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        s.theme_use('clam')
        
        self.framehold = {}
        
        self.frame1 = ttk.Frame(self, width = 400, height = 400, relief = tk.SUNKEN)
        self.frame2 = ttk.Frame(self, width = 400, height = 400, relief = tk.SUNKEN)
        self.frame3 = ttk.Frame(self, width = 400, height = 400, relief = tk.SUNKEN)
        
        self.add(self.frame1, text = 'Not Started')
        self.add(self.frame2, text = 'In Progress')
        self.add(self.frame3, text = 'Completed')
        
        self.grid(row = 1, column = 1, padx = 5, pady = 5)
        
        
        #--------------------------------------------------------------------------------------
        #STATIC LEFT SIDE WINDOW ---- ~ -----------
        """
        This widget will be a static (permanent) group displayed on left hand side of the GUI.
        Current Widget planned implementation:
                - Calendar
                - Reminders/To Do's
                - Daily check list
        """
        
        #Frame Widget ---
        self.left_frame_staticwidgets = tk.Frame(parent)
        self.left_frame_staticwidgets.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)
        
        #Labelframes/Seperators ---
        self.cal_lframe = tk.LabelFrame(self.left_frame_staticwidgets, text = 'Calendar')
        self.cal_lframe.grid(row = 0, column = 0, padx = 3, pady = 3)
        
        self.remind_lframe = tk.LabelFrame(self.left_frame_staticwidgets, text = 'Daily Chk List/Reminders')
        self.remind_lframe.grid(row = 1, column = 0, padx = 3, pady = 3)
        
        #TEST WIDGETS ---- to be REMOVED
        labcal = tk.Label(self.cal_lframe, text = 'Calendar goes here!')
        labcal.grid()
        
        labremind = tk.Label(self.remind_lframe, text = 'Reminder Port goes here!')
        labremind.grid()
        
        
        
        #END of STATIC LEFT SIDE --- ~ --
        #--------------------------------------------------------------------------------------
                
        
        #NOTEBOOK - BINDINGS -----------------------------
        self.bind('<<NotebookTabChanged>>', self.selected_tab)
        self.bind('<3>', self.undo_disable)
        
        for n,i in enumerate([self.frame1, self.frame2, self.frame3]):
            self.framehold[n] = i
            maker_notebook.count += 1

        self.btn = ttk.Button(self.parent, text='Add/Insert Tab at END', command = self.AddTab)
        self.btn.grid(row = 6, column = 0, padx = 5, pady = 5)
    
        self.btn2 = ttk.Button(self.parent, text='Disable Tab', command = self.disableTab)
        self.btn2.grid(row = 5, column = 0, padx = 5, pady = 5)
        
        self.strdisplay = r'Tab ID:{}'.format(self.select())
        ttk.Label(self.frame1, text = self.strdisplay).grid(row = 0, column = 0)
        
        self.strdisplay2 = 'Tab index:{}'.format(self.index(self.select()))
        ttk.Label(self.frame1, text = self.strdisplay2).grid(row = 0, column = 1)
        
        self.lbox_tab1 = tk.Listbox(self.frame1, height = 10, width = 50)
        self.lbox_tab1.grid(row = 2, columnspan = 2, padx = 5, pady = 5, sticky = tk.NS)
        
        self.lbox_tab2 = tk.Listbox(self.frame2, height = 10, width = 50)
        self.lbox_tab2.grid(row = 2, columnspan = 2, padx = 5, pady = 5, sticky = tk.NS)
        
        self.lbox_tab3 = tk.Listbox(self.frame3, height = 10, width = 50)
        self.lbox_tab3.grid(row = 2, columnspan = 2, padx = 5, pady = 5, sticky = tk.NS)
        
        self.load_lb()
    
    
    
    #-----------------------------------------------------------------------------------
    def undo_disable(self,event):
        """ 
        
        """
                
        selected_tab = self.tab('@{},{}'.format(event.x,event.y))
        #tab_state = event.widget.tab(selected_tab, 'state')
        if selected_tab['state'] == 'disabled':
            self.tab('@{},{}'.format(event.x,event.y), state = 'normal')
            self.t
            #self.select(self.tab('@{},{}'.format(event.x,event.y)))
        else:
            print('Tab selected is not disabled')
        
        #x,y = event.x, event.y
        #print(x,y)
                
        
        #k = event.widget.winfo_children()
        #tabs = self.tabs()
        ##c = event.widget.identify(event.x,event.y)
        #c = self.tab('@{},{}'.format(event.x,event.y))
        #print([x for (z,y) in c.items()])
        
        
        #for i in range(3):
            #temp = self.tab(i)
            #print(temp)
            #if temp['state'] == 'disabled':
                #self.tab(i, state = 'norma')
            #else:
                #pass
                    
        #for i in k:
            #if i.cget('state') == tk.DISABLED:
                #i.config(state = tk.NORMAL)
            #else:
                #pass
            
            
            
        #print(k)
        #tabs = repr(self.tabs())
        #print(tabs)
        
        #for i in tabs:
            #if self.tab(i)['state'] == 'normal':
                #pass
            #else:
                #self.tab(i, state = 'normal')
            

    
    
    #------------------------------------------
    def load_lb(self):
        """ 
        
        """
        
        for i in customer:
            self.lbox_tab1.insert(tk.END, i)
    
    
    
    #------------------------------------------
    def selected_tab(self, event):
        """ 
        When tab otherthan 'Current' this event function is called.
        #The first line sets up a widget selection object for the event. The second line specifies that
        #it should be the text of the tab that we're interested in. We can test our two tabs in an if statement. Add this: 
        """
        
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")        
        
        if tab_text == "Not Started":
            print("Not Started Tab- Selected")     
        if tab_text == "In Progress":        
            print("In Progress Tab - Selected")        
        if tab_text == "Completed":        
            print("Completed Tab - Selected")     
            
    
    
    #------------------------------------------
    def AddTab(self):
        """ 
        Function to add new tab widget to the Notebook parent
        """
        
        numb_tabs = len(self.tabs())
        F = ttk.Frame(self, width = 400, height = 400, relief = tk.SUNKEN)
        self.add(F, text = 'New Tab - #{}'.format(numb_tabs + 1))
        self.update()
        return
    
    
    #------------------------------------------
    def destroyTab(self):
        """ 
        Destroys selected tab from the parent Notebook
        """
        
        k = self.winfo_children()
        k.pop().destroy()
        return
    
    
    #------------------------------------------
    def disableTab(self):
        """ 
        
        """
        
        selec = self.select()
        self.tab(selec, state = 'disabled')
        return
    




######################################################    
#----------------------------------------------------------------------------     
class maker_buttons(ttk.Button):

    #---------------------------------
    def __init__(self, *args):
        """ 
        
        """        
        
        super(maker_notebook).__init__()
        ttk.Button.__init__(self, *args)
        self.grid(padx = 3, pady = 3)
    
    #---------------------------------
    def config_button(self, txt, *args):
        """ 
        
        """
        
        self.config(text = txt)
        self.bind()
        


######################################################
#----------------------------------------------------------------------------  
class maker_entry(ttk.Entry):
    
    #------------------------------
    def __init__(self, *args):
        """ 
        
        """
         
        ttk.Entry.__init__(self, *args)
        
 
    #------------------------------
    def config_entry(self, *args):
        """ 
        
        """
         
        pass
    
    

######################################################
#----------------------------------------------------------------------------  
if __name__ == '__main__':
    """ """
    
    root = tk.Tk()
    root.title('Pump Commander - Sandbox')
    
    maker_notebook(root)
    
    b1 = maker_buttons()
    b1.config_button('< Move')
    
    b2 = maker_buttons()
    b2.config_button('Move >')
    
    root.mainloop()
