from marsh import app
from flask import jsonify
from marsh.Models import Author, AuthorSchema


@app.route('/user')
def index():
    one = Author.query.all()
    schema = AuthorSchema(many=True)
    result = schema.dump(one)
    return jsonify(result.data)


@app.route('/user/<int:id>')
def user_id(id):
    one = Author.query.get(id)
    schema = AuthorSchema()
    result = schema.dump(one)
    return jsonify(result.data)