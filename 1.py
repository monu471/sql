
import mysql.connector as conn
from  sqlalchemy import create_engine ,types
import pandas as pd
if __name__  == "__main__":
    eng = create_engine("mysql://root:monu471@localhost/civil")
    df1 = pd.read_csv(r"C:\Users\MY\seaborn-data\iris.csv")
    df1.to_sql("iris", con = eng,index = False,if_exists="append" )
    db = conn.connect(host = "localhost",user = "root",password = "monu471",database = "civil")
    cursor = db.cursor()
    q = "create database civil"
    q1 = "create table iris (sepal_length float(10),sepal_width	float(10),petal_length float(10),petal_width float(10),species varchar(25))"
# cursor.execute(q1)
    q3 = "select species from iris where sepal_length = 5.7  "
    cursor.execute(q3)
    for i in cursor.fetchall():
        print(i)
