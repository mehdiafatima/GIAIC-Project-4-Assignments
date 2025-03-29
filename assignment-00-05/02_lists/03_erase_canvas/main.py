import tkinter as tk

# Constants for canvas and grid
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 20  # Size of each cell in the grid

def create_grid(canvas, rows, cols):
    """Draws a grid of blue rectangles on the canvas."""
    cells = []
    for row in range(rows):
        row_cells = []
        for col in range(cols):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            cell = canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="white")
            row_cells.append(cell)
        cells.append(row_cells)
    return cells

def erase(event):
    """Erases cells by setting them to white when the eraser is dragged over them."""
    x, y = event.x, event.y
    row = y // CELL_SIZE
    col = x // CELL_SIZE

    # Ensure the coordinates are within bounds
    if 0 <= row < len(cells) and 0 <= col < len(cells[0]):
        cell = cells[row][col]
        canvas.itemconfig(cell, fill="yellow")

# Initialize the main window
root = tk.Tk()
root.title("Eraser on Canvas")

# Create the canvas widget
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# Calculate number of rows and columns
rows = CANVAS_HEIGHT // CELL_SIZE
cols = CANVAS_WIDTH // CELL_SIZE

# Draw the grid
cells = create_grid(canvas, rows, cols)

# Add the eraser functionality
canvas.bind("<B1-Motion>", erase)  # Detect mouse drag with left button pressed

# Run the tkinter event loop
root.mainloop()
