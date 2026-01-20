import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


data = {
    "hours_studied": [1, 2, 3, 4, 5, 6, 7, 8],
    "exam_score":   [35, 40, 50, 60, 65, 75, 85, 90]
}

df = pd.DataFrame(data)
print(df)
plt.scatter(df["hours_studied"], df["exam_score"])
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.title("Study Hours vs Exam Score")
plt.show()
# Step 3: Prepare input (X) and output (y)
X = df[["hours_studied"]]   # input (feature)
y = df["exam_score"]        # output (label)

# Step 4: Train the model
model = LinearRegression()
model.fit(X, y)

# Step 5: Make a prediction
new_data = pd.DataFrame({"hours_studied": [5.5]})
predicted_score = model.predict(new_data)

print("Predicted score for 5.5 hours of study:", predicted_score[0])
