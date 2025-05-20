from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def register():
    ocr하기
    결과 던져주기

