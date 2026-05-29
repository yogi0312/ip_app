from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return {"message": f"The IP address is: {ip_address}"}

@app.get("/greet")
def say_hello():
    return {"message": "Hi how are you"}
