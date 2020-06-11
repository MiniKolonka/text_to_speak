# Перевод текста в голос и *.mp3

# pip install gTTS
from gtts import gTTS as speaker

# Модуль для полушение битрейта видео
from io import BytesIO


class Text_to_speak():
    """Инструменты для спикинга"""

    # Инициализируем класс
    def __init__(self, text, lang):
        self.text = text
        self.lang = lang

    
    def to_mp3(self):
        """Преводим текст в *.mp3"""
        tts = speaker(f'{self.text}', lang=f'{self.lang}')
        tts.save('speak.mp3')
        print("Создался файл speak.mp3") 

    
    def to_play(self):
        """Проигрываем наш текст"""
        mp3_fp = BytesIO()
        tts = speaker(f'{self.text}', lang=f'{self.lang}')
        tts.write_to_fp(mp3_fp)


    def streams(self):
        """Получаем потоки"""
        tts = speaker(f'{self.text}', lang=f'{self.lang}')
        urls = tts.get_urls()
        return urls
    
    def stream(self):
        """Получаем поток"""
        tts = speaker(f'{self.text}', lang=f'{self.lang}')
        urls = tts.get_urls()
        url = urls[0]
        return url

    
    def mp3_to_text(self, _file):
        """Считываем файл и получаем текст"""
        tts = speaker(f'{self.text}', lang=f'{self.lang}')
        with open(f'{_file}', 'wb') as f:
            tts.write_to_fp(f)





