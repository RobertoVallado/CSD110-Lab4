from whichturtle import whichturtle 

if whichturtle == "ASCII":

    # Adapted from here: https://stackoverflow.com/a/13103231/1030345
    class Turtle(object):
        def __init__(self):
            self.path = [(0, 0, True)]              # Sequential list of turtle locations
            self.draw = True                        # True if pen is down; False otherwise
            self.direction = (1, 0)                 # Direction vector, (x, y)
            self.show_penup_path = False            # True to show path even when pen is up

        def showturtle(self):
            """Show the turtle's path, even if pen is up.
                NOTE: This is different than the effect on TK turtle, 
                but it's used to keep the interface consistent.
            """
            self.show_penup_path = True
        def st(self):
            self.showturtle()

        def hideturtle(self):
            """Do not show the turtle's path when the pen is up.
                NOTE: This is different than the effect on TK turtle, 
                but it's used to keep the interface consistent.
            """
            self.show_penup_path = False
        def ht(self):
            self.hideturtle()

        def _drag_pen(self, distance, direction=1):
            """Move the turtle distance spaces in the given direction
                - Distance must be an integer
                - Direction must be 1 or -1
            """
            (prev_x, prev_y, prev_space_marked) = self.path[-1]
            if distance != 0 and self.draw and not prev_space_marked:
                # If the pen is down and the previous space in the path has no mark,
                # (i.e the pen was brought down between this move and the last)
                # then it needs to get marked, otherwise the space on which the pen came
                # down won't get a mark
                self.path[-1] = (prev_x, prev_y, True)
            for i in range(1, distance + 1):
                self.path.append((prev_x + direction*self.direction[0] * i,
                                prev_y + direction*self.direction[1] * i,
                                self.draw))

        def forward(self, distance):
            """Move the turtle forward distance spaces
                - Distance must be an integer
            """
            self._drag_pen(distance, 1)
        def fd(self, distance):
            self.forward(distance)
                
        def backward(self, distance):
            """Move the turtle backward distance spaces
                - Distance must be an integer
            """
            self._drag_pen(distance, -1)
        def back(self, distance):
            self.backward(distance)
        def bk(self, distance):
            self.backward(distance)

        def penup(self):
            """Pull the turtle's pen up, so it does not draw while it is moving
            """
            self.draw = False
        def up(self):
            self.penup()
        def pu(self):
            self.penup()
        
        def pendown(self):
            """Put the turtle's pen down, so it draws while it is moving
            """
            self.draw = True
            #(x, y, _) = self.path[-1]
            #self.path[-1] = (x, y, True)
        def down(self):
            self.penup()
        def pd(self):
            self.penup()
            
        def right(self, angle):
            """Turn the turtle to the right by `angle` degrees
                - Angle must be 90
            """
            assert angle == 90, "asciiturtle only allows 90deg turns"
            self.direction = self.direction[1], -self.direction[0]
        def rt(self, distance):
            self.right(distance)

        def left(self, angle):
            """Turn the turtle to the left by `angle` degrees
                - Angle must be 90
            """
            assert angle == 90, "asciiturtle only allows 90deg turns"
            self.direction = -self.direction[1], self.direction[0]
        def lt(self, distance):
            self.left(distance)
            
        def get_path_grid(self):
            """Convert the path to a square grid with the path marked"""

            # Determine the furthest positions of the turtle in each direction
            minx, maxx, maxy, miny = [f(xy[i] for xy in self.path)
                            for i in [0, 1] for f in [min, max]]
            miny, maxy = -miny, -maxy  # Flip the y-coordinates so that positive is down

            # Make a 2d grid of spaces of a size that will fit the whole path
            grid = [[' '] * (maxx - minx + 1) for _ in range(maxy - miny + 1)]

            # Draw the path onto the grid
            for x, y, draw in self.path:
                current_mark = grid[-y - miny][x - minx]

                # Don't overwrite pendown marks with penup-path marks
                if ( current_mark != '#' ):
                    grid[-y - miny][x - minx] = '#' if draw else ('.' if self.show_penup_path else ' ')
                if self.show_penup_path and x == self.path[-1:][0][0] and y == self.path[-1:][0][1]:
                    turtle_mark = ">"
                    if self.direction == (0,1):
                        turtle_mark = "^"
                    elif self.direction == (0,-1):
                        turtle_mark = "v"
                    elif self.direction == (-1,0):
                        turtle_mark = "<"
                    grid[-y - miny][x - minx] = turtle_mark
                    
            return grid

        # This is just here so that TK turtle scripts that involve speed calls
        # work as asciiturtle scripts also
        def speed(self, s):
            pass

        def path_as_str(self):
            """Convert the path grid to a string"""
            return '\n'.join(''.join(row) for row in self.get_path_grid())

        def print(self):
            """Print the path taken by the turtle to the console"""
            print(self.path_as_str())

    def done():
        pass

else:
    import turtle

    Turtle = turtle.Turtle
    done = turtle.done