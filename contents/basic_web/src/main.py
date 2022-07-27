from flask import Flask, render_template, request, url_for, redirect, jsonify

app = Flask(__name__)

@app.before_request
def before_request():
    print("Antes de la petición...")


@app.after_request
def after_request(response):
    print("Después de la petición")
    return response


@app.route('/')
def index():
    topics = [
        {"title": 'Problems', "url":"https://github.com/mmagdiel/devs_in_training_2022/tree/master/problems"}, 
        {"title": 'ORM', "url":"https://github.com/mmagdiel/devs_in_training_2022/tree/master/contents/orm"},
        {"title": 'SQL', "url":"https://github.com/mmagdiel/devs_in_training_2022/tree/master/contents/sql"}, 
        {"title": 'Basic WEB',"url": "https://github.com/mmagdiel/devs_in_training_2022/tree/master/contents/basic_web"}
    ]
    data = {
        'title': 'Temario, devs in training',
        'hero': '¡Saludos!',
        'sub_hero': "Aqui encotraras el temario del curso",
        'topics': topics,
        'number': len(topics)
    }
    return render_template('index.html', data=data)


@app.route('/contacto/<nombre>/<int:edad>')
def contacto(nombre, edad):
    data = {
        'titulo': 'Contacto',
        'nombre': nombre,
        'edad': edad
    }
    return render_template('contacto.html', data=data)

def query_string():
    print(request)
    print(request.args)
    print(request.args.get('param1'))
    print(request.args.get('param2'))
    return "Ok"

def pagina_no_encontrada(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.add_url_rule('/query_string', view_func=query_string)
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True, port=5000)
