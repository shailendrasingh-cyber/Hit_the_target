import tkinter as tk
from typing import List
import random
import time

# Reset game
global LBL_SCORE
global BTN_RESET

# Introduction
global FRM_USER_INFO
global LBL_USER
global ENT_USERNAME
global BTN_SUBMIT

# Choose Level
global FRM_LEVELS
global LBL_LEVEL
global BTN_EASY
global BTN_INTERMEDIATE
global BTN_HARD

# Game Layout variables
global FRM_INFO
global LBL_USERNAME
global LBL_POINTS
global LBL_TIME
global FRM_GAME
global BTN_TARGET

game_settings = {
    'username': "",
    'difficulty_chosen': "",
    'easy': { 
        'x': 6, 
        'y': 3,
        'x_axis_max': 485,
        'y_axis_max': 485},
    'intermediate': { 
        'x': 3, 
        'y': 1,
        'x_axis_max': 510,
        'y_axis_max': 515},
    'hard': { 
        'x': 0, 
        'y': 0,
        'x_axis_max': 530,
        'y_axis_max': 515}
}


def introduction():
    global FRM_USER_INFO
    global LBL_USER
    global ENT_USERNAME
    global BTN_SUBMIT

    FRM_USER_INFO = tk.Frame(master=window)
    FRM_USER_INFO.pack(fill=tk.BOTH, expand=True)

    LBL_USER = tk.Label(master=FRM_USER_INFO, text="Choose a username: ", font=("Arial", 20), pady=15)
    LBL_USER.pack()

    ENT_USERNAME = tk.Entry(master=FRM_USER_INFO, font=("Arial", 12))
    ENT_USERNAME.pack()

    BTN_SUBMIT = tk.Button(master=FRM_USER_INFO, text="Submit", command=game_levels, font=("Arial", 12))
    BTN_SUBMIT.pack()

    LBL_GAME_DETAILS = tk.Label(master=FRM_USER_INFO, text="The goal of this game is to click on \nthe black square as quick as possible \n before the time runs out.", font=("Arial", 13))
    LBL_GAME_DETAILS.place(width=280, x=140, y=150)


def game_levels():
    """
    Function to display and choose difficulty of level
    """

    global FRM_LEVELS
    global LBL_LEVEL
    global BTN_EASY
    global BTN_INTERMEDIATE
    global BTN_HARD
    global game_settings

    game_settings['username'] = ENT_USERNAME.get()

    FRM_USER_INFO.pack_forget()
    LBL_USER.pack_forget()
    ENT_USERNAME.pack_forget
    BTN_SUBMIT.pack_forget()

    FRM_LEVELS = tk.Frame(master=window, height=550, width=550, borderwidth=4, relief=tk.SUNKEN)
    FRM_LEVELS.pack(fill=tk.BOTH)

    LBL_LEVEL = tk.Label(master=FRM_LEVELS, text="Choose a Level:", pady=20, font=("Arial", 15))
    LBL_LEVEL.pack()

    BTN_EASY = tk.Button(
        master=FRM_LEVELS, 
        text="Easy", 
        height=3, width=15, 
        font=("Arial", 12),
        command=lambda : game_layout(game_settings['username'], game_settings['easy'])
        )

    BTN_INTERMEDIATE = tk.Button(
        master=FRM_LEVELS, 
        text="Intermediate", 
        height=3, width=15,
        font=("Arial", 12),
        command=lambda : game_layout(game_settings['username'], game_settings['intermediate'])
        )

    BTN_HARD = tk.Button(
        master=FRM_LEVELS, 
        text="Hard", 
        height=3, width=15,
        font=("Arial", 12),
        command=lambda : game_layout(game_settings['username'], game_settings['hard'])
        )

    BTN_EASY.pack(side=tk.TOP, fill=tk.BOTH)
    BTN_INTERMEDIATE.pack(side=tk.TOP, fill=tk.BOTH)
    BTN_HARD.pack(side=tk.TOP, fill=tk.BOTH)


def game_layout(username: str, difficulty: List):
    """
    Functions to display the game layout
    """

    global FRM_INFO
    global LBL_USERNAME
    global LBL_POINTS
    global LBL_TIME
    global FRM_GAME
    global BTN_TARGET

    FRM_LEVELS.pack_forget()
    LBL_LEVEL.pack_forget()
    BTN_EASY.pack_forget()
    BTN_INTERMEDIATE.pack_forget()
    BTN_HARD.pack_forget()

    # Display username and points
    FRM_INFO = tk.Frame(master=window, padx=10, pady=10)
    LBL_USERNAME = tk.Label(master=FRM_INFO, text=username, font=("Arial", 15))
    LBL_POINTS = tk.Label(master=FRM_INFO, text=0, font=("Arial", 15))
    LBL_TIME = tk.Label(master=FRM_INFO, text=10, font=("Arial", 15))

    FRM_INFO.pack(fill=tk.BOTH, side=tk.TOP)
    LBL_USERNAME.pack(side=tk.LEFT)
    LBL_POINTS.pack(side=tk.LEFT)
    LBL_TIME.pack(side=tk.RIGHT)

    # Game
    FRM_GAME = tk.Frame(master=window, height=550, width=550, relief=tk.SUNKEN, borderwidth=4)
    BTN_TARGET = tk.Button(
        master=FRM_GAME, 
        height=difficulty['y'], 
        width=difficulty['x'],
        borderwidth=3,
        command=lambda: btn_position(difficulty),
        bg="black"
    )

    FRM_GAME.pack()
    BTN_TARGET.place(x=230, y=230)
    
    timer()


def btn_position(game_level):
    x_axis = random.randint(0, game_level['x_axis_max'])
    y_axis = random.randint(0, game_level['y_axis_max'])
    LBL_POINTS['text'] += 1
    BTN_TARGET.place(x=x_axis, y=y_axis)


def timer():
    global LBL_TIME
    global BTN_TARGET
    global FRM_GAME
    global LBL_POINTS
    global LBL_SCORE
    global BTN_RESET

    LBL_TIME['text'] -= 1

    if LBL_TIME['text'] == 0:
        BTN_TARGET.place_forget()

        LBL_SCORE = tk.Label(master=FRM_GAME, text=f"Your score was: {LBL_POINTS['text']}", font=("Arial", 20))
        LBL_SCORE.place(x=150, y=170)

        BTN_RESET = tk.Button(master=FRM_GAME, text="Try Again", command=reset, width=10)
        BTN_RESET.place(x=230, y=220)
        return 0

    LBL_TIME.after(1000, timer)


def reset():
    global LBL_SCORE
    global BTN_RESET
    global FRM_INFO
    global FRM_GAME

    LBL_SCORE.pack_forget()
    BTN_RESET.pack_forget()
    FRM_INFO.pack_forget()
    FRM_GAME.pack_forget()

    game_levels()


window = tk.Tk()
window.title("Hit the target if you can")
window.geometry("560x600")

introduction()

window.mainloop()