import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, ax = plt.subplots(figsize=(8, 8))

# Grid limits
ax.set_xlim(0, 50)
ax.set_ylim(0, 50)

# Draw the squares
squares = [
    (15, 15, 20, 20),  # 20x20 square: x=15-35, y=15-35
    (16, 16, 5, 5),    # 5x5 square: x=16-21, y=16-21
    (23, 23, 10, 10),  # 10x10 square: x=23-33, y=23-33
    (30, 18, 1, 1),    # 1x1 square: x=30-31, y=30-31
]

for x, y, w, h in squares:
    ax.add_patch(Rectangle((x, y), w, h,
                           fill=False,
                           edgecolor='red',
                           linewidth=2))

# Draw grid
ax.set_xticks(range(0, 51))
ax.set_yticks(range(0, 51))
ax.grid(True)

# Make cells square
ax.set_aspect('equal')

plt.title("50×50 Grid with Squares")
plt.show()