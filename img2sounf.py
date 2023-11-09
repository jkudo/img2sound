import base64
import numpy as np
from scipy.io.wavfile import write

# 画像ファイルをBase64にエンコードする関数
def image_to_base64(file_path):
    with open(file_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

# Base64文字列をオーディオデータに変換し、WAVファイルとして保存する関数
def base64_to_audio(base64_string, output_file):
    # Base64デコード
    audio_data = base64.b64decode(base64_string)
    # オーディオバッファのサイズを2の倍数に調整
    if len(audio_data) % 2 != 0:
        audio_data = audio_data[:-1]  # 最後の余分なバイトを取り除く
    # NumPy配列に変換
    np_audio = np.frombuffer(audio_data, dtype=np.int16)
    # WAVファイルとして保存
    write(output_file, 44100, np_audio)

# 画像ファイルのパスを指定
image_file_path = 'neko.jpg'  # 画像ファイルへのパスを指定

# Base64エンコード
base64_string = image_to_base64(image_file_path)

# 出力ファイルのパスを指定
audio_output_file = 'neko.wav'

# Base64文字列からオーディオデータを生成してWAVファイルとして保存
base64_to_audio(base64_string, audio_output_file)
