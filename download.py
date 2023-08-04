import urllib.request
from PIL import Image
  
# Retrieving the resource located at the URL
# and storing it in the file name a.png


champs = ["akshan", "aphelios", "ashe", "azir", "belveth", "cassiopeia", "chogath", "darius", "ekko", "galio", "garen", "gwen", "heimerdinger", "irelia", "jarvan", "jayce",
"jhin", "jinx", "ksante", "kaisa", "kalista", "karma", "kassadin", "katarina", "kayle", "kled", "lissandra", "lux", "malzahar", "maokai", "nasus", "orianna", "poppy",
"reksai", "renekton", "ryze", "samira", "sejuani", "senna", "sett", "shen", "sion", "sona", "soraka", "swain", "taliyah", "taric", "teemo", "tristana", "urgot",
"velkoz", "vi", "viego", "warwick", "yasuo", "zed", "zeri"]

for champ in champs:
    url = "https://cdn.mobalytics.gg/assets/tft/images/champions/thumbnail/set9/" + champ + ".jpg?v=,0"
    urllib.request.urlretrieve(url, champ + ".jpg")
  
# # Opening the image and displaying it (to confirm its presence)
# img = Image.open(r"ashe.jpg")
# img.show()