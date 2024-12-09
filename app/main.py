import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 10))
ax.set_xlim(0, 10)
ax.set_ylim(0, 15)
ax.axis("off")

# Define the boxes and their positions
boxes = [
    (1, 14, "1. Підготовка імплантату\n(очищення, знежирення)"),
    (1, 12, "2. Вибір матеріалу покриття\n(гідроксиапатит, титановий сплав)"),
    (1, 10, "3. Нанесення покриття\n(мікроплазмове напилення)"),
    (1, 8, "4. Термічний цикл\n(нагрівання, утримання, охолодження)"),
    (1, 6, "5. Контроль якості покриття\n(візуальний огляд, тестування)"),
    (1, 4, "6. Фінальна обробка\n(полірування, стерилізація)")
]

# Draw the boxes
for x, y, text in boxes:
    box = FancyBboxPatch(
        (x, y), 8, 1.5, boxstyle="round,pad=0.3", edgecolor="black", facecolor="#cceeff"
    )
    ax.add_patch(box)
    ax.text(
        x + 4, y + 0.75, text, ha="center", va="center", fontsize=10, wrap=True
    )

# Draw the arrows
for i in range(len(boxes) - 1):
    x_start = boxes[i][0] + 4
    y_start = boxes[i][1]
    x_end = boxes[i + 1][0] + 4
    y_end = boxes[i + 1][1] + 1.5
    ax.annotate(
        "",
        xy=(x_end, y_end),
        xytext=(x_start, y_start - 0.5),
        arrowprops=dict(facecolor="black", shrink=0.05, width=1, headwidth=8)
    )

# Add the title
plt.title("Блок-схема процесу нанесення покриття на зубний імплантат", fontsize=12, pad=20)

# Save and display the figure
plt.show()
