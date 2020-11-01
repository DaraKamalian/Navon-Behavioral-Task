from psychopy import gui, visual
from Window import window
import Config
win = window.win
class dialoguebox(object):
    def showDialogBox(self):
        subjectInfo = []
        flag = True
        while flag:
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
            if Dlg.OK:
                if Config.validateFields(ok_data):
                    for i in range(0, 9):
                        subjectInfo.append(ok_data[i])
                    flag = False
        return subjectInfo