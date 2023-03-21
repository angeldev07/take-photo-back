from flask import Flask, request, abort, jsonify
import base64

app = Flask(__name__)

def writeImg(file,img):
    with open(file, 'wb') as f:
        f.write(img)


@app.route('/api/imageSave',  methods=['POST'])
def saveImg():
    data = request.get_json()
    img = data['img']
    codigo = data['codigo']
    #obtengo la imagenBase64 y el codigo del estudiante 
    # img = img.encode('utf-8')
    img = base64.b64decode(img)

    #genero la ruta donde se almacenaran las imagenes
    file_name = f'C:\\Users\\AngelG\\Pictures\\ejemplo\\{codigo}.jpg'

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