"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# Constant to define static value
SIZE = 10

# Global Variable
window = GWindow(width=800, height=500, title='MyLine')
click_count = False # To track click time. False:, True: even
last_oval = None # To get the last Oval info (Store Object)

def main():

    onmouseclicked(draw)

def draw(event):

    global last_oval
    global click_count

    if click_count:
        # if click = even, eliminate last oval and connect 2 nodes to line
        line = GLine(last_oval.x + last_oval.width/2, last_oval.y + last_oval.height/2, event.x, event.y)
        window.remove(last_oval)
        window.add(line)
        click_count = False
    else:
        # if click = odd, create an oval on the window
        oval = GOval(SIZE, SIZE)
        window.add(oval, event.x - oval.width / 2, event.y - oval.height / 2)
        last_oval = oval
        click_count = True

if __name__ == "__main__":
    main()
