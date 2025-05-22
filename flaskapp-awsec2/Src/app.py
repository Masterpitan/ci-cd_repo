from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello_docker():
    return '<h1> This is Adepitan Adetunji</h1><br><p>Thank you for checking out my page. Stay tuned for my DevOps journey.</p> '

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
