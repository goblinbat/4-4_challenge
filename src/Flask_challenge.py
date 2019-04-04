from flask import Flask, jsonify, request, Response, json

Dictionary = [{'dog': "lab",
'a_id': 1,
'name': "Billybob"}]

app = Flask(__name__)

@app.route('/', methods=["GET"])
def get_all():
    response = Dictionary 
    return jsonify(response)

@app.route('/<a_id>', methods=["GET"])
def get_one_by_is(a_id):
    for d in Dictionary:
        if d['a_id'] == int(a_id):
            return Response(
                mimetype='application/json',
                response=json.dumps(d),
                status=200
            )
        
@app.route('/add', methods=["POST"])
def add_dict():
    req_data = request.get_json()
    n_id = req_data.get('a_id')
    dog = req_data.get('dog')
    name = req_data.get('name')
    Dictionary.append({
        'dog': dog,
        'a_id': n_id,
        'name': name,
    })
    return Response(
        mimetype="application/json",
        status = 201
    )

@app.route('/update/<int:did>', methods=['PUT', 'DELETE'])
def update_dict(did):
    if request.method == 'PUT':
        req_data = request.get_json()
        n_id = req_data.get('a_id')
        dog = req_data.get('dog')
        name = req_data.get('name')
        for i in Dictionary:
            if i['a_id'] == did:
                i['a_id'] = n_id
                i['dog'] = dog
                i['name'] = name
                return jsonify(i)
    elif request.method == 'DELETE':
        for i in Dictionary:
            if i['a_id'] == int(did):
                ind = Dictionary.index(i)
                del Dictionary[ind]
                return Response(
                    mimetype='application/json',
                    status= 200
                )

# @app.route('/delete/<did>', methods=['DELETE']) 
# def del_dict(did):
#     for i in Dictionary:
#         if i['a_id'] == int(did):
#             ind = Dictionary.index(i)
#             del Dictionary[ind]
#             return Response(
#                 mimetype='application/json',
#                 status= 200
#             )


if __name__ == '__main__':
    app.run()