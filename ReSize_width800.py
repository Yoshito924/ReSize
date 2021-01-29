
import os
from PIL import Image
from pathlib import Path
import glob

for image_name in glob.glob("./images/*.*"):
    #画像のパスを取得
    image_path = Path(image_name)

    #画像の情報を取得
    image = Image.open(image_path)

    #リサイズする幅と高さを指定
    width = 800
    ratio = width / image.width
    height = int(image.height * ratio)

    #LANCZOSフィルターでリサイズ
    image_resized = image.resize((width,height),Image.LANCZOS)

    #画像を保存するファイルのパスを指定
    saved_path = os.path.join('resized',image.filename)

    #画像を保存
    image_resized.save(saved_path)
