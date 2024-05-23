# import tensorflow as tf
# # from keras.preprocessing.image import ImageDataGenerator
# # from keras.preprocessing.image import ImageDataGenerator
# from keras.preprocessing.image import ImageDataGenerator
#
#
# from keras.models import Sequential
# from keras.layers import GlobalAveragePooling2D, Dense
# from keras.optimizers import Adam
#
# # 设定基本路径
# base_dir = './split_data/'
#
# # 创建 ImageDataGenerator 实例
# train_datagen = ImageDataGenerator(
#     rescale=1./255,
#     rotation_range=40,
#     width_shift_range=0.2,
#     height_shift_range=0.2,
#     shear_range=0.2,
#     zoom_range=0.2,
#     horizontal_flip=True,
#     fill_mode='nearest'
# )
#
# validation_datagen = ImageDataGenerator(rescale=1./255)
#
# # 加载训练和验证数据
# train_generator = train_datagen.flow_from_directory(
#     base_dir + 'train/',
#     target_size=(224, 224),
#     batch_size=16,
#     class_mode='categorical',
#     shuffle=True
# )
#
# validation_generator = validation_datagen.flow_from_directory(
#     base_dir + 'val/',
#     target_size=(224, 224),
#     batch_size=16,
#     class_mode='categorical'
# )
#
# # 创建模型函数
# def create_model(input_shape=(224, 224, 3), num_classes=2):
#     base_model = tf.keras.applications.MobileNetV2(input_shape=input_shape, include_top=False, weights='imagenet')
#     base_model.trainable = False  # 冻结基模型
#     model = Sequential([
#         base_model,
#         GlobalAveragePooling2D(),
#         Dense(num_classes, activation='softmax')
#     ])
#     model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
#     return model
#
# # 创建模型
# model = create_model(num_classes=len(train_generator.class_indices))
#
# # 训练模型
# def train_model():
#     history = model.fit(
#         train_generator,
#         steps_per_epoch=len(train_generator),
#         validation_data=validation_generator,
#         validation_steps=len(validation_generator),
#         epochs=10
#     )
#     model.save('models/garbage_classification_model.h5')
#     return history
#
# if __name__ == '__main__':
#     train_model()
#
#
#
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import GlobalAveragePooling2D, Dense
from keras.optimizers import Adam

# 检查 GPU 是否可用
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    try:
        # 设置 TensorFlow 在每个 GPU 上动态增长内存，避免占满整个 GPU 内存
        for gpu in gpus:
            tf.config.experimental.set_memory_growth(gpu, True)
        print("Using GPU")
    except RuntimeError as e:
        print(e)
else:
    print("GPU is not available, using CPU instead.")

# 设定基本路径
base_dir = './split_data/'

# 创建 ImageDataGenerator 实例
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

validation_datagen = ImageDataGenerator(rescale=1./255)

# 加载训练和验证数据
train_generator = train_datagen.flow_from_directory(
    base_dir + 'train/',
    target_size=(224, 224),
    batch_size=16,
    class_mode='categorical',
    shuffle=True
)

validation_generator = validation_datagen.flow_from_directory(
    base_dir + 'val/',
    target_size=(224, 224),
    batch_size=16,
    class_mode='categorical'
)

# 创建模型函数
def create_model(input_shape=(224, 224, 3), num_classes=2):
    base_model = tf.keras.applications.MobileNetV2(input_shape=input_shape, include_top=False, weights='imagenet')
    base_model.trainable = False  # 冻结基模型
    model = Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# 创建模型
model = create_model(num_classes=len(train_generator.class_indices))

# 训练模型
def train_model():
    history = model.fit(
        train_generator,
        steps_per_epoch=len(train_generator),
        validation_data=validation_generator,
        validation_steps=len(validation_generator),
        epochs=10
    )
    model.save('models/garbage_classification_model.h5')
    return history

if __name__ == '__main__':
    train_model()
