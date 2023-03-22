from flask import Flask, request, abort, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

import base64
import os 

app = Flask(__name__)
CORS(app)
load_dotenv()

def writeImg(file,img):
    with open(file, 'wb') as f:
        f.write(img)


@app.route('/api/imageSave',  methods=['POST'])
def saveImg():
    data = request.get_json()
    img = data['imgBase64']
    codigo = data['studentCode']
    #obtengo la imagenBase64 y el codigo del estudiante 
    # img = img.encode('utf-8')
    img = base64.b64decode(img)

    #genero la ruta donde se almacenaran las imagenes (cambiar esta ruta dependiendo donde se quiera guardar, se lee el .env)
    file_name = str(os.getenv('MY_PATH')+f'\\{codigo}.jpg')
    print(file_name)
    
    try: 
        #mando a llamar la funcion para escribir la imagen en el sistema
        writeImg(file_name, img)
        #retorno si todo esta bien
        return jsonify({ 'ok': True, 'msg': 'La foto se proceso exitosamente' })
    except: 
        #si algo sale mal, aborto la operacion
        return abort(400, jsonify({ 'ok': False, 'msg': 'Faltan datos por ser procesados' }))
    


@app.route('/')
def hello():
    return '<h1> Hola mundo </h1>'

if __name__ == '__main__':
    app.run()
    