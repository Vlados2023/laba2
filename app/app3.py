from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# 2.1 Первый роут для GET-запросов
@app.route('/get_example', methods=['GET'])
def get_example():
    if request.method == 'GET':
        params = request.args.to_dict()
        return jsonify(params)
    return "Метод не поддерживается", 405

# 2.2 Второй роут для POST-запросов
@app.route('/post_example', methods=['POST'])
def post_example():
    if request.method == 'POST':
        params = request.form.to_dict()
        return jsonify(params)
    return "Метод не поддерживается", 405

# 2.3 Третий роут для HEAD-запросов
@app.route('/head_example', methods=['HEAD'])
def head_example():
    if request.method == 'HEAD':
        return '', 200
    return "Метод не поддерживается", 405

# 2.4 Четвертый роут для OPTIONS-запросов
@app.route('/options_example', methods=['OPTIONS'])
def options_example():
    if request.method == 'OPTIONS':
        return '', 200
    return "Метод не поддерживается", 405

# Роут для главной страницы
@app.route('/')
def home():
    return render_template('app.html')

if __name__ == '__main__':
    app.run(debug=True)
