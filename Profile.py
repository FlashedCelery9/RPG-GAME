import tkinter as tk
import json
from tkinter import PhotoImage

import main
from Auth import login
from main import restart

global_coins = 0
global_damage = 0
global_hp = 0
players_stats = {}
players_artifacts = []
artifacts_list = ['Leg sword', 'Health']
leg_sword = False
angel_hp = False
class PlayerProfile:
    def __init__(self, player_name: str):
        self.player_name = player_name
        self.artifact_list = artifacts_list
        self.players_artifacts = players_artifacts
        self.global_coins = global_coins
        self.global_hp = global_hp
        self.global_damage = global_damage
        self.leg_sword = leg_sword
        self.angel_hp = angel_hp
        try:
            with (open('DataBase/Profile_info.json', 'r', encoding='utf-8')) as rd:
                self.players_stats = json.load(rd)
                self.global_coins = self.players_stats[self.player_name]['Coins']
                self.global_damage = self.players_stats[self.player_name]['Global_Damage']
                self.global_hp = self.players_stats[self.player_name]['Global_Hp']
                self.players_artifacts = self.players_stats[self.player_name]['Artifacts']
                if 'Leg sword' in self.players_artifacts:
                    self.leg_sword = True
                elif 'Health' in self.players_artifacts:
                    self.angel_hp = True




        except:
            self.players_stats = {}
        if self.player_name not in self.players_stats:
            self.players_stats[self.player_name] = {
                'Coins': self.global_coins,
                'Artifacts': self.players_artifacts,
                'Global_Hp': self.global_hp,
                'Global_Damage': self.global_damage
            }
            self.update()
    def update(self):
        with open('DataBase/Profile_info.json', 'w', encoding='UTF-8') as wr:
            json.dump(self.players_stats, wr, indent=4, ensure_ascii=False)
    def health_up(self, h: int):
        self.players_stats[self.player_name]['Global_Hp'] = self.global_hp + h
        self.update()
    def damage_up(self, d: int):
        self.players_stats[self.player_name]['Global_Damage'] = self.global_damage + d
        self.update()
    def give_crystal(self):
        self.global_coins += 1
        self.players_stats[self.player_name]['Coins'] = self.global_coins
        print(self.players_stats)
        self.update()
    def artifact_add(self, artifactr: str):
        match artifactr:
            case 'Health':
                self.health_up(2)

            case 'Leg sword':
                self.damage_up(1)

    def artifact_give(self, artifact: str):
        try:
            players_artifacts.append(artifacts_list[artifacts_list.index(artifact)])
            self.players_stats[self.player_name]['Artifacts'] = players_artifacts
            self.update()

            self.artifact_add(artifact)
        except:
            print('Неправильна назва артифакту')
    def name(self):
        return self.player_name
    def coins(self):
        return self.global_coins
    def legsw(self):
        return self.leg_sword
    def anghp(self):
        return self.angel_hp
    def gl_hp(self):
        return self.global_hp
    def gl_dm(self):
        return self.global_damage
    def start_LVL1(self):
        main.initGame(3, 5, 2)



player = PlayerProfile(login)
my_ptofile = tk.Tk()
my_ptofile.title('My Profile')
my_ptofile.geometry('500x500')
tk.Label(my_ptofile, text='Твій профіль', font=7).grid(row=0, column=1, pady=5)
tk.Label(my_ptofile, text=f"Ім'я {player.name()}", font=4).grid(row=1, column=1, pady=10)
crystal_icon = PhotoImage(file='Project_imgs/crystal_icon.png')
angel_heal_icon = PhotoImage(file='Project_imgs/Angel_artefact.png')
tk.Label(my_ptofile, image=crystal_icon).grid(row=2, column=0)
tk.Label(my_ptofile, text=f'{player.coins()}', font=7).grid(row=2, column=1)
#TEST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
tk.Button(my_ptofile, text='TEST', command=player.give_crystal).grid(row=10, column=2)
#TEST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
tk.Label(my_ptofile, text='Доступні артифакти:', font=5).grid(row=3, column=1, pady=10)
if player.anghp():
    tk.Label(my_ptofile, image=angel_heal_icon).grid(row=4, column=0)
    tk.Label(my_ptofile, text='Благословіння ангела', font=1).grid(row=5, column=0)
    tk.Label(my_ptofile, text='Благословіння ангела додає +1 хп до загального').grid(row=6, column=0)
elif player.legsw():
    tk.Label(my_ptofile, image=angel_heal_icon).grid(row=4, column=1)
    tk.Label(my_ptofile, text='Легендарний меч', font=1).grid(row=5, column=1)
    tk.Label(my_ptofile, text='Легендарний меч додає +1 до загальної сили').grid(row=6, column=1)
else:
    tk.Label(my_ptofile, text='NONE', font=4).grid(row=4, column=2)
tk.Button(my_ptofile, text='Go', command=player.start_LVL1).grid(row=7)
my_ptofile.mainloop()



# with open('DataBase/Profile_info.json', 'w', encoding='UTF-8') as wr:
#     json.dump(profile_info, wr, indent=4, ensure_ascii=False)