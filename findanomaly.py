import pandas as pd

data = pd.DataFrame({"amount": [100,120,130,125,5000,135,128]})

#Calculate Z-score Standard Deviation
mean, std = data["amount"].mean(), data["amount"].std()
data["z_score"] = (data["amount"] - mean) / std
data["anomaly_z"] = data["z_score"].apply(lambda x: abs(x) > 2)


#Calculate Interquartile Range (IQR)
Q1, Q3 = data["amount"].quantile([0.25, 0.75])
IQR = Q3 - Q1
lower, upper = Q1 - 1.5*IQR, Q3 + 1.5*IQR

data["anomaly_iqr"] = ~data["amount"].between(lower, upper)

print(data)



