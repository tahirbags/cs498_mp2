import flask
from flask import Flask, request
import socket
import subprocess

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def serve():
    # Stress the CPU to the specified usage
    if request.method == 'POST':
        # Create a subprocess to run the stress_cpu.py script
        # It will stress to 100% utilization for approximately 1 minute
        subprocess.Popen(["python3", "stress_cpu.py"])
        hostname = socket.gethostname()
        return f"push EC2 instance {socket.gethostbyname(hostname)} to maximum CPU utilization"

    # Return the IP address of the current EC2 instance
    if request.method == 'GET':
        hostname = socket.gethostname()
        return socket.gethostbyname(hostname)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
