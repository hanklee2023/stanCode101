"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global Variable
window = GWindow(800, 500, title='bouncing_ball.py')
oval = GOval(SIZE, SIZE) # Announce the ball
count = 0 # To count for total mouse click
lock = False # A lock for ball bouncing

def main():
    oval.filled = True
    oval.fill_color = 'black'
    window.add(oval, START_X, START_Y)

    onmouseclicked(ball_move)

def ball_move(event):
    global vy
    global count
    global lock

    if not lock:
        lock = True
        vy = 0 # Velocity for y-axis

        while oval.x <= window.width:
            vy += GRAVITY
            oval.move(VX, vy)
            if oval.y >= window.height:
                vy = -vy * REDUCE
            pause(DELAY)

        count += 1

        if count < 3:
            window.add(oval, START_X, START_Y)
            lock = False

if __name__ == "__main__":
    main()
