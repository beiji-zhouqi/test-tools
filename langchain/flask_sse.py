from flask import Flask, Response
import time
import json

app = Flask(__name__)

@app.route('/')
def index():
    return Response('''
<!DOCTYPE html>
<html>
<head>
    <title>Flask SSE Example</title>
</head>
<body>
    <div id="output"></div>
    <script>
        var outputEl = document.getElementById('output');
        var source = new EventSource('/sse');
        source.onmessage = function(event) {
            outputEl.innerText += JSON.parse(event.data).chunk;
        };
        // don't auto restart connection
        source.onerror = function(event) { source.close(); };
    </script>
</body>
</html>
''', mimetype='text/html')


@app.route('/sse')
def sse():
    def _stream():
        for i in range(10):
            data = {'chunk': f'{i}\n'}
            yield 'data: {}\n\n'.format(json.dumps(data))
            time.sleep(1)
    return Response(_stream(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(threaded=True, debug=True)