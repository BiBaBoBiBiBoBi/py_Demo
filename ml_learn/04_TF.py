import tensorflow as tf

def tf_test_01():
    (x, y), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    # 1. 统一归一化 + 加通道维
    x = (x / 255.0)[..., tf.newaxis]
    x_test = (x_test / 255.0)[..., tf.newaxis]
    # 2. 稍大一点的网络 + 更好的初始化
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, 3, activation='relu', padding='same',
                               kernel_initializer='he_normal',
                               input_shape=(28, 28, 1)),
        tf.keras.layers.MaxPool2D(2),
        tf.keras.layers.Conv2D(64, 3, activation='relu', padding='same',
                               kernel_initializer='he_normal'),
        tf.keras.layers.MaxPool2D(2),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu',
                              kernel_initializer='he_normal'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(x, y, epochs=3, validation_split=0.1, verbose=2)
    print('Test acc:', model.evaluate(x_test, y_test, verbose=0)[1])

if __name__ == '__main__':
    tf_test_01()


