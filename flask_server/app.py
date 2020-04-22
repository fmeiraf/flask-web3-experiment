from flask import Flask, render_template, url_for
from dynaconf import FlaskDynaconf, settings

app = Flask(__name__)
FlaskDynaconf(app)

@app.route('/')
def index():
    contract_adress = settings.CONTRACT_ADRESS
    return render_template('index.html', c_address = contract_adress)


if __name__ == "__main__":
    app.run()