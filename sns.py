import matplotlib.pyplot as plt

# First subplot
plt.subplot(1, 2, 1)
plt.title("Left Plot")
plt.plot([1, 2, 3], [4, 5, 6])

# Second subplot
plt.subplot(1, 2, 2)
plt.title("Right Plot")
plt.plot([1, 2, 3], [6, 5, 4])

plt.tight_layout()  # Adjust spacing
plt.show()
