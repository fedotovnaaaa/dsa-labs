from flask import Flask, request, jsonify
import random

app = Flask(__name__)

operations = ["sum", "sub", "mul", "div"]

# GET: param -> случайное число * param
@app.route('/number/', methods=['GET'])
def get_number():
    # получаем параметр из строки запроса
    param = request.args.get('param')

    # проверяем, что параметр присутствует
    if param is None:
        return jsonify({"error": "param обязателен"}), 400

    try:
        param = int(param) # преобразуем param в число
    except ValueError:
        return jsonify({"error": "param должен быть числом"}), 400

    rand_num = random.randint(1, 10)
    result = rand_num * param

    return jsonify({
        "number": result,
        "operation": "mul"
    })


# POST: jsonParam -> случайная операция 
@app.route('/number/', methods=['POST'])
def post_number():
    # проверяем, что запрос содержит JSON
    if not request.is_json:
        return jsonify({"error": "нужен JSON"}), 400

    # получаем jsonParam из JSON тела запроса
    data = request.get_json()
    json_param = data.get("jsonParam")

    # проверяем, что jsonParam присутствует
    if json_param is None:
        return jsonify({"error": "jsonParam обязателен"}), 400

    rand_num = random.randint(1, 10)
    operation = random.choice(operations)

    if operation == "sum":
        result = rand_num + json_param
    elif operation == "sub":
        result = rand_num - json_param
    elif operation == "mul":
        result = rand_num * json_param
    elif operation == "div":
        if json_param == 0:
            return jsonify({"error": "на ноль делить нельзя!"}), 400
        result = rand_num / json_param

    return jsonify({
        "number": result,
        "operation": operation
    })


# DELETE: случайное число и случайная операция
@app.route('/number/', methods=['DELETE'])
def delete_number():
    rand_num = random.randint(1, 10)
    operation = random.choice(operations)

    return jsonify({
        "number": rand_num,
        "operation": operation
    })


# 2 раздел
def run_client():
    import requests

    url = "http://127.0.0.1:5000/number/"

    # GET: param -> случайное число
    param = random.randint(1, 10)
    r1 = requests.get(url, params={"param": param}).json()

    # POST: jsonParam -> случайное число
    param2 = random.randint(1, 10)
    r2 = requests.post(url, json={"jsonParam": param2}).json()

    # DELETE: без параметров
    r3 = requests.delete(url).json()

    print("GET:", r1)
    print("POST:", r2)
    print("DELETE:", r3)

    # вычисление результата
    result = r1["number"]

    # функция для применения операции
    def apply(a, b, op):
        if op == "sum":
            return a + b
        elif op == "sub":
            return a - b
        elif op == "mul":
            return a * b
        elif op == "div":
            return a / b if b != 0 else 0

    result = apply(result, r2["number"], r1["operation"])
    result = apply(result, r3["number"], r2["operation"])

    result = int(result)

    print("\nИТОГ:")
    print(f"{r1['number']} {r1['operation']} {r2['number']} {r2['operation']} {r3['number']}")
    print("Результат:", result)

    return result


if __name__ == '__main__':
    app.run(debug=True)
