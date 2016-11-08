import os
import random
import csv
import subprocess

choices = random.sample(os.listdir("images-queue"), 2)
winner = choices[0]
loser = choices[1]

techniques = []
with open("forty-eight_self-defense_diagrams.csv", mode="rb") as diagrams:
    reader = csv.DictReader(diagrams)
    for row in reader:
        techniques.append((row.get("WINNING TECHNIQUE"), row.get("LOSING TECHNIQUE")))
technique = random.choice(techniques)
winning_technique = technique[0]
losing_technique = technique[1]

winner = os.path.join("images-queue", winner)
loser = os.path.join("images-queue", loser)
os.system("convert {0} -geometry x400 {1}".format(winner, os.path.join("images-bubishibot", os.path.split(winner)[1])))
os.system("convert {0} -geometry x400 {1}".format(loser, os.path.join("images-bubishibot", os.path.split(loser)[1])))

winner = os.path.join("images-bubishibot", os.path.split(winner)[1])
loser = os.path.join("images-bubishibot", os.path.split(loser)[1])
os.system("convert {0} -flop {0}".format(loser))

winning_technique = "WINNING TECHNIQUE\n" + winning_technique + "\n"
losing_technique = "LOSING TECHNIQUE\n" + losing_technique + "\n"

subprocess.call(["C:\Program Files\ImageMagick-6.9.0-Q16\convert.exe", winner, "-gravity", "south", "-stroke", "#000C", "-strokewidth", "2", "-pointsize", "20", "-annotate", "0", winning_technique, winner])
subprocess.call(["C:\Program Files\ImageMagick-6.9.0-Q16\convert.exe", winner, "-gravity", "south", "-stroke", "none", "-fill", "white", "-pointsize", "20", "-annotate", "0", winning_technique, winner])
subprocess.call(["C:\Program Files\ImageMagick-6.9.0-Q16\convert.exe", loser, "-gravity", "south", "-stroke", "#000C", "-strokewidth", "2", "-pointsize", "20", "-annotate", "0", losing_technique, loser])
subprocess.call(["C:\Program Files\ImageMagick-6.9.0-Q16\convert.exe", loser, "-gravity", "south", "-stroke", "none", "-fill", "white", "-pointsize", "20", "-annotate", "0", losing_technique, loser])

os.system("convert {0} {1} +append {2}".format(winner, loser, os.path.join("images-bubishibot", "image.jpg")))
os.system("composite vs.png -gravity center {0} {0}".format(os.path.join("images-bubishibot", "image.jpg")))

os.remove(winner)
os.remove(loser)
