# step3_tools.py
import pandas as pd
import sqlite3

# --- TOOL 1: Query Sales Data ---
def query_sales(query: str) -> str:
    """Run SQL query on gold layer sales data."""
    conn = sqlite3.connect("gold_layer.db")
    try:
        return pd.read_sql_query(query, conn).to_string()
    except Exception as e:
        return str(e)


# --- TOOL 2: Correct Sales Data ---
def correct_sales(region: str, date: str, value: int) -> str:
    """Correct invalid sales value in gold layer."""
    conn = sqlite3.connect("gold_layer.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE sales_data SET sales=? WHERE region=? AND date=?",
        (value, region, date),
    )
    conn.commit()
    return f"✅ Corrected sales for {region} on {date} → {value}"


# --- QUICK TEST ---
if __name__ == "__main__":
    print("🔎 Querying table before correction:")
    print(query_sales("SELECT * FROM sales_data"))

    print("\n🛠 Correcting anomaly...")
    print(correct_sales("South", "2025-08-02", 250))

    print("\n✅ Querying table after correction:")
    print(query_sales("SELECT * FROM sales_data"))
