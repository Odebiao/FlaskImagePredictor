# from flask import Flask, request, render_template, redirect, flash
# from werkzeug.utils import secure_filename
# import tensorflow as tf
# import numpy as np
# from PIL import Image
# import cv2
# import os
# import secrets
#
# # 生成一个安全的密钥
# secret_key = secrets.token_hex(16)
# # print(secret_key)
#
# # 初始化 Flask 应用
# app = Flask(__name__)
# app.secret_key = secret_key  # 确保替换为你自己的密钥
#
# # 全局变量定义
# class_names = ['剩饭', '垃圾', '干电池']
# IMG_HEIGHT = 224
# IMG_WIDTH = 224
# IMG_CHANNEL = 3
#
# # 加载 TensorFlow 模型
# model = tf.keras.models.load_model("models/garbage_classification_model.h5")
#
# def predict_img(image_path):
#     """用于预测图像类别的函数"""
#     img = Image.open(image_path)
#     img = img.convert("RGB")
#     img = np.array(img)
#     img = cv2.resize(img, (IMG_HEIGHT, IMG_WIDTH))
#     img = img[np.newaxis, :]
#     img = img.astype("float32")
#
#     pred = model(img)
#     print(np.argmax(pred),class_names[np.argmax(pred)])
#     return class_names[np.argmax(pred)]
#
# @app.route('/uploader', methods=['GET', 'POST'])
# def upload_file():
#     """处理文件上传并进行预测"""
#     if request.method == 'POST':
#         f = request.files['file']
#         if f:
#             filename = secure_filename(f.filename)
#             file_path = os.path.join('tempdir', filename)
#             f.save(file_path)
#             label = predict_img(file_path)
#             return label
#         else:
#             flash('文件上传失败，请重新尝试！')
#             return redirect(request.url)
#     return render_template('upload.html')
#
# @app.route('/')
# def upload():
#     """主页面路由"""
#     return render_template('upload.html')
#
# if __name__ == '__main__':
#     app.run(debug=True)
import os
from flask import Flask, request, render_template, redirect, flash
from werkzeug.utils import secure_filename
import secrets
import tensorflow as tf  # 确保已正确安装 TensorFlow

# 加载模型
model = tf.keras.models.load_model("models/garbage_classification_model.h5")

# 设置类别名称
class_names = ['剩饭', '垃圾', '干电池']  # 根据实际情况调整

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

def predict_img(image_path):
    """函数用于预测图像类别"""
    from PIL import Image
    import numpy as np
    import cv2
    img = Image.open(image_path)
    img = img.convert("RGB")
    img = np.array(img)
    img = cv2.resize(img, (224, 224))  # 根据模型要求调整尺寸
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)
    return class_names[np.argmax(pred)]

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if f:
            filename = secure_filename(f.filename)
            tempdir = 'uploads'  # 更改为适当的目录名称
            os.makedirs(tempdir, exist_ok=True)
            file_path = os.path.join(tempdir, filename)
            f.save(file_path)
            # 调用预测函数
            result = predict_img(file_path)
            # 返回预测结果
            return f'预测结果: {result}'
        else:
            flash('文件上传失败，请重新尝试！')
            return redirect(request.url)
    return render_template('upload.html')

@app.route('/')
def upload():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)

