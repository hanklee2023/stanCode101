"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gimage import GImage
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.

class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.__window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        paddle_x = (self.__window.width - paddle_width) / 2
        paddle_y = self.__window.height - paddle_offset
        self.__paddle = GRect(paddle_width, paddle_height, x=paddle_x, y=paddle_y)
        self.__paddle.filled = True
        self.__paddle.fill_color = 'black'
        self.__paddle.color = 'black'
        self.__window.add(self.__paddle)

        # Create a scoreboard
        self.create_the_scoreboard()

        # Center a filled ball in the graphical window
        self.__ball_radius = ball_radius
        self.reset_the_ball()

        # Default initial velocity for the ball
        self.initialize_the_velocity()

        # Initialize our mouse listeners
        # Create a mouse lock to check ball move
        self.__lock = False
        onmouseclicked(self.handle_click)
        onmousemoved(self.handle_move)

        # Initial other Variable
        self.__additional_bricks = 0
        self.__total_brick = BRICK_ROWS * BRICK_ROWS + self.__additional_bricks

        # Draw bricks
        self.__brick_width = brick_width
        self.__brick_height = brick_height
        self.__brick_spacing = brick_spacing
        self.__brick_offset = brick_offset

        for y in range(brick_rows):
            for x in range(brick_cols):
                bx = x * (self.__brick_width + self.__brick_spacing)
                by = brick_offset + y * (self.__brick_height + self.__brick_spacing)
                self.__brick = GRect(self.__brick_width, self.__brick_height, x=bx, y=by)
                self.__brick.filled = True

                if y < 2:
                    self.__brick.fill_color = 'red'
                    self.__brick.color = 'red'
                elif 2 <= y < 4:
                    self.__brick.fill_color = 'orange'
                    self.__brick.color = 'orange'
                elif 4 <= y < 6:
                    self.__brick.fill_color = 'yellow'
                    self.__brick.color = 'yellow'
                elif 6 <= y < 8:
                    self.__brick.fill_color = 'green'
                    self.__brick.color = 'green'
                else:
                    self.__brick.fill_color = 'blue'
                    self.__brick.color = 'blue'

                self.__window.add(self.__brick)

    # Instance Method to reset the ball
    def reset_the_ball(self):
        ball_x = (self.__window.width - self.__ball_radius * 2) / 2
        ball_y = (self.__window.height - self.__ball_radius * 2) / 2
        self.__ball = GOval(self.__ball_radius * 2, self.__ball_radius * 2, x=ball_x, y=ball_y)
        self.__ball.filled = True
        self.__ball.fill_color = 'black'
        self.__ball.color = 'black'
        self.__window.add(self.__ball)

    # Instance Method to initialize the velocity
    def initialize_the_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED

        if (random.random() > 0.5):
            self.__dx = -self.__dx

    # Instance Method to create the scoreboard
    def create_the_scoreboard(self):
        self.__score = 0
        self.__score_b = GLabel("Score: "+str(self.__score))
        self.__score_b.font = '-30'
        self.__score_b.color = 'black'
        self.__window.add(self.__score_b, x=0, y=self.__window.height)

        # Create the icon for lives
        self.__img1 = GImage('love.jpeg')
        self.__window.add(self.__img1, self.__window.width - self.__img1.width,
                          self.__window.height - self.__img1.height)
        self.__img2 = GImage('love.jpeg')
        self.__window.add(self.__img2, self.__window.width - 2 * self.__img1.width,
                          self.__window.height - self.__img2.height)
        self.__img3 = GImage('love.jpeg')
        self.__window.add(self.__img3, self.__window.width - 3 * self.__img3.width,
                          self.__window.height - self.__img3.height)

    # Instance Method to check score items and life icons
    def get_the_scoreboard(self):
        self.__score_icon = []
        self.__score_icon.append(self.__score_b)
        self.__score_icon.append(self.__img1)
        self.__score_icon.append(self.__img2)
        self.__score_icon.append(self.__img3)
        return self.__score_icon

    # Instance Method to get the latest score
    def get_the_score(self):
        return self.__score

    # Instance Method to get window
    def get_window(self):
        return self.__window

    # Instance Method to get paddle
    def get_paddle(self):
        return self.__paddle

    # Instance Method to get ball
    def get_ball(self):
        return self.__ball

    # Instance Method to get ball x velocity
    def get_ball_dx(self):
        return self.__dx

    # Instance Method to get ball x velocity
    def get_ball_dy(self):
        return self.__dy

    # Instance Method to get ball move lock
    def get_lock(self):
        return self.__lock

    # Instance Method to get ball move lock
    def set_lock(self, switch):
        self.__lock = switch

    # Instance Method to get total bricks
    def get_total_brick(self):
        return self.__total_brick

    # Instance Method to check collision object
    def check_collision(self):
        obj = None

        for x in range(1):
            for y in range(1):
                bx = self.__ball.x + x * self.__ball.width
                by = self.__ball.y + y * self.__ball.height
                obj = self.__window.get_object_at(bx, by)
                if obj is not None:
                    break
        return obj

    # Instance Method to reflect mouse click
    def handle_click(self, event):
        if not self.__lock:
            self.__lock = True

    # Instance Method to handle mouse move
    def handle_move(self, event):
        if event.x - self.__paddle.width/2 <= 0:
            self.__paddle.x = 0
        elif event.x + self.__paddle.width/2 >= self.__window.width:
            self.__paddle.x = self.__window.width - self.__paddle.width
        else:
            self.__paddle.x = event.x - self.__paddle.width/2

    # Instance Method to set life
    def set_lives(self, life):
        if life == -1:
            self.__window.remove(self.__window.get_object_at(self.__window.width - self.__img1.width * self.__life,
                                                             self.__window.height - self.__img1.height))
            self.__life -= 1
        else:
            self.__life = life

    # Calculate total score and update scoreboard
    # red = 50, orange = 40, yellow = 30, green = 20, blue = 10
    def calculate_score(self, brick):
        # one unit = brick_height + brick_spacing
        unit = self.__brick_height + self.__brick_spacing
        if self.__brick_offset <= brick.y < self.__brick_offset + 2 * unit:
            self.__score += 50
        elif self.__brick_offset + 2 * unit <= brick.y < self.__brick_offset + 4 * unit:
            self.__score += 40
        elif self.__brick_offset + 4 * unit <= brick.y < self.__brick_offset + 6 * unit:
            self.__score += 30
        elif self.__brick_offset + 6 * unit <= brick.y < self.__brick_offset + 8 * unit:
            self.__score += 20
        elif self.__brick_offset + 8 * unit <= brick.y < self.__brick_offset + 10 * unit:
            self.__score += 10

        self.__score_b.text = "Score: "+str(self.__score)
        self.__total_brick -= 1

    # Calculate the result for game finish
    def show_the_result(self):
        self.__window.clear()
        title = GLabel("Your Final Score")
        title.font = '-40'
        title.color = 'green'

        score = GLabel(self.__score)
        score.font = '-100'
        score.color = 'blue'

        self.__window.add(title, (self.__window.width - title.width)/2, title.height + 100)
        self.__window.add(score, (self.__window.width - score.width)/2, (self.__window.height + score.height)/2)