#CS361 Project: Tyler Purcell
#Car log program to keep track of any and all maintenance done for a vehicle!


import PySimpleGUI as sg
from datetime import date
import webbrowser
import os.path

sg.theme('Dark Green 2') #Overall theme for GUI

#Each function has to access the GUI so the layout while not the same, has to be accessed each time

def initial_window():
    #First window users see when the application runs
    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Text(text="Hello! Welcome to My Maintenance Record Keeper!"), sg.Push()],
        [sg.Push(), sg.Text(text='Please click the button below to understand how this program works!'), sg.Push()],
        [sg.Push(), sg.Button('Understanding the Program!'), sg.Push()],
        [sg.Push(), sg.Button('Take me to the logger!'), sg.Push()],
        [sg.VPush()]
    ]

    window = sg.Window('Car Logger', layout, size=(500, 300))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Close Window':
            break
        print(values)
        
        if event == 'Understanding the Program!':
            understanding_program()

        if event == 'Take me to the logger!':
            window.close()
            maintenance_logger()

def understanding_program():
    #Help window function for the car logger
    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Text(text='Hello! Thank you for utilizing my program!', font='Arial 18'), sg.Push()],
        [sg.Push(), sg.Text(text='We will cover a few items that you will encounter!', font='Arial 14'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text(text='The first few items will be buttons!'), sg.Button('Click me to see what I can do!'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text('Bellow are examples of buttons that you might encounter! You can click each one to learn more about them.'), sg.Push()],
        [sg.Push(), sg.Button('Create New Car Log'), sg.Button('Add Maintenance'), sg.Button('Access Car Log'), sg.Button('Close Window'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text(text='When you are ready to start logging, click the button below!')],
        [sg.Push(), sg.Button('Take me to the logger!')]
    ]

    window = sg.Window('Help Window', layout, size=(800,400))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        print(values)
        
        if event == 'Take me to the logger!':
            window.close()
            maintenance_logger()

        if event == 'Click me to see what I can do!':
            button_help()
           
        if event == 'Create New Car Log':
            car_log_help()

        if event == 'Add Maintenance':
            maintenance_help()

        if event == 'Access Car Log':
            access_car_log()

        if event == 'Close Window':
            close_window()

    window.close()

def button_help():
    #What users see when they navigate to the button help
    button_intro = [
        [sg.VPush()],
        [sg.Push(), sg.Text(text='Buttons are cool! They will open new windows that increase the possibilites for this program!', font='Arial 13'), sg.Push()],
        [sg.Push(), sg.Text(text='If something gets too overwhelming, just click "Close Window" or click the red X in the top right corner', font='Arial 13'), sg.Push()],
        [sg.Push(), sg.Text(text='If a button closes a window for you, you don\'t need to worry! That means you no longer need that window!', font='Arial 13'), sg.Push()],
        [sg.Push(), sg.Text(text='When you are ready to explore the other features, click the Close Window Button below!', font='Arial 13'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Button('Close Window'), sg.Push()],
        [sg.VPush()]
    ]

    window = sg.Window('Buttons!', button_intro, size=(800, 400))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Close Window':
            break
    window.close()

def car_log_help():
    #Initial help window for the car logger
    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Text(text='Create a car log!', font='Arial 15'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text(text='When creating a new car log you will encounter Input Boxes.', font='Arial 13'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text(text='These input boxes will look like the following', font='Arial 13'), sg.Push()],
        [sg.Push(), sg.Input(), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text(text='The input boxes are where you will Input the data that is asked.', font='Arial 13'), sg.Push()],
        [sg.Push(), sg.Text('To do this, simply click in the box and start typing!', font='Arial 13'), sg.Push()],
        [sg.VPush()],
        [sg.VPush()],
        [sg.Push(), sg.Button('Back'), sg.Push()],
        [sg.VPush()]
    ]

    window = sg.Window('Car Log Help', layout, size=(800, 400))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Back':
            break
    window.close()

def maintenance_help():
    #How maintenance function of logger works
    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Text(text='When adding maintenance to a car log, you will encounter the following:', font='Arial 13'), sg.Push()],
        [sg.VPush()],
        [sg.VPush()],
        [sg.Push(), sg.Text(text='You will see input boxes', font='Arial 13'), sg.Push()],
        [sg.Push(), sg.Input(), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text(text='You will see buttons', font='Arial 13'), sg.Push()],
        [sg.Push(), sg.Button('I am a button!'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text(text='These items will allow you to input information that will be stored.', font='Arial 13'), sg.Push()],
        [sg.Push(), sg.Text(text='Buttons will either store the information or cancel it', font='Arial 13'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Button('Back')]
    ]

    window = sg.Window('Maintenance help', layout, size=(800,400))
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        if event == 'I am a button!':
            button_help()

        if event == 'Back':
            break
        window.close()
            

    window.close()

def access_car_log():
    #How to utilize the access log function
    database = open("database.txt", 'r')
    car_database = database.read()
    car_list = car_database.split('\n')

    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Text(text='When requesting access to a car log, you will see mulitple items.', font='Arial 13'), sg.Push()],
        [sg.VPush()],
        [sg.VPush()],
        [sg.Push(), sg.Text(text='You will have drop down boxes:', font='Arial 13'), sg.Push()],
        [sg.Push(), sg.Combo(size=(41), values=car_list), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text(text='You will see buttons', font='Arial 13'), sg.Push()],
        [sg.Push(), sg.Button('I am a button!'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text(text='These items will allow you to make a request to the microservice my partner has designed.', font='Arial 13'), sg.Push()],
        [sg.Push(), sg.Text(text='The microservice will then send information back, for it to be displayed!', font='Arial 13'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Button('Back')]
    ]

    window = sg.Window('Access Help', layout, size=(800,400))
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break

        if event == 'I am a button!':
            button_help()

        if event == 'Back':
            break
        window.close()

def close_window():
    #How the close window works for the application
    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Text(text='This is a simple button!', font='Arial 13'), sg.Push()],
        [sg.Push(), sg.Button('Close Window'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text(text='If you see this button, it will simply close the window you are in', font='Arial 13'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text(text='You can test it with the above button!', font='Arial 13'), sg.Push()],
        [sg.VPush()],
    ]

    window = sg.Window('Close Window', layout, size=(800,400))
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Close Window':
            break          
    window.close()


def maintenance_logger():
    #When accessing the logger, initial window for the logger
    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Text(text='Please choose an item below!', font='Arial 15'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Button("Edit Car Log"), sg.Push(), sg.Button('Create New Car Log'), sg.Push(), sg.Button("Add Maintenance"), sg.Push(), sg.Button('Access Car Log'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Button('Delete Car Log'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Button("Understanding the Logger"), sg.Push()],
        [sg.VPush()],
        [sg.VPush()],
        [sg.Push(), sg.Button("Close Application", button_color=('black on red'))]
    ]

    window = sg.Window("CS361 Product", layout, size=(500, 300))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close Window':
            break
        print(event, values)

        if event == 'Understanding the Logger':
            window.close()
            understanding_program()

        if event == 'Edit Car Log':
            edit_car_log()
            
        if event == 'Create New Car Log':
            new_car_log()

        if event == 'Add Maintenance':
            add_maintenance()

        if event == 'Delete Car Log':
            delete_car_log()

        if event == 'Access Car Log':
            access_log()

        if event == 'Close Application':
            exit()

    window.close()

def new_car_log():
    #Function to create a new car log
    layout = [
        [sg.Text(text='Please enter the year, Make, and Model of the new entry.')],
        [sg.Input()],
        [sg.Button("Create Entry"), sg.Button("Cancel Entry")]
    ]
    window = sg.Window('New Vehicle Entry', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel Entry':
            break
        print(event, values)

        if event == 'Create Entry':
            today = str(date.today())
            new_car = values[0]
            file_name = str(new_car).replace( ' ', '.') 
            print(file_name)
            if os.path.exists(file_name + '.txt') == True:
                sg.popup(title='Already Exists', custom_text='This Car Log Already Exists')
                if event == "This Car Log Already Exists":
                    window.close()
            else:
                car_log = open(file_name.lower() + ".txt", "x")
                with car_log:
                    car_log.write((str(new_car)) + " car log created! Date Created: " + today)
                    car_database = open("database.txt", "a")
                    car = str(file_name).replace('.', ' ')
                    with car_database:
                        car_database.write((str(car) + '\n'))
                sg.popup(title='New car log created!', custom_text='New Car log created')
                if event == "New Car log created!":
                    break
                window.close()
        
    window.close()

def edit_car_log():
    #Function to edit the car log
    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Text(text='This feature allows you to edit a car log if you need to.'), sg.Push()],
        [sg.VPush()],
        [sg.VPush()],
        [sg.Push(), sg.Text(text='Please note, that you are editing the file itself.'), sg.Push()],
        [sg.Push(), sg.Button('Edit a Car Log'), sg.Push(), sg.Button('Close Window'), sg.Push()],
        [sg.VPush()]
    ]
        

    window = sg.Window('Edit Car Log', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Close Window':
            break
        print(event, values)

        if event == "Edit a Car Log":
            edit_layout = [
                [sg.VPush()],
                [sg.Push(), sg.Text(text='Please enter the log you want to edit'), sg.Push()],
                [sg.VPush()],
                [sg.VPush()],
                [sg.Push(), sg.Input(), sg.Push()],
                [sg.Push(), sg.Button('Edit Log'), sg.Push()],
                [sg.VPush()],
                [sg.Push(), sg.Button('Cancel', button_color='black on red')]
            ]

            new_window = sg.Window('Proceed', edit_layout)
            while True:
                event, values = new_window.read()
                if event == sg.WINDOW_CLOSED or event == 'Cancel':
                    break
                if event == 'Edit Log':
                    find_car = values[0]
                    find_file = str(find_car).replace(' ', '.')
                    print(find_file)
                    if os.path.exists(find_file + '.txt') == False:
                        sg.popup(title='This Car Log does not exist', custom_text='This Car Log does not exist')
                        if event == "This Car Log does not exists":
                            break
                    if event == 'Close Window':
                        new_window.close()
                    else:
                        webbrowser.open(find_file.lower() + '.txt')
            new_window.close()
    window.close()


def delete_car_log():
    #Function to delete a specific car log

    database = open("database.txt", 'r')
    car_database = database.read()
    car_list = car_database.split('\n')
    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Text(text='Here you can select a car log to delete if you need to.', font='Arial 15'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text(text='This will delete the file in its entirety.', font='Arial 20'), sg.Push()],
        [sg.VPush()],
        [sg.Push(), sg.Text('Please select the Log to delete'), sg.Combo(size=(41), values=car_list), sg.Push()],
        [sg.Push(), sg.Button('Delete Car Log'), sg.Push(), sg.Button('Cancel'), sg.Push()],
        [sg.VPush()]
    ]
        

    window = sg.Window('Edit Car Log', layout, size=(800,400))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
            break
        print(event, values)

        if event == "Delete Car Log":
            value = values[0]
            delete_helper(value)
            sg.popup('Car log deleted')
            break

    window.close()

def delete_helper(value):
    #Helper function that passes in value for deleting the car log file and name from database

    layout = [
        [sg.VPush()],
        [sg.Push(), sg.Text('Do you wish to procede to delete the car log?', font='Arial 15'), sg.Push()],
        [sg.Push(), sg.Button('Yes I am sure'), sg.Push(), sg.Button('No! Cancel!'), sg.Push()],
        [sg.VPush()]
    ]

    window = sg.Window('Last Chance', layout, size=(800, 400))
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'No! Cancel!':
            break
        window.close()

        if event == 'Yes I am sure':
            file_delete = value
            file_name = str(file_delete).replace(' ', '.')
            if os.path.exists(file_name.lower() + '.txt') == False:
                sg.popup(title='The car log does not exist', custom_text='The car log does not exist')
                if event == 'The car log does not exist':
                    break
                window.close()
            else:
                os.remove(file_name.lower() + '.txt')
                with open('database.txt', 'r') as data:
                    new_data = data.readlines()
                with open('database.txt', 'w') as updated:
                    for line in new_data:
                        if line.strip('\n') != file_delete:
                            updated.write(line)
                break
            window.close()
    window.close()
def access_log():
    #Function for utilizing partners microservice

    database = open("database.txt", 'r')
    car_database = database.read()
    car_list = car_database.split('\n')

    layout = [
        [sg.Text(text='Here you can search for an existing car log!')],
        [sg.Text(text='To search for a log, simply select the Year, Make, and Model below!')],
        [sg.Combo(size=(41), values=car_list)], [sg.Button('Access Car Log')],
        [sg.Button('Close Window')]
    ]

    window = sg.Window('Access Log', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close Window':
            break
        window.close()

        if event == 'Access Car Log':
            data_file = open('data_file.txt', 'w')
            with data_file:
                data_file.write(str(values[0]))
                data_file.close()
                sg.popup("Car Found, gathering information")
                break          
    window.close()
                

def add_maintenance():
    #Function to add a maintenance event to the car log

    database = open("database.txt", 'r')
    car_database = database.read()
    car_list = car_database.split('\n')

    layout = [
        [sg.Text(text='Here you can add Maintenance Completed to Cars!')],
        [sg.Text(text='Select the Year, Make, and Model here!')], [sg.Combo(size=(41), values=car_list)],
        [sg.Text(text='Enter Maintenance Type here!')], [sg.Input()],
        [sg.Text(text='Enter Mileage here!')], [sg.Input()],
        [sg.Button('Add Item'), sg.Button('Close Window')]
    ]
    
    window = sg.Window('Add Maintenance', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close Window':
            break
        window.close()
            
        if event == 'Add Item':
            car_type = values[0]
            maintenance_type = values[1]
            mileage = values[2]
            car_log = str(car_type).replace(' ', '.')
            file_name = open(car_log +'.txt', 'a')
            with file_name:
                file_name.write('\n')
                file_name.write('Completed on: ' + str(date.today()) + '\n')
                file_name.write('Maintenance Type: ' + str(maintenance_type) + '\n')
                file_name.write('Mileage Performed at: ' + str(mileage) + '\n')
                sg.popup(custom_text='Maintenance Record Added!')
                break
    window.close()
        
                


if __name__ == '__main__':
    initial_window()