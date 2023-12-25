from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# あなたのOpenAIのAPIキーを設定してください
openai.api_key = 'your-api-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clock')
def clock():
    return render_template('clock.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        
        # ファイルを保存する
        filename = 'upload/' + file.filename
        file.save(filename)

        # ここでWhisper APIを使ってファイルを文字に変換
        # ※ここはWhisper APIの仮想コードです。実際のAPIリクエストには適宜修正が必要です。
        try:
            text = openai.Audio.transcribe(filename)
            transcription = text['text']
        except Exception as e:
            return jsonify({'error': '音声の変換に失敗しました。', 'details': str(e)})

        # その後、ChatGPT APIを使って要約
        # ※ここはChatGPT APIの仮想コードです。実際のAPIリクエストには適宜修正が必要です。
        try:
            response = openai.ChatCompletion.create(
                messages=[{"role": "system", "content": "要約してください。"},
                          {"role": "user", "content": transcription}]
            )
            summary = response['choices'][0]['message']['content']
        except Exception as e:
            return jsonify({'error': '要約の生成に失敗しました。', 'details': str(e)})

        # 要約結果を返す
        return jsonify({'message': summary})
    return jsonify({'error': 'ファイルがありません'})

if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=5000, debug=True)