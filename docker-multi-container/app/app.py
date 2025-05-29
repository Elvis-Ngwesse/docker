from flask import Flask
from flask_mysqldb import MySQL
from faker import Faker
import random

app = Flask(__name__)

# MySQL config from env vars
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'userdb'

mysql = MySQL(app)
faker = Faker()

genders = ['Male', 'Female', 'Other']

@app.route('/')
def create_users():
    cur = mysql.connection.cursor()

    for _ in range(400):
        name = faker.name()
        address = faker.address().replace("\n", ", ")
        gender = random.choice(genders)
        profession = faker.job()
        country = faker.country()

        cur.execute("""
            INSERT INTO users (name, address, gender, profession, country)
            VALUES (%s, %s, %s, %s, %s)
        """, (name, address, gender, profession, country))

    mysql.connection.commit()
    cur.close()
    return "400 users created!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
