# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:03:37 2019

Drawing a clock with module 'turtle'.
@author: Artemis

"""
import turtle
from datetime import datetime

        
class Clock():
    """
    Represents a clock with hour hand, minute hand and second hand.
    """
    def __init__(self):
        pass
    
    def __skip(self,step):
        """
        Raises the brush, moves it forward a distance, and puts it down.
        """
        turtle.penup()
        turtle.forward(step)
        turtle.pendown()
    
    def __make_hands(self,name,length):
        """
        Draws the hand of clock.
        """
        turtle.reset()
        self.__skip(-length * 0.1)
        turtle.begin_poly() #The beginning of recoding the polygon vertices.
        turtle.forward(length * 1.1)
        turtle.end_poly() #The beginning of recoding the polygon vertices, and connects the last vertice with the first vertice.
        hand_form = turtle.get_poly()
        turtle.register_shape(name, hand_form)
        
    def __init_hands(self):
        """
        Initializes hour hand, minute hand and second hand.
        """
        global sec_hand, min_hand, hur_hand, printer
        turtle.mode("logo")
        self.__make_hands("sec_hand", 135)
        self.__make_hands("min_hand", 125)
        self.__make_hands("hur_hand", 90)
        sec_hand = turtle.Turtle()
        sec_hand.shape("sec_hand")
        min_hand = turtle.Turtle()
        min_hand.shape("min_hand")
        hur_hand = turtle.Turtle()
        hur_hand.shape("hur_hand")
        
        for hand in sec_hand, min_hand, hur_hand:
            hand.shapesize(1, 1, 3)
            hand.speed(8)
            
        printer = turtle.Turtle() #Outputs text of the turtle.
        printer.hideturtle()
        printer.penup()
        
    def __clock_outline(self,radius):
        """
        Draws the outline of the clock.
        Takes the radius of the clock, and draws the outline of the clock.
        """
        turtle.reset()
        turtle.pensize(7)
        for i in range(60):
            self.__skip(radius)
            if i % 5 == 0:
                turtle.forward(20)
                self.__skip(-radius - 20)
                
                self.__skip(radius + 20)
                if i == 0:
                    turtle.write(int(12), align="center", font=("Courier", 14, "bold"))
                elif i == 30:
                    self.__skip(25)
                    turtle.write(int(i/5), align="center", font=("Courier", 14, "bold"))
                    self.__skip(-25)
                elif (i == 25 or i == 35):
                    self.__skip(20)
                    turtle.write(int(i/5), align="center", font=("Courier", 14, "bold"))
                    self.__skip(-20)
                else:
                    turtle.write(int(i/5), align="center", font=("Courier", 14, "bold"))
                self.__skip(-radius - 20)
            else:
                turtle.dot(5)
                self.__skip(-radius)
            turtle.right(6)
            
    def __get_week(self, today):
        """
        Gets the day of week.
        Takes the date of today, and returns the day of week.
        """
        week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        return week[today.weekday()]
    
    def __get_date(self, today):
        """
        Takes the date of today, and returns year, month and day of today.
        """
        y = today.year
        m = today.month
        d = today.day
        return "%d/%d/%s" % (d, m, y)
    
    def __dynamic_display(self):
        """
        Draws a dynamic display of the clock hands.
        """
        now = datetime.today()
        second = now.second + now.microsecond * 0.000001
        minute = now.minute + second / 60.0
        hour = now.hour + minute / 60.0
        sec_hand.setheading(6 * second)
        min_hand.setheading(6 * minute)
        hur_hand.setheading(30 * hour)
        
        turtle.tracer(False)
        printer.forward(65)
        printer.write(self.__get_week(now), align="center",
                      font=("Courier", 14, "bold"))
        printer.back(130)
        printer.write(self.__get_date(now), align="center",
                      font=("Courier", 14, "bold"))
        printer.home()
        turtle.tracer(True)
           
        # Continues to call the function after 100ms.
        turtle.ontimer(self.__dynamic_display(), 100)
        
    def handle(self):
        """
        Turns on/off animation and set a delay for updating the drawing.
        """
        turtle.tracer(False)
        self.__init_hands()
        self.__clock_outline(160)
        turtle.tracer(True)
        self.__dynamic_display()
        turtle.mainloop()
        	
        
if __name__ == '__main__':    
    Clock().handle()
        