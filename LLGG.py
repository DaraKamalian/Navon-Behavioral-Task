from psychopy import core, event
import random
import xlsxwriter
import datetime
import os

from ImageStims import Images
from Window import window
from EndMessage import EndMessage

window = window()
win = window.win

images = Images()
imageHH = images.imageHH
imageHS = images.imageHS
imageSH = images.imageSH
imageSS = images.imageSS
imageStims = [imageHS, imageSH, imageHH, imageSS]

globalFirstInstructionImage = images.globalFirstInstructionImage
instructionImage2 = images.instructionImage2
globalSecondInstructionImage = images.globalSecondInstructionImage
localFirstInstructionImage = images.localFirstInstructionImage
localSecondInstructionImage = images.localSecondInstructionImage
fixationPoint = images.fixationPoint
questionMark = images.questionMark
correct = images.correct
wrong = images.wrong
exitIcon = images.exitIcon

Headers = ['ImageFile', 'Congruency', 'Visual Field', 'Block', 'Trial', 'Key-Resp', 'Cor-Ans', 'Accuracy', 'R-time',
           'Trial-Start', 'Key-Resp-Start']

Cells = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

positions = [(166.75, 75), (-60, 301.77), (-286.77, 75), (-60, -151.77)]

event.globalKeys.clear()
event.globalKeys.add(key='q', func=os._exit, func_args=[1], func_kwargs=None)

class LLGG(object):
    def LLGGtask(self, subjectInfoList):
        workbook = xlsxwriter.Workbook(
            str(subjectInfoList[0]) + 'S' + str(subjectInfoList[6] + 'D' + str(subjectInfoList[2]) + '.xlsx')
        )

        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Subject Name: ' + str(subjectInfoList[0]))
        worksheet.write('B1', 'Subject Number: ' + str(subjectInfoList[1]))
        worksheet.write('C1', 'Subject Age: ' + str(subjectInfoList[4]))
        worksheet.write('D1', 'Subject Gender: ' + str(subjectInfoList[3]))
        worksheet.write('E1', 'Subject Number: ' + str(subjectInfoList[1]))
        worksheet.write('F1', 'Subject Handedness: ' + str(subjectInfoList[7]))
        worksheet.write('G1', 'Stimulation Site: ' + str(subjectInfoList[5]))
        worksheet.write('H1', 'Experiment Session: ' + str(subjectInfoList[6]))
        worksheet.write('I1', 'Experiment Day: ' + str(subjectInfoList[2]))
        worksheet.write('J1', 'Datetime: ' + str(datetime.datetime.today()))

        HeaderFormat = workbook.add_format({
            'bold': True,
            'text_wrap': False,
            'valign': 'top',
            'fg_color': '#D7E4BC',
            'border': 1})

        for i in range(0, 11):
            worksheet.write(Cells[i] + '2', Headers[i], HeaderFormat)
        
        trialstart = 0
        
        generalTimer = core.getTime()

        for index1 in range(1, 3):
            # Local instruction
            localFirstInstructionImage.draw()
            win.flip()
            flag1 = True
            while flag1:
                keys = event.waitKeys(keyList=['m'])
                for key in keys:
                    if key[0] == 'm':
                        localFirstInstructionImage.autoDraw = False
                        instructionImage2.draw()
                        win.flip()
                        flag1 = False

            flag2 = True
            while flag2:
                keys = event.waitKeys(keyList=['m'])
                for key in keys:
                    if key[0] == 'm':
                        instructionImage2.autoDraw = False
                        win.flip()

                        i_counter = 0
                        c_counter = 0
                        # Local Practice
                        rightShown = False
                        leftShown = False
                        downShown = False
                        upShown = False
                        for index in range(1, 5):
                            rand1 = random.randint(0, 3)
                            rand2 = 3 - rand1

                            fixationPoint.draw()
                            win.flip()
                            core.wait(1)

                            fixationPoint.autoDraw = False
                            ltypeRandom = random.randint(0, 1)
                            # 0 -> congruent
                            # 1 -> incongruent

                            locationRand = random.randint(0, 3)

                            if locationRand == 0 and rightShown:
                                locationRand = 1
                            if locationRand == 1 and leftShown:
                                locationRand = 2
                            if locationRand == 2 and upShown:
                                locationRand = 3
                            if locationRand == 3 and downShown:
                                if not rightShown:
                                    locationRand = 0
                                elif not leftShown:
                                    locationRand = 1
                                elif not upShown:
                                    locationRand = 2
                            print('locations is :' + str(locationRand))

                            if locationRand == 0:
                                rightShown = True
                            if locationRand == 1:
                                leftShown = True
                            if locationRand == 2:
                                upShown = True
                            if locationRand == 3:
                                downShown = True

                            if ltypeRandom == 0 and c_counter == 2:
                                ltypeRandom = 1
                            if ltypeRandom == 1 and i_counter == 2:
                                ltypeRandom = 0

                            if ltypeRandom == 0 and (rand1 == 2 or rand1 == 3):
                                imageStims[rand1].setPos(positions[locationRand])
                                imageStims[rand1].draw()
                                win.flip()
                                core.wait(0.3)
                                c_counter += 1

                            if ltypeRandom == 0 and (rand1 == 0 or rand1 == 1):
                                imageStims[rand2].setPos(positions[locationRand])
                                imageStims[rand2].draw()
                                win.flip()
                                core.wait(0.3)
                                c_counter += 1

                            if ltypeRandom == 1 and (rand1 == 0 or rand1 == 1):
                                imageStims[rand1].setPos(positions[locationRand])
                                imageStims[rand1].draw()
                                win.flip()
                                core.wait(0.3)
                                i_counter += 1

                            if ltypeRandom == 1 and (rand1 == 2 or rand1 == 3):
                                imageStims[rand2].setPos(positions[locationRand])
                                imageStims[rand2].draw()
                                win.flip()
                                core.wait(0.3)
                                i_counter += 1

                            imageStims[rand1].autoDraw = False
                            imageStims[rand2].autoDraw = False
                            questionMark.draw()
                            testTimer1 = core.CountdownTimer(4)
                            win.flip()

                            flag = True
                            while flag:
                                keys = event.waitKeys(keyList=['1', '2', 'end', 'down'], maxWait=4)
                                if keys:
                                    if ltypeRandom == 0 and (rand1 == 1 or rand1 == 2):
                                        if keys[0] == '1' or keys[0] == 'end':
                                            correct.draw()
                                            win.flip()
                                            core.wait(2)
                                        else:
                                            wrong.draw()

                                            win.flip()
                                            core.wait(2)

                                    if ltypeRandom == 0 and (rand1 == 0 or rand1 == 3):
                                        if keys[0] == '2' or keys[0] == 'down':
                                            correct.draw()
                                            win.flip()
                                            core.wait(2)
                                        else:
                                            wrong.draw()
                                            win.flip()
                                            core.wait(2)

                                    if ltypeRandom == 1 and (rand1 == 0 or rand1 == 3):
                                        if keys[0] == '2' or keys[0] == 'down':
                                            correct.draw()
                                            win.flip()
                                            core.wait(2)
                                        else:
                                            wrong.draw()
                                            win.flip()
                                            core.wait(2)

                                    if ltypeRandom == 1 and (rand1 == 1 or rand1 == 2):
                                        if keys[0] == '1' or keys[0] == 'end':
                                            correct.draw()
                                            win.flip()
                                            core.wait(2)
                                        else:
                                            wrong.draw()
                                            win.flip()
                                            core.wait(2)
                                    flag = False
                                elif testTimer1.getTime() <= 0:
                                    wrong.draw()
                                    win.flip()
                                    core.wait(2)
                                    flag = False
                        flag2 = False

            localSecondInstructionImage.draw()
            time1 = core.getTime()
            win.flip()
            flag3 = True
            while flag3:
                keys = event.waitKeys(keyList=['m'])
                for key in keys:
                    if key[0] == 'm':
                        localSecondInstructionImage.autoDraw = False
                        win.flip()
                        main_i_counter = 0
                        main_c_counter = 0

                        # Local Main task
                        rightShown = False
                        leftShown = False
                        downShown = False
                        upShown = False
                        for index in range(1, 5):
                            if index1 == 2:
                                index += 4
                            worksheet.write('E' + str(index + 2), str(index))
                            worksheet.write('D' + str(index + 2), '0')


                            rand1 = random.randint(0, 3)
                            rand2 = 3 - rand1

                            locationRand = random.randint(0, 3)

                            if locationRand == 0 and rightShown:
                                locationRand = 1
                            if locationRand == 1 and leftShown:
                                locationRand = 2
                            if locationRand == 2 and upShown:
                                locationRand = 3
                            if locationRand == 3 and downShown:
                                if not rightShown:
                                    locationRand = 0
                                elif not leftShown:
                                    locationRand = 1
                                elif not upShown:
                                    locationRand = 2
                            print('locations is :' + str(locationRand))

                            if locationRand == 0:
                                rightShown = True
                                worksheet.write('C' + str(index + 2), 'Right')
                            if locationRand == 1:
                                leftShown = True
                                worksheet.write('C' + str(index + 2), 'Left')
                            if locationRand == 2:
                                upShown = True
                                worksheet.write('C' + str(index + 2), 'Up')
                            if locationRand == 3:
                                downShown = True
                                worksheet.write('C' + str(index + 2), 'Down')

                            globalSecondInstructionImage.autoDraw = False
                            fixationPoint.draw()
                            localTimer = core.getTime()

                            win.flip()
                            core.wait(1)

                            fixationPoint.autoDraw = False
                            trialstart = localTimer - generalTimer
                            worksheet.write('J' + str(index + 2), str(trialstart))

                            maintypeRandom = random.randint(0, 1)
                            # 0 -> congruent
                            # 1 -> incongruent
                            if maintypeRandom == 0 and main_c_counter == 2:
                                maintypeRandom = 1
                            if maintypeRandom == 1 and main_i_counter == 2:
                                maintypeRandom = 0

                            if maintypeRandom == 0 and (rand1 == 2 or rand1 == 3):
                                worksheet.write('B' + str(index + 2), '1')

                                imageStims[rand1].setPos(positions[locationRand])
                                imageStims[rand1].draw()

                                win.flip()

                                core.wait(0.3)
                                main_c_counter += 1
                                if rand1 == 2:
                                    worksheet.write('A' + str(index + 2), 'ex1')
                                    worksheet.write('G' + str(index + 2), '1')

                                else:
                                    worksheet.write('A' + str(index + 2), 'ex4')
                                    worksheet.write('G' + str(index + 2), '2')

                            if maintypeRandom == 0 and (rand1 == 0 or rand1 == 1):
                                worksheet.write('B' + str(index + 2), '1')

                                imageStims[rand2].setPos(positions[locationRand])
                                imageStims[rand2].draw()

                                win.flip()

                                core.wait(0.3)
                                main_c_counter += 1
                                if rand1 == 0:
                                    worksheet.write('A' + str(index + 2), 'ex4')
                                    worksheet.write('G' + str(index + 2), '2')

                                else:
                                    worksheet.write('A' + str(index + 2), 'ex1')
                                    worksheet.write('G' + str(index + 2), '1')

                            if maintypeRandom == 1 and (rand1 == 0 or rand1 == 1):
                                worksheet.write('B' + str(index + 2), '0')

                                imageStims[rand1].setPos(positions[locationRand])
                                imageStims[rand1].draw()

                                win.flip()

                                core.wait(0.3)
                                main_i_counter += 1
                                if rand1 == 0:
                                    worksheet.write('A' + str(index + 2), 'ex3')
                                    worksheet.write('G' + str(index + 2), '2')

                                else:
                                    worksheet.write('A' + str(index + 2), 'ex2')
                                    worksheet.write('G' + str(index + 2), '1')

                            if maintypeRandom == 1 and (rand1 == 2 or rand1 == 3):
                                worksheet.write('B' + str(index + 2), '0')

                                imageStims[rand2].setPos(positions[locationRand])
                                imageStims[rand2].draw()

                                win.flip()

                                core.wait(0.3)
                                main_i_counter += 1
                                if rand1 == 2:
                                    worksheet.write('A' + str(index + 2), 'ex2')
                                    worksheet.write('G' + str(index + 2), '1')

                                else:
                                    worksheet.write('A' + str(index + 2), 'ex3')
                                    worksheet.write('G' + str(index + 2), '2')

                            imageStims[rand1].autoDraw = False
                            imageStims[rand2].autoDraw = False
                            questionMark.draw()

                            win.flip()

                            counter = core.CountdownTimer(4)

                            flag = True
                            while flag:
                                keys = event.waitKeys(keyList=['1', '2', 'end', 'down'], maxWait=4)
                                if keys:
                                    for key in keys:
                                        if key == '1' or key == 'end':
                                            worksheet.write('F' + str(index + 2), '1')
                                        if key == '2' or key == 'down':
                                            worksheet.write('F' + str(index + 2), '2')

                                        worksheet.write('H' + str(index + 2), '=IF(G' + str(index + 2) + '= F' +
                                                        str(index + 2) + ',1,0)')
                                        worksheet.write('I' + str(index + 2), str(4 - counter.getTime() + 0.3))
                                        worksheet.write('K' + str(index + 2),
                                                        str(4 - counter.getTime() + 0.3 + trialstart + 1))

                                        flag = False

                                elif counter.getTime() <= 0:
                                    worksheet.write('F' + str(index + 2), 'None')
                                    worksheet.write('I' + str(index + 2), 'None')
                                    worksheet.write('K' + str(index + 2), 'None')
                                    worksheet.write('H' + str(index + 2), 'None')
                                    flag = False
                        flag3 = False

            questionMark.autoDraw = False
            win.flip()

        for index2 in range(1, 3):
            # Global Instruction
            globalFirstInstructionImage.draw()
            win.flip()
            flag = True
            while flag:
                keys = event.waitKeys(keyList=['m'])
                for key in keys:
                    if key[0] == 'm':
                        globalFirstInstructionImage.autoDraw = False
                        instructionImage2.draw()
                        win.flip()
                        flag = False

            temp = True
            while temp:
                keys = event.waitKeys(keyList=['m'])
                for key in keys:
                    if key[0] == 'm':
                        instructionImage2.autoDraw = False
                        win.flip()

                        c_counter = 0
                        i_counter = 0
                        # Global Practice
                        rightShown = False
                        leftShown = False
                        downShown = False
                        upShown = False
                        for j in range(1, 5):
                            rand1 = random.randrange(0, 3)
                            rand2 = 3 - rand1
                            print(rand1)
                            print(rand2)

                            instructionImage2.autoDraw = False
                            fixationPoint.draw()
                            win.flip()
                            core.wait(1)

                            fixationPoint.autoDraw = False

                            gtypeRandom = random.randint(0, 1)
                            # 0 -> congruent
                            # 1 -> incongruent

                            locationRand = random.randint(0, 3)

                            if locationRand == 0 and rightShown:
                                locationRand = 1
                            if locationRand == 1 and leftShown:
                                locationRand = 2
                            if locationRand == 2 and upShown:
                                locationRand = 3
                            if locationRand == 3 and downShown:
                                if not rightShown:
                                    locationRand = 0
                                elif not leftShown:
                                    locationRand = 1
                                elif not upShown:
                                    locationRand = 2
                            print('locations is :' + str(locationRand))

                            if locationRand == 0:
                                rightShown = True
                            if locationRand == 1:
                                leftShown = True
                            if locationRand == 2:
                                upShown = True
                            if locationRand == 3:
                                downShown = True

                            if gtypeRandom == 0 and c_counter == 2:
                                gtypeRandom = 1

                            if gtypeRandom == 1 and i_counter == 2:
                                gtypeRandom = 0

                            if gtypeRandom == 0 and (rand1 == 2 or rand1 == 3):
                                imageStims[rand1].setPos(positions[locationRand])
                                imageStims[rand1].draw()

                                win.flip()
                                core.wait(0.3)
                                c_counter += 1

                            if gtypeRandom == 0 and (rand1 == 0 or rand1 == 1):
                                imageStims[rand2].setPos(positions[locationRand])
                                imageStims[rand2].draw()
                                win.flip()
                                core.wait(0.3)
                                c_counter += 1

                            if gtypeRandom == 1 and (rand1 == 0 or rand1 == 1):
                                imageStims[rand1].setPos(positions[locationRand])
                                imageStims[rand1].draw()
                                win.flip()
                                core.wait(0.3)
                                i_counter += 1

                            if gtypeRandom == 1 and (rand1 == 2 or rand1 == 3):
                                imageStims[rand2].setPos(positions[locationRand])
                                imageStims[rand2].draw()
                                win.flip()
                                core.wait(0.3)
                                i_counter += 1

                            imageStims[rand1].autoDraw = False
                            imageStims[rand2].autoDraw = False
                            questionMark.draw()
                            win.flip()

                            testTimer = core.CountdownTimer(4)
                            flag = True
                            while flag:
                                keys = event.waitKeys(keyList=['1', '2', 'end', 'down'], maxWait=4)
                                if keys:

                                    if gtypeRandom == 0 and (rand1 == 1 or rand1 == 2):
                                        if keys[0] == '1' or keys[0] == 'end':
                                            correct.draw()
                                            win.flip()
                                            core.wait(2)
                                        else:
                                            wrong.draw()
                                            win.flip()
                                            core.wait(2)

                                    if gtypeRandom == 0 and (rand1 == 0 or rand1 == 3):
                                        if keys[0] == '2' or keys[0] == 'down':
                                            correct.draw()
                                            win.flip()
                                            core.wait(2)
                                        else:
                                            wrong.draw()
                                            win.flip()
                                            core.wait(2)

                                    if gtypeRandom == 1 and (rand1 == 0 or rand1 == 3):
                                        if keys[0] == '1' or keys[0] == 'end':
                                            correct.draw()
                                            win.flip()
                                            core.wait(2)
                                        else:
                                            wrong.draw()
                                            win.flip()
                                            core.wait(2)

                                    if gtypeRandom == 1 and (rand1 == 1 or rand1 == 2):
                                        if keys[0] == '2' or keys[0] == 'down':
                                            correct.draw()
                                            win.flip()
                                            core.wait(2)
                                        else:
                                            wrong.draw()
                                            win.flip()
                                            core.wait(2)

                                    flag = False
                                elif testTimer.getTime() <= 0:
                                    wrong.draw()
                                    win.flip()
                                    core.wait(2)
                                    flag = False

                        temp = False

            globalSecondInstructionImage.draw()
            win.flip()

            temp1 = True
            while temp1:
                keys = event.waitKeys(keyList=['m'])
                for key in keys:
                    if key[0] == 'm':
                        globalSecondInstructionImage.autoDraw = False
                        win.flip()

                        main_i_counter = 0
                        main_c_counter = 0

                        # Global main task
                        rightShown = False
                        leftShown = False
                        downShown = False
                        upShown = False
                        for index in range(1, 5):
                            if index2 == 1:
                                index += 8
                            if index2 == 2:
                                index += 12
                            worksheet.write('E' + str(index + 2), str(index))
                            worksheet.write('D' + str(index + 2), '1')

                            rand1 = random.randint(0, 3)
                            rand2 = 3 - rand1

                            locationRand = random.randint(0, 3)

                            if locationRand == 0 and rightShown:
                                locationRand = 1
                            if locationRand == 1 and leftShown:
                                locationRand = 2
                            if locationRand == 2 and upShown:
                                locationRand = 3
                            if locationRand == 3 and downShown:
                                if not rightShown:
                                    locationRand = 0
                                elif not leftShown:
                                    locationRand = 1
                                elif not upShown:
                                    locationRand = 2
                            print('locations is :' + str(locationRand))

                            if locationRand == 0:
                                rightShown = True
                                worksheet.write('C' + str(index + 2), 'Right')
                            if locationRand == 1:
                                leftShown = True
                                worksheet.write('C' + str(index + 2), 'Left')
                            if locationRand == 2:
                                upShown = True
                                worksheet.write('C' + str(index + 2), 'Up')
                            if locationRand == 3:
                                downShown = True
                                worksheet.write('C' + str(index + 2), 'Down')

                            globalSecondInstructionImage.autoDraw = False
                            fixationPoint.draw()
                            globalTimer = core.getTime()

                            win.flip()
                            core.wait(1)

                            fixationPoint.autoDraw = False

                            trialstart = globalTimer - generalTimer
                            worksheet.write('J' + str(index + 2), str(trialstart))

                            maintypeRandom = random.randint(0, 1)
                            # 0 -> congruent
                            # 1 -> incongruent

                            if maintypeRandom == 0 and main_c_counter == 2:
                                maintypeRandom = 1
                            if maintypeRandom == 1 and main_i_counter == 2:
                                maintypeRandom = 0

                            if maintypeRandom == 0 and (rand1 == 2 or rand1 == 3):
                                worksheet.write('B' + str(index + 2), '1')

                                imageStims[rand1].setPos(positions[locationRand])
                                imageStims[rand1].draw()
                                win.flip()
                                core.wait(0.3)
                                main_c_counter += 1
                                if rand1 == 2:
                                    worksheet.write('A' + str(index + 2), 'ex1')
                                    worksheet.write('G' + str(index + 2), '1')
                                else:
                                    worksheet.write('A' + str(index + 2), 'ex4')
                                    worksheet.write('G' + str(index + 2), '2')

                            if maintypeRandom == 0 and (rand1 == 0 or rand1 == 1):
                                worksheet.write('B' + str(index + 2), '1')

                                imageStims[rand2].setPos(positions[locationRand])
                                imageStims[rand2].draw()
                                win.flip()

                                core.wait(0.3)
                                main_c_counter += 1
                                if rand1 == 0:
                                    worksheet.write('A' + str(index + 2), 'ex4')
                                    worksheet.write('G' + str(index + 2), '2')

                                else:
                                    worksheet.write('A' + str(index + 2), 'ex1')
                                    worksheet.write('G' + str(index + 2), '1')

                            if maintypeRandom == 1 and (rand1 == 0 or rand1 == 1):
                                worksheet.write('B' + str(index + 2), '0')

                                imageStims[rand1].setPos(positions[locationRand])
                                imageStims[rand1].draw()
                                win.flip()

                                core.wait(0.3)
                                main_i_counter += 1
                                if rand1 == 0:
                                    worksheet.write('A' + str(index + 2), 'ex3')
                                    worksheet.write('G' + str(index + 2), '1')

                                else:
                                    worksheet.write('A' + str(index + 2), 'ex2')
                                    worksheet.write('G' + str(index + 2), '2')

                            if maintypeRandom == 1 and (rand1 == 2 or rand1 == 3):
                                worksheet.write('B' + str(index + 2), '0')

                                imageStims[rand2].setPos(positions[locationRand])
                                imageStims[rand2].draw()
                                win.flip()

                                core.wait(0.3)
                                main_i_counter += 1
                                if rand1 == 2:
                                    worksheet.write('A' + str(index + 2), 'ex2')
                                    worksheet.write('G' + str(index + 2), '2')

                                else:
                                    worksheet.write('A' + str(index + 2), 'ex3')
                                    worksheet.write('G' + str(index + 2), '1')

                            imageStims[rand1].autoDraw = False
                            imageStims[rand2].autoDraw = False

                            questionMark.draw()
                            win.flip()
                            counter = core.CountdownTimer(4)
                            flag = True
                            while flag:
                                keys = event.waitKeys(keyList=['1', '2', 'end', 'down'], maxWait=4)
                                if keys:
                                    for key in keys:
                                        if key == '1' or key == 'end':
                                            worksheet.write('F' + str(index + 2), '1')
                                        if key == '2' or key == 'down':
                                            worksheet.write('F' + str(index + 2), '2')

                                        worksheet.write('H' + str(index + 2), '=IF(G' + str(index + 2) + '= F' +
                                                        str(index + 2) + ',1,0)')
                                        worksheet.write('I' + str(index + 2), str(4 - counter.getTime() + 0.3))
                                        worksheet.write('K' + str(index + 2),
                                                        str(4 - counter.getTime() + 0.3 + trialstart + 1))

                                        flag = False

                                elif counter.getTime() <= 0:
                                    worksheet.write('F' + str(index + 2), 'None')
                                    worksheet.write('I' + str(index + 2), 'None')
                                    worksheet.write('K' + str(index + 2), 'None')
                                    worksheet.write('H' + str(index + 2), 'None')
                                    flag = False

                            temp1 = False
            questionMark.autoDraw = False
            win.flip()

        EndMessage().displayEndMessage()
        workbook.close()
        core.quit()