import matplotlib.pyplot as plt

y = [10, 191, 11, 12]
x = ["a", "b", "c", "d"]

# Define colors as a list of color names or RGB values
colors = ['r', 'g', 'b', 'y']

# Create bars with different colors
bars = plt.bar(x, y, color=colors)

# Add labels for each bar (optional)
for bar in bars:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(bar.get_height()),ha='center', va='bottom')

# Create legend
plt.legend(bars, x)

plt.xlabel("all")
plt.ylabel("num")
plt.title("bar graph")

plt.show()
