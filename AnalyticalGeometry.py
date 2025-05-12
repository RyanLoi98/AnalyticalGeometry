'''
Name: Ryan Loi
Date (dd/mm/yr): 27/09/21
Class: CPSC 231 Lecture 01 Fall 2021
Tutorial: T08

Description: Assignment 1, a program utilizing python 3 to obtain input from the user (and then cast them to their proper type) which define: 
the X and Y coordinates (as integers) of a circle's center, the radius of the circle (as a float), 
the beginning and ending (X and Y) coordinates (as integers) of a line (as many lines as the user desires) 
and then draws it using the turtle graphics module on a 800 x 600 pixel window/coordinate system. The program will then use the math module 
to perform analytical geometry to determine the intersections (or report the lack of an intersection) between the user
defined line(s) and circle, then it will circle any intersection(s). The program is broken down
into functions each performing a specific task, and controlled by the main() function which can
send and receive data to/from other functions.
'''


# importing the turtle and math modules
import turtle 
import math 


# CONSTANTS:

# Constants for full screen dimensions and middle of the screen dimensions in pixels
WIDTH = 800
HALF_WIDTH = 400
HEIGHT = 600
HALF_HEIGHT = 300

# Defining constants of the origin for the coordinate system's bottom left corner
X_ORIGIN = 0
Y_ORIGIN = 0

# Defining constants for a starting position on the screen for the turtle graphics window to open
WINDOW_POSITION_X = 0
WINDOW_POSITION_Y = 0

# Defining some constants for commonly used angles to set the turtle's heading with
ZERO_DEGREE = 0
TWO_SEVENTY_DEGREE = 270

# Defining constants for some commonly used colors in the program
AXIS_COLOR = 'black'
CIRCLE_COLOR = 'red'
LINE_COLOR = 'blue'
INTERSECTION_CIRCLE_COLOR = 'green'
TEXT_COLOR = 'green'

# Creating a font and text size preset constant to format text printed by the turtle.
FONT = ("Arial", 15)

# Defining a constant for 1 possible intersection between a line and a circle that the user inputs
# based on the solution to the radicand (value under the root) in the quadratic formula
ONE_INTERSECTION = 0

# Defining a constant for the accuracy epsilon used to determine if there is an intersection
# between a point and a circle that the user defines
EPSILON = 0.75

# Defining a constant for the radius of the circle drawn around each intersection between a line
# or a point and the circle that the user defines
INTERSECTION_RADIUS = 5

# Defining constants used for number of intersects found, these constants will be used with a counter
# to keep track of the total number of intersections found at a specific time
ONE_INTERSECTION_FOUND = 1



# PROVIDED CODE
# NEED TO SET WIDTH AND HEIGHT TO USE
# Setup the world (get objects, set screen size and coordinate system, hide turtle pointer)
screen = turtle.getscreen()
screen.setup(WIDTH, HEIGHT, WINDOW_POSITION_X, WINDOW_POSITION_Y)
screen.setworldcoordinates(X_ORIGIN, Y_ORIGIN, WIDTH, HEIGHT)
screen.delay(delay=0)
turtle.hideturtle()  # A different command that is able to hide the turtle pointer permanently, and the turtle.turtle() pointer will not be 
                     # assigned to a different variable so commands to move the pointer will be done through the turtle. call 
# END PROVIDED CODE



# PROGRAM

# Main function, controls the overall operation of the program and the order of operations.
# It also activates other functions by calling upon them and can receive data from these functions
# and store them as variables local to the main function while also sending data to other functions for further processing

def main():    
    Xc, Yc, Radius = circle_I()   # Calls the circle_I() function which prompts the user to enter a circle's radius, X and Y coordinates for the circle's center
                                  # Then the function returns these values in a specific order to be stored in the main function for further use under the respective 
                                  # Variable names (Xc, Yc, Radius), which is also the order that they are returned.
      
    draw_axis() # Calls the draw_axis() function which draws (in black) the X and Y axes that identifies the center of the screen at (400, 300) == (HALF_WIDTH, HALF_HEIGHT) pixels.
                              
    draw_circle(Radius, Xc, Yc, CIRCLE_COLOR) # Calls the draw_circle() function, while providing it arguments which consists of the user's inputs that define the circle
                  # (radius, and X, Y coordinates for the circles center) and the color to draw the circle. Then this function will draw the circle. 
    
    Intercept_counter = 0 # Creating a variable local to the main function to count how many intercepts are found between the user defined line(s) and circle.
                           

    X_Start, Y_Start, X_End, Y_End = line_I()  # Calling the line_I() function which will prompt the user to enter the X and Y coordinates of the starting and ending
                                               # points of a line. The function will then return these inputs to be stored locally in the main () function in a specific
                                               # order (the order they are returned): X_Start, Y_Start, X_End, Y_End. (Start = starting point of a line, end = ending point)
                                               # These variables will also be the condition tested in the condition controlled (while) loop.

    # Initiating a condition controlled (while) loop which will continually test the variables: X_Start, Y_Start, X_End, Y_End which represent the
    # X and Y coordinates for the starting and ending points of a line that the user specifies. While the variables are not empty spaces (which would
    # designate the user wants the loop to end) the loop will continue to reiterate, and as a result the line_I() function will be called with each 
    # iteration allowing the user to continue and enter more starting and ending X and Y coordinates of a line. This will result in more lines
    # being drawn onto the coordinate grid, and intersections between the newly drawn lines and the user defined circle continually being determined. 
    
    while X_Start != '' and Y_Start != '' and X_End != '' and Y_End != '': # only one variable must be empty to stop the loop

        # casting the user's inputs for the starting and ending X and Y coordinates of a line from a string into an integer and storing them in the same variable
        # by reassigning the variable to the new integer value.
        X_Start = int(X_Start)
        Y_Start = int(Y_Start)
        X_End = int(X_End)
        Y_End = int(Y_End)

        # sending the starting and ending X and Y coordinates of a line to the draw_line() function as an argument, so each line will be drawn
        # onto the coordinate grid by the turtle. 
        draw_line(X_Start, Y_Start, X_End, Y_End)

        # Sending the starting and ending point X and Y coordinates of the line to the calculate_a_b_c() function as arguments.
        # The function will then determine the a, b, c parameters of the quadratic formula used in analytical geometry to determine
        # the intersection points between the user defined circle and line, and return them back to the main() function for local storage
        # and future use. Returns in the order a, b, c.
        a, b, c = calculate_a_b_c(X_Start, Y_Start, X_End, Y_End, Radius, Xc, Yc)
             
        
        # determining the radicand (value under the root) in the quadratic formula which will be used to determine the number of intersections        
        radicand = ((b**2) - (4 * a * c))
      

        #creating an if else conditional to differentiate between if the user entered values is for a line or a single point.

        if X_Start == X_End and Y_Start == Y_End:  #if this conditional holds true the user entered starting and ending X and Y coordinates is actually a point
         
            Intersect = point_intercept(X_Start, Y_Start, Xc, Yc, Radius)  # since the line is a point the starting and ending X and Y coordinates are the same
                                                                           # so in this case we only have to use either the starting or ending variables.
                                                                           # Therefore, the point_intercept() function is called and the X and Y variables 
                                                                           # the user entered for a line's starting point is sent to the function as an argument
                                                                           # along with the circle's radius and X and Y coordinates for its center.
                                                                           # The function will then return a True or False boolean condition to be assigned to the
                                                                           # Intersect variable.
                                                    
            # if the point is on the circle the point_intercept() function will have returned the True boolean condition making this statement true
            # this will call the draw_circle() function providing the following arguements: INTERSECTION_RADIUS, X_Start, Y_Start, INTERSECTION_CIRCLE_COLOR
            # this will cause the circle function to draw a green circle with the radius of 5 (INTERSECTION_RADIUS) around the point of intersection between the point and the circle.
            # It will also add 1 (ONE_INTERSECTION_FOUND constant) to the intercept_counter variable keeping track of the number of intercepts found. 
            if Intersect: 
                draw_circle(INTERSECTION_RADIUS, X_Start, Y_Start, INTERSECTION_CIRCLE_COLOR)
                Intercept_counter += ONE_INTERSECTION_FOUND

            # if the point was not on the circle the point_intercept() function would return the False boolean condition resulting in the message_no_intersection() function
            # being called and printing the message "no intersection" in green in the middle of the window on the coordinate grid. 
            else:            
                message_no_intersection()
          


        else: # the else clause triggers if the, if statement is false and the user entered values is not a point and is indeed a line

            # the if statement will then test to see if the radicand (the value under the root from the quadratic formula) is less than the CONSTANT
            # for one intersection. If the condition is true then there are no intersections and the message_no_intersection() function is called
            # which will print the message "no intersection" in green and in the middle of the window on the coordinate grid.
            if radicand < ONE_INTERSECTION:
                message_no_intersection()
            

            # the elif statment will test if the radicand is equal to the CONSTANT for one intersection. If the condition is true the elif statment executes
            #  the statements within.
            elif radicand == ONE_INTERSECTION:
                alpha_1, alpha_2 = calculate_alpha(radicand, a, b)  # the elif satement will then call the calculate_alpha() function while passing the arguments
                                                                    # radicand, a, b to the function. This function will then solve the quadratic formula returning
                                                                    # two alpha values (designated here alpha_1 and alpha_2) to be stored locally in the main function.
                                                                    # since a radicand equal to the ONE_INTERSECTION constant is 0, the solution to the quadratic formula
                                                                    # produces two identical alpha values, so only alpha_1 will be used in the coming calculations.

                # the if statement then tests to see if the alpha value is greater than or equal to 0 and less than or equal to 1 (as alpha values outside that
                # range are intersections not between the two points of the line). If the condition is true the statements within are executed.
                if alpha_1 >= 0 and alpha_1 <= 1:
                    X_Intercept, Y_Intercept = calculate_X_Y_Intersection (alpha_1, X_Start, Y_Start, X_End, Y_End) # the calculate_X_Y_Intersection() is then called
                                                                                                                    # with the arguments alpha_1, X_Start, Y_Start, X_End, Y_End
                                                                                                                    # passed to the function. The function will then
                                                                                                                    # determine the X and Y coordinates of where
                                                                                                                    # the line intersects the circle and return 
                                                                                                                    # the coordinates in the order X, Y which
                                                                                                                    # will be stored locally for further use.

                    # calls the draw_circle() function while passing the following arguments:INTERSECTION_RADIUS, X_Intercept, Y_Intercept, INTERSECTION_CIRCLE_COLOR.
                    # The function will then draw a green circle with the radius of 5 (intersection radius) around the intersection point between the line and the circle.                                                                                            
                    draw_circle(INTERSECTION_RADIUS, X_Intercept, Y_Intercept, INTERSECTION_CIRCLE_COLOR)       

                    Intercept_counter += ONE_INTERSECTION_FOUND  # The intersection counter will also be increased by 1
                
                # if the alpha value is less than 0 or greater than 1 then the intersection is not between the beginning and ending points of the line
                # thus the message_no_intersection() function triggers and prints the message "no intersection" in green and size 15 Arial font in the middle
                # of the coordinate grid.
                else:
                    message_no_intersection()
              
            # the final elif statement tests if the radicand (value under the root of the quadratic formula) is greater than the constant for one intersection
            # if the condition is true the statements within will execute.
            elif radicand > ONE_INTERSECTION:
                alpha_1, alpha_2 = calculate_alpha(radicand, a, b)  # the elif statement will then call the calculate_alpha() function while passing the arguments
                                                                    # radicand, a, b to the function. This function will then solve the quadratic formula returning
                                                                    # two alpha values (designated here alpha_1 and alpha_2) to be stored locally in the main function.
                                                                    
               
                # the if statement then tests to see if the alpha_1 value is greater than or equal to 0 and less than or equal to 1 (as alpha values outside that
                # range are intersections not between the two points of the line). If the condition is true the statements within are executed.
                if alpha_1 >= 0 and alpha_1 <= 1:
                    X_Intercept, Y_Intercept = calculate_X_Y_Intersection (alpha_1, X_Start, Y_Start, X_End, Y_End) # the calculate_X_Y_Intersection() is then called
                                                                                                                    # with the arguements alpha_1, X_Start, Y_Start, X_End, Y_End
                                                                                                                    # passed to the function. The function will then
                                                                                                                    # determine the X and Y coordinates of where
                                                                                                                    # the line intersects the circle and return 
                                                                                                                    # the coordinates in the order X, Y which
                                                                                                                    # will be stored locally for further use.

                    # calls the draw_circle() function while passing the following arguments:INTERSECTION_RADIUS, X_Intercept, Y_Intercept, INTERSECTION_CIRCLE_COLOR.
                    # The function will then draw a green circle with the radius of 5 (intersection radius) around the intersection point between the line and the circle.    
                    draw_circle(INTERSECTION_RADIUS, X_Intercept, Y_Intercept, INTERSECTION_CIRCLE_COLOR)                    
                    Intercept_counter += ONE_INTERSECTION_FOUND  # The intersection counter will also be increased by 1
                    no_intersect_1 = False  # A variable called no_intersect_1 (for no intersection with alpha variable 1) is assigned the False boolean condition
                                            # because there is an intersection between the user defined line and circle with the alpha_1 value.
                
                # if the alpha value is less than 0 or greater than 1 then the intersection is not between the beginning and ending points of the line
                # so the no_intersect_1 variable is assigned the True boolean condition as there is no intersection between the user defined line and circle
                # with the alpha_1 value.
                else:
                    no_intersect_1 = True
               

                # the if statement then tests to see if the alpha_2 value is greater than or equal to 0 and less than or equal to 1 (as alpha values outside that
                # range are intersections not between the two points of the line). If the condition is true the statements within are executed.
                if alpha_2 >= 0 and alpha_2 <= 1:
                    X_Intercept, Y_Intercept = calculate_X_Y_Intersection (alpha_2, X_Start, Y_Start, X_End, Y_End) # the calculate_X_Y_Intersection() is then called
                                                                                                                    # with the arguements alpha_2, X_Start, Y_Start, X_End, Y_End
                                                                                                                    # passed to the function. The function will then
                                                                                                                    # determine the X and Y coordinates of where
                                                                                                                    # the line intersects the circle and return 
                                                                                                                    # the coordinates in the order X, Y which
                                                                                                                    # will be stored locally for further use.

                    # calls the draw_circle() function while passing the following arguments:INTERSECTION_RADIUS, X_Intercept, Y_Intercept, INTERSECTION_CIRCLE_COLOR.
                    # The function will then draw a green circle with the radius of 5 (intersection radius) around the intersection point, between the line and the circle.
                    draw_circle(INTERSECTION_RADIUS, X_Intercept, Y_Intercept, INTERSECTION_CIRCLE_COLOR)                    
                    Intercept_counter += ONE_INTERSECTION_FOUND # The intersection counter will also be increased by 1
                    no_intersect_2 = False # A variable called no_intersect_2 (for no intersection with alpha variable 2) is assigned the False boolean condition
                                            # because there is an intersection between the user defined line and circle with the alpha_2 value.

                # if the alpha value is less than 0 or greater than 1 then the intersection is not between the beginning and ending points of the line
                # so the no_intersect_2 variable is assigned the True boolean condition as there is no intersection between the user defined line and circle
                # with the alpha_2 value.
                else:
                    no_intersect_2 = True
                
                # the last if statement is present in the event that there is no intersection with both alpha_1 and alpha_2 values and it tests this by
                # testing if both no_intersect_1 and no_intersect_2 values are True. If that is the case there is no intersection between the user defined
                # line and circle, and thus the message_no_intersection() function is called and the "no intersection" message is printed in green and size 15
                # Arial font in the middle of the screen.
                if no_intersect_1 and no_intersect_2:
                    message_no_intersection()
                   

       
        # prints how many intersections have been counted by the intersection counter variable so far during each iteration of the while loop,
        # and the message "intercepts have been found so far"
        print(Intercept_counter, 'intercepts have been found so far')
        
        # Again calls the line_I() function to prompt the user to enter the X and Y coordinates of the starting and ending points of a line
        # and if the user does not enter empty values (presses the enter key without entering anything) for any of the starting and ending coordinates
        # the while loop will reiterate and the process will continue. If the user does enter an empty value for any of the starting and ending coordinates
        # the while loop will terminate. The function will then return these X and Y coordinates of the starting and ending points of a line.
        X_Start, Y_Start, X_End, Y_End = line_I() 

    # after the while loop terminates the following message will be printed telling the user the program has ended and to click on the 
    # turtle graphics display to close it.    
    print('The end of the program has been reached, Click anywhere on the turtle graphics display to close it.')

#A function called circle_I (I for input) to get the user's inputs (and store them in variables) that define a circle's radius, 
#and center with coordinates Xc (X coordinate), Yc (Y coordinate). Then the function returns these variables in a specific order
#(Xc, Yc, Radius) back to the main function for further use. The function also casts the user's input from a string into a float
#if the input is for the circle's radius, and into integers if the input is for the circle's center X and Y coordinates.
def circle_I():    
    Xc = int(input("Please enter an integer for the X coordinate of a circle's center: "))
    Yc = int(input("Please enter an integer for the Y coordinate of a circle's center: "))
    Radius = float(input('Please enter a float for the radius of a circle: '))
    return Xc, Yc, Radius



# creating a function (line_I for line input) that will ask the user to input the
# coordinates for the starting point and ending points of a line. The coordinates 
# will be assigned to local variables which will then be returned to the main function 
# in the order: X_Start, Y_Start, X_End, Y_End and then stored in the main function for further use.
# This function will also record if the user presses the enter key without entering a coordinate
# and in turn return the empty values back to the main function which will be used to end a loop 
# that allows for the line_I() function to be continually called and keep collecting input for
# as many lines as the user desires to input.
def line_I():
  
    X_Start = input("Press the enter key to stop, otherwise please enter the X coordinate (as an integer) of a line's starting point: ")

    Y_Start = input("Press the enter key to stop, otherwise please enter the Y coordinate (as an integer) of a line's starting point: ")

    X_End = input("Press the enter key to stop, otherwise please enter the X coordinate (as an integer) of a line's ending point: ")

    Y_End = input("Press the enter key to stop, otherwise please enter the Y coordinate (as an integer) of a line's ending point: ")

    return X_Start, Y_Start, X_End, Y_End


    
# draw_axis() function that will draw the x and y axes defining the middle of the screen at (400, 300) == (HALF_WIDTH, HALF_HEIGHT) pixels. 
# The AXES will also be drawn in black.
def draw_axis():
    turtle.pencolor(AXIS_COLOR) 
    turtle.penup()

    #drawing the X axis 
    turtle.goto(X_ORIGIN,HALF_HEIGHT)    
    turtle.pendown()
    turtle.goto(WIDTH, HALF_HEIGHT)
    turtle.penup()

    #drawing the Y axis
    turtle.goto(HALF_WIDTH, HEIGHT)
    turtle.pendown()
    turtle.goto(HALF_WIDTH,Y_ORIGIN)



# draw_circle() function will draw the circle as defined by the arguments sent from the 
# main() function which it accepts as the parameters: Radius, X & Y(coordinates for the circles center), and
# color (which is the color the circle will be drawn in).
def draw_circle(Radius, X, Y, color):
    turtle.penup()
    turtle.goto(X, Y) # going to the circles center coordinates
    turtle.setheading(TWO_SEVENTY_DEGREE) # moving the turtle away from the center of the circle by
    turtle.forward(Radius)                # the distance of the radius to account for the radius of the circle and where turtle starts drawing
    turtle.setheading(ZERO_DEGREE) #setting the turtle to 0 degrees to account for the counter clockwise drawing direction
    turtle.pendown()
    turtle.pencolor(color)
    turtle.circle(Radius)
    


# draw_line() function that will draw a line (in blue) as defined by the starting (X_Start, Y_Start) 
# and ending (X_End, Y_End) point coordinates which were passed as arguments from the main() function
# and accepted by the draw_line() function as parameters. 
 
def draw_line(X_Start, Y_Start, X_End, Y_End):
    turtle.penup()    
    turtle.goto(X_Start, Y_Start)
    turtle.pencolor(LINE_COLOR) #draws the line in blue
    turtle.pendown()
    turtle.goto(X_End, Y_End)



# function to write the message that there is no intersection at the center of the coordinate system in green and with the size 15 font Arial when called
def message_no_intersection():
    turtle.penup()
    turtle.goto(HALF_WIDTH, HALF_HEIGHT)
    turtle.color(TEXT_COLOR)
    turtle.write('No Intersection', align="center", font = FONT) # printing no intersection aligned to the center of the screen with the font constant



# function to calculate the alpha value by solving the quadratic formula, to do this it accepts the arguments radicand, a, b
# as parameters then returns the two alpha values: alpha_1, alpha_2 back in that particular order.
def calculate_alpha(radicand, a, b):
    root = math.sqrt(radicand)
    alpha_1 = (-(b)/(2 * a)) + (root / (2 * a))
    alpha_2 = (-(b)/(2 * a)) - (root / (2 * a))
    return alpha_1, alpha_2


# function to calculate the a, b, c value  parameters of a quadratic by accepting the following arguments: X_Start, Y_Start, X_End, Y_End, Radius, Xc, Yc
# as parameters. Then it returns the values a, b, c in that order back to the main function after calculating their values.
def calculate_a_b_c(X_Start, Y_Start, X_End, Y_End, Radius, Xc, Yc ):
    
    a = (((X_End - X_Start)**2) + ((Y_End - Y_Start)**2))

    b = 2 * (((X_Start - Xc) * (X_End - X_Start)) + ((Y_Start - Yc) * (Y_End - Y_Start)))

    c = (((X_Start - Xc)**2) + ((Y_Start - Yc)**2) - ((Radius)**2))

    return a, b, c


# A function that accepts the arguments: alpha, X_Start, Y_Start, X_End, Y_End as parameters and uses them to 
# calculate the X and Y coordinates of the intercept between a user defined line and circle. Then it returns the X and Y coordinates
# (in that order) back to the main function().
def calculate_X_Y_Intersection(alpha, X_Start, Y_Start, X_End, Y_End):

    X_Intercept = (((1 - alpha) * X_Start) + (alpha * X_End))

    Y_Intercept = (((1 - alpha) * Y_Start) + (alpha * Y_End))

    return X_Intercept, Y_Intercept


# A function to calculate if a point is intersecting a circle, and it accepts the variables: X_Start, Y_Start, Xc, Yc, Radius
# (Sent from the main() function) as parameters.
def point_intercept(X_Start, Y_Start, Xc, Yc, Radius):
    distance_from_center_circle = math.hypot((X_Start - Xc), (Y_Start - Yc))         # calculating the distance of a point from the
                                                                                     # center of the circle using the math module's hypotnuse function
                                                                                     # and using the circle's X and Y coordinates subtracted from the 
                                                                                     # point's X and Y coordinate to fill in the X and Y requirements of 
                                                                                     # the hypotnuse function (which is a pythagorean therom calculator).
                                                                                     # The result is the distance from the center of the circle, which will then be compared
                                                                                     # to the radius to determine if it is on the circumference or not.

    
    # Determining the acceptable tolerance range of how far or close a point can be from the circle's center to be considered
    # as intersecting the circle's circumference. This is determined with the epsilon error value added and subtracted to the radius.

    tolerance_over = Radius + EPSILON  # the furthest distance the point can be from the middle of the circle and still be considered as intersecting the circle

    tolerance_under = Radius - EPSILON #the closest distance the point can be to the middle of the circle and still be considered as intersecting the circle

    # creating a conditional to determine if the point falls within the acceptable distance tolerance range 
    if distance_from_center_circle > tolerance_over or distance_from_center_circle < tolerance_under:
        return False  #if the point exceeds the tolerance range the boolean condition False is returned to the main() function
    
    else:
        return True  #if the point doesn't exceed the tolerance range the boolean condition True is returned to the main() function

  

#calling the main() function to start the program
main()

#keeping the turtle graphics window open until it is clicked on
screen.exitonclick()
