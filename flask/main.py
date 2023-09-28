from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
        <html>
          <head>
            <meta charset="utf-8">
            <title>01_文本插入</title>
            <!-- 开发环境版本，包含了有帮助的命令行警告 -->
            <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
          </head>
          <body>
            <div id="app">
              {{ message }}
            </div>

            <script type="text/javascript">
              var app = new Vue({
              el: '#app',
              data: {
                message: 'Hello Flask!'
              }
            })
            </script>
          </body>
        </html>
    """

@app.route("/<name>")
def diy(name):
    # return f"Hello, {escape(name)}!"
    return f"Hello, {name}!"

@app.route('/hello')
def hello():
    return 'Hello, World'


if __name__=="__main__":
    app.run(debug=True)