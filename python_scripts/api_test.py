import openai
import os
openai.api_key = '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'

audio_file= open("./1.mp3", "rb")
# response_formatを指定することで文字起こしファイルを作成できる。（デフォルトはjson）
transcript = openai.Audio.transcribe("whisper-1", audio_file, response_format="vtt")

with open("output.vtt", "w", encoding="utf-8") as file:
    file.write(transcript)
