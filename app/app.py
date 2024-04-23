from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    data = {
        'span': 'Bienvenido',
        'span1':'Platos',
        'span2': 'Reservas',
        'span3': 'Quiénes somos' 
    }
    return render_template('index.html',data=data)


if __name__ == '__main__':
    app.run(debug=True)