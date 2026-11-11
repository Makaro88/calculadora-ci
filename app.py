from flask import Flask, request, jsonify
import redis
from calculadora import sumar, restar, multiplicar, dividir, potencia

app = Flask(__name__)
# Conecta al contenedor redis-db
r = redis.Redis(host='redis-db', port=6379, db=0, decode_responses=True)

@app.route('/')
def index():
    return "API Calculadora funcionando. Los resultados se guardan en Redis."

@app.route('/operar', methods=['POST'])
def operar():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    op = data.get('op')
    
    if op == 'suma': resultado = sumar(a, b)
    elif op == 'resta': resultado = restar(a, b)
    elif op == 'multiplicacion': resultado = multiplicar(a, b)
    elif op == 'division': resultado = dividir(a, b)
    elif op == 'potencia': resultado = potencia(a, b)
    else: return jsonify({"error": "Operación no válida"}), 400

    registro = f"{op}: {a} y {b} = {resultado}"
    r.lpush("historial", registro)
    
    return jsonify({"resultado": resultado, "historial": r.lrange("historial", 0, -1)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)