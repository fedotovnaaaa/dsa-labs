from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/number/', methods=['GET'])
def get_number():
    # Получаем param из строки запроса
    param = request.args.get('param', type=int)
    
    # Если параметр не передан или не число — ошибка
    if param is None:
        return jsonify({"error": "Параметр param обязателен"}), 400
    
    rand_num = random.randint(1, 100)
    result = rand_num * param
    
    # Возвращаем в формате JSON
    return jsonify({
        "number": result
    })


if __name__ == '__main__':
    app.run(debug=True)
