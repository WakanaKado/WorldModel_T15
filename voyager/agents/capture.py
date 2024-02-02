import base64
import requests
import os
import glob

# OpenAI API Key
api_key = "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"

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
folder_path = '../env/mineflayer/images/'
file_list = glob.glob(folder_path + '*.png')
if not file_list:
    raise ValueError("指定されたフォルダに画像ファイルが存在しません。")

# 最終変更時間に基づいて最も新しいファイルを見つける
latest_file = max(file_list, key=os.path.getmtime)
image_path = latest_file

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "You are a great assistant to infer information from images.\
                  This image is a Minecraft play screen. \
                  My ultimate goal is to create a gold pickaxe.\
                  Please guess what information you think would be useful to the player \
                  and give the information by reading that information from the image.\
                  If the image is unclear, please just answer N/A.\
                  Here's an example response.\
                  Reasoning:\
                  Information: "

        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image}"
          }
        }
      ]
    }
  ],
  "max_tokens": 400
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

data = response.json()

# 必要な情報を抽出
message_content = data['choices'][0]['message']['content']

# 出力
print(message_content)