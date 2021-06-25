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

# - TODO on 2021.05.02 for extension
# - 1. Life Icon
# - 2. different score for colors - more comment
# - 3. three difficulty for the games - hard, medium, easy
# - 4. hard is to speed up for scores, and supplement new bricks
# - 5. medium is the assignment, easy is the lowest one
# - 6. Create intro page and finish page

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

        # Initial brick Variable
        self.__brick_width = brick_width
        self.__brick_height = brick_height
        self.__brick_spacing = brick_spacing
        self.__brick_offset = brick_offset
        self.__brick_rows = brick_rows
        self.__brick_cols = brick_cols
        self.__brick_move = 0

        # Initial Paddle Variable
        self.__paddle_width = paddle_width
        self.__paddle_height = paddle_height
        self.__paddle_offset = paddle_offset

        # Initial Ball Variable
        self.__ball_radius = ball_radius

        # Initial other Variable
        self.__score = 0                        # Track total scores
        self.__difficulty = None                # Track difficulty
        self.__lock = False
        self.__initial_page_lock = False        # The lock for initial difficulty selection
        self.__list_of_tools = []               # Set additional list to track extra tools for bonus/surprise

        # Create a initial window page
        self.initial_page()

        # Create a paddle
        paddle_x = (self.__window.width - self.__paddle_width) / 2
        paddle_y = self.__window.height - self.__paddle_offset
        self.__paddle = self.create_the_paddle(self.__paddle_width, self.__paddle_height, x=paddle_x, y=paddle_y)

        # Initialize our mouse listeners
        # Create a mouse lock to check ball move
        onmouseclicked(self.handle_click)
        onmousemoved(self.handle_move)

    # Instance Method to initialize page for difficulty selection
    def initial_page(self):
        self.__initial_page_lock = True

        # Define Options
        self.__option = GLabel("Click Difficulty")
        self.__option.font = '-40'
        self.__option.color = 'green'
        self.__window.add(self.__option, (self.__window.width - self.__option.width) / 2, self.__option.height)

        # Define Easy Intro
        self.__easy_label = GLabel("EASY")
        self.__easy_label.font = '-80'
        self.__easy_label.color = 'black'
        self.__window.add(self.__easy_label, (self.__window.width - self.__easy_label.width)/2,
                          (self.__window.height + self.__easy_label.height)/ 4 * 3 )
        self.__easy_intro = GLabel("velocity is slow, brick is more, brick is static")
        self.__easy_intro.font = '-20'
        self.__easy_intro.color = 'blue'
        self.__window.add(self.__easy_intro, (self.__window.width - self.__easy_intro.width) / 2,
                          self.__easy_label.y + 20)
        # Define Mid Intro
        self.__mid_label = GLabel("NORMAL")
        self.__mid_label.font = '-80'
        self.__mid_label.color = 'black'
        self.__window.add(self.__mid_label, (self.__window.width - self.__mid_label.width) / 2,
                          (self.__window.height + self.__mid_label.height) / 4 * 2 )
        self.__mid_intro = GLabel("velocity is normal, brick is normal, brick is static")
        self.__mid_intro.font = '-20'
        self.__mid_intro.color = 'blue'
        self.__window.add(self.__mid_intro, (self.__window.width - self.__mid_intro.width) / 2, self.__mid_label.y + 20)

        # Define Hard Intro
        self.__hard_label = GLabel("HARD")
        self.__hard_label.font = '-80'
        self.__hard_label.color = 'black'
        self.__window.add(self.__hard_label, (self.__window.width - self.__hard_label.width) / 2,
                          (self.__window.height + self.__hard_label.height) / 4 * 1 )
        self.__hard_intro = GLabel("velocity is fast, brick is normal, brick is moving")
        self.__hard_intro.font = '-20'
        self.__hard_intro.color = 'blue'
        self.__window.add(self.__hard_intro, (self.__window.width - self.__hard_intro.width) / 2, self.__hard_label.y + 20)

    # Instance Method to configure initial set in different difficulty
    def initialize_set(self, difficulty):
        self.__window.add(self.__paddle)

        # Create a scoreboard
        self.create_the_scoreboard()

        # Center a filled ball in the graphical window
        self.reset_the_ball()

        # Default initial velocity for the ball
        self.initialize_the_velocity(difficulty)

        # Layout the bricks in different difficulty
        self.create_the_brick(difficulty)

    # Instance Method to create new filled paddle
    def create_the_paddle(self, width, height, x=0, y=0):
        paddle = GRect(width, height, x=x, y=y)
        paddle.filled = True
        paddle.fill_color = 'black'
        paddle.color = 'black'

        return paddle

    # Instance Method to reset the ball
    def reset_the_ball(self):
        ball_x = (self.__window.width - self.__ball_radius * 2) / 2
        ball_y = (self.__window.height - self.__ball_radius * 2) / 2 + \
                 self.__brick_move * (self.__brick_height + self.__brick_spacing)
        self.__ball = GOval(self.__ball_radius * 2, self.__ball_radius * 2, x=ball_x, y=ball_y)
        self.__ball.filled = True
        self.__ball.fill_color = 'black'
        self.__ball.color = 'black'
        self.__window.add(self.__ball)

    # Instance Method to initialize the velocity
    def initialize_the_velocity(self, difficulty):
        if difficulty == 'easy':
            self.__dx = random.randint(1, MAX_X_SPEED - 2)
            self.__dy = INITIAL_Y_SPEED
        elif difficulty == 'mid':
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
        elif difficulty == 'hard':
            self.__dx = random.randint(3, MAX_X_SPEED + 5)
            self.__dy = INITIAL_Y_SPEED

        if (random.random() > 0.5):
            self.__dx = -self.__dx

    # Instance Method to create the scoreboard
    def create_the_scoreboard(self):
        self.__score_b = GLabel("Score: " + str(self.__score))
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

    # Instance Method to layout bricks
    def create_the_brick(self, difficulty):
        if difficulty == 'easy':
            self.__brick_rows = self.__brick_rows + 2

        for y in range(self.__brick_rows):
            for x in range(self.__brick_cols):
                bx = x * (self.__brick_width + self.__brick_spacing)
                by = self.__brick_offset + y * (self.__brick_height + self.__brick_spacing)
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
                elif 8 <= y < 10:
                    self.__brick.fill_color = 'blue'
                    self.__brick.color = 'blue'
                else:
                    self.__brick.fill_color = 'purple'
                    self.__brick.color = 'purple'

                self.__window.add(self.__brick)

        self.__total_brick = self.__brick_rows * self.__brick_cols

    # Instance Method to check initial selection
    def check_initial_result(self):
        return self.__initial_page_lock

    # Instance Method to get the list of score items and life icons
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

    # Instance Method to get difficulty
    def get_difficulty(self):
        return self.__difficulty

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

    # Instance Method to handle mouse click
    def handle_click(self, event):
        if self.__initial_page_lock:
            if self.__window.get_object_at(event.x, event.y) == self.__easy_label:
                self.__difficulty = 'easy'
                self.__window.clear()
                self.__initial_page_lock = False
            elif self.__window.get_object_at(event.x, event.y) == self.__mid_label:
                self.__difficulty = 'mid'
                self.__window.clear()
                self.__initial_page_lock = False
            elif self.__window.get_object_at(event.x, event.y) == self.__hard_label:
                self.__difficulty = 'hard'
                self.__window.clear()
                self.__initial_page_lock = False
        else:
            if not self.__lock:
                self.__lock = True

    # Instance Method to handle mouse move
    def handle_move(self, event):
        if self.__initial_page_lock:
            pass
        else:
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

        if self.__brick_move >= 12:
            self.revert_the_brick()

    # Instance Method to calculate total score and update scoreboard
    # red = 50, orange = 40, yellow = 30, green = 20, blue = 10, purple = 10
    def calculate_score(self, brick, difficulty='mid'):
        # one unit = brick_height + brick_spacing
        if difficulty == 'mid' or difficulty == 'easy':         # Easy and mid difficulty
            k = 0
        else:                                                   # Hard mode. The brick shifted before
            k = self.__brick_move

        unit = self.__brick_height + self.__brick_spacing
        if self.__brick_offset <= brick.y < self.__brick_offset + (2+k) * unit:
            self.__score += 50
        elif self.__brick_offset + (2+k) * unit <= brick.y < self.__brick_offset + (4+k) * unit:
            self.__score += 40
        elif self.__brick_offset + (4+k) * unit <= brick.y < self.__brick_offset + (6+k) * unit:
            self.__score += 30
        elif self.__brick_offset + (6+k) * unit <= brick.y < self.__brick_offset + (8+k) * unit:
            self.__score += 20
        elif self.__brick_offset + (8+k) * unit <= brick.y < self.__brick_offset + (10+k) * unit:
            self.__score += 10
        else:
            self.__score += 10

        self.__score_b.text = "Score: "+str(self.__score)
        self.__total_brick -= 1

        if difficulty == 'hard':                                # Hard mode. The brick might shift
            dice = random.randint(1,100)
            if dice > 95:
                self.move_brick()

    # Instance Method to generate tools for surprise
    # Total tools are 5 colors and different length for purpose
    # Type1: length = 18, color = 'pink', paddle increase 10%
    # Type2: length = 19, color = 'salmon', paddle decrease 10%
    # Type3: length = 20, color = 'darkgreen', score + 50
    # Type4: length = 21, color = 'deepskyblue', score + 100
    # Type5: length = 22, color = 'silver', score - 100
    # The total tools in the same screen should be less than (and equal) 5
    def generate_tools(self, type, x, y):
        if len(self.__list_of_tools) <= 5:
            if type == 1:
                obj = GRect(18, 18)
                obj.filled = True
                obj.fill_color = 'pink'
                obj.color = 'pink'
            elif type == 2:
                obj = GRect(19, 19)
                obj.filled = True
                obj.fill_color = 'salmon'
                obj.color = 'salmon'
            elif type == 3:
                obj = GRect(20, 20)
                obj.filled = True
                obj.fill_color = 'darkgreen'
                obj.color = 'darkgreen'
            elif type == 4:
                obj = GRect(21, 21)
                obj.filled = True
                obj.fill_color = 'deepskyblue'
                obj.color = 'deepskyblue'
            elif type == 5:
                obj = GRect(22, 22)
                obj.filled = True
                obj.fill_color = 'silver'
                obj.color = 'silver'

            self.__list_of_tools.append(obj)
            self.__window.add(obj, x, y)

    # Instance Method to return extra tool list
    def get_tool_list(self):
        return self.__list_of_tools

    # Instance Method to check tool result
    # Type1: length = 18, color = 'pink', paddle increase 10%
    # Type2: length = 19, color = 'salmon', paddle decrease 10%
    # Type3: length = 20, color = 'darkgreen', score + 50
    # Type4: length = 21, color = 'deepskyblue', score + 100
    # Type5: length = 22, color = 'silver', score - 100
    def check_tool_result(self, tool_list):
        for tool in tool_list:
            if self.__window.get_object_at(tool.x, tool.y + tool.height + 1) == self.__paddle \
                    or self.__window.get_object_at(tool.x + tool.width, tool.y + tool.height + 1) == self.__paddle:
                    self.__window.remove(tool)

                    if tool.width == 18:
                        new_paddle = self.create_the_paddle(self.__paddle.width * 1.1, self.__paddle.height, x=self.__paddle.x, y=self.__paddle.y)
                        self.__window.remove(self.__paddle)
                        self.__paddle = None
                        self.__paddle = new_paddle
                        self.__window.add(self.__paddle)
                    elif tool.width == 19:
                        new_paddle = self.create_the_paddle(self.__paddle.width * 0.9, self.__paddle.height, x=self.__paddle.x, y=self.__paddle.y)
                        self.__window.remove(self.__paddle)
                        self.__paddle = None
                        self.__paddle = new_paddle
                        self.__window.add(self.__paddle)
                    elif tool.width == 20:
                        self.__score += 50
                    elif tool.width == 21:
                        self.__score += 100
                    elif tool.width == 22:
                        self.__score -= 100

                    tool_list.remove(tool)

            if tool.y + tool.height > self.__window.height:
                self.__window.remove(tool)
                tool_list.remove(tool)

    # Instance Method to shift total bricks for 2 rows and supplement 2 new black rows
    def move_brick(self):
        if self.__brick_move <= 12:
            # Shift brick for 2 units (space + height)
            for y in range(self.__brick_rows + self.__brick_move, 0, -1):
                for x in range(self.__brick_cols):
                    bx = x * (self.__brick_width + self.__brick_spacing)
                    by = self.__brick_offset + y * (self.__brick_height + self.__brick_spacing) - self.__brick_spacing
                    obj = self.__window.get_object_at(bx, by)

                    if obj is not None:
                        self.__window.remove(obj)
                        self.__window.add(obj, bx, by + 1 * self.__brick_height + 2 * self.__brick_spacing)

            # Supplement 2 rows of bricks
            for y in range(2):
                for x in range(self.__brick_cols):
                    bx = x * (self.__brick_width + self.__brick_spacing)
                    by = self.__brick_offset + y * (self.__brick_height + self.__brick_spacing)
                    self.__brick = GRect(self.__brick_width, self.__brick_height, x=bx, y=by)
                    self.__brick.filled = True
                    self.__brick.color = 'black'
                    self.__brick.fill_color = 'black'
                    self.__window.add(self.__brick)

            self.__brick_move += 2
            self.__total_brick += 20

    # Instance Method to shift upward 2 row of bricks if too many bricks shifted
    def revert_the_brick(self):
        # Remove bricks for x(move_back) rows
        remove_brick = 0

        if self.__brick_move <= 12:
            move_back = 6
        else:
            move_back = 8

        # Remove x(move_back) rows for brick
        for y in range(move_back):
            for x in range(self.__brick_cols):
                bx = x * (self.__brick_width + self.__brick_spacing)
                by = self.__brick_offset + y * (self.__brick_height + self.__brick_spacing)
                obj = self.__window.get_object_at(bx, by)

                if obj is not None:
                    self.__window.remove(obj)
                    remove_brick += 1
        # Move upward x(move_back) rows for brick
        for y in range(self.__brick_rows + self.__brick_move):
            for x in range(self.__brick_cols):
                bx = x * (self.__brick_width + self.__brick_spacing)
                by = self.__brick_offset + y * (self.__brick_height + self.__brick_spacing)
                obj = self.__window.get_object_at(bx, by)

                if obj is not None:
                    self.__window.remove(obj)
                    self.__window.add(obj, bx, by - move_back * (self.__brick_height + self.__brick_spacing))

        self.__brick_move -= move_back
        self.__total_brick -= remove_brick

    # Instance Method to calculate the result
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