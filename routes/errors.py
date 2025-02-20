from app import app
from flask import jsonify

@app.errorhandler(404)
def not_found(e):
    return jsonify({
        'success': False,
        'message': 'The requested resource was not found',
        'error': 404
    }), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({
        'success': False,
        'message': 'Internal server error',
        'error': 500
    }), 500