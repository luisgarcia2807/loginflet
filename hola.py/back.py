from flask import Flask, jsonify

app = Flask(__name__)

# Ruta que devuelve una lista de pacientes
@app.route('/patients', methods=['GET'])
def get_patients():
    patients = [
        {"id": 1, "name": "Juan Perez", "age": 35},
        {"id": 2, "name": "Maria Garcia", "age": 29},
        {"id": 3, "name": "Carlos Lopez", "age": 42}
    ]
    return jsonify(patients)

if __name__ == '__main__':
    app.run(debug=True)

