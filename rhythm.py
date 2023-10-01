import tkinter as tk
import time
class BasicGui3:

    def __init__(self):
        self.mainWin = tk.Tk()
        self.scaling=0.5
        # buttons
        quitButton = tk.Button(self.mainWin, text="Quit",
                               font="Arial 16",command=self.quitCallback)
        quitButton.grid(row=1, column=1)

        # Scoring Label
        self.accScore=0
        self.multNum = 0
        self.scoreLabel = tk.Label(self.mainWin)
        self.scoreLabel.config(text = self.accScore,
                          font = "Arial 18 bold",
                          bg = "white",
                          relief = tk.RIDGE)
        self.scoreLabel.grid(row = 2, column = 4)

        # Combo/Multiplier Identifier
        self.Combo = tk.Label(self.mainWin)
        self.Combo.config(text = str(1 + self.multNum) + "x", font = "Arial 18 bold", bg = "white", relief = tk.RIDGE)
        self.Combo.grid(row = 0, column = 3)

        self.myCanvas = tk.Canvas(self.mainWin)
        self.myCanvas["width"] = 800*self.scaling
        self.myCanvas["height"] = 1200*self.scaling
        self.myCanvas["bg"] = "pink"
        self.myCanvas["bd"] = 5
        self.myCanvas["relief"] = tk.SUNKEN
        self.myCanvas.grid(row=10, column=0)

        # HP Bar - depletes as player misses and ends game when HP bar is at 0
        self.hpBar = self.myCanvas.create_line(0, 25, 50, 25, width=10, fill = "white")

        # keybinds that call a function - checks if the arrow is in range of y and whether the player gets the points or not
        self.mainWin.bind("<d>", self.Left)
        self.mainWin.bind("<f>", self.Up)
        self.mainWin.bind("<h>", self.Down)
        self.mainWin.bind("<j>", self.Right)
        self.mainWin.bind("<Left>", self.Left)
        self.mainWin.bind("<Up>", self.Up)
        self.mainWin.bind("<Down>", self.Down)
        self.mainWin.bind("<Right>", self.Right)

        # arrow designs inside canvas
        self.myCanvas.create_line(-2*self.scaling, 1000*self.scaling, 850*self.scaling, 1000*self.scaling,  width=15*self.scaling)
        self.myCanvas.create_line(200*self.scaling, 0*self.scaling, 200*self.scaling, 1200*self.scaling, width=15*self.scaling)
        self.myCanvas.create_line(600*self.scaling, 0*self.scaling, 600*self.scaling, 1200*self.scaling, width=15*self.scaling)
        self.myCanvas.create_line(400*self.scaling, 0*self.scaling, 400*self.scaling, 1200*self.scaling, width=15*self.scaling)
        self.myCanvas.create_line(20*self.scaling, 1100*self.scaling, 180*self.scaling, 1100*self.scaling, arrow= tk.FIRST,arrowshape=(40*self.scaling,50*self.scaling,40*self.scaling),width=35*self.scaling)
        self.myCanvas.create_line(620*self.scaling, 1100*self.scaling, 780*self.scaling, 1100*self.scaling, arrow=tk.LAST,arrowshape=(40*self.scaling,50*self.scaling,40*self.scaling), width=35*self.scaling)
        self.myCanvas.create_line(300*self.scaling, 1180*self.scaling, 300*self.scaling, 1020*self.scaling, arrow=tk.LAST,arrowshape=(40*self.scaling,50*self.scaling,40*self.scaling),width=35*self.scaling)
        self.myCanvas.create_line(500*self.scaling, 1180*self.scaling, 500*self.scaling, 1020*self.scaling, arrow=tk.FIRST,arrowshape=(40*self.scaling,50*self.scaling,40*self.scaling), width=35*self.scaling)

        # Left arrow spawn
        self.arrowleft=self.myCanvas.create_line(20*self.scaling, 0*self.scaling, 180*self.scaling, 0*self.scaling, arrow=tk.FIRST, arrowshape=(40*self.scaling, 50*self.scaling, 40*self.scaling), width=35*self.scaling,
                                                 fill="white")
        self.arrowleft2 = self.myCanvas.create_line(20 * self.scaling, -2100 * self.scaling, 180 * self.scaling, -2100 * self.scaling, arrow=tk.FIRST,
                                                   arrowshape=(40 * self.scaling, 50 * self.scaling, 40 * self.scaling),
                                                   width=35 * self.scaling,
                                                   fill="white")
        self.arrowleft3 = self.myCanvas.create_line(20 * self.scaling, -4100 * self.scaling, 180 * self.scaling,
                                                    -4100 * self.scaling, arrow=tk.FIRST,
                                                    arrowshape=(
                                                    40 * self.scaling, 50 * self.scaling, 40 * self.scaling),
                                                    width=35 * self.scaling,
                                                    fill="white")
        self.arrowleft4 = self.myCanvas.create_line(20 * self.scaling, -4350 * self.scaling, 180 * self.scaling,
                                                    -4350 * self.scaling, arrow=tk.FIRST,
                                                    arrowshape=(
                                                    40 * self.scaling, 50 * self.scaling, 40 * self.scaling),
                                                    width=35 * self.scaling,
                                                    fill="white")
        self.arrowleft5 = self.myCanvas.create_line(20 * self.scaling, -4600 * self.scaling, 180 * self.scaling,
                                                    -4600 * self.scaling, arrow=tk.FIRST,
                                                    arrowshape=(
                                                    40 * self.scaling, 50 * self.scaling, 40 * self.scaling),
                                                    width=35 * self.scaling,
                                                    fill="white")
        self.arrowleft6 = self.myCanvas.create_line(20 * self.scaling, -4850 * self.scaling, 180 * self.scaling,
                                                    -4850 * self.scaling, arrow=tk.FIRST,
                                                    arrowshape=(
                                                    40 * self.scaling, 50 * self.scaling, 40 * self.scaling),
                                                    width=35 * self.scaling,
                                                    fill="white")
        self.arrowleft7 = self.myCanvas.create_line(20 * self.scaling, -5100 * self.scaling, 180 * self.scaling,
                                                    -5100 * self.scaling, arrow=tk.FIRST,
                                                    arrowshape=(
                                                    40 * self.scaling, 50 * self.scaling, 40 * self.scaling),
                                                    width=35 * self.scaling,
                                                    fill="white")
        self.arrowleft8 = self.myCanvas.create_line(20 * self.scaling, -5350 * self.scaling, 180 * self.scaling,
                                                    -5350 * self.scaling, arrow=tk.FIRST,
                                                    arrowshape=(
                                                    40 * self.scaling, 50 * self.scaling, 40 * self.scaling),
                                                    width=35 * self.scaling,
                                                    fill="white")
        self.arrowleft9 = self.myCanvas.create_line(20 * self.scaling, -5600 * self.scaling, 180 * self.scaling,
                                                    -5600 * self.scaling, arrow=tk.FIRST,
                                                    arrowshape=(
                                                    40 * self.scaling, 50 * self.scaling, 40 * self.scaling),
                                                    width=35 * self.scaling,
                                                    fill="white")
        self.arrowleft10 = self.myCanvas.create_line(20 * self.scaling, -5850 * self.scaling, 180 * self.scaling,
                                                    -5850 * self.scaling, arrow=tk.FIRST,
                                                    arrowshape=(
                                                    40 * self.scaling, 50 * self.scaling, 40 * self.scaling),
                                                    width=35 * self.scaling,
                                                    fill="white")
        self.arrowleft11 = self.myCanvas.create_line(20 * self.scaling, -7500 * self.scaling, 180 * self.scaling,
                                                     -7500 * self.scaling, arrow=tk.FIRST,
                                                     arrowshape=(
                                                         40 * self.scaling, 50 * self.scaling, 40 * self.scaling),
                                                     width=35 * self.scaling,
                                                     fill="white")


        # Right arrow spawn
        self.arrowright = self.myCanvas.create_line(620*self.scaling, -1600*self.scaling, 780*self.scaling, -1600*self.scaling, arrow=tk.LAST, arrowshape=(40*self.scaling, 50*self.scaling, 40*self.scaling), width=35*self.scaling,
                                                   fill="white")

        self.arrowright2 = self.myCanvas.create_line(620 * self.scaling, -3700 * self.scaling, 780 * self.scaling, -3700 * self.scaling, arrow=tk.LAST, arrowshape=(40 * self.scaling, 50 * self.scaling, 40 * self.scaling), width=35 * self.scaling,
                                                    fill="white")
        self.arrowright3 = self.myCanvas.create_line(620 * self.scaling, -6050 * self.scaling, 780 * self.scaling,
                                                     -6050 * self.scaling, arrow=tk.LAST, arrowshape=(
            40 * self.scaling, 50 * self.scaling, 40 * self.scaling), width=35 * self.scaling,
                                                     fill="white")



        # up arrow spawn
        self.arrowup1 = self.myCanvas.create_line(300*self.scaling, -1070*self.scaling, 300*self.scaling, -930*self.scaling, arrow=tk.FIRST, arrowshape=(40*self.scaling, 50*self.scaling, 40*self.scaling), width=35*self.scaling,
                                                   fill="white")
        self.arrowup2 = self.myCanvas.create_line(300 * self.scaling, -3170 * self.scaling, 300 * self.scaling,
                                                  -3030 * self.scaling, arrow=tk.FIRST,
                                                  arrowshape=(40 * self.scaling, 50 * self.scaling, 40 * self.scaling),
                                                  width=35 * self.scaling,
                                                  fill="white")
        self.arrowup3 = self.myCanvas.create_line(300 * self.scaling, -6580 * self.scaling, 300 * self.scaling,
                                                  -6440 * self.scaling, arrow=tk.FIRST,
                                                  arrowshape=(40 * self.scaling, 50 * self.scaling, 40 * self.scaling),
                                                  width=35 * self.scaling,
                                                  fill="white")

        # down arrow spawn
        self.arrowdown2 = self.myCanvas.create_line(500*self.scaling, -500*self.scaling, 500*self.scaling, -650*self.scaling, arrow=tk.FIRST, arrowshape=(40*self.scaling, 50*self.scaling, 40*self.scaling), width=35*self.scaling,
                                                   fill="white")
        self.arrowdown3 = self.myCanvas.create_line(500 * self.scaling, -2600 * self.scaling, 500 * self.scaling,
                                                    -2750 * self.scaling, arrow=tk.FIRST, arrowshape=(
            40 * self.scaling, 50 * self.scaling, 40 * self.scaling), width=35 * self.scaling,
                                                    fill="white")
        self.arrowdown4 = self.myCanvas.create_line(500 * self.scaling, -7000 * self.scaling, 500 * self.scaling,
                                                    -7150 * self.scaling, arrow=tk.FIRST, arrowshape=(
                40 * self.scaling, 50 * self.scaling, 40 * self.scaling), width=35 * self.scaling,
                                                    fill="white")






    def go(self):
        """Takes no inputs, and runs its own loop for the GUI.  This is so we can
        move the balls without waiting for some user input."""
        try:
            while True:
                self.progress()  # call local method to update ball positions
                self.mainWin.update_idletasks() # redraw
                self.mainWin.update() # process events
        except tk.TclError:
            pass # to avoid errors when the window is closed

    def progress(self):
        """ This controls the speed in which the arrows drop down the map, as well as how the arrow is 'spawned'."""
        # spawn left arrows
        self.myCanvas.move(self.arrowleft, 0*self.scaling, 15*self.scaling)
        self.myCanvas.move(self.arrowleft2, 0 * self.scaling, 15 * self.scaling)
        self.myCanvas.move(self.arrowleft3, 0 * self.scaling, 15 * self.scaling)
        self.myCanvas.move(self.arrowleft4, 0 * self.scaling, 15 * self.scaling)
        self.myCanvas.move(self.arrowleft5, 0 * self.scaling, 15 * self.scaling)
        self.myCanvas.move(self.arrowleft6, 0 * self.scaling, 15 * self.scaling)
        self.myCanvas.move(self.arrowleft7, 0 * self.scaling, 15 * self.scaling)
        self.myCanvas.move(self.arrowleft8, 0 * self.scaling, 15 * self.scaling)
        self.myCanvas.move(self.arrowleft9, 0 * self.scaling, 15 * self.scaling)
        self.myCanvas.move(self.arrowleft10, 0 * self.scaling, 15 * self.scaling)
        self.myCanvas.move(self.arrowleft11, 0 * self.scaling, 15 * self.scaling)

        # spawn down arrows
        self.myCanvas.move(self.arrowdown2, 0 * self.scaling, 15 * self.scaling)
        self.myCanvas.move(self.arrowdown3, 0 * self.scaling, 15 * self.scaling)
        self.myCanvas.move(self.arrowdown4, 0 * self.scaling, 15 * self.scaling)

        # spawn right arrows
        self.myCanvas.move(self.arrowright, 0 * self.scaling, 15 * self.scaling)
        self.myCanvas.move(self.arrowright2, 0 * self.scaling, 15 * self.scaling)
        self.myCanvas.move(self.arrowright3, 0 * self.scaling, 15 * self.scaling)

        # spawn up arrows
        self.myCanvas.move(self.arrowup1, 0 * self.scaling, 15 * self.scaling)
        self.myCanvas.move(self.arrowup2, 0 * self.scaling, 15 * self.scaling)
        self.myCanvas.move(self.arrowup3, 0 * self.scaling, 15 * self.scaling)

        time.sleep(0.01)

    def multiplierFunc(self,note):
        """ This function updates a multiplier variable
        based on accumulated successive hits but resets when the player misses. The accumulator variable is multiplied
         with the amount of score that the player gets from the successful hit"""
        self.multAcc = 1
        if note == "hit":
            self.multAcc = self.multAcc + 1
        elif note == "miss":
            self.multAcc = 1

    def scoringFunc(self,note):
        """ This function updates a scoring variable based on how much multiplier the player has accumulated and
        whether the player gets a successful hit or not.
        A fail hit won't deduct any points, just no points would be given."""
        xtr = self.scoreLabel.cget("text")
        if note=="hit":
            self.multNum = self.multNum + 1
            xtrr= self.multNum * 300+int(xtr)

            self.scoreLabel["text"] = xtrr
            self.Combo["text"] = str(1 + self.multNum) + "x"

        elif note=="miss":
            self.multNum = 0
            self.Combo["text"] = str(1 + self.multNum) + "x"

    def Left(self, event):
        """ This checks what overlaps in the area where the left arrow is, if the player misses
                it returns 'miss'. Otherwise, it deletes the arrow and registers as a 'hit"""
        list = self.myCanvas.find_overlapping(100*self.scaling, 1000*self.scaling, 101*self.scaling, 1200*self.scaling)
        if len(list) >= 3:
            self.myCanvas.delete(list[2])
            self.multiplierFunc("hit")
            self.scoringFunc("hit")
        else:
            self.multiplierFunc("miss")
            self.scoringFunc("miss")

    def Right(self, event):
        """ This checks what overlaps in the area where the right arrow is, if the player misses
                        it returns 'miss'. Otherwise, it deletes the arrow and registers as a 'hit"""
        list = self.myCanvas.find_overlapping(700*self.scaling, 1000*self.scaling, 710*self.scaling, 1100*self.scaling)
        if len(list) >= 3:
            self.myCanvas.delete(list[2])
            if len(list) >= 3:
                self.myCanvas.delete(list[2])
                self.multiplierFunc("hit")
                self.scoringFunc("hit")
            else:
                self.multiplierFunc("miss")
                self.scoringFunc("miss")

    def Up(self, event):
        """ This checks what overlaps in the area where the up arrow is, if the player misses
                        it returns 'miss'. Otherwise, it deletes the arrow and registers as a 'hit"""
        list = self.myCanvas.find_overlapping(300*self.scaling, 1000*self.scaling, 310*self.scaling, 1100*self.scaling)
        if len(list) >= 3:
            self.myCanvas.delete(list[2])
            if len(list) >= 3:
                self.myCanvas.delete(list[2])
                self.multiplierFunc("hit")
                self.scoringFunc("hit")
            else:
                self.multiplierFunc("miss")
                self.scoringFunc("miss")

    def Down(self, event):
        """ This checks what overlaps in the area where the down arrow is, if the player misses
                it returns 'miss'. Otherwise, it deletes the arrow and registers as a 'hit"""
        list = self.myCanvas.find_overlapping(500*self.scaling, 1000*self.scaling, 510*self.scaling, 1100*self.scaling)
        if len(list) >= 3:
            self.myCanvas.delete(list[2])
            self.multiplierFunc("hit")
            self.scoringFunc("hit")
        else:
            self.multiplierFunc("miss")
            self.scoringFunc("miss")

    def quitCallback(self):
        """This is a callback method attached to the quit button.
        It destroys the main window, which ends the program"""
        self.mainWin.destroy()

# ------------------ Main program ----------------------

myGuiii= BasicGui3()
myGuiii.go()

