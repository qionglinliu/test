# 划分数据集

import os
import shutil
from sklearn.model_selection import train_test_split

# 定义数据集的路径
dataset_path = 'dataset'
image_dir = os.path.join(dataset_path, 'image')
label_dir = os.path.join(dataset_path, 'labels')

# 定义输出的文件夹
train_image_dir = os.path.join(dataset_path, 'train', 'images')
val_image_dir = os.path.join(dataset_path, 'val', 'images')
test_image_dir = os.path.join(dataset_path, 'test', 'images')
train_label_dir = os.path.join(dataset_path, 'train', 'labels')
val_label_dir = os.path.join(dataset_path, 'val', 'labels')
test_label_dir = os.path.join(dataset_path, 'test', 'labels')

# 创建输出文件夹
for dir_path in [train_image_dir, val_image_dir, test_image_dir, train_label_dir, val_label_dir, test_label_dir]:
    os.makedirs(dir_path, exist_ok=True)

# 获取所有的图像和标签文件
image_files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
label_files = [f for f in os.listdir(label_dir) if os.path.isfile(os.path.join(label_dir, f))]

# 确保图像和标签文件数量相同
assert len(image_files) == len(label_files), "The number of images and labels must be the same."

# 将图像和标签文件名组合为元组列表
files = list(zip(image_files, label_files))

# 切分数据集
train_files, test_files = train_test_split(files, test_size=0.2, random_state=42)  # 80% training, 20% testing
train_files, val_files = train_test_split(train_files, test_size=0.25, random_state=42)  # 75% training, 12.5% validation

# 定义切分后的数据集比例
train_size = len(train_files)
val_size = len(val_files)
test_size = len(test_files)

print(f"Training set: {train_size}, Validation set: {val_size}, Test set: {test_size}")

# 复制文件到相应的文件夹
for image_name, label_name in train_files:
    shutil.copy(os.path.join(image_dir, image_name), train_image_dir)
    shutil.copy(os.path.join(label_dir, label_name), train_label_dir)

for image_name, label_name in val_files:
    shutil.copy(os.path.join(image_dir, image_name), val_image_dir)
    shutil.copy(os.path.join(label_dir, label_name), val_label_dir)

for image_name, label_name in test_files:
    shutil.copy(os.path.join(image_dir, image_name), test_image_dir)
    shutil.copy(os.path.join(label_dir, label_name), test_label_dir)

print("Dataset split completed.")
