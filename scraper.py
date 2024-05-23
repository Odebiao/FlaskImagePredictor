# import requests
# import re
# import os
#
#
# def download_images():
#     # 用户输入下载的图片类别和数量
#     x = input("请输入需要下载的图片类别数量（1个类别下载60张图片，2个类别下载120张图片）: ")
#     for _ in range(int(x)):
#         category = input("请输入要下载的图片类别：")
#         num_images = 60 if int(x) == 1 else 120  # 根据输入决定下载的图片数量
#         directory = os.path.join(os.getcwd(), 'data', category)
#
#         # 确保存储目录存在
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#
#         # 构造URL并设置请求头
#         url = f'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={category}&ct=201326592&v=flip'
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#         response = requests.get(url, headers=headers)
#         html = response.content.decode()
#
#         # 提取图片链接
#         image_urls = re.findall('"objURL":"(.*?)",', html)
#
#         # 下载图片
#         count = 0
#         for url in image_urls:
#             if count < num_images:
#                 try:
#                     img_response = requests.get(url, timeout=10)
#                     if img_response.status_code == 200:
#                         with open(os.path.join(directory, f'{category}_{count + 1}.jpg'), 'wb') as f:
#                             f.write(img_response.content)
#                         print(f"成功下载第{count + 1}张图片！")
#                         count += 1
#                 except Exception as e:
#                     print(f"下载失败：{str(e)}")
#             else:
#                 break
#
#
# if __name__ == "__main__":
#     download_images()
import requests
import re
import os

def download_images():
    # 用户输入下载的图片类别和数量
    x = input("请输入需要下载的图片类别数量（输入1下载150张图片，输入2下载300张图片）: ")
    num_images = 150 if int(x) == 1 else 300  # 根据输入决定下载的图片数量

    for _ in range(int(x)):
        category = input("请输入要下载的图片类别：")
        directory = os.path.join(os.getcwd(), 'data', category)

        # 确保存储目录存在
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 初始化
        count = 0
        page_number = 0
        while count < num_images:
            # 构造URL并设置请求头，模拟翻页
            url = f'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={category}&ct=201326592&v=flip&pn={page_number}'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            response = requests.get(url, headers=headers)
            html = response.content.decode()

            # 提取图片链接
            image_urls = re.findall('"objURL":"(.*?)",', html)
            if not image_urls:
                print("没有更多图片或达到请求限制")
                break

            # 下载图片
            for url in image_urls:
                if count < num_images:
                    try:
                        img_response = requests.get(url, timeout=10)
                        if img_response.status_code == 200:
                            with open(os.path.join(directory, f'{category}_{count + 1}.jpg'), 'wb') as f:
                                f.write(img_response.content)
                            print(f"成功下载第{count + 1}张图片！")
                            count += 1
                    except Exception as e:
                        print(f"下载失败：{str(e)}")
                else:
                    break
            page_number += 60  # 假设每页约有60张图

if __name__ == "__main__":
    download_images()
