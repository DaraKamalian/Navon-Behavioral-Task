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
localFirstInstructionImage = images.localFirstInstructionImage
localSecondInstructionImage = images.localSecondInstructionImage

fixationPoint = images.fixationPoint
questionMark = images.questionMark
correct = images.correct
wrong = images.wrong

positions = [(166.75, 75), (-286.77, 75), (-60, 301.77), (-60, -151.77)]


class Local(object):
    def Local(self):
        imagefile = ''
        congruency = ''
        rtime = 0
        visualfield = ''
        accuracy = 0
        keyrespstart = 0

        corans = ''
        isLate = False

        Config.blockcounter += 1
        generalTimer = core.getTime()
        localFirstInstructionImage.draw()
        win.flip()
        flag = True
        while flag:
            keys = event.getKeys(keyList=['m'])
            for key in keys:
                if key[0] == 'm':
                    localFirstInstructionImage.autoDraw = False
                    instructionImage2.draw()
                    win.flip()
                    flag = False

        temp = True
        # Local Practice
        while temp:
            keys = event.getKeys(keyList=['m'])
            for key in keys:
                if key[0] == 'm':
                    instructionImage2.autoDraw = False
                    win.flip()

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

                    for j in range(1, 17):
                        fixationPoint.draw()
                        win.flip()
                        core.wait(1)

                        fixationPoint.autoDraw = False

                        typerandom = random.randint(0, 1)
                        # 0 -> Incongruent
                        # 1 -> Congruent

                        if typerandom and c_counter == 8:
                            typerandom = 0
                        if not typerandom and i_counter == 8:
                            typerandom = 1

                        drawlist = []
                        if typerandom:
                            c_counter += 1
                            locrand = random.randint(0, 3)

                            if locrand == 0 and c_right == 2:
                                locrand = 1
                            if locrand == 1 and c_left == 2:
                                locrand = 2
                            if locrand == 2 and c_up == 2:
                                locrand = 3
                            if locrand == 3 and c_down == 2:
                                if c_up < 2:
                                    locrand = 2
                                elif c_left < 2:
                                    locrand = 1
                                elif c_right < 2:
                                    locrand = 0

                            if locrand == 0:
                                c_right += 1

                            if locrand == 1:
                                c_left += 1

                            if locrand == 2:
                                c_up += 1

                            if locrand == 3:
                                c_down += 1

                            list = [imageStims[2], imageStims[3]]
                            rand = random.randint(0, 1)
                            list[rand].setPos(positions[locrand])
                            list[rand].draw()
                            win.flip()
                            core.wait(0.3)
                            drawlist.append(list[rand])
                        else:
                            i_counter += 1
                            locrand = random.randint(0, 3)

                            if locrand == 0 and i_right == 2:
                                locrand = 1
                            if locrand == 1 and i_left == 2:
                                locrand = 2
                            if locrand == 2 and i_up == 2:
                                locrand = 3
                            if locrand == 3 and i_down == 2:
                                if i_up < 2:
                                    locrand = 2
                                elif i_left < 2:
                                    locrand = 1
                                elif i_right < 2:
                                    locrand = 0

                            if locrand == 0:
                                i_right += 1

                            if locrand == 1:
                                i_left += 1

                            if locrand == 2:
                                i_up += 1

                            if locrand == 3:
                                i_down += 1

                            list = [imageStims[0], imageStims[1]]
                            rand = random.randint(0, 1)
                            list[rand].setPos(positions[locrand])
                            list[rand].draw()
                            win.flip()
                            core.wait(0.3)
                            drawlist.append(list[rand])

                        drawlist[0].autoDraw = False
                        questionMark.draw()
                        win.flip()
                        counter = core.CountdownTimer(4)
                        flag = True
                        while flag:
                            keys = event.waitKeys(keyList=['end', 'down', '1', '2'], maxWait=4)
                            if keys:
                                if keys[0] == '2' or keys[0] == 'down':
                                    if drawlist[0] == imageStims[1]:
                                        wrong.draw()
                                        win.flip()
                                        core.wait(2)
                                    if drawlist[0] == imageStims[3]:
                                        correct.draw()
                                        win.flip()
                                        core.wait(2)
                                    if drawlist[0] == imageStims[0]:
                                        correct.draw()
                                        win.flip()
                                        core.wait(2)
                                    if drawlist[0] == imageStims[2]:
                                        wrong.draw()
                                        win.flip()
                                        core.wait(2)
                                if keys[0] == '1' or keys[0] == 'end':
                                    if drawlist[0] == imageStims[1]:
                                        correct.draw()
                                        win.flip()
                                        core.wait(2)
                                    if drawlist[0] == imageStims[3]:
                                        wrong.draw()
                                        win.flip()
                                        core.wait(2)
                                    if drawlist[0] == imageStims[0]:
                                        wrong.draw()
                                        win.flip()
                                        core.wait(2)
                                    if drawlist[0] == imageStims[2]:
                                        correct.draw()
                                        win.flip()
                                        core.wait(2)
                                flag = False

                            elif counter.getTime() <= 0:
                                wrong.draw()
                                win.flip()
                                core.wait(2)
                                flag = False
                    temp = False

        localSecondInstructionImage.draw()
        win.flip()
        myflag = True
        while myflag:
            keys = event.waitKeys(keyList=['m'])
            for key in keys:
                if key[0] == 'm':
                    localSecondInstructionImage.autoDraw = False
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

        # Local main task
        for i in range(1, 49):
            Config.trialcounter += 1
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

            block = '0'
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
                    corans = '1'
                # HS, ex3
                else:
                    imagefile = 'ex3'
                    congruency = '0'
                    corans = '2'

            drawlist[0].autoDraw = False
            questionMark.draw()
            win.flip()
            counter = core.CountdownTimer(4)
            anslist = []
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

            Headers = ['ImageFile', 'Congruency', 'Visual Field', 'Block', 'G.L.Block', 'Trial', 'Key-Resp', 'Cor-Ans', 'Accuracy',
                       'R-time', 'Trial-Start', 'Key-Resp-Start']

            toWrite = {'ImageFile': imagefile, 'Congruency': congruency, 'Visual Field': visualfield,
                       'Block': Config.blockcounter,'G.L.Block': block, 'Trial': Config.trialcounter, 'Key-Resp': keyresp,
                       'Cor-Ans': corans, 'Accuracy': accuracy,
                       'R-time': rtime, 'Trial-Start': trialstart,
                       'Key-Resp-Start': keyrespstart}
            Config.append_dict_as_row(file_name=Config.filename, dict_of_elem=toWrite, headers=Headers)

            Config.trialfinished = core.getTime()

            if keyrespstart == 'None':
                Config.practiceDuration += 5.3
            else:
                Config.practiceDuration = keyrespstart
