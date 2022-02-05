from gtts import gTTS
from io import BytesIO
import sounddevice as sd
import soundfile as sf
import librosa
from pydub import AudioSegment


myobj = gTTS(text='Тест', lang='ru', slow=False)

b = BytesIO()

myobj.write_to_fp(b)


#myobj.save('mp3_fp.mp3')

s = AudioSegment.empty()

#data, semplerate = sf.read()
# sd.play(data, semplerate)
# sd.wait()