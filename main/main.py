# Перевод текста в голос и *.mp3

# pip install gTTS
from gtts import gTTS as speaker

# Модуль для полушение битрейта видео
from io import BytesIO


class Text_to_speak():
    """Инструменты для спикинга"""

    # Инициализируем текст
    def __init__(self, text, lang):
        self.text = text
        self.lang = lang

    # Преводим текст в *.mp3
    def to_mp3(self):
        tts = speaker(f'{self.text}', lang=f'{self.lang}')
        tts.save('speak.mp3')

    # Проигрываем наш текст
    def to_play(self):
        mp3_fp = BytesIO()
        tts = speaker(f'{self.text}', lang=f'{self.lang}')
        tts.write_to_fp(mp3_fp)

    # Получаем поток
    def stream(self):
        tts = speaker(f'{self.text}', lang=f'{self.lang}')
        urls = tts.get_urls()
        url = urls[0]

    # Считываем файл и получаем текст
    def mp3_to_text(self, _file):
        tts = speaker(f'{self.text}', lang=f'{self.lang}')
        with open(f'{_file}', 'wb') as f:
            tts.write_to_fp(f)

def main():
    _text = str(input("Введите такст: "))
    _lang = str(input("Введите язык: "))
    _speaker = Text_to_speak(_text, _lang)
    _speaker.to_mp3()




if __name__ == "__main__":
    main()



