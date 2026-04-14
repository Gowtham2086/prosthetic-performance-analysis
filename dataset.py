import pandas as pd
import numpy as np

np.random.seed(42)

data = {
    "user_id": range(1, 51),
    "accuracy": np.random.randint(60, 100, 50),
    "comfort": np.random.randint(4, 10, 50),
    "signal_strength": np.random.uniform(0.5, 1.0, 50),
    "session_time": np.random.randint(10, 60, 50)
}

df = pd.DataFrame(data)
df.to_csv("prosthetic_data.csv", index=False)

print("Dataset created!")
print(df.head())