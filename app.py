from flask import Flask, render_template
import mlab
from mongoengine import *

app = Flask(__name__)

mlab.connect()

class Food(Document):
    name = StringField()
    price = IntField()
    description = StringField()
    image = StringField()

# food = Food(name="Bánh bông lan trứng muối", price=50000, description="Bánh bông lan có phủ trứng muối", image="https://scontent.fhan2-2.fna.fbcdn.net/v/t1.0-9/17634478_1225413234242102_1221498165439821652_n.jpg?oh=4533692af15c9dae5fa3c46bd6c90ee7&oe=5A5A086A")
#
# food.save()


@app.route('/')
def index():
    return render_template("index.html", food_list=Food.objects())


app.run(debug=True)
