from flask import Flask , render_template , request

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/submit',method=['POST'])
def submit():
    username = request.form.get('username')
    return render_template('home.html',username=username)

if __name__ == '__main__':
    application.run(host='0.0.0.0',port=5000)