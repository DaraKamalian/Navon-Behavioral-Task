
from DialogueBox import dialoguebox
from EndMessage import EndMessage
import Config, datetime, glob, os
from psychopy import core, event


from Global import Global
from Local import Local

event.globalKeys.clear()
event.globalKeys.add(key='q', func=os._exit, func_args=[1], func_kwargs=None)

for filename in glob.glob('./*.csv'):
    os.remove(filename)
subjectInfo = dialoguebox().showDialogBox()
Config.filename = subjectInfo[0] + '.' + subjectInfo[1] + '.D' + subjectInfo[3] + '.S' + subjectInfo[7] + '.csv'
Config.createFile(Config.filename)

if int(subjectInfo[2]) % 6 == 0:
    for index in range(1, 3):
        Global().Global()
        Local().Local()

if int(subjectInfo[2]) % 6 == 1:

    Global().Global()
    for index in range(1, 3):
        Local().Local()
    Global().Global()

if int(subjectInfo[2]) % 6 == 2:

    Local().Local()
    for index in range(1, 3):
        Global().Global()
    Local().Local()

if int(subjectInfo[2]) % 6 == 3:
    for index in range(1, 3):
        Local().Local()
    for index in range(1, 3):
        Global().Global()

if int(subjectInfo[2]) % 6 == 4:
    for index in range(1, 3):
        Global().Global()
    for index in range(1, 3):
        Local().Local()

if int(subjectInfo[2]) % 6 == 5:
    for index in range(1, 3):
        Local().Local()
        Global().Global()
print('here')
Config.append_list_as_row(Config.filename, ['Subject Name: ' + str(subjectInfo[0]) + ' ' + str(subjectInfo[1]),
                                            'Subject Number: ' + str(subjectInfo[2]),
                                            'Age: ' + str(subjectInfo[6]), 'Gender: ' + str(subjectInfo[5]),
                                            'Handedness: ' + str(subjectInfo[8]),
                                            'Stimulation Site: ' + str(subjectInfo[7]),
                                            'Session: ' + str(subjectInfo[8]),
                                            'Datetime: ' + str(datetime.datetime.today())])

Config.convertToExcel()
for filename in glob.glob('./*.csv'):
    os.remove(filename)
EndMessage().displayEndMessage()
core.quit()





