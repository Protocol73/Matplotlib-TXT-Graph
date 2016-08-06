
#Graph from a txt file
import Tkinter as tk
import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.animation as animation
from matplotlib.figure import Figure

Large_Font= ("Verdana", 12)

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)

def animate(i):
    pullData = open("Test-Data.txt", 'r').read()
    dataList = pullData.split('\n')
    xList = []
    yList = []
    for eachLine in dataList:
        if len (eachLine) > 1:
            x, y = eachLine.split(',')
            xList.append(int(x))
            yList.append(int(y))
    a.clear() 
    a.plot(xList, yList)       

class TextDapp (tk.Tk):

      def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args,**kwargs)
        tk.Tk.wm_title(self, "Sea of BTC Client")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand="true")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, GraphP):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

      def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Text Data Graph', font=Large_Font)
        label.pack(pady=10, padx=10)
        label = tk.Label(self, text='This is a Test Python script that Graphs numbers from a .txt File')
        label.pack()
        button0 = ttk.Button(self,text='Graph',command=lambda: controller.show_frame(GraphP))
        button0.pack()
        button1 = ttk.Button(self, text='Exit', command=quit)
        button1.pack()
        label = tk.Label(self, text='Make sure Test-Data.txt is in the same Dir as the script & 1,2,3 ect in Each Line then a (,) &  then your # ')
        label.pack()

class GraphP(tk.Frame):

    def __init__(self,parent , controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Graph Page", font=Large_Font)
        label.pack(pady=10, padx=10)
        button5 = ttk.Button(self, text='Quit', command=quit) 
        button5.pack()
        button6 = ttk.Button(self, text='Home', command=lambda: controller.show_frame(StartPage))
        button6.pack()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = "true")

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = "true")

app = TextDapp()
ani = animation.FuncAnimation(f, animate, interval=2000)
app.mainloop()

