import psycopg2

# 创建连接对象
conn = psycopg2.connect(database="postgres", user="postgres", password="123456", host="localhost", port="5432")
# 获取游标
cur = conn.cursor()
# 执行SQL
cur.execute("select * from user_info")
# 获取结果 返回元组
res = cur.fetchall()
print(res)
# 提交事务
conn.commit()
# 关闭连接
cur.close()
conn.close()