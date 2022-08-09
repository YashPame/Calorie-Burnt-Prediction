from tkinter import *
from tkinter import ttk
import pyautogui
from tkinter import messagebox
import pickle
import pandas as pd
import numpy as np


data = pd.read_csv('FinalDataset_CalorieBurntPrediction.csv')
model = pickle.load(open('CalorieBurntPredictionModel.pkl', 'rb'))
class CalorieBurntPrediction:
    def __init__(self, root):
        self.root = root
        self.root.geometry()

        w = 1375
        h = 777

        self.root.geometry(f"{w}x{h}+272+151")

        mainFrame = Frame(self.root, bd=5, relief=RIDGE)
        mainFrame.place(x=0, y=0, width=1375, height=777)

        mainFrameHeadLBL = Label(mainFrame, text='Calorie Burnt Prediction', font='times 15 bold', bd=4, relief=RIDGE)
        mainFrameHeadLBL.place(x=281, y=63, width=812, height=50)

        def CBP():

            def CalBurnt():
                if cmb.get() == 'Select':
                    messagebox.showerror("ERROR", "Select Gender")
                else:
                    try:
                        G = cmb.get()
                        if G == 'Male':
                            G = 0
                        else:
                            G = 1

                        A = AgeEntry.get()
                        A = int(A)

                        H = HeightEntry.get()
                        H = float(H)

                        W = WeightEntry.get()
                        W = float(W)

                        D = DurationEntry.get()
                        D = float(D)

                        HR = HeartRateEntry.get()
                        HR = float(HR)

                        B = BodyTempEntry.get()
                        B = float(B)

                        inputData = (G, A, H, W, D, HR, B)
                        inputData_asNumpyArray = np.asarray(inputData)
                        inputData_Reshaped = inputData_asNumpyArray.reshape(1, -1)
                        prediction = model.predict(inputData_Reshaped)
                        CalorieBurnt.set(str(prediction[0]))

                        CalorieBurntDisplayLBL = Label(Frame1, text='Total Calories\nBurnt Are', font='lucida 15',
                                                       relief=RIDGE, bd=2)
                        CalorieBurntDisplayLBL.place(x=380, y=140, width=250, height=70)

                        CalorieBurntDisplay = Label(Frame1, textvariable=CalorieBurnt, font='lucida 17', relief=RIDGE,
                                                    bd=2)
                        CalorieBurntDisplay.place(x=380, y=220, width=250, height=50)

                    except:
                        messagebox.showerror("ERROR", "Invalid Entries Found\nPlease Check")

            Age = StringVar()
            Height = StringVar()
            Weight = StringVar()
            Duration = StringVar()
            HeartRate = StringVar()
            BodyTemp = StringVar()
            CalorieBurnt = StringVar()

            Age.set("20")
            Height.set("170")
            Weight.set("53")
            Duration.set("30")
            HeartRate.set("110")
            BodyTemp.set("40")

            Frame1 = Frame(mainFrame, bd=3, relief=RIDGE)
            Frame1.place(x=362, y=170, width=650, height=500)

            LBL = Label(Frame1, text='Details', font='lucida 12', relief=RIDGE, bd=2)
            LBL.place(x=13, y=13, width=157, height=45)

            GenderLBL = Label(Frame1, text='Gender', font='lucida 11', relief=RIDGE, bd=2)
            GenderLBL.place(x=13, y=68, width=155, height=38)
            select = ['Male', 'Female']

            cmb = ttk.Combobox(Frame1, values=select)
            cmb.place(x=200, y=68, width=155, height=38)
            cmb.current(0)
            AgeLBL = Label(Frame1, text='Age', font='lucida 11', relief=RIDGE, bd=2)
            AgeLBL.place(x=13, y=118, width=155, height=38)
            AgeEntry = Entry(Frame1, textvariable=Age, font='lucida 12', relief=RIDGE, bd=2)
            AgeEntry.place(x=200, y=118, width=155, height=38)

            HeightLBL = Label(Frame1, text='Height(cm)', font='lucida 11', relief=RIDGE, bd=2)
            HeightLBL.place(x=13, y=168, width=155, height=38)
            HeightEntry = Entry(Frame1, textvariable=Height, font='lucida 12', relief=RIDGE, bd=2)
            HeightEntry.place(x=200, y=168, width=155, height=38)

            WeightLBL = Label(Frame1, text='Weight(kg)', font='lucida 11', relief=RIDGE, bd=2)
            WeightLBL.place(x=13, y=218, width=155, height=38)
            WeightEntry = Entry(Frame1, textvariable=Weight, font='lucida 12', relief=RIDGE, bd=2)
            WeightEntry.place(x=200, y=218, width=155, height=38)

            DurationLBL = Label(Frame1, text='Duration', font='lucida 11', relief=RIDGE, bd=2)
            DurationLBL.place(x=13, y=268, width=155, height=38)
            DurationEntry = Entry(Frame1, textvariable=Duration, font='lucida 12', relief=RIDGE, bd=2)
            DurationEntry.place(x=200, y=268, width=155, height=38)

            HeartRateLBL = Label(Frame1, text='Heart Rate', font='lucida 11', relief=RIDGE, bd=2)
            HeartRateLBL.place(x=13, y=318, width=155, height=38)
            HeartRateEntry = Entry(Frame1, textvariable=HeartRate, font='lucida 12', relief=RIDGE, bd=2)
            HeartRateEntry.place(x=200, y=318, width=155, height=38)

            BodyTempLBL = Label(Frame1, text='Body Temp', font='lucida 11', relief=RIDGE, bd=2)
            BodyTempLBL.place(x=13, y=368, width=155, height=38)
            BodyTempEntry = Entry(Frame1, textvariable=BodyTemp, font='lucida 12', relief=RIDGE, bd=2)
            BodyTempEntry.place(x=200, y=368, width=155, height=38)

            CheckCalBTN = Button(Frame1, text='Check Calorie Burnt', font='lucida 11', relief=RAISED, bd=4,
                                 command=CalBurnt)
            CheckCalBTN.place(x=13, y=418, width=280, height=45)

        CBP()


if __name__ == '__main__':
    root = Tk()
    obj = CalorieBurntPrediction(root)
    root.mainloop()
