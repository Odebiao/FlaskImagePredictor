import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

# 1. 导入必要的库
# 已经包括 TensorFlow, NumPy, OpenCV 和 PIL

# 2. 基本参数
class_names = ['剩饭', '垃圾', '干电池']
IMG_HEIGHT = 224
IMG_WIDTH = 224
IMG_CHANNEL = 3

# 3. 加载模型
model = tf.keras.models.load_model("models/garbage_classification_model.h5")

# 4. 预测函数
def predict_img(imgpath):
    # 从文件路径加载图片
    img = Image.open(imgpath)
    img = img.convert("RGB")
    img = np.array(img)

    # 调整图片大小
    img = cv2.resize(img, (IMG_HEIGHT, IMG_WIDTH))

    # 增加一个新维度以匹配模型输入格式
    img = img[np.newaxis, :]

    # 将图片像素值转换为浮点数
    img = img.astype("float32")

    # 进行预测
    pred = model(img)

    # 打印预测结果
    print(np.argmax(pred), class_names[np.argmax(pred)])

# 主函数，测试几张图片
if __name__ == "__main__":
    predict_img("split_data/train/干电池/干电池_1.jpg")
    # predict_img("split_data/val/卫裤/卫裤12.jpg")
    # predict_img("split_data/val/裙装/裙装45.jpg")
