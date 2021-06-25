"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    """
    Approach: Total width = width - 2 * GRAPH_MARGIN_SIZE
    The 1st x-axis (index == 0) is x = GRAPH_MARGIN_SIZE
    The width between 2 consecutive point: unit = (width - 2 * GRAPH_MARGIN_SIZE)/len(YEARS)
    The return x-point should be GRAPH_MARGIN_SIZE + index * unit
    """
    width_unit = (width-2 * GRAPH_MARGIN_SIZE)/len(YEARS)
    return GRAPH_MARGIN_SIZE + year_index * width_unit

def get_y_coordinate(height, name, name_data, year):
    """
    Given the height of the canvas, the name of specific baby, total name list,
    and specific year to calculate y coordinate

    Input:
        height (int): The height of the canvas
        name (str): The name for specific baby
        name_data (dict): Dictionary holding baby name data
        year (int): The specific year to get rank
    Returns:
        y_coordinate (int): The y coordinate of the vertical line associated
                              with the specified year.
    """
    """
    Approach
    The y coordinate for plot is linear with the rank, that is:
    y = int(GRAPH_MARGIN_SIZE + (rank/MAX_RANK) * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)
    a_height is the available height between top and bottom line
    str_year is to convert year (int) to year (str)
    """
    a_height = height - 2 * GRAPH_MARGIN_SIZE
    str_year = str(year)

    if str_year in name_data[name] and int(name_data[name][str_year]) < 1000:
        return int(GRAPH_MARGIN_SIZE + int(name_data[name][str_year])/MAX_RANK * a_height)
    else:
        return height - GRAPH_MARGIN_SIZE


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # Draw top and bottom horizon lines
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # Draw Vertical lines with year attached
    for index in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, index)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=str(YEARS[index]), anchor=tkinter.NW)

def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    """
    Create additional get_x_coordinate function to get y-axis
    
    Variable
    x0 is the x source coordinate
    y0 is the y source coordinate
    x1 is the x target coordinate
    y1 is the y target coordinate
    """
    # Iterate each lookup name to plot

    for name_index in range(len(lookup_names)):
        for year_index in range(len(YEARS)):
            # Get the x0 and y0 coordinate
            x0 = get_x_coordinate(CANVAS_WIDTH, year_index)
            y0 = get_y_coordinate(CANVAS_HEIGHT, lookup_names[name_index], name_data, YEARS[year_index])
            # Draw text for source point
            if y0 == CANVAS_HEIGHT - GRAPH_MARGIN_SIZE:
                canvas.create_text(x0+TEXT_DX, y0, text=f'{lookup_names[name_index]} *',
                                   anchor=tkinter.SW, fill=COLORS[name_index % 4])
            else:
                canvas.create_text(x0 + TEXT_DX, y0,
                                   text=f'{lookup_names[name_index]} {name_data[lookup_names[name_index]][str(YEARS[year_index])]}',
                                   anchor=tkinter.SW, fill=COLORS[name_index % 4])

            if YEARS[year_index] != 2010:
                # Get the target point(Text) and draw the line(Source/Target xy coordinate)
                x1 = get_x_coordinate(CANVAS_WIDTH, year_index + 1)
                y1 = get_y_coordinate(CANVAS_HEIGHT, lookup_names[name_index], name_data, YEARS[year_index+1])
                canvas.create_line(x0, y0, x1, y1, fill=COLORS[name_index % 4], width=LINE_WIDTH)
            else:
                # Draw the last point(Text)
                if y1 == CANVAS_HEIGHT - GRAPH_MARGIN_SIZE:
                    canvas.create_text(x1 + TEXT_DX, y1, text=f'{lookup_names[name_index]} *',
                                       anchor=tkinter.SW, fill=COLORS[name_index % 4])
                else:
                    canvas.create_text(x1 + TEXT_DX, y1,
                                       text=f'{lookup_names[name_index]} {name_data[lookup_names[name_index]][str(YEARS[year_index])]}',
                                       anchor=tkinter.SW, fill=COLORS[name_index % 4])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
