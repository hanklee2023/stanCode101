"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    dx = graphics.get_ball_dx()     # Get initial x-axis speed
    dy = graphics.get_ball_dy()     # Get initial y-axis speed
    life = NUM_LIVES                # Total lives
    graphics.set_lives(life)        # Update Life boards

    # Add animation loop here!
    while True:
        pause(FRAME_RATE)

        if graphics.get_lock():
            graphics.get_ball().move(dx, dy)

            # The condition to bounce for the window boundary
            if graphics.get_ball().x + graphics.get_ball().width >= graphics.get_window().width or \
                    graphics.get_ball().x <= 0:
                dx = -dx
            if graphics.get_ball().y <= 0:
                dy = -dy

            # The condition that life will reduce
            if graphics.get_ball().y + graphics.get_ball().height > \
                    graphics.get_window().height + graphics.get_ball().height:
                graphics.set_lives(-1)
                life -= 1
                if life > 0:
                    graphics.reset_the_ball()               # Move the ball back to initial position
                    graphics.initialize_the_velocity()      # Initialize the speed
                    dx = graphics.get_ball_dx()
                    dy = graphics.get_ball_dy()
                    graphics.set_lock(False)
                else:
                    break

            # The condition that whole bricks are eliminated
            if graphics.get_total_brick() == 0:
                break

            # Local variable for collision result
            obj = graphics.check_collision()
            if obj is not None:
                if obj == graphics.get_paddle():
                    graphics.get_ball().y = graphics.get_paddle().y - graphics.get_ball().height
                    dy = -dy
                elif obj in graphics.get_the_scoreboard():
                    pass
                else:
                    graphics.get_window().remove(obj)
                    graphics.calculate_score(obj)
                    dy = -dy

    graphics.show_the_result()


if __name__ == '__main__':
    main()
