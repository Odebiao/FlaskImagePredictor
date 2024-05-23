# from flask import Flask,request,render_template
#
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     if request.method == "GET":
#         return render_template('index.html')
#
# def req():
#     if request.method == 'POST':
#         file = request.files['file']
#         print(file.filename)
#         print(type(file))
#
#         return '上传成功'
#     else:
#         return '上传失败'
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template, redirect, url_for, flash
import os
import secrets

# 生成一个安全的密钥
secret_key = secrets.token_hex(16)
# print(secret_key)

app = Flask(__name__)
app.secret_key = secret_key  # 设置一个秘密密钥，用于维护会话


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/req', methods=['GET','POST'])
def req():
    if request.method == 'POST':
        file = request.files['file']
        print(file.filename)
        print(type(file))

        return '上传成功'
    else:
        return '上传失败'
    # if 'file' not in request.files:
    #     flash('没有文件部分')  # 使用 flash 提示没有文件上传
    #     return redirect(request.url)

    # file = request.files['file']
    # if file.filename == '':
    #     flash('没有选择文件')  # 使用 flash 提示没有选择文件
    #     return redirect(request.url)
    #
    # if file and allowed_file(file.filename):
    #     try:
    #         # 如果需要，处理文件保存逻辑
    #         file.save(os.path.join('save', file.filename))
    #         return '上传成功'
    #     except Exception as e:
    #         flash('文件保存失败')  # 使用 flash 提示保存失败
    #         return redirect(request.url)
    # else:
    #     flash('文件类型不允许')  # 使用 flash 提示文件类型不允许
    #     return redirect(request.url)


# def allowed_file(filename):
#     return '.' in filename and \
#         filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}


if __name__ == '__main__':
    app.run(debug=True)
