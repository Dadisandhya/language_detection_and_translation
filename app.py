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
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0  # ensures consistent language detection

app = Flask(__name__)

# Mapping of language codes to language names for translation
LANGUAGES = {
    "af": "Afrikaans", "sq": "Albanian", "am": "Amharic", "ar": "Arabic",
    "hy": "Armenian", "az": "Azerbaijani", "eu": "Basque", "be": "Belarusian",
    "bn": "Bengali", "bs": "Bosnian", "bg": "Bulgarian", "ca": "Catalan",
    "ceb": "Cebuano", "ny": "Chichewa", "zh-cn": "Chinese (Simplified)",
    "zh-tw": "Chinese (Traditional)", "co": "Corsican", "hr": "Croatian",
    "cs": "Czech", "da": "Danish", "nl": "Dutch", "en": "English",
    "eo": "Esperanto", "et": "Estonian", "tl": "Filipino", "fi": "Finnish",
    "fr": "French", "fy": "Frisian", "gl": "Galician", "ka": "Georgian",
    "de": "German", "el": "Greek", "gu": "Gujarati", "ht": "Haitian Creole",
    "ha": "Hausa", "haw": "Hawaiian", "iw": "Hebrew", "hi": "Hindi",
    "hmn": "Hmong", "hu": "Hungarian", "is": "Icelandic", "ig": "Igbo",
    "id": "Indonesian", "ga": "Irish", "it": "Italian", "ja": "Japanese",
    "jw": "Javanese", "kn": "Kannada", "kk": "Kazakh", "km": "Khmer",
    "ko": "Korean", "ku": "Kurdish", "ky": "Kyrgyz", "lo": "Lao",
    "la": "Latin", "lv": "Latvian", "lt": "Lithuanian", "lb": "Luxembourgish",
    "mk": "Macedonian", "mg": "Malagasy", "ms": "Malay", "ml": "Malayalam",
    "mt": "Maltese", "mi": "Maori", "mr": "Marathi", "mn": "Mongolian",
    "my": "Myanmar (Burmese)", "ne": "Nepali", "no": "Norwegian", "ps": "Pashto",
    "fa": "Persian", "pl": "Polish", "pt": "Portuguese", "pa": "Punjabi",
    "ro": "Romanian", "ru": "Russian", "sm": "Samoan", "gd": "Scots Gaelic",
    "sr": "Serbian", "st": "Sesotho", "sn": "Shona", "sd": "Sindhi",
    "si": "Sinhala", "sk": "Slovak", "sl": "Slovenian", "so": "Somali",
    "es": "Spanish", "su": "Sundanese", "sw": "Swahili", "sv": "Swedish",
    "tg": "Tajik", "ta": "Tamil", "te": "Telugu", "th": "Thai",
    "tr": "Turkish", "uk": "Ukrainian", "ur": "Urdu", "uz": "Uzbek",
    "vi": "Vietnamese", "cy": "Welsh", "xh": "Xhosa", "yi": "Yiddish",
    "yo": "Yoruba", "zu": "Zulu"
}

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)

@app.route('/trans', methods=['POST'])
def trans():
    text = request.form['text']
    target_lang = request.form['target_lang']

    # Translate text
    translated_text = GoogleTranslator(source='auto', target=target_lang).translate(text)

    # Detect language
    detected_code = detect(text)
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

    detected_code = detect(text)
    detected_name = LANGUAGES.get(detected_code, detected_code)

    return render_template('index.html',
                           original_text=text,
                           detected_lang=detected_name,
                           languages=LANGUAGES)

if __name__ == "__main__":
    app.run(debug=True, port=5500)
