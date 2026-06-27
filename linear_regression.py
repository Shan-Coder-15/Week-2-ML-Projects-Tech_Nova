import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create Dataset
x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 4, 5, 4, 5, 7])

# Step 2: Calculate Slope (m)
mean_x = np.mean(x)
mean_y = np.mean(y)

numerator = np.sum((x - mean_x) * (y - mean_y))
denominator = np.sum((x - mean_x) ** 2)

m = numerator / denominator

# Step 3: Calculate Intercept (c)
c = mean_y - (m * mean_x)

# Step 4: Make Predictions
y_pred = m * x + c

# Step 5: Calculate Mean Squared Error (MSE)
mse = np.mean((y - y_pred) ** 2)

# Display Results
print("Slope (m):", round(m, 2))
print("Intercept (c):", round(c, 2))
print("Predicted Values:", np.round(y_pred, 2))
print("Mean Squared Error:", round(mse, 2))

# Step 6: Visualization (Optional)
plt.scatter(x, y, color="blue", label="Actual Data")
plt.plot(x, y_pred, color="red", label="Regression Line")
plt.title("Linear Regression from Scratch")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
