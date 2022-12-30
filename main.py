import datetime
import random
from replit import db
from flask import Flask
app = Flask(__name__)
@app.route('/')
def main():
  imgs = open("images.txt")
  imgs = imgs.read()
  imgs = imgs.split(",")
  date_time = datetime.datetime.now()



  date = date_time.strftime("%d/%m/%Y")

  if date in db["lastdate"]:
    image = db["currentimage"]
  
  else:
    image = random.choices(imgs)
    db["currentimage"] = image
    db["lastdate"] = date
    print(image[0])
  return f"<h1>Daily Ohio for {date}</h1><br><img src='{image[0]}'>"
app.run(host='0.0.0.0', port=8080, debug = False)