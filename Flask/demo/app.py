from db_config import app
from flask_cors import CORS
from handler.test import test
from handler.login import login

# 解决跨域
CORS(app, supports_credentias=True)

app.register_blueprint(test, url_prefix='/test')
app.register_blueprint(login, url_prefix='/login')

@app.route('/')
def Welcome():
    return "Hello World" 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)