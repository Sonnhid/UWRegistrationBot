import PySimpleGUI as sg
import getWeb 

class botGUI:

    def layout():
        #row 1 of layout
        login = [[sg.Text("UW ID")],
                [sg.Input()],
                [sg.Text("Passward")],
                [sg.Input()]]
        about =[[sg.Text("UW Regisration Bot")],
                [sg.Text("Thank you for using the bot")]]
        userinput = [[sg.Frame('User Info', login)]]

        #row 2 of layout
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

        
        submission = [[sg.Text('Registration Time (hour:minute:second)')],
                    [sg.Input(size =15)],
                    [sg.Button('Run')]]
        submission_frame =[[sg.Frame('Submission',submission,element_justification='right')]]

        row1 =[[sg.Column(userinput),sg.Column(about)]]
        row2 =[[sg.Column(class_frame),
                sg.Column(submission_frame,vertical_alignment='bottom', element_justification='right' )]]

        layout = [[row1],[row2]]
        return sg.Window("UW Registration Bot",layout)

    def window(self):
        # Create the window
        window = botGUI.layout()

        # Create an event loop
        while True:
            event, values = window.read()
            print(values)
            getWeb.getData(values)
            # End program if user closes window or
            # presses the OK button
            if event == sg.WIN_CLOSED:
                break
        

        window.close()
 