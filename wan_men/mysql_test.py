import pymysql

DATABASE={
    'host':'127.0.0.1',
    'database':'orm_db',
    'user':'root',
    'password':'12345678'
}
db = pymysql.connect(**DATABASE)
sql = "select * from article_article"
cursor = db.cursor()
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print(row)

try:
    sql_insert = 'insert `article_article`(`name`) values("今日新闻20200505")'
    cursor = db.cursor()
    cursor.execute(sql_insert)
    db.commit()
except Exception as e:
    print("exception:{0}".format(e))
    db.rollback()
