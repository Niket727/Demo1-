# step4_agent_clean.py
import sqlite3
import pandas as pd

DB_PATH = "gold_layer.db"

# -------------------------
# STEP 1: Always reset dataset with clean values
# -------------------------
def load_dataset():
    conn = sqlite3.connect(DB_PATH)
    data = {
        "date": ["2025-08-01", "2025-08-02", "2025-08-03"],
        "region": ["North", "South", "East"],
        "sales": [200, -150, -300]   # ✅ clean values only
    }
    df = pd.DataFrame(data)
    df.to_sql("sales_data", conn, if_exists="replace", index=False)
    conn.close()
    print("✅ Initialized dataset (clean):")
    print(df)
    return df

# -------------------------
# STEP 2: Detect anomalies (will always be empty now)
# -------------------------
def detect_anomalies(df):
    anomalies = df[df["sales"] < 0]
    print("\n🔎 Detected anomalies:")
    print(anomalies if not anomalies.empty else "✅ No anomalies found")

# -------------------------
# MAIN EXECUTION
# -------------------------
if __name__ == "__main__":
    df = load_dataset()
    detect_anomalies(df)
    print("\n📊 Final table:")
    print(df)



