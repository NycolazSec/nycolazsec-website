from flask import Blueprint, request, render_template, send_file, jsonify
from io import BytesIO


Offucats = Blueprint('offucats', __name__)

@Offucats.route('/offucats', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file selected'}), 400

        if not request.files['file'].filename.endswith('.py'):
            return jsonify({'error': 'File must be a Python file'}), 400

        file = request.files['file']
    
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        try:
            file_content = file.read().decode('utf-8')
            obfuscated_code = "exec(''.join([chr(int(hex(ord(c) ^ 0xAA + 0x55), 16)) for c in '" + ''.join([f'\\x{ord(c) ^ 0xAA + 0x55:02x}' for c in file_content]) + "']))"
        except UnicodeDecodeError:
            return jsonify({'error': 'Le fichier doit être encodé en UTF-8'}), 400

        return jsonify({'content': obfuscated_code}), 200

    return render_template('offucats/offucats.html')
    
