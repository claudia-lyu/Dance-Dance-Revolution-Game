from cmu_112_graphics import *
from aubio import source, onset
import pygame
from beatLst import onsettimes_list
import random
import math
import decimal
import copy
################################################################################

#Name: Claudia Lyu
#Andrew ID: clyu

################################################################################

##### Website Cite: 
### Music Download from https://ilkpop.net/index.xhtml 
#   ("Don't Go.mp3"; "Peter Pan.mp3"; "Don't fight the feeling.mp3")
#   ('Don't Go.mp3' is background music without editing)
#   (testing by the other two songs, which are edited)
### Music Cuts to 35 seconds from Website: https://mp3cut.net/
### ALL Images are downloaded from:
#   https://id.pinterest.com/oppafg/exo-wallpaper/
### beatLst reference see beatLst.py

################################################################################
# Splash Screen Mode
################################################################################
#####
#Main screen  
#####
def splashScreenMode_header(app, canvas):   
    # This is a helper function for redrawAll
    # This draws the the main page
    canvas.create_image(app.width/2, app.height/2, 
                        image=ImageTk.PhotoImage(app.mainpageImage))
    canvas.create_text(app.width/2, 40, text="Welcome to EXO-Revolution", 
                        font='Arial 35 bold', 
                        fill=random.choice(['#7F00FF', "white"]))
    canvas.create_text(app.width/2, 42, text="Welcome to EXO-Revolution", 
                        font='Arial 35 bold', 
                        fill=random.choice(['#7F00FF', "white"]))

def splashScreenMode_input_userName(app, canvas):
    canvas.create_text(app.width/2, 100, text=app.message, font='Arial 20 bold',
                        fill='#FFE5CC')

def splashScreenMode_draw_description(app, canvas):
    words = app.exo
    update = app.width/8
    x = 0
    y = app.height * (4/5)
    for char in words:
        if 0 <= x < app.width-update:
            x += update
        else:
            y += app.width/25
            x = update
        canvas.create_text(x, y, text=char, font='Arial 10 bold', 
                            fill=random.choice(["white", "#FFFFCC"]))

def splashScreenMode_intro(app, canvas):
    canvas.create_text(app.introX, 150, text=app.intro, font='Arial 20 bold', 
                        fill=random.choice(["silver", "white"]))

def splashScreenMode_timerFired(app):
    app.counter += 1
    if app.introX <  -(len(app.intro*5)):
        app.introX =  app.width+(len(app.intro)*3)
    else:   app.introX -= 18
    if app.counter % 2 == 0:
        app.oval1_x1, app.oval1_y1 = app.oval1_x1-2, app.oval1_y1-2
        app.oval1_x2, app.oval1_y2 = app.oval1_x2+2, app.oval1_y2+2
        app.oval2_x1, app.oval2_y1 = app.oval2_x1-2, app.oval2_y1-2
        app.oval2_x2, app.oval2_y2 = app.oval2_x2+2, app.oval2_y2+2
        app.oval3_x1, app.oval3_y1 = app.oval3_x1-2, app.oval3_y1-2
        app.oval3_x2, app.oval3_y2 = app.oval3_x2+2, app.oval3_y2+2
    elif app.counter % 2 != 0:
        app.oval1_x1, app.oval1_y1 = app.oval1_x1+2, app.oval1_y1+2
        app.oval1_x2, app.oval1_y2 = app.oval1_x2-2, app.oval1_y2-2
        app.oval2_x1, app.oval2_y1 = app.oval2_x1+2, app.oval2_y1+2
        app.oval2_x2, app.oval2_y2 = app.oval2_x2-2, app.oval2_y2-2
        app.oval3_x1, app.oval3_y1 = app.oval3_x1+2, app.oval3_y1+2
        app.oval3_x2, app.oval3_y2 = app.oval3_x2-2, app.oval3_y2-2

def splashScreenMode_circle_choose(app, canvas):
    oval1_x1, oval1_y1 = app.oval1_x1, app.oval1_y1
    oval1_x2, oval1_y2 = app.oval1_x2, app.oval1_y2
    canvas.create_oval(oval1_x1, oval1_y1, oval1_x2, oval1_y2, 
                        outline='#9933FF', width=1.5)
    canvas.create_oval(oval1_x1+1, oval1_y1+1, oval1_x2+1, oval1_y2+1, 
                        outline='white', width=1.5)
    canvas.create_text(oval1_x1+(oval1_x2-oval1_x1)//2, 
                        oval1_y1+(oval1_y2-oval1_y1)//2, 
                        fill=random.choice(["white","#E0E0E0", "#FFCCE5"]),
                        text="Select Your Song",font='Arial 14 bold')

    oval2_x1, oval2_y1 = app.oval2_x1, app.oval2_y1
    oval2_x2, oval2_y2 = app.oval2_x2, app.oval2_y2
    canvas.create_oval(oval2_x1, oval2_y1, oval2_x2, oval2_y2, 
                        outline='#9933FF', width=1.5)
    canvas.create_oval(oval2_x1+1, oval2_y1+1, oval2_x2+1, oval2_y2+1, 
                        outline='white', width=1.5)
    canvas.create_text(oval2_x1+(oval2_x2-oval2_x1)//2, 
                        oval2_y1+(oval2_y2-oval2_y1)//2, 
                        fill=random.choice(["white", "#E0E0E0", "#FFCCE5"]),
                        text="Play Game!",font='Arial 14 bold')

    oval3_x1, oval3_y1 = app.oval3_x1, app.oval3_y1
    oval3_x2, oval3_y2 = app.oval3_x2, app.oval3_y2
    canvas.create_oval(oval3_x1, oval3_y1, oval3_x2, oval3_y2,
                        outline='#9933FF', width=1.5)
    canvas.create_oval(oval3_x1+1, oval3_y1+1, oval3_x2+1, oval3_y2+1, 
                        outline='white', width=1.5)
    canvas.create_text(oval3_x1+(oval3_x2-oval3_x1)//2, 
                        oval3_y1+(oval3_y2-oval3_y1)//2, 
                        fill=random.choice(["white", "#E0E0E0", "#FFCCE5"]),
                        text="History",font='Arial 14 bold')

def splashScreenMode_redrawAll(app, canvas):
    splashScreenMode_header(app, canvas)
    splashScreenMode_input_userName(app, canvas)
    splashScreenMode_intro(app, canvas)
    splashScreenMode_draw_description(app, canvas)
    splashScreenMode_circle_choose(app, canvas)

def splashScreenMode_mousePressed(app, event):
    if (app.oval1_x1 <= event.x <= app.oval1_x2 and
        app.oval1_y1 <= event.y <= app.oval1_y2):
        app.mode = 'importSongMode'
    elif (app.oval2_x1 <= event.x <= app.oval2_x2 and
        app.oval2_y1 <= event.y <= app.oval2_y2):
        app.mode = 'GameMainPageMode'
    elif (app.oval3_x1 <= event.x <= app.oval3_x2 and
        app.oval3_y1 <= event.y <= app.oval3_y2):
        if app.songList != []:
            app.mode = 'historyMode'
    else:
        name = app.getUserInput('Dear EXO-L, what is your name?')
        if (name == None or name == ""): 
            app.message = 'EXO-L'
        elif name != None:
            app.showMessage('You entered: ' + name)
            app.message = f'Hi, {name}!'

def splashScreenMode_keyPressed(app, event):
    if event.key == "m":
        if sound_isPlaying():
            pygame.mixer.music.stop()
        else:
            app.song = soundStarted(app.bk_song, app.bk_vol)

################################################################################
# importSong Mode
################################################################################
def importSongMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.musicImport_image))
    canvas.create_oval(app.width/10, app.height/20, 
                        app.width-app.width/10, app.height/7, outline='silver',
                        width=1.5)                    
    canvas.create_text(app.width/2, app.height/10, 
                        text="File Path of Your Song:", font='Arial 28 bold', 
                        fill=random.choice(['#E5CCFF','#E0E0E0']))
    
    canvas.create_rectangle(app.width/5, app.height/6, 
                            app.width-app.width/5,app.height/4,outline='silver')
    canvas.create_text(app.width/5 + (app.width-app.width/5*2)//2, 
                        app.height/6 + (app.height/4-app.height/6)//2,
                        text=app.music_select, font='Arial 18 bold', 
                        fill=random.choice(['#FF9933','#FFCC99']))

    font = 'Arial 24 bold italic'
    y = app.height//2
    canvas.create_text(app.width/2, y-20, 
                       text='You must import song before playing game',
                       font=font, fill='#E5CCFF')
    canvas.create_text(app.width/2, y+20, 
                       text='Click the white box above to import song',
                       font=font, fill='#E5CCFF')
    canvas.create_text(app.width/2, y+60, 
                       text='Press e: back to main page',
                       font=font, fill='#E5CCFF')
    canvas.create_text(app.width/2, y+100, 
                       text='Press l: see your song list & play game!',
                       font=font, fill='#E5CCFF')

def importSongMode_mousePressed(app, event):
    if (app.height/5 <= event.x <= app.width-app.width/5
        and app.height/6 <= event.y <= app.height/4):
        name = app.getUserInput('What is the song name?')
        if name == None:
            app.music_select = "You Cancelled! Try Again!"
        elif ".mp3" not in name:
            app.music_select = "File should end with .mp3"
        else:
            app.music_select = f'{name}'
            if app.music_select not in app.songList:
                app.songList += [app.music_select]
                app.songDict[app.music_select]=0

def importSongMode_keyPressed(app, event):
    if (event.key == 'l'):
        app.mode = 'songListMode'
    elif (event.key == 'e'):
        app.mode = 'splashScreenMode'

################################################################################
# songList Mode
################################################################################
### Import your song
### Create your songList
def songListMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.musicImport_image))
    x1, y1 = app.width/5, app.height/6
    x2, y2 = app.width-app.width/5, app.height/4
    a1, a2 = (app.width/5 + (app.width-app.width/5*2)//2, 
                app.height/6 + (app.height/4-app.height/6)//2)
    if len(app.songList) == 0:
        canvas.create_rectangle(x1, y1, x2, y2, outline='silver')
        canvas.create_text(a1, a2, text='No song so far...',
                            font='Arial 18 bold', 
                            fill='Orange')

    for i in range (len(app.songList)):
        song = app.songList[i]
        canvas.create_rectangle(x1, y1, x2, y2, outline='silver')
        canvas.create_text(a1, a2, text=f'[{i}]. {song}',
                            font='Arial 18 bold', 
                            fill='#FFB266')
        d = y2-y1
        x1, y1 = x1, y2
        x2, y2 = x2, y2+d
        a1, a2 = a1, y1+d//2
    canvas.create_text(app.width//2, app.height//25, 
                        text='Final Decision: Type your song number',
                        font='Arial 24 bold', fill='#B266FF')
    canvas.create_text(app.width//2, app.height//11, text=
                    '(song number: the number in the bracket before song name)',
                    font='Arial 15 bold', fill='#E5CCFF')
    canvas.create_text(app.width//2, app.height//8, 
                        text='(Press s: return to select_Song page)',
                        font='Arial 15 bold', fill='#E5CCFF')

def songListMode_keyPressed(app, event):
    if event.key == "s":
        app.mode = 'importSongMode'
    elif event.key.isdigit():
        bound = len(app.songList)
        if 0 <= int(event.key) < bound:
            app.music_select = app.songList[int(event.key)]

################################################################################
# GameMainPage Mode
################################################################################
###way 1. songList-->SelectSong--->PlayGame(main_screen)
###way 2. songList-->typy number and start game 
def GameMainPageMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.game_Image))
    canvas.create_text(app.width//2, 
                        app.height//2-50, text="EXO-L, Select Game Level !",
                        font='Arial 20 bold', 
                        fill=random.choice(["#FFCC99","#FF9999"]))
    canvas.create_text(app.width//2, 
                        app.height//2+10, text="(Press e: back to main page)",
                        font='Arial 17 bold',
                        fill=random.choice(["#FFCC99","#FF9999"]))

    oval1_x1, oval1_y1 = app.oval1_x1, app.oval1_y1
    oval1_x2, oval1_y2 = app.oval1_x2, app.oval1_y2
    canvas.create_oval(oval1_x1, oval1_y1, oval1_x2, oval1_y2, outline='silver',
                        width=1.5)
    canvas.create_oval(oval1_x1+1, oval1_y1+1, oval1_x2+1, oval1_y2+1, 
                        outline='white', width=1.5)
    canvas.create_text(oval1_x1+(oval1_x2-oval1_x1)//2, 
                        oval1_y1+(oval1_y2-oval1_y1)//2,
                        text="INTRO",font='Arial 15 bold',
                        fill=random.choice(["#FFCC99","#FF9999"]))
    canvas.create_text(oval1_x1+(oval1_x2-oval1_x1)//2+1, 
                        oval1_y1+(oval1_y2-oval1_y1)//2+1,
                        text="INTRO",font='Arial 15 bold',
                        fill=random.choice(["#FFCC99","#FF9999"]))    
    
    oval2_x1, oval2_y1 = app.oval2_x1, app.oval2_y1
    oval2_x2, oval2_y2 = app.oval2_x2, app.oval2_y2
    canvas.create_oval(oval2_x1, oval2_y1, oval2_x2, oval2_y2, outline='silver',
                        width=1.5)
    canvas.create_oval(oval2_x1+1, oval2_y1+1, oval2_x2+1, oval2_y2+1, 
                        outline='white', width=1.5)
    canvas.create_text(oval2_x1+(oval2_x2-oval2_x1)//2, 
                        oval2_y1+(oval2_y2-oval2_y1)//2, 
                        text="PRACTICE",font='Arial 15 bold',
                        fill=random.choice(["#FFCC99","#FF9999"]))
    canvas.create_text(oval2_x1+(oval2_x2-oval2_x1)//2+1, 
                        oval2_y1+(oval2_y2-oval2_y1)//2+1, 
                        text="PRACTICE",font='Arial 15 bold',
                        fill=random.choice(["#FFCC99","#FF9999"]))

    oval3_x1, oval3_y1 = app.oval3_x1, app.oval3_y1
    oval3_x2, oval3_y2 = app.oval3_x2, app.oval3_y2
    canvas.create_oval(oval3_x1, oval3_y1, oval3_x2, oval3_y2, outline='silver',
                        width=1.5)
    canvas.create_oval(oval3_x1+1, oval3_y1+1, oval3_x2+1, oval3_y2+1, 
                        outline='white', width=1.5)
    canvas.create_text(oval3_x1+(oval3_x2-oval3_x1)//2, 
                        oval3_y1+(oval3_y2-oval3_y1)//2,
                        text="BATTLE",font='Arial 15 bold',
                        fill=random.choice(["#FFCC99","#FF9999"]))
    canvas.create_text(oval3_x1+(oval3_x2-oval3_x1)//2+1, 
                        oval3_y1+(oval3_y2-oval3_y1)//2+1, 
                        text="BATTLE",font='Arial 15 bold',
                        fill=random.choice(["#FFCC99","#FF9999"]))

    canvas.create_text(app.width//2, 
                        140, fill="brown",
                        text=app.instruct,font='Arial 15 bold')
    
    canvas.create_text(app.width//2, 
                        600, fill="white",
                        text=app.instruct2,font='Arial 15 bold')

def GameMainPageMode_timerFired(app):
    app.counter1 += 1
    if app.counter1 % 2 == 0:
        app.oval1_x1, app.oval1_y1 = app.oval1_x1-2, app.oval1_y1-2
        app.oval1_x2, app.oval1_y2 = app.oval1_x2+2, app.oval1_y2+2
        app.oval2_x1, app.oval2_y1 = app.oval2_x1-2, app.oval2_y1-2
        app.oval2_x2, app.oval2_y2 = app.oval2_x2+2, app.oval2_y2+2
        app.oval3_x1, app.oval3_y1 = app.oval3_x1-2, app.oval3_y1-2
        app.oval3_x2, app.oval3_y2 = app.oval3_x2+2, app.oval3_y2+2
    elif app.counter1 % 2 != 0:
        app.oval1_x1, app.oval1_y1 = app.oval1_x1+2, app.oval1_y1+2
        app.oval1_x2, app.oval1_y2 = app.oval1_x2-2, app.oval1_y2-2
        app.oval2_x1, app.oval2_y1 = app.oval2_x1+2, app.oval2_y1+2
        app.oval2_x2, app.oval2_y2 = app.oval2_x2-2, app.oval2_y2-2
        app.oval3_x1, app.oval3_y1 = app.oval3_x1+2, app.oval3_y1+2
        app.oval3_x2, app.oval3_y2 = app.oval3_x2-2, app.oval3_y2-2

def GameMainPageMode_mousePressed(app, event):
    if (app.oval1_x1 <= event.x <= app.oval1_x2 and
        app.oval1_y1 <= event.y <= app.oval1_y2):
        if (app.music_select != "No song so far..." 
            and app.music_select !=  "You Cancelled! Try Again!"
            and app.music_select != "File should end with .mp3"):
            app.timerDelay = 400
            pygame.mixer.music.stop()
            app.gameSound = Sound(app.music_select)
            app.play_game = GameMode_Playgame(app.gameSound, app)
            app.mode = 'gameMode'
    elif (app.oval2_x1 <= event.x <= app.oval2_x2 and
        app.oval2_y1 <= event.y <= app.oval2_y2):
        if (app.music_select != "No song so far..."
            and app.music_select !=  "You Cancelled! Try Again!"
            and app.music_select != "File should end with .mp3"):
            app.timerDelay = 300
            pygame.mixer.music.stop()
            app.gameSound = Sound(app.music_select)
            app.play_game = GameMode_Playgame(app.gameSound, app)            
            app.mode = 'gameMode'
    elif (app.oval3_x1 <= event.x <= app.oval3_x2 and
        app.oval3_y1 <= event.y <= app.oval3_y2):
        if (app.music_select != "No song so far..."
            and app.music_select !=  "You Cancelled! Try Again!"
            and app.music_select != "File should end with .mp3"
            and app.music_select+'-intro' in app.songD
            and app.music_select+'-practice' in app.songD):
            pygame.mixer.music.stop()
            app.gameSound = Sound(app.music_select)
            app.play_game = GameMode_Playgame(app.gameSound, app)
            app.mode = 'gameMode'

def GameMainPageMode_keyPressed(app, event):
    if (event.key == 'e'):
        if app.songList != []:
            l = app.songList
            song = app.music_select
            dic = app.songDict
            d = app.songD
            s = Sound(song)
            g = GameMode_Playgame(s, app)
            infor1 = app.hit1
            Intro = app.Intro
            prac = app.prac
            best = app.best
            pf, gr, ob = app.perfect, app.great, app.obstacle
            mu,sc,mi = app.multi, app.score, app.miss
            pf1, gr1, ob1 = app.perfect1, app.great1, app.obstacle1
            mu1,sc1,mi1 = app.multi1, app.score1, app.miss1
            app.my_score = {app.music_select: [pf, gr, ob, mu, sc, mi]}
            app.AI_score = {app.music_select: [pf1, gr1, ob1, mu1,sc1,mi1]}
            
            my, other = copy.deepcopy(app.my_score), copy.deepcopy(app.AI_score)
            battle = app.battle
            app.scored = {app.music_select: app.score}
            app.score1d = {app.music_select: app.score1}
            score, score1 = app.scored, app.score1d
            appStarted(app)
            app.songList = l
            app.music_select = song
            app.songDict = dic
            app.gameSound = s
            app.play_game = g
            app.songD = d
            app.hit1 = infor1
            app.Intro = Intro
            app.prac = prac
            app.best = best
            app.scored, app.score1d = score, score1
            app.battle = battle
            app.perfect, app.great, app.obstacle = pf, gr, ob
            app.multi, app.score, app.miss = mu,sc,mi
            app.perfect1, app.great1, app.obstacle1 = pf1, gr1, ob1
            app.multi1, app.score1, app.miss1 = mu1, sc1, mi1
            
            app.my_score, app.AI_score = my, other
            app.bk_song = "Don't Go.mp3"
        app.mode = 'splashScreenMode'

    
################################################################################
# Game Mode #app.play_game
################################################################################
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

#process raw data we extracted from music file
#to new data which better fit with timerDelay in CMU_112_graphics
def processData(delay, cur_lst):
    res = []
    for time in cur_lst[0:-1]:
        res.append(roundHalfUp(time / delay) * delay)
    return res + [math.floor(cur_lst[-1]/delay)*delay]
#calculate drop time of each piece 
def dropTime(delay, first_dropt, lst):
    res = []
    for t in lst:
        diff = t - lst[0]
        res.append((first_dropt + diff))
    return [res[0]] + processData(delay, res[1:])
#calculate average 
def mu(l):
    total = 0
    for n in l:
        total += n
    return total / len(l)
#calculate standard deviation
def sigma(l, mu):
    devi_sum = 0
    for n in l:
        devi_sum += (n-mu)**2
    return (devi_sum / len(l)) ** 0.5            

class GameMode_Playgame(object):
    def __init__(self, song, app):
        self.sound_name = song.sound_name
        self.game_song = song.sound_path
        self.beatLst = song.beatLst

        self.note_speed = 5.2
        self.travel_dist = app.height-app.delta*3
        self.travel_time = roundHalfUp(self.travel_dist / self.note_speed 
                                        * app.timerDelay)
        app.timePassed = roundHalfUp(-(self.travel_dist / self.note_speed 
                                        * app.timerDelay))

        self.note_ending_position = [(app.delta * 1, self.travel_dist),
                                    (app.delta * 2, self.travel_dist),
                                    (app.delta * 3, self.travel_dist),
                                    (app.delta * 4, self.travel_dist),
                                    (app.delta * 5, self.travel_dist)]
        self.Mode = ''
        self.res = []

        if app.timerDelay == 400:
            self.Mode = "intro"
            self.dropTime_Lst = (dropTime(app.timerDelay, app.timePassed, 
                                            self.beatLst[:-16:3])) #
            self.len = len((dropTime(app.timerDelay, app.timePassed, 
                                    self.beatLst[:-16:3])))
            self.obs_dropt = (dropTime(app.timerDelay, app.timePassed, 
                                        self.beatLst[8:-12:7])) 
            self.obs_len = len((dropTime(app.timerDelay, app.timePassed, 
                                        self.beatLst[8:-12:7])))
            self.multi_dropt = (dropTime(app.timerDelay, app.timePassed, 
                                        self.beatLst[15:-12:10])) 
            self.multi_len = len((dropTime(app.timerDelay, app.timePassed, 
                                            self.beatLst[15:-12:10])))

        elif app.timerDelay == 300:
            app.timerDelay = 200
            self.Mode = "practice"
            self.dropTime_Lst = (dropTime(app.timerDelay, app.timePassed, 
                                            self.beatLst[:-20:3])) #
            self.len = len((dropTime(app.timerDelay, app.timePassed, 
                                    self.beatLst[:-20:3])))
            self.obs_dropt = (dropTime(app.timerDelay, app.timePassed, 
                                        self.beatLst[8:-12:8])) 
            self.obs_len = len((dropTime(app.timerDelay, app.timePassed, 
                                        self.beatLst[8:-12:8])))
            self.multi_dropt = (dropTime(app.timerDelay, app.timePassed, 
                                        self.beatLst[20:-12:11])) 
            self.multi_len = len((dropTime(app.timerDelay, app.timePassed, 
                                            self.beatLst[20:-12:11])))

        elif app.timerDelay == 200:
            self.Mode = "battle"
            if (f"{app.music_select}-intro" in app.songD and 
                f"{app.music_select}-practice" in app.songD):
                s = app.music_select
                if app.Intro != {} and app.prac != {} and app.best != {}:
                    l1, l2, l3 = app.Intro[s], app.prac[s], app.best[s]
                    smaller = min(len(l1), len(l2), len(l3))
                    # make sure three lists have the same length
                    l1,l2,l3 = l1[:smaller], l2[:smaller], l3[:smaller]
                    #extract all x_pos and y_pos values, make them to lists
                    x, y = [], []
                    for i in range (len(l1)):
                        cur_x = [l1[i][0], l2[i][0], l3[i][0]]
                        cur_y = [l1[i][1], l2[i][1], l3[i][1]]
                        x += [cur_x]
                        y += [cur_y]
                    #get the predicted value for AI performance 
                    for i in range (len(x)):
                        itemX, itemY = x[i], y[i]
                        mu_x = mu(itemX)
                        sigma_x = sigma(itemX, mu_x)
                        mu_y = mu(itemY)
                        sigma_y = sigma(itemY, mu_y) 
                        x_val = round(random.gauss(mu_x, sigma_x))
                        y_val = round(random.gauss(mu_y, sigma_y))
                        self.res += [(x_val, y_val)]
                elif app.Intro == {} and app.prac == {} and app.best == {}:
                    self.res = [1]

            self.dropTime_Lst = (dropTime(app.timerDelay, app.timePassed, 
                                            self.beatLst[:-20:3])) #
            self.len = len((dropTime(app.timerDelay, app.timePassed, 
                                    self.beatLst[:-20:3])))
            self.obs_dropt = (dropTime(app.timerDelay, app.timePassed, 
                                        self.beatLst[8:-12:9])) 
            self.obs_len = len((dropTime(app.timerDelay, app.timePassed, 
                                        self.beatLst[8:-12:9])))
            self.multi_dropt = (dropTime(app.timerDelay, app.timePassed, 
                                        self.beatLst[20:-12:12])) 
            self.multi_len = len((dropTime(app.timerDelay, app.timePassed, 
                                            self.beatLst[20:-12:12])))

        self.randomPath = []
        self.note_position = []
        self.stop = dropTime(app.timerDelay, app.timePassed, self.beatLst)[-4]
        self.start = dropTime(app.timerDelay, app.timePassed, self.beatLst)[0]
        self.choice = ["pink","blue","green","purple","yellow"]
        self.color_choice = ([self.choice[random.randint(0,4)] 
                            for i in range (self.len)])
        
        self.obs_path = []
        self.obs_pos = []

        self.multi_path = []
        self.multi_pos = []

    def playMusic(self):
        soundStarted(self.game_song, 1)
    
    def endMusic(self):
        pygame.mixer.music.stop()

    #place music note 
    def placeNote(self, app):
        if (app.play_game.dropTime_Lst != [] and 
            abs(app.timePassed-app.play_game.dropTime_Lst[0]) 
            <= app.timerDelay//2):
            path_choose = random.randint(0, 4)
            app.play_game.randomPath.append(path_choose)
            app.play_game.dropTime_Lst.pop(0)
            app.play_game.note_position.append((app.width//2, 0))
            return 
    # move note based on the path it chooses in placeNote
    def moveNote(self, app):
        for i in range (len(app.play_game.note_position)): 
            # move to tracker #0
            if (app.play_game.note_position[i] != None and 
                app.play_game.randomPath[i] == 0):
                #miss a piece
                if (app.play_game.note_position[i][1] > 
                    app.play_game.note_ending_position[0][1]+
                    app.delta//2+app.delta//4):
                    app.miss += 1
                    app.score -= 5
                    app.play_game.note_position.pop(i)
                    app.play_game.randomPath.pop(i)
                    app.play_game.note_position.insert(i, None)    
                    app.play_game.randomPath.insert(i, None)
                else:   
                    newx = (app.play_game.note_position[i][0]-
                            app.play_game.note_speed / 2.7)
                    newy = (app.play_game.note_position[i][1]+
                            app.play_game.note_speed)
                    app.play_game.note_position[i] = (newx, newy)  
            # move to tracker #1
            elif (app.play_game.note_position[i] != None and 
                    app.play_game.randomPath[i] == 1):
                #miss a piece
                if (app.play_game.note_position[i][1] > 
                    app.play_game.note_ending_position[0][1]+
                    app.delta//2+app.delta//4):
                    app.miss += 1
                    app.score -= 5
                    app.play_game.note_position.pop(i)
                    app.play_game.randomPath.pop(i)
                    app.play_game.note_position.insert(i, None)    
                    app.play_game.randomPath.insert(i, None)
                else:   
                    newx = (app.play_game.note_position[i][0]-
                            app.play_game.note_speed / 5.5)
                    newy = (app.play_game.note_position[i][1]+
                            app.play_game.note_speed)
                    app.play_game.note_position[i] = (newx, newy)  
            # move to tracker #2
            elif (app.play_game.note_position[i] != None and 
                    app.play_game.randomPath[i] == 2):
                #miss a piece
                if (app.play_game.note_position[i][1] > 
                    app.play_game.note_ending_position[0][1]+
                    app.delta//2+app.delta//4):
                    app.miss += 1
                    app.score -= 5
                    app.play_game.note_position.pop(i)
                    app.play_game.randomPath.pop(i)
                    app.play_game.note_position.insert(i, None)    
                    app.play_game.randomPath.insert(i, None)
                else:   
                    newx = app.play_game.note_position[i][0]
                    newy = (app.play_game.note_position[i][1]+
                            app.play_game.note_speed)
                    app.play_game.note_position[i] = (newx, newy)  
            # move to tracker #3
            elif (app.play_game.note_position[i] != None and 
                    app.play_game.randomPath[i] == 3):
                #miss a piece
                if (app.play_game.note_position[i][1] > 
                    app.play_game.note_ending_position[0][1]+
                    app.delta//2+app.delta//4):
                    app.miss += 1
                    app.score -= 5
                    app.play_game.note_position.pop(i)
                    app.play_game.randomPath.pop(i)
                    app.play_game.note_position.insert(i, None)    
                    app.play_game.randomPath.insert(i, None)
                else:  
                    newx = (app.play_game.note_position[i][0]+
                            app.play_game.note_speed / 5.5)
                    newy = (app.play_game.note_position[i][1]+
                            app.play_game.note_speed) 
                    app.play_game.note_position[i] = (newx, newy)  
            # move to tracker #4
            elif (app.play_game.note_position[i] != None and 
                    app.play_game.randomPath[i] == 4):
                #miss a piece
                if (app.play_game.note_position[i][1] > 
                    app.play_game.note_ending_position[0][1]+
                    app.delta//2+app.delta//4):
                    app.miss += 1
                    app.score -= 5
                    app.play_game.note_position.pop(i)
                    app.play_game.randomPath.pop(i)
                    app.play_game.note_position.insert(i, None)    
                    app.play_game.randomPath.insert(i, None)
                else:  
                    newx = (app.play_game.note_position[i][0]+
                            app.play_game.note_speed / 2.7)
                    newy = (app.play_game.note_position[i][1]+
                            app.play_game.note_speed)
                    app.play_game.note_position[i] = (newx, newy)  
        app.play_game.placeNote(app)   
    #obstacles
    def placeObs(self, app):
        if not app.gameOver:
            if app.play_game.obs_pos != None and app.play_game.obs_dropt != []:
                if (abs(app.timePassed-app.play_game.obs_dropt[0]) <= 
                    app.timerDelay//2):
                    path_choose = random.randint(0, 4)
                    app.play_game.obs_path.append(path_choose)
                    app.play_game.obs_dropt.pop(0)
                    app.play_game.obs_pos.append((app.width//2, 0))
                    return 

    def moveObs(self, app):
        for i in range (len(app.play_game.obs_pos)): 
            if (app.play_game.obs_pos[i] != None and 
                app.play_game.obs_path[i] == 0):
                #avoid obstacle
                if (app.play_game.obs_pos[i][1] > 
                    app.play_game.note_ending_position[0][1]+
                    app.delta//2+app.delta//4):
                    app.play_game.obs_pos.pop(i)
                    app.play_game.obs_path.pop(i)
                    app.play_game.obs_pos.insert(i, None)    
                    app.play_game.obs_path.insert(i, None)
                elif (app.play_game.obs_pos[i][1] > 
                        (app.height - app.delta * 3)//2):
                    app.obstacle1 += 1
                    app.score1 += 1
                    app.play_game.obs_pos.pop(i)
                    app.play_game.obs_path.pop(i)
                    app.play_game.obs_pos.insert(i, None)
                    app.play_game.obs_path.insert(i, None)
                else:   
                    newx = (app.play_game.obs_pos[i][0]-
                            app.play_game.note_speed / 2.7)
                    newy = app.play_game.obs_pos[i][1]+app.play_game.note_speed
                    app.play_game.obs_pos[i] = (newx, newy)
            # move to tracker #1
            elif (app.play_game.obs_pos[i] != None and 
                    app.play_game.obs_path[i] == 1):
                #avoid obstacle
                if (app.play_game.obs_pos[i][1] > 
                    app.play_game.note_ending_position[0][1]+
                    app.delta//2+app.delta//4):
                    app.play_game.obs_pos.pop(i)
                    app.play_game.obs_path.pop(i)
                    app.play_game.obs_pos.insert(i, None)    
                    app.play_game.obs_path.insert(i, None)
                elif (app.play_game.obs_pos[i][1] > 
                        (app.height - app.delta * 3)//2):
                    app.obstacle1 += 1
                    app.score1 += 1
                    app.play_game.obs_pos.pop(i)
                    app.play_game.obs_path.pop(i)
                    app.play_game.obs_pos.insert(i, None)
                    app.play_game.obs_path.insert(i, None)
                else:   
                    newx = (app.play_game.obs_pos[i][0]-
                            app.play_game.note_speed / 5.5)
                    newy = app.play_game.obs_pos[i][1]+app.play_game.note_speed 
                    app.play_game.obs_pos[i] = (newx, newy)  
            # move to tracker #2
            elif (app.play_game.obs_pos[i] != None and 
                    app.play_game.obs_path[i] == 2):
                #avoid obstacle
                if (app.play_game.obs_pos[i][1] > 
                    app.play_game.note_ending_position[0][1]+
                    app.delta//2+app.delta//4):
                    app.play_game.obs_pos.pop(i)
                    app.play_game.obs_path.pop(i)
                    app.play_game.obs_pos.insert(i, None)    
                    app.play_game.obs_path.insert(i, None)
                elif (app.play_game.obs_pos[i][1] > 
                        (app.height - app.delta * 3)//2):
                    app.obstacle1 += 1
                    app.score1 += 1
                    app.play_game.obs_pos.pop(i)
                    app.play_game.obs_path.pop(i)
                    app.play_game.obs_pos.insert(i, None)
                    app.play_game.obs_path.insert(i, None)
                else:   
                    newx = app.play_game.obs_pos[i][0]
                    newy = app.play_game.obs_pos[i][1]+app.play_game.note_speed 
                    app.play_game.obs_pos[i] = (newx, newy)  
            # move to tracker #3
            elif (app.play_game.obs_pos[i] != None and 
                    app.play_game.obs_path[i] == 3):
                #avoid obstacle
                if (app.play_game.obs_pos[i][1] > 
                    app.play_game.note_ending_position[0][1]+
                    app.delta//2+app.delta//4):
                    app.play_game.obs_pos.pop(i)
                    app.play_game.obs_path.pop(i)
                    app.play_game.obs_pos.insert(i, None)    
                    app.play_game.obs_path.insert(i, None)
                elif (app.play_game.obs_pos[i][1] > 
                        (app.height - app.delta * 3)//2):
                    app.obstacle1 += 1
                    app.score1 += 1
                    app.play_game.obs_pos.pop(i)
                    app.play_game.obs_path.pop(i)
                    app.play_game.obs_pos.insert(i, None)
                    app.play_game.obs_path.insert(i, None)
                else:  
                    newx = (app.play_game.obs_pos[i][0]+
                            app.play_game.note_speed / 5.5)
                    newy = app.play_game.obs_pos[i][1]+app.play_game.note_speed 
                    app.play_game.obs_pos[i] = (newx, newy)  
            # move to tracker #4
            elif (app.play_game.obs_pos[i] != None and 
                    app.play_game.obs_path[i] == 4):
                #avoid obstacle
                if (app.play_game.obs_pos[i][1] > 
                    app.play_game.note_ending_position[0][1]+
                    app.delta//2+app.delta//4):
                    app.play_game.obs_pos.pop(i)
                    app.play_game.obs_path.pop(i)
                    app.play_game.obs_pos.insert(i, None)    
                    app.play_game.obs_path.insert(i, None)
                elif (app.play_game.obs_pos[i][1] > 
                        (app.height - app.delta * 3)//2):
                    app.obstacle1 += 1
                    app.score1 += 1
                    app.play_game.obs_pos.pop(i)
                    app.play_game.obs_path.pop(i)
                    app.play_game.obs_pos.insert(i, None)
                    app.play_game.obs_path.insert(i, None)
                else:  
                    newx = (app.play_game.obs_pos[i][0]+
                            app.play_game.note_speed / 2.7)
                    newy = app.play_game.obs_pos[i][1]+app.play_game.note_speed 
                    app.play_game.obs_pos[i] = (newx, newy)                      
        app.play_game.placeObs(app)
    #multipliers
    def placeMulti(self, app):
        if not app.gameOver:
            if (app.play_game.multi_pos != None and 
                app.play_game.multi_dropt != []):
                if (abs(app.timePassed-app.play_game.multi_dropt[0]) <= 
                    app.timerDelay//2):
                    path_choose = random.randint(0, 4)
                    app.play_game.multi_path.append(path_choose)
                    app.play_game.multi_dropt.pop(0)
                    app.play_game.multi_pos.append((app.width//2, 0))
                    return 

    def moveMulti(self, app):
        for i in range (len(app.play_game.multi_pos)): 
            if (app.play_game.multi_pos[i] != None and 
                app.play_game.multi_path[i] == 0):
                #miss multiplier
                if (app.play_game.multi_pos[i][1] > 
                    app.play_game.note_ending_position[0][1]+
                    app.delta//2+app.delta//4):
                    app.play_game.multi_pos.pop(i)
                    app.play_game.multi_path.pop(i)
                    app.play_game.multi_pos.insert(i, None)    
                    app.play_game.multi_path.insert(i, None)
                else:   
                    newx = (app.play_game.multi_pos[i][0]-
                            app.play_game.note_speed / 2.7)
                    newy = (app.play_game.multi_pos[i][1]+
                            app.play_game.note_speed)
                    app.play_game.multi_pos[i] = (newx, newy)
            # move to tracker #1
            elif (app.play_game.multi_pos[i] != None and 
                    app.play_game.multi_path[i] == 1):
                #miss multiplier
                if (app.play_game.multi_pos[i][1] > 
                    app.play_game.note_ending_position[0][1]+
                    app.delta//2+app.delta//4):
                    app.play_game.multi_pos.pop(i)
                    app.play_game.multi_path.pop(i)
                    app.play_game.multi_pos.insert(i, None)    
                    app.play_game.multi_path.insert(i, None)
                else:   
                    newx = (app.play_game.multi_pos[i][0]-
                            app.play_game.note_speed / 5.5)
                    newy = (app.play_game.multi_pos[i][1]+
                            app.play_game.note_speed)
                    app.play_game.multi_pos[i] = (newx, newy)  
            # move to tracker #2
            elif (app.play_game.multi_pos[i] != None and 
                    app.play_game.multi_path[i] == 2):
                #miss multiplier
                if (app.play_game.multi_pos[i][1] > 
                    app.play_game.note_ending_position[0][1]+
                    app.delta//2+app.delta//4):
                    app.play_game.multi_pos.pop(i)
                    app.play_game.multi_path.pop(i)
                    app.play_game.multi_pos.insert(i, None)    
                    app.play_game.multi_path.insert(i, None)
                else:   
                    newx = app.play_game.multi_pos[i][0]
                    newy = (app.play_game.multi_pos[i][1]+
                            app.play_game.note_speed) 
                    app.play_game.multi_pos[i] = (newx, newy)  
            # move to tracker #3
            elif (app.play_game.multi_pos[i] != None and 
                    app.play_game.multi_path[i] == 3):
                #miss multiplier
                if (app.play_game.multi_pos[i][1] > 
                    app.play_game.note_ending_position[0][1]+
                    app.delta//2+app.delta//4):
                    app.play_game.multi_pos.pop(i)
                    app.play_game.multi_path.pop(i)
                    app.play_game.multi_pos.insert(i, None)    
                    app.play_game.multi_path.insert(i, None)
                else:  
                    newx = (app.play_game.multi_pos[i][0]+
                            app.play_game.note_speed / 5.5)
                    newy = (app.play_game.multi_pos[i][1]+
                            app.play_game.note_speed)
                    app.play_game.multi_pos[i] = (newx, newy)  
            # move to tracker #4
            elif (app.play_game.multi_pos[i] != None and 
                    app.play_game.multi_path[i] == 4):
                #miss multiplier
                if (app.play_game.multi_pos[i][1] > 
                    app.play_game.note_ending_position[0][1]+
                    app.delta//2+app.delta//4):
                    app.play_game.multi_pos.pop(i)
                    app.play_game.multi_path.pop(i)
                    app.play_game.multi_pos.insert(i, None)    
                    app.play_game.multi_path.insert(i, None)
                else:  
                    newx = (app.play_game.multi_pos[i][0]+
                            app.play_game.note_speed / 2.7)
                    newy = (app.play_game.multi_pos[i][1]+
                            app.play_game.note_speed)
                    app.play_game.multi_pos[i] = (newx, newy)                      
        app.play_game.placeMulti(app)


def gameMode_timerFired(app):
    app.color = random.choice(app.colorL)
    if (app.play_game.note_position == [None] * app.play_game.len):
        app.gameOver = True
        app.songD[f'{app.music_select}-{app.play_game.Mode}'] = [app.perfect, 
                                                                app.great,
                                                                app.miss, 
                                                                app.obstacle,
                                                                app.multi, 
                                                                app.score]
        app.songDict[app.music_select] = app.score
        l = app.songList
        song = app.music_select
        dic = app.songDict
        d = app.songD
        s = Sound(song)
        g = GameMode_Playgame(s, app)
        infor1 = app.hit1
        Intro = app.Intro
        prac = app.prac
        best = app.best 
        pf, gr, ob = app.perfect, app.great, app.obstacle
        mu,sc,mi = app.multi, app.score, app.miss
        pf1, gr1, ob1 = app.perfect1, app.great1, app.obstacle1
        mu1,sc1,mi1 = app.multi1, app.score1, app.miss1
        app.my_score = {app.music_select: [pf, gr, ob, mu, sc, mi]}
        app.AI_score = {app.music_select: [pf1, gr1, ob1, mu1,sc1,mi1]}
        my, other = copy.deepcopy(app.my_score), copy.deepcopy(app.AI_score)
        app.scored = {app.music_select: app.score}
        app.score1d = {app.music_select: app.score1}
        score, score1 = app.scored, app.score1d
        battle = app.battle
        appStarted(app)
        app.songList = l
        app.music_select = song
        app.songDict = dic
        app.gameSound = s
        app.play_game = g
        app.songD = d
        app.hit1 = infor1
        app.Intro = Intro
        app.prac = prac
        app.best = best 
        app.my_score, app.AI_score = my, other
        app.battle = battle 
        app.scored, app.score1d = score, score1
        app.mode = "historyMode"

    elif not app.gameOver: 
        if (app.play_game.note_position != [] and 
            app.play_game.note_position[0] != None and 
            round(abs(app.play_game.note_position[0][1]-app.height+app.delta 
                    * 3))==9):
            app.play_game.playMusic()  
        elif (app.play_game.note_position != [] and 
            app.play_game.note_position[0] == None and 
            app.play_game.note_position.count(None) == 1 and
            not app.gameSound.isPlaying()):
            app.play_game.playMusic()  

        app.play_game.moveNote(app) 
        app.play_game.moveObs(app)
        app.play_game.moveMulti(app)
        app.timePassed += app.timerDelay
        time = app.play_game.travel_time
        if app.timePassed == -(time - 2000):
            app.text, app.font = "3", 90
        elif app.timePassed == -(time - 4000):
            app.text, app.font = "2", 78
        elif app.timePassed == -(time - 6000):
            app.text, app.font = "1", 76
        elif app.timePassed == -(time - 8000):
            app.text, app.font = "GO", 78
        elif app.timePassed == -(time - 10000):
            app.text = "" 

#Helepr: calculate the distance                   
def dist(x1,x2):
    x,y,a,b = x1[0], x1[1], x2[0], x2[1]
    return ((x-a)**2 + (b-y)**2)**0.5

def gameMode_keyPressed(app, event):  
    for i in range (len(app.play_game.randomPath)):
        # keyPress for tracker #0
        if event.key == "q" and app.play_game.randomPath[i] == 0:
            d = dist(app.play_game.note_ending_position[0], 
                        app.play_game.note_position[i])
            #great
            if app.delta//4 < d <= app.delta//2:
                app.great += 1
                app.score += 1
                app.hit1 += [app.play_game.note_position[i]]
                app.play_game.note_position.pop(i)
                app.play_game.randomPath.pop(i)
                app.play_game.note_position.insert(i, None)
                app.play_game.randomPath.insert(i, None)
            #perfect
            elif 0 <= d <= app.delta//4:
                app.perfect += 2
                app.score += 2
                app.hit1 += [app.play_game.note_position[i]]
                app.play_game.note_position.pop(i)
                app.play_game.randomPath.pop(i)
                app.play_game.note_position.insert(i, None)
                app.play_game.randomPath.insert(i, None)
            app.hit += [app.play_game.note_ending_position[0]]
        # keyPress for tracker #1
        elif event.key == "w" and app.play_game.randomPath[i] == 1:
            d = dist(app.play_game.note_ending_position[1], 
                        app.play_game.note_position[i])
            #great
            if app.delta//4 < d <= app.delta//2:
                app.great += 1
                app.score += 1
                app.hit1 += [app.play_game.note_position[i]]
                app.play_game.note_position.pop(i)
                app.play_game.randomPath.pop(i)
                app.play_game.note_position.insert(i, None)
                app.play_game.randomPath.insert(i, None)
            #perfect
            elif 0 <= d <= app.delta//4:
                app.hit1 += [app.play_game.note_position[i]]
                app.perfect += 2
                app.score += 2
                app.play_game.note_position.pop(i)
                app.play_game.randomPath.pop(i)
                app.play_game.note_position.insert(i, None)
                app.play_game.randomPath.insert(i, None)
            app.hit += [app.play_game.note_ending_position[1]]
        # keyPress for tracker #2
        elif event.key == "e" and app.play_game.randomPath[i] == 2:
            d = dist(app.play_game.note_ending_position[2], 
                        app.play_game.note_position[i])
            #great
            if app.delta//4 < d <= app.delta//2:
                app.hit1 += [app.play_game.note_position[i]]
                app.great += 1
                app.score += 1
                app.play_game.note_position.pop(i)
                app.play_game.randomPath.pop(i)
                app.play_game.note_position.insert(i, None)
                app.play_game.randomPath.insert(i, None)
            #perfect
            elif 0 <= d <= app.delta//4:
                app.hit1 += [app.play_game.note_position[i]]
                app.perfect += 2
                app.score += 2
                app.play_game.note_position.pop(i)
                app.play_game.randomPath.pop(i)
                app.play_game.note_position.insert(i, None)
                app.play_game.randomPath.insert(i, None)
            app.hit += [app.play_game.note_ending_position[2]]
        # keyPress for tracker #3
        elif event.key == "o" and app.play_game.randomPath[i] == 3:
            d = dist(app.play_game.note_ending_position[3], 
                        app.play_game.note_position[i])
            #great
            if app.delta//4 < d <= app.delta//2:
                app.great += 1
                app.score += 1
                app.hit1 += [app.play_game.note_position[i]]
                app.play_game.note_position.pop(i)
                app.play_game.randomPath.pop(i)
                app.play_game.note_position.insert(i, None)
                app.play_game.randomPath.insert(i, None)
            #perfect
            elif 0 <= d <= app.delta//4:
                app.perfect += 2
                app.score += 2
                app.hit1 += [app.play_game.note_position[i]]
                app.play_game.note_position.pop(i)
                app.play_game.randomPath.pop(i)
                app.play_game.note_position.insert(i, None)
                app.play_game.randomPath.insert(i, None)
            app.hit += [app.play_game.note_ending_position[3]]
        # keyPress for tracker #4
        elif event.key == "p" and app.play_game.randomPath[i] == 4:
            d = dist(app.play_game.note_ending_position[4], 
                        app.play_game.note_position[i])
            #great
            if app.delta//4 < d <= app.delta//2:
                app.hit1 += [app.play_game.note_position[i]]
                app.great += 1
                app.score += 1
                app.play_game.note_position.pop(i)
                app.play_game.randomPath.pop(i)
                app.play_game.note_position.insert(i, None)
                app.play_game.randomPath.insert(i, None)
            #perfect
            elif 0 <= d <= app.delta//4:
                app.hit1 += [app.play_game.note_position[i]]
                app.perfect += 2
                app.score += 2
                app.play_game.note_position.pop(i)
                app.play_game.randomPath.pop(i)
                app.play_game.note_position.insert(i, None)
                app.play_game.randomPath.insert(i, None)
            app.hit += [app.play_game.note_ending_position[4]]
    # keyPress for AI
    if app.play_game.res != []:
        if app.play_game.res == [1]: 
            app.play_game.res = [None]   
            app.score1 = app.score
        else:
            for i in range (len(app.play_game.res)):
                if app.play_game.res[i] != None:    
                    (x, y) = app.play_game.res[i]
                    #path: tracker 0
                    if app.delta//2 <= x <= app.delta + app.delta//2:
                        d = dist(app.play_game.note_ending_position[0], (x, y))
                        #great
                        if app.delta//4 < d <= app.delta//2:
                            app.great1 += 1
                            app.score1 += 1
                        #perfect
                        elif 0 <= d <= app.delta//4:
                            app.perfect1 += 2
                            app.score1 += 2
                        else:
                            app.miss1 += 1
                            app.score1 -= 2
                        app.play_game.res.pop(i)
                        app.play_game.res.insert(i, None)
                    #path: tracker 1
                    elif app.delta+app.delta//2<x<= 2*app.delta+app.delta//2:
                        d = dist(app.play_game.note_ending_position[1], (x, y))
                        #great
                        if app.delta//4 < d <= app.delta//2:
                            app.great1 += 1
                            app.score1 += 1
                        #perfect
                        elif 0 <= d <= app.delta//4:
                            app.perfect1 += 2
                            app.score1 += 2
                        else:
                            app.miss1 += 1
                            app.score1 -= 2
                        app.play_game.res.pop(i)
                        app.play_game.res.insert(i, None)
                    #path: tracker 2
                    elif 2*app.delta+app.delta//2<x<= 3*app.delta+app.delta//2:
                        d = dist(app.play_game.note_ending_position[2], (x, y))
                        #great
                        if app.delta//4 < d <= app.delta//2:
                            app.great1 += 1
                            app.score1 += 1
                        #perfect
                        elif 0 <= d <= app.delta//4:
                            app.perfect1 += 2
                            app.score1 += 2
                        else:
                            app.miss1 += 1
                            app.score1 -= 2
                        app.play_game.res.pop(i)
                        app.play_game.res.insert(i, None)
                    #path: tracker 3
                    elif 3*app.delta+app.delta//2<x<= 4*app.delta+app.delta//2:
                        d = dist(app.play_game.note_ending_position[3], (x, y))
                        #great
                        if app.delta//4 < d <= app.delta//2:
                            app.great1 += 1
                            app.score1 += 1
                        #perfect
                        elif 0 <= d <= app.delta//4:
                            app.perfect1 += 2
                            app.score1 += 2
                        else:
                            app.miss1 += 1
                            app.score1 -= 2
                        app.play_game.res.pop(i)
                        app.play_game.res.insert(i, None)
                    #path: tracker 4
                    elif 4*app.delta+app.delta//2<x<=5*app.delta+app.delta//2:
                        d = dist(app.play_game.note_ending_position[4], (x, y))
                        #great
                        if app.delta//4 < d <= app.delta//2:
                            app.great1 += 1
                            app.score1 += 1
                        #perfect
                        elif 0 <= d <= app.delta//4:
                            app.perfect1 += 2
                            app.score1 += 2
                        else:
                            app.miss1 += 1
                            app.score1 -= 2
                        app.play_game.res.pop(i)
                        app.play_game.res.insert(i, None)
    # keyPress detect Multipliers
    for i in range (len(app.play_game.multi_path)):
        if app.play_game.multi_pos[i] != None:
            if app.play_game.multi_path[i] == 0 and event.key == "q":
                d = dist(app.play_game.note_ending_position[0], 
                         app.play_game.multi_pos[i])
                if 0 <= d < app.delta//4:
                    app.multi += 1
                    if app.score >= 0:    app.score *= 2
                    app.play_game.multi_pos.pop(i)
                    app.play_game.multi_path.pop(i)
                    app.play_game.multi_pos.insert(i, None)
                    app.play_game.multi_path.insert(i, None)
                elif (app.play_game.note_ending_position[0][1]-app.r//2 < 
                        app.play_game.multi_pos[i][1]< 
                        app.play_game.note_ending_position[0][1]-app.r1 and
                        app.play_game.Mode == "battle"):
                    if app.score1 > 0:    
                        app.score1 *= 2
                        app.multi1 += 1
                    app.play_game.multi_pos.pop(i)
                    app.play_game.multi_path.pop(i)
                    app.play_game.multi_pos.insert(i, None)
                    app.play_game.multi_path.insert(i, None)
                    
            elif app.play_game.multi_path[i] == 1 and event.key == "w":
                d = dist(app.play_game.note_ending_position[1], 
                         app.play_game.multi_pos[i])
                if 0 <= d < app.delta//4:
                    app.multi += 1
                    if app.score >= 0:    app.score *= 2
                    app.play_game.multi_pos.pop(i)
                    app.play_game.multi_path.pop(i)
                    app.play_game.multi_pos.insert(i, None)
                    app.play_game.multi_path.insert(i, None)
                elif (app.play_game.note_ending_position[0][1]-app.r//2 < 
                        app.play_game.multi_pos[i][1]< 
                        app.play_game.note_ending_position[0][1]-app.r1 and
                        app.play_game.Mode == "battle"):
                    if app.score1 > 0:    
                        app.score1 *= 2
                        app.multi1 += 1
                    app.play_game.multi_pos.pop(i)
                    app.play_game.multi_path.pop(i)
                    app.play_game.multi_pos.insert(i, None)
                    app.play_game.multi_path.insert(i, None)

            elif app.play_game.multi_path[i] == 2 and event.key == "e":
                d = dist(app.play_game.note_ending_position[2], 
                         app.play_game.multi_pos[i])
                if 0 <= d < app.delta//4:
                    app.multi += 1
                    if app.score >= 0:    app.score *= 2
                    app.play_game.multi_pos.pop(i)
                    app.play_game.multi_path.pop(i)
                    app.play_game.multi_pos.insert(i, None)
                    app.play_game.multi_path.insert(i, None)
                elif (app.play_game.note_ending_position[0][1]-app.r//2 < 
                        app.play_game.multi_pos[i][1]< 
                        app.play_game.note_ending_position[0][1]-app.r1 and
                        app.play_game.Mode == "battle"):
                    if app.score1 > 0:    
                        app.score1 *= 2
                        app.multi1 += 1
                    app.play_game.multi_pos.pop(i)
                    app.play_game.multi_path.pop(i)
                    app.play_game.multi_pos.insert(i, None)
                    app.play_game.multi_path.insert(i, None)
                    
            elif app.play_game.multi_path[i] == 3 and event.key == "o":
                d = dist(app.play_game.note_ending_position[3], 
                         app.play_game.multi_pos[i])
                if 0 <= d < app.delta//4:
                    app.multi += 1
                    if app.score >= 0:    app.score *= 2
                    app.play_game.multi_pos.pop(i)
                    app.play_game.multi_path.pop(i)
                    app.play_game.multi_pos.insert(i, None)
                    app.play_game.multi_path.insert(i, None)
                elif (app.play_game.note_ending_position[0][1]-app.r//2 < 
                        app.play_game.multi_pos[i][1]< 
                        app.play_game.note_ending_position[0][1]-app.r1 and
                        app.play_game.Mode == "battle"):
                    if app.score1 > 0:    
                        app.score1 *= 2
                        app.multi1 += 1
                    app.play_game.multi_pos.pop(i)
                    app.play_game.multi_path.pop(i)
                    app.play_game.multi_pos.insert(i, None)
                    app.play_game.multi_path.insert(i, None)
                    
            elif app.play_game.multi_path[i] == 4 and event.key == "p":
                d = dist(app.play_game.note_ending_position[4], 
                         app.play_game.multi_pos[i])
                if 0 <= d < app.delta//4:
                    app.multi += 1
                    if app.score >= 0:    app.score *= 2
                    app.play_game.multi_pos.pop(i)
                    app.play_game.multi_path.pop(i)
                    app.play_game.multi_pos.insert(i, None)
                    app.play_game.multi_path.insert(i, None)
                elif (app.play_game.note_ending_position[0][1]-app.r//2 < 
                        app.play_game.multi_pos[i][1]< 
                        app.play_game.note_ending_position[0][1]-app.r1 and
                        app.play_game.Mode == "battle"):
                    if app.score1 > 0:    
                        app.score1 *= 2
                        app.multi1 += 1
                    app.play_game.multi_pos.pop(i)
                    app.play_game.multi_path.pop(i)
                    app.play_game.multi_pos.insert(i, None)
                    app.play_game.multi_path.insert(i, None)
    if app.play_game.Mode == 'intro':
        app.Intro[app.music_select] = app.hit1
        app.best[app.music_select] = app.hit
    elif app.play_game.Mode == 'practice':
        app.prac[app.music_select] = app.hit1
        app.best[app.music_select] = app.hit
    elif app.play_game.Mode == 'battle':
        app.battle[app.music_select] = True

def gameMode_mousePressed(app, event):
    for i in range (len(app.play_game.obs_path)):
        if app.play_game.obs_pos[i] != None:
            d = dist((event.x, event.y), app.play_game.obs_pos[i])
            y = (app.height - app.delta * 3) 
            if 0 <= d <= app.delta//4 and event.y <= y//2:
                app.obstacle += 1
                app.score += 1
                app.play_game.obs_pos.pop(i)
                app.play_game.obs_path.pop(i)
                app.play_game.obs_pos.insert(i, None)
                app.play_game.obs_path.insert(i, None)
                       
def gameMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, 
                        image=ImageTk.PhotoImage(app.g_image))
    y = app.height - app.delta * 3       # =451
    canvas.create_line(0, y, app.width, y, fill="brown", width=3)
    gameMode_drawTrackers(app, canvas)
    gameMode_drawScoreBasket(app, canvas)
    gameMode_countDown(app, canvas)
    if not app.gameOver:
        for i in app.play_game.note_position:
            if i != None:
                x,y = i[0], i[1]
                index = app.play_game.note_position.index((x,y))
                canvas.create_oval(x-app.r1, y-app.r1,
                                    x+app.r1, y+app.r1, 
                                    fill=app.play_game.color_choice[index])
        #draw free-hit; also called "obstacle" in the code 
        for i in app.play_game.obs_pos:    
            if i != None:
                x, y = i[0], i[1]
                canvas.create_oval(x-app.r1, y-app.r1,
                                    x+app.r1, y+app.r1,
                                    fill="white")
                canvas.create_rectangle(x-app.r1, y-app.r1,
                                        x+app.r1, y+app.r1,
                                        outline = "red", width = 3)
        #draw multiplier
        for i in app.play_game.multi_pos:   
            if i != None:
                x, y = i[0], i[1]
                canvas.create_oval(x-app.r1, y-app.r1,
                                    x+app.r1, y+app.r1,
                                    fill="brown")
                x0 = x-app.r1+(x+app.r1-(x-app.r1))//2
                y0 = y-app.r1+(y+app.r1-(y-app.r1))//2
                canvas.create_text(x0, y0, text="x2", fill="#0080FF", 
                                    font="Arial 30 bold")
        if (len(app.play_game.note_position) == app.play_game.len and 
            app.play_game.note_position[-3] == None):
            if app.score > 50:  x = 'Good Job !!!'
            elif app.score < 50:    x = 'Try Again !!!'
            canvas.create_text(app.width//2, app.height//2, 
                                fill=random.choice(["#0080FF","white"]),
                                font="Arial 20 bold", text=x)
#helper: draw 5 trackers
def gameMode_drawTrackers(app, canvas):
    d = app.delta
    x1, y1, x2, y2 = 0, app.height, d, 0
    x3, y3, x4, y4 = 5*d, 0, app.width, app.height
    canvas.create_line(x1, y1, x2, y2, fill="silver", width=5)
    canvas.create_line(x3, y3, x4, y4, fill="silver", width=5)
    cx, cy, r = d, app.height-d*3, d//2
    colorL = ["pink","blue","green","purple","yellow"]
    for i in range (5): # have 5 trackers
        color = colorL[0]
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, outline=color, width=3)  
        canvas.create_oval(cx-r//2, cy-r//2, cx+r//2, cy+r//2, fill=color)  
        cx, cy, r = cx+d, cy, r
        colorL.pop(0)
#draw score baskets
def gameMode_drawScoreBasket(app, canvas):
    L = []
    r = app.delta//4
    x,y = app.delta + 2*r, app.height-app.delta*3 + 3*r
    xa1, ya1, xa2, ya2 = app.delta, y, app.delta+4*r, y
    L.append((xa1, ya1, xa2, ya2))
    xb1, yb1, xb2, yb2 = xa1, ya1, xa1-r, ya1+2*r
    xB1, yB1, xB2, yB2 = xa2, ya2, xa2+r, ya2+2*r
    L += [(xb1, yb1, xb2, yb2), (xB1, yB1, xB2, yB2)]
    xc1, yc1, xc2, yc2 = xb2, yb2, xa1+(xa2-xa1)//2, yb1+7*r
    xC1, yC1, xC2, yC2 = xB2, yB2, xc2, yc2
    L += [(xc1, yc1, xc2, yc2), (xC1, yC1, xC2, yC2)]
    xd1, yd1, xd2, yd2 = xa1+(xa2-xa1)//3-10, ya1, xb2+(xB2-xb2)//4*3, yb1+4.5*r
    xD1, yD1, xD2, yD2 = xa1+(xa2-xa1)//3*2+10, ya1, xb2+(xB2-xb2)//4, yd2
    L += [(xd1, yd1, xd2, yd2), (xD1, yD1, xD2, yD2)]
    L += [(xb2,yb2,xB2,yB2)]
    xe1, ye1, xe2, ye2 = xa1, ya1, xb2+(xB2-xb2)//10, yb2
    xE1, yE1, xE2, yE2 = xa2, ya2, xB2-(xB2-xb2)//10, yB2
    L += [(xe1, ye1, xe2, ye2), (xE1, yE1, xE2, yE2)]
    xf1, yf1, xf2, yf2 = xe2, ye2, xe1, yb2+1.6*r
    xF1, yF1, xF2, yF2 = xE2, yE2, xE1, yf2
    L += [(xf1, yf1, xf2, yf2), (xF1, yF1, xF2, yF2)]
    xg1, yg1, xg2, yg2 = xf1, yf1, xc2, yc2
    xG1, yG1, xG2, yG2 = xF1, yF1, xC2, yC2
    L += [(xg1, yg1, xg2, yg2), (xG1, yG1, xG2, yG2)]
    L_mid = gameMode_scoreBasket_helper(L, r)
    L_left = gameMode_scoreBasket_helper(L_mid, r)
    gameMode_drawBasket_helper(L, app, canvas)
    canvas.create_text(L[0][0]+(L[0][2]-L[0][0])//2, L[0][1]+r, 
                        text="free-hit", fill=app.color,
                        font='Arial 20 bold')
    canvas.create_text(L[0][0]+(L[0][2]-L[0][0])//2, L[0][1]+4*r, 
                        text=f'{app.obstacle}', fill="pink",
                        font='Arial 20 bold')    
    gameMode_drawBasket_helper(L_mid, app, canvas)
    canvas.create_text(L_mid[0][0]+(L_mid[0][2]-L_mid[0][0])//2, L[0][1]+r, 
                        text="score", fill=app.color,
                        font='Arial 20 bold')
    canvas.create_text(L_mid[0][0]+(L_mid[0][2]-L_mid[0][0])//2, L[0][1]+4*r, 
                        text=f'{app.score}', fill="pink", 
                        font='Arial 20 bold')
    gameMode_drawBasket_helper(L_left, app, canvas)
    canvas.create_text(L_left[0][0]+(L_left[0][2]-L_left[0][0])//2, L[0][1]+r, 
                        text="multiplier", fill=app.color,
                        font='Arial 20 bold')
    canvas.create_text(L_left[0][0]+(L_left[0][2]-L_left[0][0])//2, L[0][1]+4*r, 
                        text=f'{app.multi}', fill="pink",
                        font='Arial 20 bold')

def gameMode_drawBasket_helper(L, app, canvas):
    for i in L:
        x, y, z, k = i[0], i[1], i[2], i[3]
        canvas.create_line(x, y, z, k, fill=app.color, width=3)

def gameMode_scoreBasket_helper(L, r):
    res = []
    for val in L:
        cur_tuple = [list(val)[1],list(val)[3]]
        for i in [list(val)[0],list(val)[2]]:
            index = list(val).index(i)
            i += 6.5*r
            cur_tuple.insert(index,i)
        res += [cur_tuple]
    return res 
#countdown
def gameMode_countDown(app, canvas):
    canvas.create_text(app.width//2, app.height//2-20, text=app.text,
                        fill="Yellow",font=f'Arial {app.font} bold')

################################################################################
# historyMode
################################################################################

def historyMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, 
                        image=ImageTk.PhotoImage(app.historyImage))
    canvas.create_text(app.his_x, 15, text='Press f: return to main page!' +  
                        ' After BATTLE mode, click the mouse to enter the song' 
                        + ' file name, then click l for detailed information !',
                       font='Arial 20 bold', fill='black')
    canvas.create_text(app.width/2, 40, text='Your History', 
                       font='Arial 26 bold', fill='black')
    if app.songDict != {}:    
        historyMode_showScore(app, canvas)

#display score
def historyMode_showScore(app, canvas):
    x1, y1 = app.width/5, app.height/9
    x2, y2 = app.width-app.width/5, app.height/7
    a1, a2 = x1+(x2-x1)//2, y1+(y2-y1)//2
    for s in app.songD:
        canvas.create_text(a1, a2, text=f'{s}: {app.songD[s][-1]}',
                            font='Arial 18 bold', 
                            fill='#FF66B2')
        d = y2 - y1
        x1, y1 = x1, y1+d+20
        x2, y2 = x2, y1+d
        a1, a2 = x1+(x2-x1)//2, y1+(y2-y1)//2

def historyMode_mousePressed(app, event):
    name = app.getUserInput('Enter the song file name: ')
    if (name == None or name == ""): 
        app.showMessage('You Cancelled...')
    elif name[-3:] != 'mp3':
        app.showMessage('Song file name should end with .mp3')
    elif (name in app.my_score and name in app.AI_score and
            name not in app.battle):
        app.showMessage('Need to complete Intro, Practice, and Battle first<')
    elif (name not in app.my_score and name not in app.AI_score and
            name not in app.battle):
        app.showMessage('Need to complete Intro, Practice, and Battle first<')
    elif (name in app.my_score and name in app.AI_score and 
            app.battle[name] == True):
        app.showMessage('You entered: ' + name)
        app.stat_song = name

def historyMode_timerFired(app):
    if app.his_x < -600:
        app.his_x = app.width + 200
    else:   app.his_x -= 10

def historyMode_keyPressed(app, event):
    if event.key == "f":
        if app.songList != []:
            l = app.songList
            song = app.music_select
            dic = app.songDict
            d = app.songD
            s = Sound(song)
            g = GameMode_Playgame(s, app)
            infor1 = app.hit1
            Intro = app.Intro
            prac = app.prac
            best = app.best
            name = app.stat_song
            pf, gr, ob = app.perfect, app.great, app.obstacle
            mu,sc,mi = app.multi, app.score, app.miss
            pf1, gr1, ob1 = app.perfect1, app.great1, app.obstacle1
            mu1,sc1,mi1 = app.multi1, app.score1, app.miss1
            app.my_score = {app.music_select: [pf, gr, ob, mu, sc, mi]}
            app.AI_score = {app.music_select: [pf1, gr1, ob1, mu1,sc1,mi1]}
            app.scored = {app.music_select: app.score}
            app.score1d = {app.music_select: app.score1}
            score, score1 = app.scored, app.score1d
            my, other = copy.deepcopy(app.my_score), copy.deepcopy(app.AI_score)
            appStarted(app)
            app.songList = l
            app.music_select = song
            app.songDict = dic
            app.gameSound = s
            app.play_game = g
            app.songD = d
            app.hit1 = infor1 
            app.Intro = Intro
            app.prac = prac
            app.best = best
            app.scored, app.score1d = score, score1
            app.perfect, app.great, app.obstacle =  pf, gr, ob
            app.multi, app.score, app.miss = mu,sc,mi
            app.perfect1, app.great1, app.obstacle1 = pf1, gr1, ob1
            app.multi1, app.score1, app.miss1 = mu1, sc1, mi1
            app.my_score, app.AI_score = my, other
            app.stat_song = name
        app.bk_song = "Don't Go.mp3"
        app.mode = 'splashScreenMode'
    # statMode (see score plot)
    if event.key == 'l':
        if app.stat_song != '':
            print(app.my_score, app.AI_score, app.battle, app.score1, app.score)
            app.mode = 'statMode'

################################################################################
# statMode (display score)
################################################################################
def statMode_redrawAll(app, canvas):
    canvas.create_image(app.width/2, app.height/2, 
                        image=ImageTk.PhotoImage(app.statImage))
    canvas.create_text(app.stat_x, 15, text='Press s: return to history page!',
                       font='Arial 20 bold', fill='#B266FF')
    canvas.create_text(app.width//2, 150, text=app.stat_song[:-4],
                       font='Arial 20 bold', fill='black')
    a, b, c, d = app.delta*4.5, 60, app.width-10, 60+app.delta
    canvas.create_rectangle(a, b, c, d)
    canvas.create_text((c-a)//2+a, (d-b)//3+b, text='Me: red',
                       font='Arial 18 bold', fill='#FF6666')
    canvas.create_text((c-a)//2+a, (d-b)//3*2+b, text='EXO: blue',
                       font='Arial 18 bold', fill='#3399FF')
    #x-axis
    x, y = app.delta//1.5, app.height-app.delta*2.5
    z, k = app.width-app.delta//2, y
    #y-axis
    m, l, o, p = x, app.delta*2.2, x, y
    canvas.create_line(x, y, z, k, width=2)
    canvas.create_line(m, l, o, p, width=2)
    canvas.create_line(m, l, m-10, l+10*1.73, width=2)
    canvas.create_line(m, l, m+10, l+10*1.73, width=2)
    canvas.create_line(z, k, z-10*1.73, p-10, width=2)
    canvas.create_line(z, k, z-10*1.73, p+10, width=2)
    canvas.create_text(z+12, k+12, text="type",
                       font='Arial 16 bold', fill='black')
    canvas.create_text(m-9, l-10, text="hit number",
                       font='Arial 16 bold', fill='black')
    #sub-unit
    dx, dy = (z-x) // 6, (p-l) // 9
    types = ['perfect', 'great', 'multiplier', 'miss', 'free-hit']
    nums = ['8', '16', '24', '32', '40', '48', '56', '64']
    sta = app.delta//1.5
    for i in range (len(types)):
        canvas.create_line(sta+dx*(i+1), y-3, sta+dx*(i+1), y+3, width=2)
        canvas.create_text(sta+dx*(i+1), y+15, text=types[i], 
                            font='Arial 16 bold')
    st = app.height-app.delta*2.5
    y_cor = []
    for n in range (len(nums)):
        canvas.create_line(app.delta//1.5-3, st-dy*(n+1), app.delta//1.5+3, 
                            st-dy*(n+1), width=2)
        canvas.create_text(app.delta//1.5-20, st-dy*(n+1), text=nums[n], 
                            font='Arial 16 bold')
        y_cor.append(st-dy*(n+1))
    # get the position of each value 
    cor_me = score_helper(app.my_score[app.stat_song], sta, dx, y_cor, dy)
    cor_AI = score_helper(app.AI_score[app.stat_song], sta, dx, y_cor, dy)
    statMode_draw_score(app.my_score[app.stat_song], cor_me, app, canvas, 
                        '#FF6666')
    statMode_draw_score(app.AI_score[app.stat_song], cor_AI, app, canvas, 
                        '#3399FF')
    canvas.create_text(app.delta*3, app.height-app.height//4 + 10, 
                        fill='#FF6666', 
                        text=f'My Score: {app.scored[app.music_select]}', 
                        font='Arial 15 bold')
    canvas.create_text(app.delta*3, app.height-app.height//4 + 30, 
                        fill='#3399FF', 
                        text=f'EXO Score: {app.score1d[app.music_select]}', 
                        font='Arial 15 bold')

def score_helper(l, sta, dx, y_cor, dy):
    res = []
    L = l[:2] + [l[3]] + [l[5]] + [l[2]]
    #[perfect, great, free-hit, multiplier, total, miss]
    for i in range (len(L)):
        #perfect
        if i == 0:
            y = find_y(L[0], y_cor, dy)
            res.append([sta+dx, y])
        #great
        elif i == 1:
            y = find_y(L[1], y_cor, dy)
            res.append([sta+dx*2, y])
        #multiplier
        elif i == 2: 
            y = find_y(L[2], y_cor, dy)
            res.append([sta+dx*3, y])
        #miss
        elif i == 3:
            y = find_y(L[3], y_cor, dy)
            res.append([sta+dx*4, y])
        #free-hit
        elif i == 4:
            y = find_y(L[4], y_cor, dy)
            res.append([sta+dx*5, y])
    return res

def find_y(n, y_cor, dy):
    #          8      16      24        32     40    48     56     64   
    #y_cor = [458.5, 424.5,  390.5,   356.5, 322.5, 288.5, 254.5, 220.5]
    #dy = 34
    y = 0
    if 0 <= n <= 8:    y = (y_cor[0] + dy) - dy*(n/10)
    elif 8 < n <= 16:  y = (y_cor[1] + dy) - dy*(n/20)
    elif 16 < n <= 24:  y = (y_cor[2] + dy) - dy*(n/30)
    elif 24 < n <= 32:  y = (y_cor[3] + dy) - dy*(n/40)
    elif 32 < n <= 40:  y = (y_cor[4] + dy) - dy*(n/50)
    elif 40 < n <= 48:  y = (y_cor[5] + dy) - dy*(n/60)
    elif 48 < n <= 56:  y = (y_cor[6] + dy) - dy*(n/70)
    elif 56 < n <= 64:  y = (y_cor[7] + dy) - dy*(n/80)
    elif 64 < n:  y = y_cor[7] - dy//2
    return y

def statMode_draw_score(l1, l, app, canvas, color):
    #draw dot
    r = 1
    n = 0
    L1 = l1[:2] + [l1[3]] + [l1[5]] + [l1[2]]
    for (x,y) in l:
        canvas.create_oval(x-r, y-r, x+r, y+r, fill=color, outline=color, 
                            width=3)
        #indicate number
        if color == '#FF6666':
            canvas.create_text(x, y-9, text=L1[n], font='Arial 15', fill=color)
        elif color == '#3399FF':
            canvas.create_text(x, y+9, text=L1[n], font='Arial 15', fill=color)
        n += 1
    #draw lines to connect each dot
    for i in range (len(l)):
        if i < len(l) - 1:
            canvas.create_line(l[i][0], l[i][1], l[i+1][0], l[i+1][1], 
                                fill=color, width=1)

def statMode_timerFired(app):
    if app.stat_x < -200:
        app.stat_x = app.width + 100
    else:   app.stat_x -= 20

def statMode_keyPressed(app, event):
    if event.key == 's':
        l = app.songList
        song = app.music_select
        dic = app.songDict
        d = app.songD
        s = Sound(song)
        g = GameMode_Playgame(s, app)
        infor1 = app.hit1
        Intro = app.Intro
        prac = app.prac
        best = app.best
        pf, gr, ob = app.perfect, app.great, app.obstacle
        mu,sc,mi = app.multi, app.score, app.miss
        pf1, gr1, ob1 = app.perfect1, app.great1, app.obstacle1
        mu1,sc1,mi1 = app.multi1, app.score1, app.miss1
        app.my_score = {app.music_select: [pf, gr, ob, mu, sc, mi]}
        app.AI_score = {app.music_select: [pf1, gr1, ob1, mu1,sc1,mi1]}
        my, other = copy.deepcopy(app.my_score), copy.deepcopy(app.AI_score)
        name = app.stat_song
        app.scored = {app.music_select: app.score}
        app.score1d = {app.music_select: app.score1}
        score, score1 = app.scored, app.score1d
        appStarted(app)
        app.songList = l
        app.music_select = song
        app.songDict = dic
        app.gameSound = s
        app.play_game = g
        app.songD = d
        app.hit1 = infor1 
        app.Intro = Intro
        app.prac = prac
        app.best = best
        app.perfect, app.great, app.obstacle = pf, gr, ob
        app.multi, app.score, app.miss = mu,sc,mi
        app.perfect1, app.great1, app.obstacle1 = pf1, gr1, ob1
        app.multi1, app.score1, app.miss1 = mu1, sc1, mi1
        app.my_score, app.AI_score = my, other
        app.my_score, app.AI_score = my, other
        app.stat_song = name
        app.scored, app.score1d = score, score1
        app.mode = 'historyMode'


################################################################################
# Main App
################################################################################
#sound class
#https://www.cs.cmu.edu/~112/notes/notes-animations-part4.html#playingSoundsWith
#Pygame 
class Sound(object):
    def __init__(self, path):
        self.sound_name = path[0:-4]
        self.sound_path = path
        self.beatLst = onsettimes_list(self.sound_path)
        self.height = 534
        pygame.mixer.music.load(self.sound_path)

    def isPlaying(self):
        return bool(pygame.mixer.music.get_busy())

    def start(self, loops=False):
        self.loops = loops
        pygame.mixer.music.play(loops=loops)

    def stop(self):
        pygame.mixer.music.stop()

def appStarted(app):
    #1. splashScreenMode
    app.counter = 0
    app.mainpageImage = app.loadImage("MainPage.jpg")
    app.message = 'Click the mouse to enter your name!'
    app.exo = '''EXO is a South Korean-Chinese boy band based in Seoul, 
                consisting of nine members: Xiumin, Suho, Lay, Baekhyun, Chen, 
                Chanyeol, D.O., Kai and Sehun. The band was formed by SM 
                Entertainment in 2011 and debuted in 2012. The fan name is 
                EXO-L.'''.split()
    app.intro = ("1. Select Your Own Music. " + "---> 2. Enjoy Your Game! --->" 
                + "3.Don't forget to Check History!" + 
                "<YOU WILL SEE GAME RULES AFTER ENTERING THE GAME>..." + 
                " HAVE FUN!!!")
    app.introX = app.width+(len(app.intro)*3)
    app.instruct=('''       There will be five trackers, and pieces are randomly
        generated. From left to right, each tracker represents the letter in 
        ['q','w','e','o','p']. <hit as precise as you can!>

       * INTRO & PRACTICE: single-player; BATTLE: play with EXO! *

       * Perfect = 2 points; Great == 1 points; Missing = -5 points *

       * Click free-hit(circle inside red box) when it's in the top half of  
         the screen-> 1 point; otherwise, you lose the chance but no penalty *
    
       * Hit multiplier (x2 inside a circle) as regular pieces only within 
         'perfect' constrain, score multiplies by 2 *
    ''')
    app.instruct2=('''
    * Note: In BATTLE, 

                1. when free-hit moves to the second half of the 
                    screen, 1 point counts to EXO

                2. if you didn't hit multiplier within 'perfect', mutiplier 
                    counts to EXO

                Get ready for BATTLE by doing INTRO & PRACTICE first

                GOOD LUCK !!!                                         
                   ''')
    app.update = app.width/8
    app.oval1_x1, app.oval1_y1 = app.update/2, app.height/2+app.update
    app.oval1_x2, app.oval1_y2 = app.update*2.5, app.height/2+app.update*2.5
    app.r = app.oval1_x2 - app.oval1_x1
    app.oval2_x1, app.oval2_y1 = app.oval1_x2 + app.update//2, app.oval1_y1
    app.oval2_x2, app.oval2_y2 = app.oval2_x1+app.r, app.oval1_y2
    app.oval3_x1, app.oval3_y1 = app.oval2_x2 + app.update//2, app.oval1_y1
    app.oval3_x2, app.oval3_y2 = app.oval3_x1+app.r, app.oval1_y2
    app.bk_song = "Don't Go.mp3"
    app.bk_vol = 0.2
    #2. importSongMode
    app.musicImport_image = app.loadImage("selectSong.jpg")
    app.music_select = "No song so far..."
    app.songList = []
    app.songDict = {}
    pygame.mixer.init()
    app.song = soundStarted(app.bk_song, app.bk_vol)
    #3. GameMainPageMode
    app.game_Image = app.loadImage("game_image.jpeg")
    app.counter1 = 0
    #4. GameMode -- class
    app.g_image = app.loadImage("g.jpeg")
    app.gameSound = None 
    app.play_game = None
    app.delta = app.width//6
    app.cx = app.width//2
    app.cy = 0        
    app.r1 = 20
    app.timerDelay = 200
    app.timePassed = 0
    app.text, app.font = "", 20
    app.perfect, app.great, app.miss, app.obstacle, app.multi = 0, 0, 0, 0, 0
    app.perfect1, app.great1, app.miss1, app.obstacle1, app.multi1 = 0,0,0,0,0
    app.score, app.score1 = 0, 0 #score of player, score of AI
    app.gameOver = False 
    app.colorL = ["white", "silver"]
    app.color = ""
    app.songD = {}
    app.hit1 = []
    app.Intro = {}
    app.prac = {}
    app.hit = []
    app.best = {}
    app.my_score = {app.music_select: [app.perfect, app.great, 
                                        app.obstacle, app.multi, 
                                        app.score, app.miss]}
    app.AI_score = {app.music_select: [app.perfect1, app.great1, 
                                        app.obstacle1, app.multi1, 
                                        app.score1, app.miss1]}
    app.battle = {}
    #5. historyMode
    app.his_x = app.width + 200
    app.historyImage = app.loadImage("history.jpg")
    #5. stat (score plot)
    app.stat_song = ''
    app.statImage = app.loadImage("stat.jpg")
    app.stat_x = app.width + 100
    app.score1d = {}
    app.scored = {}
    # main
    app.mode = 'splashScreenMode'

def soundStarted(file, volume):
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()

def sound_isPlaying():
    return bool(pygame.mixer.music.get_busy())

runApp(width=500, height=700)