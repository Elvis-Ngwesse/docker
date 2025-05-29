🐳 Docker Multi-Container Setup Instructions
===========================================

🔧 1. Start the Containers
--------------------------
Run the following command to build and start all services:

    docker-compose -f docker-multi-container/docker-compose.yaml up --build


🌐 2. Access the Web Service
----------------------------
Open in your browser:

    http://localhost:5001

Or test using curl:

    curl http://localhost:5001


📋 3. Check Running Containers
------------------------------
List all running containers:

    docker ps


🛠️ 4. Connect to MySQL Container
--------------------------------
Enter the MySQL container with:

    docker exec -it mysql_db mysql -uroot -p

🔑 When prompted, enter the MySQL root password  
(Use `password` if you’re using the `.env` file from earlier)


💾 5. Run SQL Commands Inside MySQL
-----------------------------------
Once you're inside the MySQL prompt (`mysql>`), run:

    SHOW DATABASES;
    USE userdb;
    SELECT * FROM users LIMIT 10;

✅ You should now see a sample list of users from the database!
