from app import app
from flask import jsonify

@app.route('/api/v1/check-installation', methods=['GET'])
def index():
    return jsonify({
        'success': True,
        'message': 'Windows client is installed and running.'
    })