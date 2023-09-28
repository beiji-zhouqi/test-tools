from flask import Flask, Response
from flask_sse import sse

import time

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

@app.route("/")
def index():
    return """
    <html>
        <head>
            <script src="https://cdn.jsdelivr.net/npm/vue"></script>
        </head>
        <body>
            <div id="app">
                {{ message }}
            </div>
            <script type="text/javascript">
                var app = new Vue({
                    el: '#app',
                    data: {
                        message: 'Hello Vue!'
                    },
                    mounted() {
                        var eventSource = new EventSource('/stream/time');
                        eventSource.onmessage = function(event) {
                            app.message = event.data;
                        };
                    }
                })
            </script>
        </body>
    </html>
    """

@app.route("/time")
def time_stream():
    def generate():
        while True:
            yield "event: time\n"
            yield "data: {}\n\n".format(time.strftime('%H:%M:%S'))
            time.sleep(2)
    
    return Response(generate(), mimetype="text/event-stream")

if __name__=="__main__":
    app.run(debug=True)