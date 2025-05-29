

docker-compose -f docker-multi-container/docker-compose.yaml up --build

http://localhost:5001

curl http://localhost:5001


docker ps
docker exec -it mysql_db mysql -uroot -p
Enter password (password if using .env you showed earlier).
You will get MySQL prompt:
mysql>
SHOW DATABASES;
USE userdb;
SELECT * FROM users LIMIT 10;

