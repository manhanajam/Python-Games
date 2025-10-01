# Assignment: Manha_Muneebah_Game
# Description: This is a game where the user has control over the ball and must try to go through the holes and not hit any objects
# Version: 3.9
# Name: Manha Najam and Muneebah Younas
# Date: January 21, 2022
# Course Code: ICS3U1-01

import tkinter
import time

#Dimension of the game
window_dimen = 500

#The amount the ball will move horizontally 
move_amount = 10

#Width of rectangle in which circle is drawn
circle_size = 40

ball_falling = 2 

#These are the dimensions of the bottom hole/obstacles 
hole_height = 15
hole_left = 100
hole_right = 160

#The dimensions of the top hole/obstacles
hole_height2 = 240
hole_left2 = 300
hole_right2 = 370

#making an empty array to fill with information from the text file
file_info = []

#Each picture will display for 3/10 ths of a second
delay_seconds = .01

#Initialize variables
#Start ball at the top of the window, and in the middle horizontally
upper_left_x = (window_dimen // 2) - (circle_size // 2)
upper_left_y = 0
lower_right_x = (window_dimen // 2) + (circle_size // 2)
lower_right_y = circle_size

program_done = False
ballMove = True
hit_floor = False
result_message = ""
crash = False

#Open the file
file_in_name = "Manha_Muneebah_game_settings.txt"

input_file = open(file_in_name, 'r')
line_read = input_file.readline()

#reads what is writted in the file, and adds it to the lists for colour and coordinates
for i in range (1):      
    line_read = input_file.readline ()
    print(line_read)
    file_info.append(line_read)
input_file.close()

print(file_info)

#When spltiing the line, it takes all the individual strings in variables and breaks them up,
#then the information is stored into an array 
line_read= line_read.split()

#telling the user which colours have been chosen in file 
print("The colour for the game piece is",line_read[0])
print ("The colour for the background is",line_read[1])
print("The colour for the obstacles are",line_read[2])
    
#Create basic window
window = tkinter.Tk()
window.geometry("500x500")
window.title("Dodge Obstacles game")

#Define commands (functions)


#this is the command to pop up instructions
def open_window():
    #setting up the window
    window = tkinter.Tk()
    window.geometry("400x400")
    window.title("Instructions Page")

    canvas = tkinter.Canvas(window, bg = "light blue", height=400, width = 400)

    #writing the instructions

    label_one = tkinter.Label(window, text = "EASY! QUICK! FUN!")
    label_one.grid(row = 0, column = 0)

    label_two = tkinter.Label(window, text = "Use your LEFT and RIGHT arrow keys in order to move the ball")
    label_two.grid(row = 1, column = 0)

    label_three = tkinter.Label(window, text = "DO NOT hit the obstacles")
    label_three.grid(row = 2, column = 0)

    label_four = tkinter.Label(window, text = "Guide the ball the way to the bottom hole, where it can be safe")
    label_four.grid(row = 3, column = 0)

    label_five = tkinter.Label(window, text = "Press ESC to quit")
    label_five.grid(row = 4, column = 0)

    label_six = tkinter.Label(window, text = "Enjoy!")
    label_six.grid(row = 5, column = 0)
    
#function to move gamepeice/ball to the right
def move_right(event=" "):
    global move_amount, upper_left_x, lower_right_x

    upper_left_x = upper_left_x + move_amount
    lower_right_x = lower_right_x + move_amount

    if lower_right_x > window_dimen :
        #Reached edge of window, so redraw shape at edge
        upper_left_x = window_dimen - circle_size
        lower_right_x = window_dimen

#function to move gamepeice/ball to the left
def move_left(event=" "):
    global move_amount, upper_left_x, lower_right_x
    upper_left_x = upper_left_x - move_amount
    lower_right_x = lower_right_x - move_amount
   
    if upper_left_x < 0 :
        #Reached edge of window, so redraw shape at edge
        upper_left_x = 0
        lower_right_x = circle_size
        
#function for the program to end    
def end_program(event=" "):
    global program_done
    program_done = True

#validating that user can only move ball left or right
window.bind("<Right>", move_right)
window.bind("<Left>", move_left)

#user can quit using the ESC key
window.bind("<Escape>", end_program)


#Placing button to open up instructions window
open_button = tkinter.Button(window, text = "Rules", command = open_window)
open_button.pack(side="right", padx=5, pady=5)


#This checks to see weather the game peice has passed through a gate or not
#defaults as False
stage1_Pass = False
stage2_Pass = False


#Main animation loop
while not program_done:

    #If ball is still in play
    if ballMove:
       
        #Ball is moving down
        upper_left_y = upper_left_y + ball_falling
        lower_right_y = lower_right_y + ball_falling


        #Determine if the ball is still falling, made it through the holes, or whether it has crashed

        #check for the upper hole
        if lower_right_y > 260 and stage1_Pass == False :
            if  upper_left_x < hole_left2:
                hit_floor = True
                ballMove = False
                #validating that if it crashes to stop moving 


            elif lower_right_x > hole_right2:
                hit_floor = True
                ballMove = False
                #validating that if it crashes to stop moving 

            else:
                hit_floor = False
                stage1_Pass = True
                #if it gets past here, then it has passed the hole,
                #stage pass turns into True becuase game peice has gone through 


        #check for the bottom hole      
        if (lower_right_y > (window_dimen - hole_height) and stage1_Pass):
            #Check if floor hit or through hole

            if upper_left_x < hole_left : 
                #Ball hit wall
                hit_floor = True
                  
            elif lower_right_x > hole_right:
                #Ball hit wall
                hit_floor = True
   
            else:
                #Ball made it through hole
                hit_floor = False
                stage2_Pass = True

               
            ballMove = False
            

    # Add text to the game window so the user will know to press the escape key to quit the game
    canvas = tkinter.Canvas(window, width=window_dimen, height=window_dimen,
                        bg=line_read[1])

    text_exit = canvas.create_text(10, 10, font = 9.5, anchor = "w",
                                   text = "Press ESC key to exit")

   #Drawing the first hole/obstacles
    hole_left_side = canvas.create_polygon(0, window_dimen - hole_height,
                                            hole_left, window_dimen - hole_height, 
                                            hole_left, window_dimen,
                                            0, window_dimen,
                                            fill=line_read[2])

    hole_right_side = canvas.create_polygon(hole_right, window_dimen - hole_height,
                                            window_dimen, window_dimen - hole_height,
                                            window_dimen, window_dimen,
                                            hole_right, window_dimen,
                                            fill=line_read[2])
    #Drawing second hole/obstacles 
    hole_left_side = canvas.create_polygon(0, window_dimen - 200,
                                            hole_left2, window_dimen - 200,
                                            hole_left2, 260,
                                            0, 260,
                                            fill=line_read[2])

    hole_right_side = canvas.create_polygon(hole_right2, window_dimen - 200,
                                            window_dimen, window_dimen - 200,
                                            window_dimen, 260,
                                            hole_right2, 260, fill = line_read[2])


     #Ball has already reached the end; display text indicating result                                      
    if not ballMove:
        if hit_floor:
            result_message = "OOPS! You crashed."
            move_amount = 0

        elif stage1_Pass and stage2_Pass:
            result_message = "YAY! You did it!"
            ballMove = True
           ## validating that the game peice has passed both levels


        font_name= ("Comic Sans MS", 20, "bold")


        text_result = canvas.create_text(window_dimen // 2, 50, font = font_name,
                                         text = result_message) 
    
    #Draw the game piece
    ball = canvas.create_oval(upper_left_x, upper_left_y,
                          lower_right_x, lower_right_y,
                          fill=line_read[0])

    canvas.pack()
    canvas.update()


    time.sleep(delay_seconds)
   
    #After the user has seen the image, clear the window for the next image
    canvas.destroy()

   
window.mainloop()
exit()
