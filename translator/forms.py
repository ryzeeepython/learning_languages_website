from django import forms




languages = [
    ('af','Afrikaans'),
    ('sq','Albanian'),
    ('am','Amharic'),
    ('ar','Arabic'),
    ('hy','Armenian'),
    ('az','Azerbaijani'),
    ('eu','Basque'),
    ('be','Belarusian'),
    ('bn','Bengali'),
    ('bs','Bosnian'),
    ('bg','Bulgarian'),
    ('ca','Catalan'),
    ('ceb','Cebuano'),
    ('ny','Chichewa'),
    ('zh-cn','Chinese (simplified)'),
    ('zh-tw','Chinese (traditional)'),
    ('co','Corsican'),
    ('hr','Croatian'),
    ('cs','Czech'),
    ('da','Danish'),
    ('nl','Dutch'),
    ('en','English'),
    ('eo','Esperanto'),
    ('et','Estonian'),
    ('tl','Filipino'),
    ('fi','Finnish'),
    ('fr','French'),
    ('fy','Frisian'),
    ('gl','Galician'),
    ('ka','Georgian'),
    ('de','German'),
    ('el','Greek'),
    ('gu','Gujarati'),
    ('ht','Haitian creole'),
    ('ha','Hausa'),
    ('haw','Hawaiian'),
    ('iw','Hebrew'),
    ('he','Hebrew'),
    ('hi','Hindi'),
    ('hmn','Hmong'),
    ('hu','Hungarian'),
    ('is','Icelandic'),
    ('ig','Igbo'),
    ('id','Indonesian'),
    ('ga','Irish'),
    ('it','Italian'),
    ('ja','Japanese'),
    ('jw','Javanese'),
    ('kn','Kannada'),
    ('kk','Kazakh'),
    ('km','Khmer'),
    ('ko','Korean'),
    ('ku','Kurdish (kurmanji)'),
    ('ky','Kyrgyz'),
    ('lo','Lao'),
    ('la','Latin'),
    ('lv','Latvian'),
    ('lt','Lithuanian'),
    ('lb','Luxembourgish'),
    ('mk','Macedonian'),
    ('mg','Malagasy'),
    ('ms','Malay'),
    ('ml','Malayalam'),
    ('mt','Maltese'),
    ('mi','Maori'),
    ('mr','Marathi'),
    ('mn','Mongolian'),
    ('my','Myanmar (burmese)'),
    ('ne','Nepali'),
    ('no','Norwegian'),
    ('or','Odia'),
    ('ps','Pashto'),
    ('fa','Persian'),
    ('pl','Polish'),
    ('pt','Portuguese'),
    ('pa','Punjabi'),
    ('ro','Romanian'),
    ('ru','Russian'),
    ('sm','Samoan'),
    ('gd','Scots gaelic'),
    ('sr','Serbian'),
    ('st','Sesotho'),
    ('sn','Shona'),
    ('sd','Sindhi'),
    ('si','Sinhala'),
    ('sk','Slovak'),
    ('sl','Slovenian'),
    ('so','Somali'),
    ('es','Spanish'),
    ('su','Sundanese'),
    ('sw','Swahili'),
    ('sv','Swedish'),
    ('tg','Tajik'),
    ('ta','Tamil'),
    ('te','Telugu'),
    ('th','Thai'),
    ('tr','Turkish'),
    ('uk','Ukrainian'),
    ('ur','Urdu'),
    ('ug','Uyghur'),
    ('uz','Uzbek'),
    ('vi','Vietnamese'),
    ('cy','Welsh'),
    ('xh','Xhosa'),
    ('yi','Yiddish'),
    ('yo','Yoruba'),
    ('zu','Zulu')
]


class Form(forms.Form):
    text = forms.CharField(widget = forms.Textarea(attrs={'class':'form-control', 'id':'exampleFormControlTextarea1', 'rows': 10, 'placeholder': 'Text'}))    
    language = forms.ChoiceField(
        required=True,
        widget=forms.Select(attrs = {'class':'form-control form-control-lg'}),
        choices=languages,
    )