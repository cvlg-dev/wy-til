from sqlalchemy import create_engine, text

# database configuration
db = {
    'hostname'      : 'whosgooddb.japanwest.cloudapp.azure.com',
    'port'          : '1433',
    'username'      : 'lucas_seo',
    'password'      : 'Yaxiputeg*37',
    'database'      : 'sandbox_rnd'
}



db_url = "mssql+pymssql://{}:{}@{}:{}/{}".format(
    db['username'], db['password'], db['hostname'], db['port'], db['database']
)
print(db_url)

# 명시된 DB에 접속. 연결된 DB 객체를 생성
db = create_engine(db_url, echo=True)

params = {'name' : '송은우'}
rows = db.execute(text("SELECT * FROM users WHERE name = :name"), params).fetchall()
## "SELECT * FROM users WHERE name = :name"
## "SELECT * FROM users WHERE name = 송은우" 파라미터를 받

print("Count of data is: ", len(rows))

# 각 row를 읽어들임.
for row in rows:
    print("name : {}".format(row['name']))
    print("email : {}".format(row['email']))

