from io import BytesIO
from gtts import gTTS


class TextToSpeak():
    def __init__(self, text: str, lang: str) -> None:
        self.text = text
        self.lang = lang

    def to_mp3(self, filename: str = "speak") -> None:
        """convert text to .mp3"""
        tts = gTTS(self.text, lang=self.lang)
        tts.save(f"{filename}.mp3")

    def play(self) -> None:
        """plays the text"""
        mp3_fp = BytesIO()

        tts = gTTS(self.text, lang=self.lang)
        tts.write_to_fp(mp3_fp)

    def stream(self) -> str:
        """Receives stream"""
        tts = gTTS(self.text, lang=self.lang)
        urls = tts.get_urls()

        return urls[0]

    def mp3_to_text(self, filename: str) -> None:
        """Reads a file and receives text"""
        tts = gTTS(self.text, lang=self.lang)

        with open(filename, 'wb') as file:
            tts.write_to_fp(file)


def main() -> None:
    text = input("Введите такст: ")
    lang = input("Введите язык: ")
    speaker = TextToSpeak(text, lang)
    speaker.to_mp3()


if __name__ == "__main__":
    main()
