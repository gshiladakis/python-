import matplotlob.pyplot as plt

# Data for Output Formatting Techniques
categories = ['Text Formatting', 'Number Formatting', 'Table Formatting']
methods = [
    ['f-string', 'format()', '% operator'],
    ['round()', 'str.format()', 'f-string'],
    ['pandas.DataFrame', 'PrettyTable', 'tabulate']
]

# Create a plot
fig, ax = plt.subplots(figsize = (8, 5))

# Plot ach category and its methods
for i, category in enumerate(categories):
    ax.text(0.1, 0.8 - i * 0.2, f"{category}:", fontsize = 14, fomntweight = 'bold', color = 'blue')
    for j, method in enumerate(methods[i]):
        ax.text(0.15, 0.75 - i * 0.2 - j * 0.05, f" - {method}", fontsize = 12, color = 'black')

  # Hide axes and gridlines
  ax.axis('off')

# Title
plt.title("Common Output Formatting Techniques in Python", fontsize = 16)

# Save the plot as PNG
plt.savefig("3a_output_formatting.png")
plt.show()
