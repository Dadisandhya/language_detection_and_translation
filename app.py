# from flask import Flask, render_template, request
# from deep_translator import GoogleTranslator
# from langdetect import detect
# from languages import LANGUAGES

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html', languages=LANGUAGES)

# @app.route('/trans', methods=['POST'])
# def trans():
#     text = request.form['text']
#     target_lang = request.form['target_lang']

#     # Detect language using langdetect
#     detected_code = detect(text)
#     detected_name = LANGUAGES.get(detected_code, detected_code).title()

#     # Translate using GoogleTranslator
#     try:
#         translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
#     except Exception as e:
#         translated = f"Error: {e}"

#     return render_template('index.html',
#                            original_text=text,
#                            translation=translated,
#                            detected_lang=detected_name,
#                            selected_lang=target_lang,
#                            languages=LANGUAGES)

# @app.route('/detect', methods=['POST'])
# def detect_language():
#     text = request.form['text']
#     detected_code = detect(text)
#     detected_name = LANGUAGES.get(detected_code, detected_code).title()

#     return render_template('index.html',
#                            original_text=text,
#                            detected_lang=detected_name,
#                            languages=LANGUAGES)

# if __name__ == "__main__":
#     app.run(debug=True, port=5500)


from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
from languages import LANGUAGES

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/trans', methods=['POST'])
def trans():
    text = request.form['text']
    target_lang = request.form['target_lang']

    # Detect language using GoogleTranslator instead of langdetect
    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        detected_code = GoogleTranslator(source='auto', target='en').detect(text)
    except Exception as e:
        translated = f"Error: {e}"
        detected_code = 'en'

    detected_name = LANGUAGES.get(detected_code.lower(), detected_code).title()

    return render_template('index.html',
                           original_text=text,
                           translation=translated,
                           detected_lang=detected_name,
                           selected_lang=target_lang,
                           languages=LANGUAGES)

@app.route('/detect', methods=['POST'])
def detect_language():
    text = request.form['text']
    try:
        detected_code = GoogleTranslator(source='auto', target='en').detect(text)
    except Exception as e:
        detected_code = 'en'

    detected_name = LANGUAGES.get(detected_code.lower(), detected_code).title()

    return render_template('index.html',
                           original_text=text,
                           detected_lang=detected_name,
                           languages=LANGUAGES)

if __name__ == "__main__":
    app.run(debug=True, port=5500)
