# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 19:27:44 2020

@author: Natrajan
"""


from googletrans import Translator

# from gensim.summarization.summarizer import summarize

# import re

import streamlit as st

from textblob import TextBlob

#Create translator object
translator = Translator()

#streamlit text input
text = st.text_input("Enter the text in any language to analyse sentiment")


#streamlit button
if st.button("Analyze"):

    trans = translator.translate(text)
    
    #dictionary of languages
    
    detect_dict = {'af': 'afrikaans', 'sq': 'albanian', 
                   'am': 'amharic', 'ar': 'arabic', 
                   'hy': 'armenian', 'az': 'azerbaijani', 
                   'eu': 'basque', 'be': 'belarusian', 
                   'bn': 'bengali', 'bs': 'bosnian', 
                   'bg': 'bulgarian', 'ca': 'catalan', 
                   'ceb': 'cebuano', 'ny': 'chichewa', 
                   'zh-cn': 'chinese (simplified)', 
                   'zh-tw': 'chinese (traditional)', 
                   'co': 'corsican', 'hr': 'croatian', 
                   'cs': 'czech', 'da': 'danish', 
                   'nl': 'dutch', 'en': 'english', 
                   'eo': 'esperanto', 'et': 'estonian', 
                   'tl': 'filipino', 'fi': 'finnish', 
                   'fr': 'french', 'fy': 'frisian', 
                   'gl': 'galician', 'ka': 'georgian', 
                   'de': 'german', 'el': 'greek', 
                   'gu': 'gujarati', 'ht': 'haitian creole', 
                   'ha': 'hausa', 'haw': 'hawaiian', 
                   'iw': 'hebrew', 'hi': 'hindi', 
                   'hmn': 'hmong', 'hu': 'hungarian', 
                   'is': 'icelandic', 'ig': 'igbo', 
                   'id': 'indonesian', 'ga': 'irish', 
                   'it': 'italian', 'ja': 'japanese',
                   'jw': 'javanese', 'kn': 'kannada',
                   'kk': 'kazakh', 'km': 'khmer', 
                   'ko': 'korean', 'ku': 'kurdish (kurmanji)', 
                   'ky': 'kyrgyz', 'lo': 'lao',
                   'la': 'latin', 'lv': 'latvian',
                   'lt': 'lithuanian', 'lb': 'luxembourgish',
                   'mk': 'macedonian', 'mg': 'malagasy',
                   'ms': 'malay', 'ml': 'malayalam', 
                   'mt': 'maltese', 'mi': 'maori',
                   'mr': 'marathi', 'mn': 'mongolian',
                   'my': 'myanmar (burmese)', 'ne': 'nepali', 
                   'no': 'norwegian', 'ps': 'pashto',
                   'fa': 'persian', 'pl': 'polish',
                   'pt': 'portuguese', 'pa': 'punjabi',
                   'ro': 'romanian', 'ru': 'russian',
                   'sm': 'samoan', 'gd': 'scots gaelic',
                   'sr': 'serbian', 'st': 'sesotho',
                   'sn': 'shona', 'sd': 'sindhi', 
                   'si': 'sinhala', 'sk': 'slovak',
                   'sl': 'slovenian', 'so': 'somali',
                   'es': 'spanish', 'su': 'sundanese',
                   'sw': 'swahili', 'sv': 'swedish',
                   'tg': 'tajik', 'ta': 'tamil', 
                   'te': 'telugu', 'th': 'thai', 
                   'tr': 'turkish', 'uk': 'ukrainian',
                   'ur': 'urdu', 'uz': 'uzbek',
                   'vi': 'vietnamese', 'cy': 'welsh',
                   'xh': 'xhosa', 'yi': 'yiddish',
                   'yo': 'yoruba', 'zu': 'zulu',
                   'fil': 'Filipino', 'he': 'Hebrew'}
    
    for key,value in detect_dict.items():
        if key == trans.src:
            st.write("Input Language :- ",value)
    
    text1 = TextBlob(trans.text)
    
    pol = text1.sentiment.polarity
    
    st.write("Polarity :- ",pol)
    
    if pol>0:
        result = translator.translate("Positive",dest=trans.src)
        st.success(f"Review :- Positive Review ( {result.text} )")
        # st.write("Review :- Positive Review")
    elif pol<0:
        result = translator.translate("Negative",dest=trans.src)
        st.success(f"Review :- Negative Review ( {result.text} )")
    else:
        result = translator.translate("Neutral",dest=trans.src)
        st.success(f"Review :- Neutral Review ( {result.text} )")
    
    

