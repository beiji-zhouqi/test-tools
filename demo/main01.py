from flask import Flask, Response

app = Flask(__name__)

import time

@app.route('/')
def stream_timestamp():
    def generate_timestamp():
        while True:
            yield str(int(time.time())) + '\n'
            time.sleep(1)
    
    return Response(generate_timestamp(), mimetype='text/plain')


if __name__ == '__main__':
    app.run()
