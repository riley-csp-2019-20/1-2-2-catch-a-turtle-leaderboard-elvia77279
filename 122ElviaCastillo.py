#-----import statements-----
import turtle as trtl
import random 
import leaderboard as lb
# TODO 1: import leaderboard module

#-----game configuration-----
turtleshape = "circle"
turtlesize = 2
turtlecolor = "blue"
timer = 30
counter_interval = 1000 
timer_up = False

# TODO 2: add leader board variables
leaderboard_file_name = "a112_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Please enter your name-")
score = 0
#-----initialize the turtles-----
spot = trtl.Turtle(shape = turtleshape)
spot.color(turtlecolor)
spot.shapesize(turtlesize)
spot.speed(0)

score_writer = trtl.Turtle()
score_writer.penup()
score_writer.goto(-370, 270)
score_writer.ht()
score_writer.clear()
font_setup = ("Arial", 30, "normal")

score_writer.write(score, font=font_setup)

counter =  trtl.Turtle()
counter.speed(0)
counter.ht()
counter.penup()
counter.goto(275,275)

#-----game functions-----
# countdown function
def turtle_click(x,y):
  print("spot got clicked")
  change_position()
  update_score()

def change_position():
  spot.penup()
  spot.ht()
  if not timer_up:
    spotx = random.randint(-412,400)
    spoty = random.randint(-300,300)
    spot.goto(spotx,spoty)
    spot.st()

def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)


def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def manage_leaderboard():

  global leader_scores_list
  global leader_names_list
  global score
  global spot

  lb.load_leaderboard(leaderboard_file_name, leader_names_list, 
  leader_scores_list)

  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, 
  leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)
  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

#----------events----------
spot.onclick(turtle_click)
wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()
