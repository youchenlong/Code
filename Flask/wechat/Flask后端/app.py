from db_config import app
from flask_cors import CORS
from handler.test import test

# 解决跨域--针对浏览器同源策略
CORS(app, supports_credentias=True)

# 注册蓝图
app.register_blueprint(test, url_prefix='/test')

@app.route('/')
def Welcome():
    return 'Hello World'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)