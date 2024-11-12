from flask import Flask, Response
import subprocess
import datetime
import pwd
import os

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Arjun Pramod"
    username = pwd.getpwuid(os.getuid()).pw_name
    server_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')
    top_output = subprocess.getoutput("top -bn 1")

    page_content = f"""
    <html>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time:</strong> {server_time}</p>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    return Response(page_content, mimetype='text/html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
