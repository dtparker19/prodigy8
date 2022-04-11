from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'THIS IS MY SECRET'
#app.config.from_object(Config)


from app import routes