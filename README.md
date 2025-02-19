# Deployment Guide for FastAPI Application  

## **1. Install Dependencies**  
Before running the application, install the required dependencies:

```sh
pip install -r requirements.txt
```

## **2. Navigate to the Project Directory**  
Ensure you are in the correct directory where the application is located.  

```sh
cd /path/to/patentTestMig
```

Example:
```sh
cd /home/user/patentTestMig
```

## **3. Run the Application**  
Use `uvicorn` to start the FastAPI application:

```sh
python -m uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Example:
```sh
python -m uvicorn app.main:app --host 0.0.0.0 --port 8001
```



## **4. Firewall & Port Configuration (If Needed)**  
If running on a cloud server (AWS, Azure, etc.), ensure the firewall allows traffic on the specified port `$PORT` (`8001` in this case):

```sh
sudo ufw allow 8001
```

For AWS EC2, update the **Security Group** to allow inbound traffic on the required port.

---

## **5. Stopping the Application**  
If the application is running in the background, you can stop it using:

```sh
pkill -f "uvicorn"
```

Or if using `screen`:

```sh
screen -ls  # List running screens
screen -r fastapi_app  # Reattach to the session
Ctrl + C  # Stop the application
exit  # Exit the screen session
```

---

## **6. Useful Commands**
| Task                     | Command |
|--------------------------|---------|
| Install dependencies     | `pip install -r requirements.txt` |
| Run the application      | `python -m uvicorn app.main:app --host 0.0.0.0 --port 8001` |
| Stop the application     | `pkill -f "uvicorn"` |
| Start server with reload | `python -m uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload` |
