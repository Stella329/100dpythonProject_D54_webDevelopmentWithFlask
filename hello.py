# Flask: https://azcv.readthedocs.io/en/latest/quickstart.html

# import Flask
from flask import Flask
app = Flask(__name__)


@app.route("/")  # only trigger the hellow_word if user tries to access the / homepage url
def hello_world():
    return "<p>Hello, World!</p>"
@app.route("/bye")  # only trigger the hellow_word if user tries to access the / homepage url
def say_bye():
    return "<p>Bye!</p>"


# Point to the file as a server and run: add the environment variable to Flask
# 方法一：Use terminal
# # Mac
# $ export FLASK_APP=hello.py # iOS
# $ flask run
# # --Running on http://127.0.0.1:5000/
# # Win
# set FLASK_APP=hello.py
# $env:FLASK_APP = "hello.py"  #--解决：set : 无法将“C:\path\to\app>set”项识别为 cmdlet、函数、脚本文件或可运行程序的名称。请检查名称的拼写，如果包括路径，请确保路径正确，然后再试一次。
# flask run

#方法二:
if __name__ == "__main__":
    app.run()

# Press CTRL+C to quit
