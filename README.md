# Dockerized CTF Challenge - Deployment Instructions

## **Prerequisites**
Before you begin, ensure you have the following installed:
- **Docker**: [Download Here](https://www.docker.com/get-started)

Verify the installation:
```sh
docker --version
```

---

## **1. Pull the Docker Image**
Run the following command to download the challenge image from Docker Hub:

```sh
docker pull krvsn/ctf:latest
```


---
## **2. Run the Docker Container**
Start the challenge by running:
```sh
docker run -d -p 8000:8000 ctf
```
This will start the challenge and expose it on port `8000`.

---
## **3. Access the Challenge**
Once the container is running, open your web browser and navigate to:

🌐 **[http://localhost:8000](http://localhost:8000)**

You should now see the challenge landing page.

---
## **4. Download the Challenge File**
Click the **"Download Challenge"** button on the webpage to get the challenge file (`secret.zip`).
**Writeup**: [Click here](https://www.docker.com/get-started)
---
