from psychopy import gui

class dialoguebox(object):
    def showDialogBox(self):
        Dlg = gui.Dlg(title="Navon Task", pos=(525, 250))
        Dlg.addField('Subject First Name')
        Dlg.addField('Subject Surname')
        Dlg.addField('Subject Number')
        Dlg.addField('Experiment Day', choices=['1', '2', '3'])
        Dlg.addField('Gender', choices=['Male', 'Female'])
        Dlg.addField('Age')
        Dlg.addField('Stimulation Site', choices=['R-PPC', 'L-PPC', 'CZ'])
        Dlg.addField('Session', choices=['1', '2'])
        Dlg.addField('Handedness', choices=['Right', 'Left'])
        ok_data = Dlg.show()

        subjectName = ok_data[0]
        subjectSurname = ok_data[1]
        subjectNumber = ok_data[2]
        dayNumber = ok_data[3]
        subjectGender = ok_data[4]
        subjectAge = ok_data[5]
        stimSite = ok_data[6]
        sessionNumber = ok_data[7]
        handedness = ok_data[8]

        subjectInfo = [subjectName, subjectSurname, subjectNumber, dayNumber, subjectGender, subjectAge,  stimSite, sessionNumber,
                       handedness]
        return subjectInfo

