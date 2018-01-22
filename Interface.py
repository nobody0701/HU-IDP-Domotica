import tkinter as tk
from tkinter import ttk
from Database import *


class Counter_program():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Monitor")
        self.create_widgets()

    def create_widgets(self):
        self.window['padx'] = 10
        self.window['pady'] = 10


        def melding_widget():
            def combine():
                melding_frame.grid_remove()
                melding_widget()

            def data_remove(dat):
                dat1, dat2, dat3 = dat.split('-')
                dataremove(dat2, dat3)
                combine()

            melding = data(0)

            melding_frame = ttk.LabelFrame(self.window, text="Meldingen",  relief=tk.RIDGE)
            melding_frame.grid(row=1, column=1)

            my_listbox = tk.Listbox(melding_frame, height=len(melding)+1)
            for item in melding:
                my_listbox.insert(tk.END, str(item[0]) + '-' + str(item[1]) + '-' + str(item[2]))
            my_listbox.grid(row=1, column=1)
            if len(melding) > 0:
                ttk.Button(melding_frame, text='Klaar', command=lambda: data_remove(my_listbox.get(my_listbox.curselection()))).grid(row=2, column=2)
            ttk.Button(melding_frame, text='Refresh', command=combine).grid(row=2, column=1)
            my_listbox.select_set(0)

        melding_widget()

        def list_widget():
            def combine2(naam):
                if naam != "":
                    list_frame.grid_remove()
                    gegevens(naam)
            list_frame = ttk.LabelFrame(self.window, text="Selecteer de kamer", relief=tk.RIDGE)
            list_frame.grid(row=2, column=1)

            self.combobox_value = tk.StringVar()
            my_combobox = ttk.Combobox(list_frame, height=4, textvariable=self.combobox_value)
            my_combobox.pack()
            my_combobox['values'] = data(1)
            my_button = tk.Button(list_frame, text='Ga', command=lambda: combine2(my_combobox.get()))
            my_button.pack()
            my_combobox.current(0)

        list_widget()

        def gegevens(naam):
            def combine3():
                gegevens_frame.grid_remove()
                list_widget()

            gegevens_frame = ttk.LabelFrame(self.window, text="Gegevens", relief=tk.RIDGE)
            gegevens_frame.grid(row=3, column=1)
            gegevensdata = data(2)

            for x in gegevensdata:
                if x[1] == str(naam):
                    naambewoner = 'Naam van bewoner: ' + x[1]
                    kamerid = 'ID: ' + str(x[0])
                    kamernr = 'Kamernummer: ' + str(x[2])
                    startstofzuiger = 'Stofzuiger start: ' + str(x[4])
                    stoptstofzuiger = 'Stofzuiger stopt: ' + str(x[5])
                    actief = 'Actief?: ' + str(x[6])
                    opentijdgordijnen = 'Tijd opening: ' + str(x[8])
                    opengordijnen = 'Open?: ' + str(x[9])

                    ttk.Label(gegevens_frame, text=naambewoner).grid(row=1, column=1, sticky=tk.W)
                    ttk.Label(gegevens_frame, text=kamerid).grid(row=2, column=1, sticky=tk.W)
                    ttk.Label(gegevens_frame, text=kamernr).grid(row=3, column=1, sticky=tk.W)

                    stofzuiger_frame = ttk.LabelFrame(gegevens_frame, text="Stofzuiger", relief=tk.RIDGE)
                    stofzuiger_frame.grid(row=4, column=1)
                    ttk.Label(stofzuiger_frame, text=startstofzuiger).grid(row=1, column=1, sticky=tk.W)
                    ttk.Label(stofzuiger_frame, text=stoptstofzuiger).grid(row=2, column=1, sticky=tk.W)
                    ttk.Label(stofzuiger_frame, text=actief).grid(row=3, column=1, sticky=tk.W)
                    ttk.Button(stofzuiger_frame, text='Wijzigen', command=lambda: stofzuiger_wijzigen()).grid(row=4, column=1)

                    gordijnen_frame = ttk.LabelFrame(gegevens_frame, text="Gordijnen", relief=tk.RIDGE)
                    gordijnen_frame.grid(row=5, column=1)
                    ttk.Label(gordijnen_frame, text=opentijdgordijnen).grid(row=1, column=1, sticky=tk.W)
                    ttk.Label(gordijnen_frame, text=opengordijnen).grid(row=2, column=1, sticky=tk.W)
                    ttk.Button(gordijnen_frame, text='Wijzigen', command=lambda: gordijnen_wijzigen()).grid(row=4, column=1)

                    tk.Button(gegevens_frame, text='Terug', command=combine3).grid(row=6, column=1)
                    break

            def stofzuiger_wijzigen():
                stofzuiger_frame.grid_remove()
                def combine5(een, twee, drie):
                    datawijzigen1(een, twee, drie)
                    gegevens_frame.grid_remove()
                    gegevens(naam)

                stofzuigerwijzig = ttk.LabelFrame(gegevens_frame, text="Stofzuiger", relief=tk.RIDGE)
                stofzuigerwijzig.grid(row=4, column=1)
                startstofzuigerentry = ttk.Entry(stofzuigerwijzig, width=7)
                startstofzuigerentry.grid(row=1, column=2)
                ttk.Label(stofzuigerwijzig, text='Stofzuiger start:').grid(row=1, column=1, sticky=tk.W)
                startstofzuigerentry.insert(tk.END, str(x[4]))
                stopstofzuigerentry = ttk.Entry(stofzuigerwijzig, width=7)
                stopstofzuigerentry.grid(row=2, column=2)
                ttk.Label(stofzuigerwijzig, text='Stofzuiger stop:').grid(row=2, column=1, sticky=tk.W)
                stopstofzuigerentry.insert(tk.END, str(x[5]))
                ttk.Button(stofzuigerwijzig, text='Wijzigen', command=lambda: combine5(str(startstofzuigerentry.get()), str(stopstofzuigerentry.get()), str(x[0]))).grid(row=3, column=1)

            def gordijnen_wijzigen():
                gordijnen_frame.grid_remove()
                def combine4(een, twee):
                    datawijzigen(een, twee)
                    gegevens_frame.grid_remove()
                    gegevens(naam)

                gordijnen_frame.grid_remove()
                gordijnwijzig = ttk.LabelFrame(gegevens_frame, text="Gordijnen", relief=tk.RIDGE)
                gordijnwijzig.grid(row=5, column=1)
                ttk.Label(gordijnwijzig, text='Tijd opening:').grid(row=1, column=1, sticky=tk.W)
                entrytijd = ttk.Entry(gordijnwijzig, width=7)
                entrytijd.grid(row=1, column=2)
                entrytijd.insert(tk.END, str(x[8]))
                ttk.Button(gordijnwijzig, text='Wijzigen', command=lambda: combine4(str(entrytijd.get()), str(x[0]))).grid(row=4, column=1)



program = Counter_program()

program.window.mainloop()
