import pyodbc, pandas

conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};server=MRIYX05RCBV;database=sales;uid=c#_database;pwd=roots;TrustServerCertificate=yes;"
)
def retail_sales_dataset_function(conn_string):
    items = conn_string.cursor().execute("select * from retail_sales_dataset").fetchall()
    retail_sales_dataset = [{
        "Transaction_ID": item.Transaction_ID, "Date": item.Date, "Customer_ID": item.Customer_ID,
        "Gender": item.Gender, "Age": item.Age, "Product_Category": item.Product_Category, "Quantity": item.Quantity,
        "Price_per_Unit": item.Price_per_Unit, "Total_Amount": item.Total_Amount
    } for item in items]
    return retail_sales_dataset
retail_sales_dataset = pandas.DataFrame(retail_sales_dataset_function(conn))
retail_sales_dataset.to_csv("retail_sales_dataset.csv", index=False)
   

