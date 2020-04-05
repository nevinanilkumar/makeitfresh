from flask import Flask

app=Flask(__name__)
app.config['SECRET_KEY']='9b11ac4263069692c46bd2a3edefba42ede6837c'

from shopproject import routes