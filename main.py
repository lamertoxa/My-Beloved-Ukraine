import turtle
import pandas
from guess_cities import City


data = pandas.read_csv("Ukraine_regions.csv",encoding="utf-8")

screen = turtle.Screen()



screen.screensize(860,600)
screen.title("Ukrainian Cities Game")
image = "ukraine.gif"
screen.addshape(image)
maps = turtle.Turtle()
maps.shape(image)

cities = [ i for i in data.City ]
guessed_cities = []
answers = []

export_data = {
    "City":guessed_cities,
    "Correct": answers
}

score = 0
all_cities = len(data.City)



game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{score}/{all_cities} Вгаданих міст", prompt="Яке ще місто?").capitalize()
    if answer_state in guessed_cities:
        continue
    elif answer_state in cities :
        new_city = data[data.City == answer_state]
        cor_x = int (new_city.X)
        cor_y = int (new_city.Y)
        city_guess = City(answer_state, cor_x,cor_y)
        answers.append("True")
        guessed_cities.append(answer_state)
        score+=1
    else:
        answers.append("False")
        guessed_cities.append(answer_state)

    if score == all_cities:
        game_on=False

csv_answers = pandas.DataFrame(export_data)

csv_answers.to_csv("answers.csv")








screen.mainloop()