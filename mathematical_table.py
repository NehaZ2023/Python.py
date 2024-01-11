import pandas as pd

# Get the input number from the user
number = int(input("Enter a number: "))

# Create a list to store the results
results = []

# Loop from 1 to 10 and calculate the product
for i in range(1, 11):
    result = i * number
    results.append(result)

# Create a DataFrame with the results
df = pd.DataFrame({
    "Number": range(1, 11),
    "Result": results
})

# Print the DataFrame
print(df.to_string())
