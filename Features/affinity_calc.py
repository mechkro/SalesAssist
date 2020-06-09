"# -*- coding: utf-8 -*-"
import Tkinter as tk
import random

#----------------------------------------------------------------
BG = '#0C1021'
FG = 'white'
F = ('Verdana',8, 'normal')
C = 'hand2'

"""
Nr = V*D*rho / 


"""



#-----------------------------------------------------------
class AffinityCalc(tk.Tk):

    
    def __init__(self, *args, **kwargs):
        """
        Func to calculate the affinity laws for change in speed of the pumping unit. Users are expected
        to input the initial speed and the final speed the pump will run at (VFD usage).

        Also needed will be the initial inputs of current flow, head, and brake hp while at initial speed.

        OUTPUT - Final flow output, head pressure, and brake HP with reduction of as a result of
        speed reduction.

        ADD - Pump eff - n, estimated bhp,  bhp = Q*H*S.G / 3960* n
        """
        
        tk.Tk.__init__(self)
        self.config(bg = BG)

        #Menu creation -----------------------------------------------------------------------------------
        self.menubar = tk.Menu(self,
                            background = '#0C1021', foreground='white',
                            activebackground='dark goldenrod', activeforeground='white',
                            cursor = 'hand2')
        self.filemenu = tk.Menu(self.menubar, tearoff=0,
                             background='#0C1021', foreground='white',
                             activebackground='dark goldenrod', activeforeground='white',
                             cursor = 'hand2')
        
        self.filemenu.add_command(label = "Calc RPM", command = lambda: self.find_rpm_required())
        self.menubar.add_cascade(label = "Alt Calcs", menu = self.filemenu)

        self.config(bg='#0C1021', menu = self.menubar)
        #End of Menu ------------------------------------------------------------------------------------
        
        #Frame Widgets ----------------------------------------------------------------------------------
        self.frm = tk.Frame(self, bg = BG)
        self.frm.grid(row = 0, column = 0)

        self.frm_output = tk.Frame(self, bg = BG)
        self.frm_output.grid(row = 0, column = 1)

        self.botframe = tk.Frame(self, bg = BG)
        self.botframe.grid(row = 1, column = 0, columnspan = 2)
        #End of Frame -----------------------------------------------------------------------------------

        #Speed Section -------------------------------------------------------------
        self.speedlf = tk.LabelFrame(self.frm, text = 'Speed Input', bg = BG, fg = FG)
        self.speedlf.grid(row = 0, columnspan = 2, padx = 5, pady = 5)
        
        #self.speedlf.bind('<Enter>', self.bind_enter(self.speedlf))
        #self.speedlf.bind('<Leave>', self.bind_leave(self.speedlf))

        self.speed1 = tk.Label(self.speedlf, text = 'Current Speed (rpm)', bg = BG, fg = FG)
        self.speed1.grid(row = 0, column = 0, padx = 3, pady = 3)

        self.speed2 = tk.Label(self.speedlf, text = 'New Speed (rpm)', bg = BG, fg = FG)
        self.speed2.grid(row = 1, column = 0, padx = 3, pady = 3)

        self.curr_ent = tk.Entry(self.speedlf, bg = BG, fg = FG,
                                 cursor = C, insertbackground = 'white', width = 28)
        self.curr_ent.grid(row = 0, column = 1, padx = 3, pady = 3, sticky = tk.EW)

        self.new_ent = tk.Entry(self.speedlf, bg = BG, fg = FG,
                                cursor = C, insertbackground = 'white', width = 28)
        self.new_ent.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = tk.EW)

        #Value Entry Sect. ---------------------------------------------------------
        self.vallf = tk.LabelFrame(self.frm, text = 'Current Value Entry', bg = BG, fg = FG)
        self.vallf.grid(row = 1, columnspan = 2, padx = 5, pady = 5, sticky = tk.NSEW)

        self.currlab = tk.Label(self.vallf, text = 'Current Flow (gpm)', bg = BG, fg = FG)
        self.currlab.grid(row = 0, column = 0, columnspan = 2, padx = 3, pady = 3, sticky = tk.EW)

        self.cflow = tk.Entry(self.vallf, bg = BG, fg = FG, width = 45,
                              cursor = C, insertbackground = 'white')
        self.cflow.grid(row = 1, column = 0, columnspan = 2, padx = 7, pady = 3, sticky = tk.EW)

        self.headlab = tk.Label(self.vallf, text = 'Current Pressure (ft)', bg = BG, fg = FG)
        self.headlab.grid(row = 2, column = 0, columnspan = 2, padx = 3, pady = 3, sticky = tk.EW)

        self.chead = tk.Entry(self.vallf, bg = BG, fg = FG, width = 45,
                              cursor = C, insertbackground = 'white')
        self.chead.grid(row = 3, column = 0, columnspan = 2, padx = 7, pady = 3, sticky = tk.EW)

        self.hplab = tk.Label(self.vallf, text = 'Current HP (bhp)', bg = BG, fg = FG)
        self.hplab.grid(row = 4, column = 0, columnspan = 2, padx = 3, pady = 3, sticky = tk.EW)

        self.chp = tk.Entry(self.vallf, bg = BG, fg = FG, width = 45,
                            cursor = C, insertbackground = 'white')
        self.chp.grid(row = 5, column = 0, columnspan = 2, padx = 7, pady = 3, sticky = tk.EW)

        self.valbutt = tk.Button(self.vallf, text = 'Calculate',bg = BG, fg = FG, command = lambda: self.check_realistic())
        self.valbutt.grid(row = 6, column = 0, columnspan = 2, padx = 3, pady = 3, sticky = tk.EW)

        #Right Frame ---------------------------------------------------------------
        self.outlf = tk.LabelFrame(self.frm_output, text = 'Output', bg = BG, fg = FG)
        self.outlf.grid(padx = 5, pady = 5)
        
        self.txt_out = tk.Text(self.outlf, height = 10, bg = BG, fg = FG,
                               cursor = C, insertbackground = 'white')
        self.txt_out.grid(row = 0, columnspan = 2, padx = 5, pady = 5, sticky = tk.NSEW)

        self.hoursrunning = tk.Label(self.outlf, text = 'Running hrs\n(24/7 is 8760hr/yr)', bg = BG, fg = FG)
        self.hoursrunning.grid(row = 1, column = 0, padx = 3, pady =3)

        self.hours_ent = tk.Entry(self.outlf, bg = BG, fg = FG,
                                  cursor = C, insertbackground = 'white')
        self.hours_ent.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = tk.EW)

        self.costperhr = tk.Label(self.outlf, text = 'Cost $/kwh', bg = BG, fg = FG)
        self.costperhr.grid(row = 2, column = 0, padx = 3, pady =3)

        self.cost_ent = tk.Entry(self.outlf, bg = BG, fg = FG,
                                 cursor = C, insertbackground = 'white')
        self.cost_ent.grid(row = 2, column = 1, padx = 3, pady = 3, sticky = tk.EW)

        self.calc_cost = tk.Button(self.outlf, text = 'Calc Cost',bg = BG, fg = FG, command = lambda: self.calc_return())
        self.calc_cost.grid(row = 3, column = 0, columnspan = 2, padx = 3, pady = 3, sticky = tk.EW)

        #BottomFrame --------------------------------------------------------------
        self.txtlabf = tk.LabelFrame(self.botframe, text = 'Output Details', bg = BG, fg = FG)
        self.txtlabf.grid(row = 0, column = 0,  columnspan = 2, padx = 5, pady = 8, sticky = tk.NS)

        self.reflabf = tk.LabelFrame(self.botframe, text = 'Ref. Equations', bg = BG, fg = FG)
        self.reflabf.grid(row = 0, column = 2,  columnspan = 2, padx = 5, pady = 8, sticky = tk.NS)
        
        self.rtxt = tk.Text(self.txtlabf, bg = BG, fg = FG, height = 10, width = 90,
                            cursor = C, insertbackground = 'white', insertwidth = 5)
        self.rtxt.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)

        self.reftxt = tk.Text(self.reflabf, bg = BG, fg = FG, height = 10, width = 45,
                              cursor = C, insertbackground = 'white', insertwidth = 5)
        self.reftxt.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5, sticky = tk.N)

        #These are the pre-loaded equations to be loaded into text box so user can reference
        ref_tips = '''\n  See below equations for assistance\n\n'''
        ref_flow = '''  Affinity Laws\n  Flow -->  Q2/Q1 = N2/N1\n'''
        ref_head = '''  Pressure -->  H2/H1 = (N2/N1)^2\n'''
        ref_bhp = '''  Brake HP -->  P2/P1 = (N2/N1)^3 \n\n'''
        ref_pipvel = '''\n  Pipe Velocity\n  V = 0.408*(Q/D^2) gives ft/s\n  D (in), Q (gpm)\n'''
        ref_others = """\n  WHP = (Q*H)/3960
  Q(flow) = (3960*WHP)/H
  H(Head) = (3960*WHP)/Q
  n(eff) = WHP/BHP
  
  Therefore -->
  Source: https://www.ajdesigner.com/phppump/pump_equations_brake_horsepower.php#ajscroll
                     """

        for eq in [ref_tips, ref_flow, ref_head, ref_bhp, ref_pipvel, ref_others]:
            self.reftxt.insert(tk.END, eq)

        #self.rpm_calcs()
    
    #----------------------------------------------------------------
    def bind_enter(self, w):
        """ """
        
        w.config(fg = 'dark goldenrod')
    
    #----------------------------------------------------------------  
    def bind_leave(self, w):
        """ """
        
        w.config(fg = FG)   
        
        
    #----------------------------------------------------------------
    def find_rpm_required(self):
        """
        #self.frm.destroy()
        #self.rpmframe = tk.Frame(self, bg = BG)
        #self.rpmframe.grid(row = 0, column = 0)
        """
        
        self.speedlf.config(text = 'RPM Needed for:')
        self.speed1.destroy()
        self.speed2.destroy()

        self.curr_ent.destroy()
        self.new_ent.destroy()

        self.newlab = tk.Label(self.speedlf, text = 'Put in widgets', bg = BG, fg = FG)
        self.newlab.grid(padx = 8, pady = 8)
        

    #----------------------------------------------------------------
    def check_realistic(self):
        """
        Check to see if what the user enters is a realistic HP rating on there equipped motor.
        If not we should raise that concern for the user so they are aware by providing the
        calculated approximate need by the given conditions.
        """
        
        cf = float(self.cflow.get())
        cp = float(self.chead.get())
        chp = float(self.chp.get())
        bhp = (cf*cp*1.0)/(3960.0*.85)
        plow, phigh = chp*.75 , chp*1.25
        
        if bhp not in range(int(plow),int(phigh)):
            print('Not within 25% of the predicted value: {}'.format(bhp))
            print(plow)
            print(phigh)
            
        else:
            print('Good value, within 25% of the predicted: {}'.format(bhp))
            print(plow)
            print(phigh)
            
        self.calc_values()
    

    #----------------------------------------------------------------
    def calc_values(self):
        """
        Func takes the initial value inputs and runs the first set of calculations. The new values for:
                  - Flow
                  - Head
                  - HP
        """
        
        self.n1, self.n2, self.f2, self.p2, self.h2 = float(self.curr_ent.get()), float(self.new_ent.get()), float(self.cflow.get()),  float(self.chead.get()), float(self.chp.get())

        self.newflow = self.f2*(self.n2/self.n1)
        self.newhead = self.p2*((self.n2/self.n1)**2)
        self.newhp = self.h2*((self.n2/self.n1)**3)

        self.txt_out.delete(1.0, tk.END)
        self.txt_out.insert(tk.END, """

        Turndown ration = {}
        New Flow rate = {}
        New Head value = {}
        New HP Required = {}

        """.format('Test',self.newflow, self.newhead, self.newhp))

        self.energy_savings(self.newflow, self.newhead, self.newhp, self.h2)

        
    #---------------------------------------------------------------
    def energy_savings(self, nf, np, nh, nh2):
        """
        Amps = (Horsepower × 746) ÷ Efficiency ÷ Volts.
        """
        
        self.oldamps = (nh2*746.0)/(.89)/(460.0)
        self.newamps = (nh*746.0)/(.89)/(460.0)
        self.amps_diff = self.oldamps - self.newamps
        self.txt_out.insert(tk.END, """

        Olds Amps = {}
        New Amps = {}
        Amp Difference = {}

        """.format(self.oldamps, self.newamps, self.amps_diff))

        
    #---------------------------------------------------------------
    def calc_return(self):
        """
        Double checked accuracy with this site:
        http://www.vfds.org/vfd-savings-calculator.html#saving
        Seems to be accurate.....
        """
        
        self.txt_out.delete(1.0, tk.END)
        self.watts = self.newamps*460.0
        self.oldwatts = self.oldamps*460.0
        self.newcost = (float(self.cost_ent.get()))*(self.watts/1000.0)*(float(self.hours_ent.get()))
        self.oldcost = (float(self.cost_ent.get()))*(self.oldwatts/1000.0)*(float(self.hours_ent.get()))
        self.txt_out.insert(tk.END, """

        Cost for Running unit at new speed = ${}
        Compared to running at old speed which cost = ${}

        Which is saving ${}/yr
   
        """.format(self.newcost, self.oldcost, (self.oldcost-self.newcost)))

        self.results_output()


    #--------------------------------------------------------------------------
    def brake_hp_calc(self):  #, n, sg, Q, H):
        """
        n = pump eff -- i.e. .85
        sg = specific gravity -- i.e 1.00 for water, .85 for oils...etc
        Q = flow in gpm
        H = head in feet
        3960 -- constant in these units
        """
        
        sg_seq = [.85, .86, .89, .95, .99, 1.0, 1.3, 1.8, 2.5, 3.4, 4.06]
        eff_seq = [.35, .42, .56, .78, .81, .85, .86, .89]
 
    
        for i in range(15):
            Q = random.randrange(100,10000)
            H = random.randrange(25,450)
            sg = random.choice(sg_seq)
            n = random.choice(eff_seq)
            bhp = (Q*H*sg)/(3960.0*n)
            print("""

                  Q = {}
                  H = {}
                  sg = {}
                  n = {}

                  Therefore BHP = {}
                  """.format(Q,H,sg,n,bhp))

        mgdhigh = 1667.98 #gpm
        mgdlow = 250.9 #gpm

        #go from 1667.98 --> to --> 250.9, what speed reduction is required
        #assume 1800 rpm motor
        N2 = 1800.0*(250.98/1667.98)        #270 rpm
        H2 = 299.86*((270.0/1800)**2)       #6.78 ft
        DIFF = 130.0 - 88.0                 #42.0psi == 96.87ft


    #--------------------------------------------------
    def results_output(self):
        """
        Func - to format the calculated results in string
        """
        
        self.rtxt.insert(tk.END, """

        Current speed = {} rpms, New speed = {} rpms

        New Flow rate = {} gpm, old flow = {} gpm
        New Head value = {} ft, old head = {} ft
        New HP Required = {} hp, old HP = {} hp

        Olds Amps = {}
        New Amps = {}
        Amp Difference = {}

        Cost for Running unit at new speed = ${}
        Compared to running at old speed which cost = ${}

        Which is saving ${}/yr        

        """.format(self.n1, self.n2, self.newflow, self.f2, self.newhead,
                   self.p2, self.newhp, self.h2, self.oldamps, self.newamps,
                   self.amps_diff,self.newcost, self.oldcost, (self.oldcost-self.newcost)))

    #-------------------------------------------------
    def rpm_calcs(self):
        """
          N = 120*f / p
          Where:
              - N = speed (rpm)
              - f = frequency (hz)
              - p = # of motor poles
        """
        
        self.speedwin = tk.Toplevel()
        self.speedwin.config(bg = BG)
        
        self.sw_frame = tk.Frame(self.speedwin, bg = BG)
        self.sw_frame.grid(sticky = tk.NSEW)

        self.speedlab = tk.Label(self.sw_frame, text = 'Enter desired Speed (rpm)',
                                 bg = BG, fg= FG)
        self.speedlab.grid(row = 0, padx = 5, pady = 5)

        self.speedent = tk.Entry(self.sw_frame, bg = BG, fg = FG)
        self.speedent.grid(row = 1, padx = 10, pady = 10)

        self.polelab = tk.Label(self.sw_frame, text = 'Use spinbox to\nselect current poles\nof motor.',
                                 bg = BG, fg= FG)
        self.polelab.grid(row = 2, padx = 5, pady = 5)

        self.polebox = tk.Spinbox(self.sw_frame, bg = BG, fg = FG, values = ('2 (3600)','4 (1800)','6 (1200)','8 (900) ','10 (unlikely)'))
        self.polebox.grid(row = 3, padx = 10, pady = 10)

        self.b = tk.Button(self.speedwin, text = 'Calculate', command = self.calc_freq, bg = BG, fg = FG)
        self.b.grid(row = 4, padx = 5, pady = 5)

        self.resultlab = tk.Label(self.sw_frame, text = '',
                                 bg = BG, fg= FG) 
        self.resultlab.grid(row = 5, padx = 5, pady = 5)

        self.speedwin.mainloop()


    #---------------------------------------------------
    def calc_freq(self):
        """
         Func to return the frequency required to get desired rotation on motor driven equipment
        """
        
        n = int((self.speedent.get()))      #Speed rpms
        p = int((self.polebox.get()))       #Poles of the motor
        f = (n*p)/120.0                     #Frequency required to match rpms
        
        self.resultlab.config(text = 'Desired freq: {}'.format(f))
        #self.top_win_status()


    #-------------------------------------------------
    def top_win_status(self):
        """

        """
        
        print(self.winfo_children())
        self.winfo_children[-1].lift()
        self.lift()


    #----------------------------------------------
    def b_thereom(self,*args,**kwargs):
        """
        Func - to attempt and be able to come up with high level system curve to assist customers with a better
        idea of there operating pump.

        Should solve equation to produce an equation allowing us to plot friction of system
        Equation: (Source: https://www.youtube.com/watch?v=hz39dU38TAk)

        p1/gamma + z1 + v1^2/2*g + Hp = p2/gamma + z2 + v2^2/2*g + h_f + h_m

        Hp = z2 - z1 + f*(L/D)* v^2/2*g + SUM(v^2/2*g)
        """
        pass


    #------------------------------------------------
    def app_select_guide(self):
        """
        Have each industry be a dict that has keywords as pump type and there values are the applicable applications
        """
        
        water_treatment = {
                             'Centrifugal':['Raw Wastewater', 'Primary Sludge', 'Sec. Sludge', 'Effluent Wastewater', 'Flush Water',
                                            'Spray Water', 'Seal Water'],
                             'Pos. Displace':['Primary Sludge', 'Thickened Sludge', 'Digested Sludge',
                                              'Slurries', 'Chem. Feed Applications'],
                             'Prog. Cav':['All types of sludge']
                          }


    #------------------------------------------------
    def write_to_report(*args, **kwargs):
        """

        """

        report = """
        Quote #: {}
        Customer: {}
        Prepared by: {}
        Date: {}

        Q = {}
        H = {}
        sg = {}
        n = {}

        n = pump eff -- i.e. .85
        sg = specific gravity -- i.e 1.00 for water, .85 for oils...etc
        Q = flow in gpm
        H = head in feet
        3960 -- constant in these units
        
        Therefore BHP = {}

        Current speed = {} rpms, New speed = {} rpms

        N = 120*f / p
          Where:
              - N = speed (rpm)
              - f = frequency (hz)
              - p = # of motor poles

        New Flow rate = {} gpm, old flow = {} gpm
        New Head value = {} ft, old head = {} ft
        New HP Required = {} hp, old HP = {} hp

        Olds Amps = {}
        New Amps = {}
        Amp Difference = {}

        Cost for Running unit at new speed = ${}
        Compared to running at old speed which cost = ${}

        Which is saving ${}/yr   
        
        """.format([i for i in args])

        with open('floc', 'w')as F:
            F.write(report)

        return

    #----------------------------------------------------------------
    def continuity_eq(self):
        """
        For:
             - incompressible flow - A_1 * V_1 = A_2 * V_2
             - compressable flow - rho_1 * A_1 * V_1 = rho_2 * A_2 * V_2
        """
        pass
        
    
        
        
        


#---------------------------------------------------------------
class SystemCurve:
    
    def __init__(self, parent):
        """
        Attempt to create a function that will help identify or calculate a high-level calc of system curve
             - Could also just be used as a reminder of system curves and there interactions
             - Define all that goes into them
        """
        
        self.parent = parent
        self.parent.iconify()
        
        tk.Toplevel.__init__(self)
        tk.Toplevel.mainloop()



#---------------------------------------------------------------
class PDAffinity:
    
    def __init__(self, parent):
        """
        New toplevel frame to house widgets for calculating PD pumps affinity laws
             - We need to calculate the number we will use to carry out affinity equations

             - Source: http://www.mcnallyinstitute.com/13-html/13-06.htm
             
             - PD_constant = New Speed / Old speed
                    - ex.
                    - 3500/1750rpm = 2
                    - 1500/3000 rpm = 0.5

            - Calulcations:
            - CAPACITY (flow):
                    - The capacity or amount of fluid you are pumping varies directly with this number.
                    - ex.
                    - 3500/1750rpm = 2      --->  100gpm(3500rpm) x 2 = 200gpm
                    - 1500/3000 rpm = 0.5   --->  50m^3/hr(1500rpm) x 0.5 = 25m^3/hr

            - HEAD:
                    - The head varies by the square of the number.
                    - ex.
                    - 50ft head x (2^2)     --->  50x4 = 200ft head
                    - 20m head  x (0.5^2)   --->  20x0.25 = 5m head
            - HORSEPOWER:
                    - The horsepower required changes by the cube of the number.
                    - ex.
                    - 
             
        """
        
        self.parent = parent
        self.parent.iconify()
        
        self.pd_win = tk.Toplevel(self)

        self.newrpm = tk.Entry(self.pd_win)
        self.newnumb.grid()

        self.currpm = tk.Entry(self.pd_win)
        self.currpm.grid()

        tk.Toplevel.mainloop()


    #----------------------------------------------------------------
    def gather_establish_numb(self):
        """
         - PD_constant = New Speed / Old speed
                    - ex.
                    - 3500/1750rpm = 2
                    - 1500/3000 rpm = 0.5
        """
        
        nrpm = float(self.newrpm.get())
        crpm = float(self.currpm.get())
        
        establish_numb = nrpm/crpm
        

    #----------------------------------------------------------------
    def new_capacity(self):
        """
        CAPACITY (flow):
                    - The capacity or amount of fluid you are pumping varies directly with this number.
                    - ex.
                    - 3500/1750rpm = 2      --->  100gpm(3500rpm) x 2 = 200gpm
                    - 1500/3000 rpm = 0.5   --->  50m^3/hr(1500rpm) x 0.5 = 25m^3/hr
        """
        
        pass
    
    
    #----------------------------------------------------------------
    def new_head(self):
        """
        HEAD:
                    - The head varies by the square of the number.
                    - ex.
                    - 50ft head x (2^2)     --->  50x4 = 200ft head
                    - 20m head  x (0.5^2)   --->  20x0.25 = 5m head
        """
        
        pass
    
    
    #----------------------------------------------------------------
    def new_hp(self):
        """
        - HORSEPOWER:
                    - The horsepower required changes by the cube of the number.
                    - ex.
                    - 
        """
        
        pass
    
    #----------------------------------------------------------------
    def bind_enter(self, w):
        w.config(fg = 'dark goldenrod')
      
    #----------------------------------------------------------------
    def bind_leave(self, w):
        w.config(fg = FG)     
        

        


#------------------------------------------------
if __name__ == '__main__':
    root = AffinityCalc()
    root.brake_hp_calc()
    root.mainloop()
        
