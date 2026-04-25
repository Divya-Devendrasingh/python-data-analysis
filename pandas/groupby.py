import pandas as pd

df = pd.DataFrame({
    "customer": ["A", "A", "B", "C"],
    "amount": [100, 200, 300, 400]
})

print(df.groupby("customer")["amount"].sum())
