import PySimpleGUI as sg
import getWeb 
import datetime
#bot GUI is the GUI for the program and gathers all the user input
class botGUI:
    #layout of the window
    def layout():
        sg.theme('Dark Purple 3')
        #User login and about program section
        login = [[sg.Text("UW ID")],
                [sg.Input(size =30)],
                [sg.Text("Passward")],
                [sg.Input(size =30)]]
        about =[[sg.Text("UW Regisration Bot\nby Sonnhi Duong\nIt will be appreciated if star my repo")],
                [sg.Text("Thank you for using the bot\nMake sure that all information \nis correct before submitting\nNot doing so, the bot will \nnot execute ")]]
        userinput = [[sg.Frame('User Info', login)]]

        #Class information 
        class_code=[[sg.Text("SLN Code")],[sg.Input(size = 6)],[sg.Input(size = 6)],[sg.Input(size = 6)],
                [sg.Input(size = 6)],[sg.Input(size = 6)] ,[sg.Input(size = 6)] ,
                [sg.Input(size = 6)],[sg.Input(size = 6)]]

        add_code=[[sg.Text("Add Code")],[sg.Input(size = 6)],[sg.Input(size = 6)],[sg.Input(size = 6)],
                [sg.Input(size = 6)],[sg.Input(size = 6)] ,[sg.Input(size = 6)] ,
                [sg.Input(size = 6)],[sg.Input(size = 6)]]
        
        credits_num=[[sg.Text("Credits")],[sg.Input(size = 6)],[sg.Input(size = 6)],[sg.Input(size = 6)],
                [sg.Input(size = 6)],[sg.Input(size = 6)] ,[sg.Input(size = 6)] ,
                [sg.Input(size = 6)],[sg.Input(size = 6)]]
        class_option = [[sg.Column(class_code),sg.Column(add_code),sg.Column(credits_num)]]
        class_frame =[[sg.Frame('Class Info',class_option)]]

        #Drop down menu for registration time
        hours =['1','2','3','4','5','6','7','8','9','10','11','12']
        min =[]
        i =1
        while i< 60:
                min.append(i)
                i+=1
        min.append('00')
        dropdown_time = [sg.DropDown(hours),
                        sg.Text(":"),sg.DropDown(min),
                        sg.DropDown(['am','pm']),
                        sg.Text("     ")]

        submission = [[sg.Text('Registration Time (hour:minute)')],
                        dropdown_time,
                        [sg.Button('Run')]]
        submission_frame =[[sg.Frame('Submission',submission,element_justification='right')]]

        #Adding all the GUI components together
        row1 =[[sg.Column(userinput),sg.Column(about)]]
        row2 =[[sg.Column(class_frame),
                sg.Column(submission_frame,vertical_alignment='bottom', element_justification='right' )]]

        layout = [[row1],[row2]]
        return sg.Window("UW Registration Bot",layout)
    
    #Checks to see when to run the program
    #This will run one minute before registration time
    def runningState(window:any,value:any): 
            if value[28] == "pm":
                    hourInput = int(value[26])+12
            else:
                    hourInput = int(value[26])
            if value[27] == "00":
                    minInput = 59
            elif value[27] == '1':
                    minInput = 0
            else:
                    minInput = int(value[27])-1
                        
            while True:
                    window.close()
                    t = datetime.datetime.now()
                    #When it is one minute before, it will open up the browser ib
                    #The getWeb class
                    if ((t.hour == hourInput)and(t.minute == minInput)):
                            getWeb.getData(value) 

    #Creates the window and calls the runningState
    def window(self):
        # Create the window
        window = botGUI.layout()

        # Create an event loop
        while True:
            event, values = window.read()
            if event == 'Run':
                    botGUI.runningState(window,values)
            elif event == sg.WIN_CLOSED:
                break
        

        window.close()
 