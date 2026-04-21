import flask
from flask_limiter import Limiter
import routes
import tests
import config.database as db
import secrets

key = secrets.token_hex(16)

app_register = [
    routes.index,
    routes.profile,
    routes.Offucats,
    routes.projects,
]


flask_app = flask.Flask(__name__, static_folder='static', template_folder='templates')

limiter = Limiter(
    app=flask_app,
    default_limits=["10 per minute","100 per day", "20 per hour"],
    key_func=lambda: flask.request.headers.get('CF-Connecting-IP') or flask.request.remote_addr
)


for blueprint in app_register:
    flask_app.register_blueprint(blueprint)

flask_app.config["DEBUG"] = False
flask_app.config["SECRET_KEY"] = key

# CONSOLE 
print("[+] Starting Flask Application")
print("[!] Flask Application is running in DEBUG mode: " + str(flask_app.config.get("DEBUG", False)))
print("[!] Flask Application is running on: " + str(flask_app.config.get("SERVER_NAME", "127.0.0.1:5000")))
print("[!] Flask Keys : " + str(flask_app.config["SECRET_KEY"]))

## HEADERS FOR WAPPALYZER 

@flask_app.after_request
def add_header(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Powered-By'] = 'Flask' 
    response.headers['Server'] = 'Flask'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Referrer-Policy'] = 'no-referrer'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

# RATE LIMITING

@flask_app.errorhandler(429)
def ratelimit_handler(e):
    return flask.render_template('error/429.html'), 429

## ERROR HANDLERS

@flask_app.errorhandler(404)
def page_not_found(e):
    return flask.render_template('error/404.html'), 404

@flask_app.errorhandler(504)
def gateway_timeout(e):
    return flask.render_template('error/504.html'), 504

@flask_app.errorhandler(503)
def service_unavailable(e):
    return flask.render_template('error/503.html'), 503

@flask_app.errorhandler(418)
def im_a_teapot(e):
    return flask.render_template('418.html'), 418


if __name__ == "__main__":
    tests.DatabaseTest(host=db.Database().host, user=db.Database().user, password=db.Database().password, database=db.Database().db)
    flask_app.run(debug=flask_app.config.get("DEBUG", False), host='127.0.0.1', port=5000)
