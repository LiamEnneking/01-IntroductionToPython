"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and liam.
"""
###############################################################################
# Done
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

t1 = rg.SimpleTurtle()
t2 = rg.SimpleTurtle()

t1.pen = rg.Pen('green', 6)
t2.pen = rg.Pen('yellow', 8)

t1.pen_down()
for k in range(13):

    t1.draw_circle(150)

    t2.draw_square(100)