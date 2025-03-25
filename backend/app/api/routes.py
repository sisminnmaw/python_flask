from flask import jsonify
from app.api import bp

@bp.route('/hello', methods=['GET'])
def get_hello():
    return jsonify({'message': 'Hello from Flask!'}) 