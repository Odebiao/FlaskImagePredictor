import os
import shutil
import random


def data_set_split(src_data_folder, target_data_folder, train_scale=0.8, val_scale=0.2, test_scale=0.0):
    # 获取所有类别的名称
    class_names = os.listdir(src_data_folder)

    # 创建训练集、验证集、测试集的目录
    split_names = ['train', 'val', 'test']
    for split_name in split_names:
        split_path = os.path.join(target_data_folder, split_name)
        if not os.path.isdir(split_path):
            os.makedirs(split_path)
        for class_name in class_names:
            class_split_path = os.path.join(split_path, class_name)
            if not os.path.isdir(class_split_path):
                os.makedirs(class_split_path)

    # 分割数据集
    for class_name in class_names:
        # 获取当前类别的所有图片路径
        current_class_data_path = os.path.join(src_data_folder, class_name)
        all_data = os.listdir(current_class_data_path)
        random.shuffle(all_data)  # 打乱数据顺序

        # 计算训练集、验证集的数量
        total_count = len(all_data)
        train_count = int(total_count * train_scale)
        val_count = int(total_count * val_scale)

        # 分割数据
        for idx, file_name in enumerate(all_data):
            src_path = os.path.join(current_class_data_path, file_name)
            if idx < train_count:
                dst_path = os.path.join(target_data_folder, 'train', class_name, file_name)
            elif idx < train_count + val_count:
                dst_path = os.path.join(target_data_folder, 'val', class_name, file_name)
            else:
                dst_path = os.path.join(target_data_folder, 'test', class_name, file_name)
            shutil.copy2(src_path, dst_path)  # 复制文件到新的目录


# 使用示例
if __name__ == '__main__':
    src_folder = "data"
    target_folder = "split_data"
    data_set_split(src_folder, target_folder, train_scale=0.8, val_scale=0.2)
