import base64
from scipy.io.wavfile import read

# オーディオデータをBase64文字列に変換する関数
def audio_to_base64(wav_file_path):
    # WAVファイルを読み込む
    rate, audio_data = read(wav_file_path)
    # バイナリデータを取得
    audio_bytes = audio_data.tobytes()
    # Base64エンコード
    base64_encoded_data = base64.b64encode(audio_bytes)
    base64_string = base64_encoded_data.decode('utf-8')
    return base64_string

# Base64文字列から画像ファイルに変換する関数
def base64_to_image(base64_string, output_file_path):
    # Base64デコード
    image_data = base64.b64decode(base64_string)
    # 画像ファイルとして保存
    with open(output_file_path, "wb") as image_file:
        image_file.write(image_data)

# WAVファイルのパス
audio_file_path = 'neko.wav'  # オーディオファイルへのパスを指定

# Base64文字列を取得
base64_string = audio_to_base64(audio_file_path)

# 画像ファイルとして復元
image_output_file = 'restored_neko.jpg'
base64_to_image(base64_string, image_output_file)
