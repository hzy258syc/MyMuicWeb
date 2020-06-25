import pandas as pd
import pymysql
from sqlalchemy import create_engine




df = pd.read_excel(
    "D:\个人资料\编程相关\面试项目\《玩转Django 2.0》PDF+源代码\《玩转Django 2.0》PDF+源代码\源代码《玩转Django 2.0》\第11章\数据文件\index_dynamic.xls"
)
# print(df)


# 创建engine 用来执行SQL语句
# engine = create_engine("mysql+pymysql://username:password@127.0.0.1:3306/library_name", echo=False,pool_size=10, max_overflow=20)
engine = create_engine(
    "mysql+pymysql://root:4546742547@127.0.0.1:3306/my_music?charset=utf8",
    echo=False,
    max_overflow=10
)


#
df.to_sql('index_dynamic', con=engine, if_exists='append', index=False)



# ret = engine.execute("select * from index_label;")
# print(ret.fetchall())




