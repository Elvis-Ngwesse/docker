


docker build -t nginx-env-demo ./docker-variables
docker run -d -p 8080:80 -e CUSTOM_HEADER="HelloFromDocker Elvis" --name nginx-env-demo-container nginx-env-demo
open http://localhost:8080

curl -I http://localhost:8080

HTTP/1.1 200 OK
Server: nginx/1.27.5
Date: Thu, 29 May 2025 07:38:50 GMT
Content-Type: text/html
Content-Length: 142
Last-Modified: Thu, 29 May 2025 07:30:37 GMT
Connection: keep-alive
ETag: "68380d1d-8e"
X-Custom-Header: HelloFromDocker Elvis
Accept-Ranges: bytes