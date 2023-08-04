# import PySimpleGUI as sg

# layout = [[sg.Text("Hello from PySimpleGUI")],[sg.Button("Aatrox")], [sg.Button("OK")]]

# # Create the window
# window = sg.Window("Demo", layout)

# # Create an event loop
# while True:
#     event, values = window.read()
#     # End program if user closes window or
#     # presses the OK button
#     if event == "OK" or event == sg.WIN_CLOSED:
#         break

# window.close()

import PySimpleGUI as sg
from output import *


# champions = Key - Champion Name, Value - (image byte code - Str, champion cost - Int, traits - List)
champions = {}

# "Aatrox"
champions["Aatrox"] = {"image": aatrox, "cost": 5, "traits": []}

# "Ahri"
champions["Ahri"] = {"image": ahri, "cost": 5, "traits": []}

# "Akshan"
champions["Akshan"] = {"image": akshan, "cost": 3, "traits": []}

# "Aphelios"
champions["Aphelios"] = {"image": aphelios, "cost": 4, "traits": []}

# "Ashe"
champions["Ashe"] = {"image": ashe, "cost": 2, "traits": []}

# "Azir"
champions["Azir"] = {"image": azir, "cost": 4, "traits": []}

# "Belveth"
champions["Belveth"] = {"image": belveth, "cost": 5, "traits": []}

# "Cassiopeia"
champions["Cassiopeia"] = {"image": cassiopeia, "cost": 1, "traits": []}

# "Chogath"
champions["Chogath"] = {"image": chogath, "cost": 1, "traits": []}

# "Darius"
champions["Darius"] = {"image": darius, "cost": 3, "traits": []}

# "Ekko"
champions["Ekko"] = {"image": ekko, "cost": 3, "traits": []}

# "Galio"
champions["Galio"] = {"image": galio, "cost": 2, "traits": []}

# "Garen"
champions["Garen"] = {"image": garen, "cost": 3, "traits": []}

# "Gwen"
champions["Gwen"] = {"image": gwen, "cost": 4, "traits": []}

# "Heimerdinger"
champions["Heimerdinger"] = {"image": heimerdinger, "cost": 5, "traits": []}

# "Irelia"
champions["Irelia"] = {"image": irelia, "cost": 1, "traits": []}

# "Jarvan IV"
champions["Jarvan IV"] = {"image": jarvan, "cost": 4, "traits": []}

# "Jayce"
champions["Jayce"] = {"image": jayce, "cost": 3, "traits": []}

# "Jhin"
champions["Jhin"] = {"image": jhin, "cost": 1, "traits": []}

# "Jinx"
champions["Jinx"] = {"image": jinx, "cost": 2, "traits": []}

# "K'Sante"
champions["K'Sante"] = {"image": ksante, "cost": 5, "traits": []}

# "Kaisa"
champions["Kaisa"] = {"image": kaisa, "cost": 4, "traits": []}

# "Kalista"
champions["Kalista"] = {"image": kalista, "cost": 3, "traits": []}

# "Karma"
champions["Karma"] = {"image": karma, "cost": 3, "traits": []}

# "Kassadin"
champions["Kassadin"] = {"image": kassadin, "cost": 2, "traits": []}

# "Katarina"
champions["Katarina"] = {"image": katarina, "cost": 3, "traits": []}

# "Kayle"
champions["Kayle"] = {"image": kayle, "cost": 1, "traits": []}

# "Kled"
champions["Kled"] = {"image": kled, "cost": 2, "traits": []}

# "Lissandra"
champions["Lissandra"] = {"image": lissandra, "cost": 3, "traits": []}

# "Lux"
champions["Lux"] = {"image": lux, "cost": 4, "traits": []}

# "Malzahar"
champions["Malzahar"] = {"image": malzahar, "cost": 1, "traits": []}

# "Maokai"
champions["Maokai"] = {"image": maokai, "cost": 1, "traits": []}

# "Nasus"
champions["Nasus"] = {"image": nasus, "cost": 4, "traits": []}

# "Orianna"
champions["Orianna"] = {"image": orianna, "cost": 1, "traits": []}

# "Poppy"
champions["Poppy"] = {"image": poppy, "cost": 1, "traits": []}

# "Reksai"
champions["Reksai"] = {"image": reksai, "cost": 3, "traits": []}

# "Renekton"
champions["Renekton"] = {"image": renekton, "cost": 1, "traits": []}

# "Ryze"
champions["Ryze"] = {"image": ryze, "cost": 5, "traits": []}

# "Samira"
champions["Samira"] = {"image": samira, "cost": 1, "traits": []}

# "Sejuani"
champions["Sejuani"] = {"image": sejuani, "cost": 4, "traits": []}

# "Senna"
champions["Senna"] = {"image": senna, "cost": 5, "traits": []}

# "Sett"
champions["Sett"] = {"image": sett, "cost": 2, "traits": []}

# "Shen"
champions["Shen"] = {"image": shen, "cost": 4, "traits": []}

# "Sion"
champions["Sion"] = {"image": sion, "cost": 5, "traits": []}

# "Sona"
champions["Sona"] = {"image": sona, "cost": 3, "traits": []}

# "Soraka"
champions["Soraka"] = {"image": soraka, "cost": 2, "traits": []}

# "Swain"
champions["Swain"] = {"image": swain, "cost": 2, "traits": []}

# "Taliyah"
champions["Taliyah"] = {"image": taliyah, "cost": 2, "traits": []}

# "Taric"
champions["Taric"] = {"image": taric, "cost": 3, "traits": []}

# "Teemo"
champions["Teemo"] = {"image": teemo, "cost": 2, "traits": []}

# "Tristana"
champions["Tristana"] = {"image": tristana, "cost": 1, "traits": []}

# "Urgot"
champions["Urgot"] = {"image": urgot, "cost": 4, "traits": []}

# "Velkoz"
champions["Velkoz"] = {"image": velkoz, "cost": 3, "traits": []}

# "Vi"
champions["Vi"] = {"image": vi, "cost": 2, "traits": []}

# "Viego"
champions["Viego"] = {"image": viego, "cost": 1, "traits": []}

# "Warwick"
champions["Warwick"] = {"image": warwick, "cost": 2, "traits": []}

# "Yasuo"
champions["Yasuo"] = {"image": yasuo, "cost": 4, "traits": []}

# "Zed"
champions["Zed"] = {"image": zed, "cost": 2, "traits": []}

# "Zeri"
champions["Zeri"] = {"image": zeri, "cost": 4, "traits": []}


champion_grid = [
    [sg.Text('Champions')],
   
]
builder_column = [
    [sg.Button('Exit', key='Exit')]
]
currow = []
i = 0
for champion in champions:
    currow.append(
        sg.Button(champion.capitalize(), key="champions", image_data=champions[champion]["image"], 
                  button_color=(sg.theme_background_color(), sg.theme_background_color()), 
                  border_width=0)
    )
    i += 1
    if i == 8:
        champion_grid.append(currow)
        currow = []
        i = 0
layout = [
    [sg.Column(champion_grid),
     sg.VSeperator(),
     sg.Column(builder_column),]
]


window = sg.Window('', layout, no_titlebar=True)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
window.close()

# Aatrox 5
# Ahri 5
# Akshan 3
# Aphelios 4
# Ashe 2
# Azir 4
# Belveth 5
# Cassiopeia 1
# Chogath 1
# Darius 3
# Ekko 3
# Galio 2
# Garen 3
# Gwen 4
# Heimerdinger 5
# Irelia 1
# Jarvan IV 4
# Jayce 3
# Jhin 1
# Jinx 2
# K'Sante 5
# Kaisa 4
# Kalista 3
# Karma 3
# Kassadin 2
# Katarina 3
# Kayle 1
# Kled 2
# Lissandra 3
# Lux 4
# Malzahar 1
# Maokai 1
# Nasus 4
# Orianna 1
# Poppy 1
# Reksai 3
# Renekton 1
# Ryze 5
# Samira 1
# Sejuani 4
# Senna 5
# Sett 2
# Shen 4
# Sion 5
# Sona 3
# Soraka 2
# Swain 2
# Taliyah 2
# Taric 3
# Teemo 2
# Tristana 1
# Urgot 4
# Velkoz 3
# Vi 2
# Viego 1
# Warwick 2
# Yasuo 4
# Zed 2
# Zeri 4

