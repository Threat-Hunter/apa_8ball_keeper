import json
import os
from db import db
from seasons import seasons

def start():
    print_header()
    db.json_check()
    seasons.archive_check()
    menu()
    menu_input()


def print_header():
    print("""
    ___________________________________
                                    ___`.
   _______________________________,'   \ `.
   ______________________________/,d$$$/   `.
                ,-.     ,-.       `$$$`.     `.
   :::::======o(   )   ((2))          `.`.     `.
                `-'     `-'             `.`.     `.
                         ,-.              `.`.     `.
                        ((7))               `.`.     `.
                         `-'                  `.`.
     `Two-ball in the corner-pocket'            `.
""")
    print("--------------------------------------")
    print("__APA 8 Ball Team & Player Collector__")
    print("--------------------------------------")

def menu():
    print("------------------------------")
    print("|       Menu Options         |")
    print("------------------------------")
    print("Start a [S]eason")
    print("[A]rchive a Season")
    print("Add a [T]eam")
    print("Add a [P]layer (to a team)")
    print("[R]emove a Player (from a team)")
    print("[U]date a Player Skill Level")
    print("[S]tart a Match!")
    print("E[X]it")


def menu_input():
    menu_choice = ''
    while menu_choice.lower() != 'x':
        menu_choice = input("Selection: ").lower()
        if menu_choice == 's':
            seasons.season_start()
            menu()
        elif menu_choice == 'a':
            seasons.archive_season()
            menu()
        elif menu_choice == 't':
            add_team()
            menu()
        elif menu_choice == 'p':
            add_player()
            menu()
        elif menu_choice == 'r':
            remove_player()
        elif menu_choice == 'u':
            update_player()
        elif menu_choice == 's':
            print("Let's play some pool!")
        elif menu_choice == 'x':
            print("Exiting...")
            exit()
        else:
            print("No valid selection given, please try again.")

def add_team():
    print("Let's add a new team!")
    team_name = input("Enter the team name here: ")
    team_num = input("Enter the team number here: ")
    print("Comitting data to database... ")
    teams[team_name] = team_name, team_num
    with open('teams.json', 'w') as teams_json:
        json.dump(teams, teams_json)

def add_player():
    print("Let's add some players!")
    player_name = input("Enter the players name: ")
    skill_level = input("Enter the players skill level: ")
    player_team = input("Enter the team number for this player: ")
    print("Commiting data to database... ")
    players[player_name] = player_name, skill_level, player_team
    with open('players.json', 'w') as players_json:
        json.dump(players, players_json)

def remove_player():
    remove_player_name = input("Which player should be removed? ")
    if remove_player_name in players:
        del players[remove_player_name]
    else:
        print("Sorry", remove_player_name, "was not found!")

def update_player():
    update_player_data = input("Which player should be updated? ")
    if update_player_data in players:
        del players[update_player_data]
        print("Removing players data... ")
        print("Now let's re-add that player with the correct info...")
        add_player()
    else:
        print("Sorry", update_player_data, "was not found!")

players = {}
teams = {}
start()
