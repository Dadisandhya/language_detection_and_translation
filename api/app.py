from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

# Define supported languages manually (since deep_translator doesn't provide LANGUAGES)
LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'hi': 'Hindi',
    'te': 'Telugu',
    'ta': 'Tamil',
    'zh': 'Chinese',
    'ja': 'Japanese',
    'ru': 'Russian'
}

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/detect', methods=['POST'])
def detect_language():
    text = request.form['text']

    if not text.strip():
        return render_template('index.html', error="Please enter text to detect language.", languages=LANGUAGES)

    try:
        # Use deep_translator detection (simple workaround)
        detected_lang = GoogleTranslator(source='auto', target='en').translate(text)
        return render_template('index.html', detected_lang='Auto-detected language', original_text=text, translation=detected_lang, languages=LANGUAGES)
    except Exception as e:
        return render_template('index.html', error=f"Detection Error: {e}", languages=LANGUAGES)

@app.route('/trans', methods=['POST'])
def translate_text():
    text = request.form['text']
    target_lang = request.form['target_lang']

    if not text.strip():
        return render_template('index.html', error="Please enter text to translate.", languages=LANGUAGES)

    try:
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        return render_template('index.html',
                               original_text=text,
                               translation=translated,
                               selected_lang=target_lang,
                               languages=LANGUAGES)
    except Exception as e:
        return render_template('index.html', error=f"Translation Error: {e}", languages=LANGUAGES)

# Important: Do NOT use app.run() on Vercel
if __name__ == "__main__":
    app.run(debug=True)


# # from flask import Flask, render_template, request
# from flask import Flask, render_template, request
# from deep_translator import GoogleTranslator # <--- ADD THIS IMPORT
# from langdetect import detect                 # <--- You need this too
# import os
# from googletrans import Translator, LANGUAGES

# app = Flask(__name__)
# # translator = Translator()
# translator = GoogleTranslator()

# @app.route('/')
# def index():
#     return render_template('index.html', languages=LANGUAGES)


# @app.route('/trans', methods=['POST'])
# def trans():
#     text = request.form['text']
#     target_lang = request.form['target_lang']


#     translated = translator.translate(text, dest=target_lang)


#     detected = translator.detect(text)
#     detected_code = detected.lang
#     detected_name = LANGUAGES.get(detected_code, detected_code).title()

#     return render_template('index.html',
#                            original_text=text,
#                            translation=translated.text,
#                            detected_lang=detected_name,
#                            selected_lang=target_lang,
#                            languages=LANGUAGES)

# @app.route('/detect', methods=['POST'])
# def detect_language():
#     text = request.form['text']

#     detected = translator.detect(text)
#     detected_code = detected.lang
#     detected_name = LANGUAGES.get(detected_code, detected_code).title()

#     return render_template('index.html',
#                            original_text=text,
#                            detected_lang=detected_name,
#                            languages=LANGUAGES)
# if __name__ == "__main__":
#     app.run(debug=True, port=5500)


# # from flask import Flask, render_template, request
# # from googletrans import Translator, LANGUAGES
# # import os

# # app = Flask(__name__)
# # translator = Translator()

# # # Optional: Dynamic BASE_DIR if you use any JSON files
# # BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# # @app.route('/')
# # def index():
# #     return render_template('index.html', languages=LANGUAGES)

# # @app.route('/trans', methods=['POST'])
# # def trans():
# #     text = request.form['text']
# #     target_lang = request.form['target_lang']

# #     translated = translator.translate(text, dest=target_lang)

# #     detected = translator.detect(text)
# #     detected_code = detected.lang
# #     detected_name = LANGUAGES.get(detected_code, detected_code).title()

# #     return render_template('index.html',
# #                            original_text=text,
# #                            translation=translated.text,
# #                            detected_lang=detected_name,
# #                            selected_lang=target_lang,
# #                            languages=LANGUAGES)

# # @app.route('/detect', methods=['POST'])
# # def detect_language():
# #     text = request.form['text']

# #     detected = translator.detect(text)
# #     detected_code = detected.lang
# #     detected_name = LANGUAGES.get(detected_code, detected_code).title()

# #     return render_template('index.html',
# #                            original_text=text,
# #                            detected_lang=detected_name,
# #                            languages=LANGUAGES)

# # if __name__ == "__main__":
# #     # Use Render provided port or fallback to 5500 locally
# #     port = int(os.environ.get("PORT", 5500))
# #     app.run(host="0.0.0.0", port=port)
