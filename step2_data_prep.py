# step2_data_prep.py
import pandas as pd
import sqlite3

# Simulated gold layer dataset
data = {
    "date": ["2025-08-01", "2025-08-02", "2025-08-03"],
    "region": ["North", "South", "East"],
    "sales": [200, -150, 300]  # anomaly: -150 (invalid negative sales)
}

# Create dataframe
df = pd.DataFrame(data)

# Connect to SQLite (local DB file acts as gold data layer)
conn = sqlite3.connect("gold_layer.db")

# Save table
df.to_sql("sales_data", conn, if_exists="replace", index=False)

# Verify by reading back
print("Data stored in gold_layer.db:")
print(pd.read_sql_query("SELECT * FROM sales_data", conn))

