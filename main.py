from flask import Flask, render_template, request
import threading

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

@app.route('/<path:path>')
def static_file(path):
	return app.send_static_file(path)

if __name__ == "__main__":
	threading.Thread(target=app.run).start()
