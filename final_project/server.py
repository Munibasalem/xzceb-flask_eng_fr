from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('a4db08b7-5729-4ba9-8c08-f2df493465a1')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)
language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com')

## Translate
translation = language_translator.translate(
    text='Hello', model_id='en-es').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))
#List identifiable languages
languages = language_translator.list_identifiable_languages().get_result()
print(json.dumps(languages, indent=2))

Identify
language = language_translator.identify(
    'Language translator translates text from one language to another').get_result()
# # print(json.dumps(language, indent=2))

# # List models
 models = language_translator.list_models(
    source='en').get_result()
 print(json.dumps(models, indent=2))

# # Create model
 with open('glossary.tmx', 'rb') as glossary:
    response = language_translator.create_model(
         base_model_id='en-fr',
         name='custom-english-to-French',
        forced_glossary=glossary).get_result()
     print(json.dumps(response, indent=2))





# # Delete model
# response = language_translator.delete_model(model_id='<YOUR MODEL ID>').get_result()
# print(json.dumps(response, indent=2))

# # Get model details
# model = language_translator.get_model(model_id='<YOUR MODEL ID>').get_result()
# print(json.dumps(model, indent=2))
def english_to_french(text1):
"""
This function translates english to french
 """

frenchtranslation = language_translator.translate(
text=text1,
model_id='en-fr'
).get_result()

return frenchtranslation.get("translatios")[0].get("translation")


def french_to_english(text1):
"""
This function translates frenchto english 
 """

englishtranslation = language_translator.translate(
text=text1,
model_id='fr-en'
).get_result()

return frenchtranslation.get("translatios")[0].get("translation")
@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
