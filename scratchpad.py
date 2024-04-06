import turtle

# import src.lab4_4 as lab4_4
# import src.lab4_5 as lab4_5
# import src.lab4_7 as lab4_7
# import src.lab4_9 as lab4_9

if __name__ == "__main__":
    t = turtle.Turtle()

    #############################################################################
    # Use this section to experiment with the turtle module                     #
    # 
    
    # Here is some example turtle code.  You may change/remove it as much as you like.
    t.forward(10)
    t.penup()
    t.right(90)
    t.forward(2)
    t.pendown()
    t.right(90)
    t.forward(10)

    # The line below is required by the asciiturtle module to show a drawing.
    # However, it will cause an error when using the graphical turtle module.
    # It is OK to ignore this error for now.
    t.print()

    # This line will prevent the window from closing when using the GUI turtle module
    turtle.done()

    #                                                                           #
    #                                                                           #
    #############################################################################