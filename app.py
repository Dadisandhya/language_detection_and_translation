# from flask import Flask, render_template, request
# from deep_translator import GoogleTranslator
# from langdetect import detect
# import os

# app = Flask(__name__)

# # Language map (you can add more if needed)
# LANGUAGES = {
#     'en': 'English',
#     'es': 'Spanish',
#     'fr': 'French',
#     'de': 'German',
#     'hi': 'Hindi',
#     'te': 'Telugu',
#     'ta': 'Tamil',
#     'ml': 'Malayalam',
#     'zh-cn': 'Chinese (Simplified)',
#     'ja': 'Japanese',
#     'ko': 'Korean'
# }

# @app.route('/')
# def index():
#     return render_template('index.html', languages=LANGUAGES)

# @app.route('/detect', methods=['POST'])
# def detect_language():
#     text = request.form['text']
#     if not text.strip():
#         return render_template('index.html', error="Please enter text to detect.", languages=LANGUAGES)
    
#     detected_code = detect(text)
#     detected_name = LANGUAGES.get(detected_code, detected_code).title()
    
#     return render_template('index.html',
#                            original_text=text,
#                            detected_lang=detected_name,
#                            languages=LANGUAGES)

# @app.route('/trans', methods=['POST'])
# def trans():
#     text = request.form['text']
#     target_lang = request.form['target_lang']
#     if not text.strip():
#         return render_template('index.html', error="Please enter text to translate.", languages=LANGUAGES)

#     try:
#         translated_text = GoogleTranslator(source='auto', target=target_lang).translate(text)
#         detected_code = detect(text)
#         detected_name = LANGUAGES.get(detected_code, detected_code).title()

#         return render_template('index.html',
#                                original_text=text,
#                                translation=translated_text,
#                                detected_lang=detected_name,
#                                selected_lang=target_lang,
#                                languages=LANGUAGES)
#     except Exception as e:
#         return render_template('index.html', error=f"Translation failed: {e}", languages=LANGUAGES)

# if __name__ == "__main__":
#     app.run(debug=True)

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

    # Translation
    try:
        translator = GoogleTranslator(source='auto', target=target_lang)
        translated_text = translator.translate(text)
        detected_code = translator.detect(text)
    except Exception as e:
        translated_text = f"Translation Error: {str(e)}"
        detected_code = "unknown"

    detected_name = LANGUAGES.get(detected_code, detected_code)

    return render_template('index.html',
                           original_text=text,
                           translation=translated_text,
                           detected_lang=detected_name,
                           selected_lang=target_lang,
                           languages=LANGUAGES)

@app.route('/detect', methods=['POST'])
def detect_language():
    text = request.form['text']

    try:
        translator = GoogleTranslator(source='auto', target='en')
        detected_code = translator.detect(text)
    except Exception as e:
        detected_code = "unknown"

    detected_name = LANGUAGES.get(detected_code, detected_code)

    return render_template('index.html',
                           original_text=text,
                           detected_lang=detected_name,
                           languages=LANGUAGES)

if __name__ == "__main__":
    app.run(debug=True, port=5500)

