from psychopy import core, event
from ImageStims import Images
from Window import window
import random, Config

win = window.win
images = Images()
imageHH = images.imageHH
imageHS = images.imageHS
imageSH = images.imageSH
imageSS = images.imageSS
imageStims = [imageHS, imageSH, imageHH, imageSS]

globalFirstInstructionImage = images.globalFirstInstructionImage
globalSecondInstructionImage = images.globalSecondInstructionImage
instructionImage2 = images.instructionImage2

fixationPoint = images.fixationPoint
questionMark = images.questionMark
correct = images.correct
wrong = images.wrong

positions = [(166.75, 75), (-286.77, 75), (-60, 301.77), (-60, -151.77)]


class Global(object):
    def Global(self):

        imagefile = ''
        congruency = ''
        rtime = 0
        visualfield = ''
        keyrespstart = 0
        anslist = []
        corans = ''
        isLate = False
        accuracy = 0


        generalTimer = core.getTime()

        # globalFirstInstructionImage.draw()
        # win.flip()
        # flag = True
        # while flag:
        #     keys = event.getKeys(keyList=['m'])
        #     for key in keys:
        #         if key[0] == 'm':
        #             globalFirstInstructionImage.autoDraw = False
        #             instructionImage2.draw()
        #             win.flip()
        #             flag = False
        #
        # temp = True
        # # Global Practice Task
        # while temp:
        #     keys = event.getKeys(keyList=['m'])
        #     for key in keys:
        #         if key[0] == 'm':
        #             instructionImage2.autoDraw = False
        #             win.flip()
        #
        #             c_counter = 0
        #             i_counter = 0
        #
        #             # Global Practice
        #             rightcounter = 0
        #             leftcounter = 0
        #             downcounter = 0
        #             upcounter = 0
        #
        #             for j in range(1, 17):
        #                 rand1 = random.randrange(0, 3)
        #                 rand2 = 3 - rand1
        #                 print(rand1)
        #                 print(rand2)
        #
        #                 instructionImage2.autoDraw = False
        #                 fixationPoint.draw()
        #                 win.flip()
        #                 core.wait(1)
        #
        #                 fixationPoint.autoDraw = False
        #
        #                 gtypeRandom = random.randint(0, 1)
        #                 # 0 -> congruent
        #                 # 1 -> incongruent
        #
        #                 locationRand = random.randint(0, 3)
        #
        #                 if locationRand == 0 and rightcounter == 4:
        #                     locationRand = 1
        #                 if locationRand == 1 and leftcounter == 4:
        #                     locationRand = 2
        #                 if locationRand == 2 and upcounter == 4:
        #                     locationRand = 3
        #                 if locationRand == 3 and downcounter == 4:
        #
        #                     if rightcounter < 4:
        #                         locationRand = 0
        #
        #                     elif leftcounter < 4:
        #                         locationRand = 1
        #
        #                     elif not upcounter < 4:
        #                         locationRand = 2
        #
        #                 print('locations is :' + str(locationRand))
        #
        #                 if locationRand == 0:
        #                     rightcounter += 1
        #                 if locationRand == 1:
        #                     leftcounter += 1
        #                 if locationRand == 2:
        #                     upcounter += 1
        #                 if locationRand == 3:
        #                     downcounter += 1
        #
        #                 if gtypeRandom == 0 and c_counter == 8:
        #                     gtypeRandom = 1
        #
        #                 if gtypeRandom == 1 and i_counter == 8:
        #                     gtypeRandom = 0
        #
        #                 if gtypeRandom == 0 and (rand1 == 2 or rand1 == 3):
        #                     c_counter += 1
        #                     imageStims[rand1].setPos(positions[locationRand])
        #                     imageStims[rand1].draw()
        #
        #                     win.flip()
        #                     core.wait(0.3)
        #
        #
        #                 if gtypeRandom == 0 and (rand1 == 0 or rand1 == 1):
        #                     c_counter += 1
        #                     imageStims[rand2].setPos(positions[locationRand])
        #                     imageStims[rand2].draw()
        #                     win.flip()
        #                     core.wait(0.3)
        #
        #
        #                 if gtypeRandom == 1 and (rand1 == 0 or rand1 == 1):
        #                     i_counter += 1
        #                     imageStims[rand1].setPos(positions[locationRand])
        #                     imageStims[rand1].draw()
        #                     win.flip()
        #                     core.wait(0.3)
        #
        #
        #                 if gtypeRandom == 1 and (rand1 == 2 or rand1 == 3):
        #                     i_counter += 1
        #                     imageStims[rand2].setPos(positions[locationRand])
        #                     imageStims[rand2].draw()
        #                     win.flip()
        #                     core.wait(0.3)
        #
        #
        #                 imageStims[rand1].autoDraw = False
        #                 imageStims[rand2].autoDraw = False
        #                 questionMark.draw()
        #                 win.flip()
        #
        #                 testTimer = core.CountdownTimer(4)
        #                 flag = True
        #                 while flag:
        #                     keys = event.waitKeys(keyList=['end', 'down', '1', '2'], maxWait=4)
        #                     if keys:
        #
        #                         if gtypeRandom == 0 and (rand1 == 1 or rand1 == 2):
        #                             if keys[0] == 'end' or keys[0] == '1':
        #                                 correct.draw()
        #                                 win.flip()
        #                                 core.wait(2)
        #                             else:
        #                                 wrong.draw()
        #                                 win.flip()
        #                                 core.wait(2)
        #
        #                         if gtypeRandom == 0 and (rand1 == 0 or rand1 == 3):
        #                             if keys[0] == 'down' or keys[0] == '2':
        #                                 correct.draw()
        #                                 win.flip()
        #                                 core.wait(2)
        #                             else:
        #                                 wrong.draw()
        #                                 win.flip()
        #                                 core.wait(2)
        #
        #                         if gtypeRandom == 1 and (rand1 == 0 or rand1 == 3):
        #                             if keys[0] == 'end' or keys[0] == '1':
        #                                 correct.draw()
        #                                 win.flip()
        #                                 core.wait(2)
        #                             else:
        #                                 wrong.draw()
        #                                 win.flip()
        #                                 core.wait(2)
        #
        #                         if gtypeRandom == 1 and (rand1 == 1 or rand1 == 2):
        #                             if keys[0] == 'down' or keys[0] == '2':
        #                                 correct.draw()
        #                                 win.flip()
        #                                 core.wait(2)
        #                             else:
        #                                 wrong.draw()
        #                                 win.flip()
        #                                 core.wait(2)
        #
        #                         flag = False
        #                     elif testTimer.getTime() <= 0:
        #                         wrong.draw()
        #                         win.flip()
        #                         core.wait(2)
        #                         flag = False
        #             temp = False
        globalSecondInstructionImage.draw()
        win.flip()
        myflag = True
        while myflag:
            keys = event.waitKeys(keyList=['m'])
            for key in keys:
                if key[0] == 'm':
                    globalSecondInstructionImage.autoDraw = False
                    win.flip()
                    myflag = False


        c_counter = 0
        i_counter = 0

        c_right = 0
        c_left = 0
        c_up = 0
        c_down = 0

        i_right = 0
        i_left = 0
        i_up = 0
        i_down = 0

        # Global main task
        for i in range(1, 49):
            Config.trialcounter += 1
            block = '1'

            fixationPoint.draw()
            globalTimer = core.getTime()
            if Config.trialcounter == 1:
                Config.practiceDuration += globalTimer - generalTimer
            else:
                now = core.getTime()
                Config.practiceDuration += now - Config.trialfinished
            trialstart = Config.practiceDuration

            win.flip()
            core.wait(1)

            fixationPoint.autoDraw = False
            win.flip()

            typerandom = random.randint(0, 1)
            # 0 -> Incongruent
            # 1 -> Congruent

            if typerandom and c_counter == 24:
                typerandom = 0
            if not typerandom and i_counter == 24:
                typerandom = 1

            drawlist = []
            if typerandom:
                c_counter += 1
                locrand = random.randint(0, 3)

                if locrand == 0 and c_right == 6:
                    locrand = 1
                if locrand == 1 and c_left == 6:
                    locrand = 2
                if locrand == 2 and c_up == 6:
                    locrand = 3
                if locrand == 3 and c_down == 6:
                    if c_up < 6:
                        locrand = 2
                    elif c_left < 6:
                        locrand = 1
                    elif c_right < 6:
                        locrand = 0

                if locrand == 0:
                    c_right += 1
                    visualfield = 'Right'
                if locrand == 1:
                    c_left += 1
                    visualfield = 'Left'
                if locrand == 2:
                    c_up += 1
                    visualfield = 'Up'
                if locrand == 3:
                    c_down += 1
                    visualfield = 'Down'

                list = [imageStims[2], imageStims[3]]
                rand = random.randint(0, 1)
                list[rand].setPos(positions[locrand])
                list[rand].draw()
                win.flip()
                core.wait(0.3)
                drawlist.append(list[rand])
                # HH, ex1
                if rand:
                    imagefile = 'ex1'
                    congruency = '1'
                    corans = '1'
                # SS, ex4
                else:
                    imagefile = 'ex4'
                    congruency = '1'
                    corans = '2'
            else:
                i_counter += 1
                locrand = random.randint(0, 3)

                if locrand == 0 and i_right == 6:
                    locrand = 1
                if locrand == 1 and i_left == 6:
                    locrand = 2
                if locrand == 2 and i_up == 6:
                    locrand = 3
                if locrand == 3 and i_down == 6:
                    if i_up < 6:
                        locrand = 2
                    elif i_left < 6:
                        locrand = 1
                    elif i_right < 6:
                        locrand = 0

                if locrand == 0:
                    i_right += 1
                    visualfield = 'Right'
                if locrand == 1:
                    i_left += 1
                    visualfield = 'Left'
                if locrand == 2:
                    i_up += 1
                    visualfield = 'Up'
                if locrand == 3:
                    i_down += 1
                    visualfield = 'Down'

                list = [imageStims[0], imageStims[1]]
                rand = random.randint(0, 1)
                list[rand].setPos(positions[locrand])
                list[rand].draw()
                win.flip()
                core.wait(0.3)
                drawlist.append(list[rand])
                # SH, ex2
                if rand:
                    imagefile = 'ex2'
                    congruency = '0'
                    corans = '2'
                # HS, ex3
                else:
                    imagefile = 'ex3'
                    congruency = '0'
                    corans = '1'

            drawlist[0].autoDraw = False
            questionMark.draw()
            win.flip()
            counter = core.CountdownTimer(4)
            flag = True
            while flag:
                keys = event.waitKeys(keyList=['end', 'down', '1', '2'], maxWait=4)
                if keys:
                    for key in keys:
                        if key == 'end' or key == '1':
                            anslist.append('1')

                        if key == 'down' or key == '2':
                            anslist.append('2')

                        rtime = 4 - counter.getTime() + 0.3
                        keyrespstart = 4 - counter.getTime() + 0.3 + trialstart + 1
                        flag = False

                elif counter.getTime() <= 0:
                    isLate = True
                    flag = False
            questionMark.autoDraw = False
            win.flip()
            if anslist:
                keyresp = anslist[0]
                if anslist[0] == corans:
                    accuracy = 1
                else:
                    accuracy = 0
            else:
                keyresp = 'None'

            if isLate:
                rtime = 'None'
                accuracy = 'None'
                keyrespstart = 'None'

            Headers = ['ImageFile', 'Congruency', 'Visual Field', 'Block', 'Trial', 'Key-Resp', 'Cor-Ans', 'Accuracy',
                       'R-time', 'Trial-Start', 'Key-Resp-Start']

            toWrite = {'ImageFile': imagefile, 'Congruency': congruency, 'Visual Field': visualfield,
                       'Block': block, 'Trial': Config.trialcounter, 'Key-Resp': keyresp,
                       'Cor-Ans': corans, 'Accuracy': accuracy,
                       'R-time': rtime, 'Trial-Start': str(trialstart),
                       'Key-Resp-Start': keyrespstart}

            Config.append_dict_as_row(file_name=Config.filename, dict_of_elem=toWrite, headers=Headers)
            Config.trialfinished = core.getTime()

            if keyrespstart == 'None':
                Config.practiceDuration += 5.3
            else:
                Config.practiceDuration = keyrespstart
