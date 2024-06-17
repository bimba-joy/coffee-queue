# Coffee Queue

---

## Table of Contents

- Project Overview
- Features
- Technologies Used
- Prerequisites
- Installation
- Configuration
- Deployment
  - Local Deployment
  - Production Deployment
- Usage
- Testing
- Contributing
- License
- Contact

---

## Project Overview

Coffee Queue is a project that aims to manage and balance requests efficiently with built-in DDoS protection. The project is built using FastAPI and is containerized using Docker for easy deployment. It includes multiple APIs that handle different tasks and is configured with an Nginx web server as a reverse proxy.

---

## Features

- DDoS Protection: Protect your application from DDoS attacks.
- Multiple APIs: Separate endpoints for different functionalities (outer_api, inner_api, queue_api).
- Dockerized: Easily deployable using Docker and Docker Compose.
- Nginx Reverse Proxy: Efficient request handling and load balancing using Nginx.

---

## Technologies Used

- Programming Language: Python 3.9
- Framework: FastAPI
- Web Server: Nginx
- Containerization: Docker, Docker Compose
- HTTP Client: AIOHTTP

---

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have installed Docker and Docker Compose.
- You have a machine running Windows, macOS, or Linux.
- You have read the FastAPI documentation for any API-specific information you might need.

---

## Installation

1. Clone the repository:
   
```bash
git clone https://github.com/bimba-joy/coffee-queue.git
   ```
2. Navigate to the project directory:
   
```bash
cd coffee-queue
   ```
---

## Configuration

1. Dockerfile:
   
```dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
   ```
2. Docker Compose Configuration (docker-compose.yml):
   
```yaml
version: '3.8'

services:
 app:
   build: .
   ports:
     - "8000:8000"
     - "8001:8001"
     - "9999:9999"
   networks:
     - app-net

 nginx:
   image: nginx:latest
   ports:
     - "80:80"
     - "81:81"
   volumes:
     - ./nginx/nginx.conf:/etc/nginx/nginx.conf
   depends_on:
     - app
   networks:
     - app-net

networks:
 app-net:
   ```
---

## Deployment

### Local Deployment

1. Build and run the Docker containers:
   
```bash
docker-compose up --build
   ```
2. The application will be accessible at http://localhost:80, http://localhost:81, and http://localhost:99.

### Production Deployment

The application is deployed at http://51.250.93.255. To deploy the application to another server, follow these steps:
1. Ensure Docker and Docker Compose are installed on your server.
2. Transfer the repository files to your server.
3. Build and run the Docker containers:
   
```bash
docker-compose up --build -d
```   
---

## Usage

To use Coffee Queue, follow these steps:

1. Access the outer API at http://51.250.93.255:80.
2. Access the inner API at http://51.250.93.255:81.

For more detailed instructions on how to use the APIs, refer to the FastAPI documentation.

## API Endpoints

The Coffee Queue service provides several API endpoints to manage and process orders. Below is a summary of the available endpoints and their usage.

### Order Management (External API)
1. **Create Order**
   - **Method:** POST
   - **URL:** http://51.250.93.255:80/order/
   - **Description:** Creates a new order and returns an order_id.
   - **Response:**
     
```json
 {
   "order_id": "<generated_order_id>"
 }
 ```    

2. **Check Order Status**
   - **Method:** GET
   - **URL:** http://51.250.93.255:80/order/{order_id}
   - **Description:** Checks the status of an order using the order_id.
   - **Response:**
     
```json
 {
   "order_id": "<order_id>",
   "status": "<order_status>"
 }
 ```

### Worker API (Internal API)
1. **Start Order**
   - **Method:** GET
   - **URL:** http://51.250.93.255:81/start/
   - **Description:** For workers to start working on an order. This endpoint can be used to fetch the next pending order.

2. **Finish Order**
   - **Method:** POST
   - **URL:** http://51.250.93.255:81/finish/
   - **Description:** For workers to mark an order as finished.
   - **Request Body:**
     
```json
 {
   "order_id": "<your_order_id>"
 }
```
### Usage Example

Here is an example workflow using the provided API endpoints:

1. **Create an Order:**
   
```bash
curl -X POST http://51.250.93.255:80/order/ -H "Content-Type: application/json"
  ``` 

2. **Check Order Status:**
   
```bash
curl -X GET http://51.250.93.255:80/order/{order_id} -H "Content-Type: application/json"
   ```

3. **Worker Starts an Order:**
   
```bash
curl -X GET http://51.250.93.255:81/start/ -H "Content-Type: application/json"
   ```

4. **Worker Finishes an Order:**
   
```bash
curl -X POST http://51.250.93.255:81/finish/ -H "Content-Type: application/json" -d '{"order_id": "<your_order_id>"}'
   ```

These endpoints allow for efficient order management and processing within the Coffee Queue service.


---

## Load Testing

To ensure that Coffee Queue can handle the expected load, we use Locust for performing load tests. The load test scripts are located in the tests directory.

### Prerequisites

Ensure you have Locust installed. You can install it using pip:

```bash
pip install locust
```

### Load Test Scripts

The load test scripts are located in the tests directory:
- inner_api_test.py: Load test for the inner API.
- outer_api_test.py: Load test for the outer API.
- report_1718575177.6180627.html: An example report generated from a previous load test run.

### Running Load Tests

To run the load tests using Locust, follow these steps:

1. Navigate to the tests directory:
   
```bash
cd tests
   ```
   
2. Run Locust with the desired test script. For example, to run the test for the outer API:
```bash
locust -f outer_api_test.py
```   

   
3. Open your browser and navigate to http://localhost:8089 to access the Locust web interface.

   Here, you can configure the number of users to simulate and the hatch rate (users spawned per second).


---

## Contributing

Contributions are always welcome! Please follow the contributing guidelines.

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -m 'Add some feature').
5. Push to the branch (git push origin feature-branch).
6. Open a Pull Request.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## Contact

Maintainer: Apashynskyi Dmytro
Email: dev@papashanskiy.ru

For issues, please open an issue on the issue tracker.

---

Thank you for using Coffee Queue! If you encounter any issues, feel free to contact us through the Contact section. Happy coding!
