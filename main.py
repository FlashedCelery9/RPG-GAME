import random
import random as r
import tkinter
import tkinter as tk
import Auth

from tkinter import messagebox, PhotoImage, Toplevel


hp = 0
coins = 0
damage = 0

Monster_event = False
Shop_event = False

def shop_debager():
    messagebox.showerror("Помилка", "Цю дію не можна виконати.")

window = tk.Tk()

Shop_img = PhotoImage(file='Project_imgs/Shop_img.png')
Monster_img = PhotoImage(file='Project_imgs/monster_img.png')
Default_img = PhotoImage(file='Project_imgs/Default_img.png')

window.title('RPG-GAME')
window.geometry("500x800")
tk.Label(window, image=Default_img).pack()

output = tk.Text(window, height=15, width=50)
output.pack()
def shop_ev():
    global Shop_event
    Shop_event = False
def print_to_output(text):
    output.insert(tk.END, text + '\n')
    output.see(tk.END)

def printParameters():#Немає глобал?
    print_to_output(f"\nУ тебе {hp} хп, {damage} шкоди, {coins} монет")

def printHp():
    print("У тебе", hp, "хп.")

def printCoins():
    print("У тебе", coins, "монет.")

def printDamage():
    print("У тебе", damage, "сила.")

def meetShop():
    global hp, damage, coins, Shop_event
    Shop_event = True
    shop_window = tk.Toplevel(window)
    shop_window.attributes("-topmost", True)
    shop_window.title("Торговець")

    weaponLvl = r.randint(1, 3)
    weaponDmg = r.randint(1, 5) * weaponLvl
    weapons = ["AK-47", "Iron Sword", "Showel", "Flower", "Bow", "Fish"]
    weaponCost = r.randint(3, 10) * weaponLvl
    weapon = r.choice(weapons)

    oneHpCost = 5
    threeHpCost = 12

    def buy(cost):
        global coins, Shop_event
        if coins >= cost:
            coins -= cost
            print_to_output(f"Успіх, у вас залишилось {coins} монет!")
            return True
        print_to_output(f"У тебе мало монет!!")
        return False
    def shop_destroy():
        global Shop_event
        Shop_event = False
        shop_window.destroy()

    def buy_1hp():
        global hp
        if buy(oneHpCost):
            hp += 1
            print_to_output(f"Тепер у вас {hp} хп!")
    def buy_3hp():
        global hp
        if buy(threeHpCost):
            hp += 3
            print_to_output(f"Тепер у тебе {hp} хп!")
    def buy_wearpon():
        global damage, Shop_event
        if buy(weaponCost):
            damage += weaponDmg
            print_to_output(f"Успіх, ти купив(ла) {weapon}")
            print_to_output(f"Тепер у тебе {damage} шкоди")
    tk.Label(shop_window, image=Shop_img).pack()
    tk.Label(shop_window, text="Вітаємо у магазині!").pack()
    tk.Button(shop_window, text=f"Купити 1хп за {oneHpCost} монет", command=buy_1hp).pack()
    tk.Button(shop_window, text=f"Купити 3хп за {threeHpCost} монет", command=buy_3hp).pack()
    tk.Button(shop_window, text=f"Купити {weapon} з {weaponDmg} силою за {weaponCost} монет", command=buy_wearpon).pack()
    tk.Button(shop_window, text="Вихід", command=shop_destroy).pack()
    tk.Label(shop_window, text='Ваші характеристики:').pack()
    tk.Label(shop_window, text=f'{hp} 💖   {damage} 🗡️   {coins} 🪙 ').pack()
    shop_window.protocol("WM_DELETE_WINDOW", shop_ev)


def meetMonster():
    global hp, coins, Monster_event

    monsterLvl = r.randint(1, 3)
    monsterHp = monsterLvl
    monsterDmg = monsterLvl * 2 - 1
    monsters = ["Блоб", "кракен", "рептилія", "¤&#&(#&¤(", "Ангел_Смерті"]
    Monster_event = True
    monster = r.choice(monsters)
    monster_window = tk.Toplevel(window)
    monster_window.attributes("-topmost", True)
    tk.Label(monster_window, )
    monster_window.protocol("WM_DELETE_WINDOW", debager)
    monster_window.title("Битва з монстром")
    tk.Label(monster_window, image=Monster_img).pack(pady=5)
    status = tk.Label(monster_window, text=f"Ти зустрів {monster} (lvl {monsterLvl}, {monsterHp} хп, {monsterDmg} dmg)")
    status.pack(pady=10)
    tk.Label(monster_window, text='Ваші характеристики:').pack(pady=10)
    tk.Label(monster_window, text=f'{hp} 💖   {damage} 🗡️   {coins} 🪙 ').pack(pady=5)
    def update_status():
        status.config(text=f'Монстр {monster} - {monsterHp} залишилось хп')
    def atack():
        nonlocal monsterHp
        global hp, coins, Monster_event

        monsterHp -= damage
        print_to_output(f'Ти вдарив монстра і в нього залишилось {monsterHp} хп')

        if monsterHp <= 0:
            loot = r.randint(0, 2) + monsterLvl
            coins += loot
            print_to_output(f'Ти вбив монстра і отримав {loot} монет')
            print_to_output(f'Тепер в тебе {coins} монет!')
            Monster_event = False
            monster_window.destroy()
            return
        hp -= monsterDmg
        print_to_output(f'Монстр атакував тебе і в тебе залишилось {hp} хп')
        if hp < 0:
            print_to_output(f'Ти програв ...')
            Monster_event = False
            monster_window.destroy()

        update_status()
    def run():
        global hp, Monster_event
        change = random.randint(0, monsterLvl)
        if change == 0:
            print_to_output(f'Тобі вдалося втекти!')
            Monster_event = False
            monster_window.destroy()
        else:
            print_to_output(f'Тебе наздогнали...')
            hp -= monsterDmg
            print_to_output(f'Тебе атакували, в тебе залишилось {hp} хп!')
            if hp <= 0:
                print_to_output(f'Ти програв...')
                monster_window.destroy()
                Monster_event = False
                restart()
    tk.Button(monster_window, text="Атакувати", command=atack).pack()
    tk.Button(monster_window, text="Втекти", command=run).pack()
def gameLoop():
    global Monster_event, Shop_event
    if Shop_event == True:
        shop_debager()
    elif Monster_event != True:

        situacion = r.randint(0, 6)
        match situacion:
            case 0:
                meetShop()
            case 1:
                meetMonster()
            case 2,3,4,5,6:
                print_to_output('Блукаємо...')
    else:
        debager()


def initGame(initHp, initCoins, initDamage):
    global hp, coins, damage

    hp = initHp
    coins = initCoins
    damage = initDamage
    output.delete("1.0", tk.END)#????
    print_to_output("Початок Пригоди! ")
    printParameters()

def debager():
    if not messagebox.askyesno("Не махлюй", "Я все бачу!! Бийся з монстром або помри!"):  # ????
        window.destroy()

def restart():
    if hp <= 0:
        if messagebox.askyesno("Гра закінчена", "Ти загинув. Хочеш грати спочатку?"):#????
            initGame(3,5,2)
tk.Button(window, text="Блукати", command=lambda: [gameLoop(), restart()]).pack()
initGame(3, 5, 2)
window.mainloop()
