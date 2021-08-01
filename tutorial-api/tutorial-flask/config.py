db = {
  "hostname"      : "whosgooddb.japanwest.cloudapp.azure.com",
  "port"          : "1433",
  "username"      : "lucas_seo",
  "password"      : "Yaxiputeg*37",
  "database"      : "sandbox_rnd",

}

DB_URL = "mssql+pymssql://{}:{}@{}:{}/{}".format(
    db['username'],
    db['password'],
    db['hostname'],
    db['port'],
    db['database']
)