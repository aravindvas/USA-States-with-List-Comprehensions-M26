import pandas
import turtle as t
s = t.Screen()
s.title("USA States Game")
img = "blank_states_img.gif"
s.addshape(img)
t.shape(img)
dte = pandas.read_csv("50_states.csv")
alls = dte.state.to_list()
gst = []

# def gtck(x,y):
#     print(x,y)
#
# t.onscreenclick(gtck)
while len(gst) < 50:
    an = s.textinput(title=f"{len(gst)}/50 States correct",
                     prompt="What's another state's name? or Exit?").title()
    if an == 'Exit':
        # misst = []
        # for st in alls:
        #     if st not in gst:
        #         misst.append(st)
        misst = [st for st in alls if st not in gst]
        # print(misst)
        newd = pandas.DataFrame(misst)
        newd.to_csv("States_missed.csv")
        break
    if an in alls:
        gst.append(an)
        tu = t.Turtle()
        tu.hideturtle()
        tu.penup()
        sd = dte[dte.state == an]
        tu.goto(int(sd.x), int(sd.y))
        # tu.write(sd.state.item())
        tu.write(an)




# t.mainloop()

# s.exitonclick()

