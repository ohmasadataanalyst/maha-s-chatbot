from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__, static_folder="static", template_folder="templates")
user_name = None

def load_qna_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        qna_data = json.load(f)
    return qna_data

def generate_greeting(name):
    return "مرحبا " + name + "، كيف يمكنني مساعدتك؟"

def generate_response(user_message, qna_data):
    for qa in qna_data:
        if user_message == qa['question']:
            return qa['answer']
    return "عذراً، لا أعرف الإجابة على هذا السؤال."

@app.route('/get-response', methods=['POST'])
def get_response():
    global user_name
    user_message = request.json['message']
    qna_data = load_qna_data("qna_data.json")
    if not user_name:
        user_name = user_message
        response = generate_greeting(user_name)
    else:
        response = generate_response(user_message, qna_data)
    return jsonify({'message': response})

@app.route('/')
def home():
    return render_template('index.html')
