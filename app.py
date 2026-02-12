import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- ВЕСЬ ВАШ КОД (IVR-обработчики) остается здесь ---
@app.route('/webhook/ivr', methods=['POST'])
def ivr_webhook():
    # ваш код обработки звонков
    pass

# ⚠️⚠️⚠️ КРИТИЧЕСКИ ВАЖНО ⚠️⚠️⚠️
if __name__ == '__main__':
    # Render задает порт через переменную окружения PORT
    port = int(os.environ.get('PORT', 5000))
    # Обязательно host='0.0.0.0' — иначе Render не сможет принимать запросы!
    app.run(host='0.0.0.0', port=port, debug=False)