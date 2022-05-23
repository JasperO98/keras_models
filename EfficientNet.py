import keras
from keras.layers import *


# Paper: https://link.springer.com/content/pdf/10.1007%2F978-3-319-24574-4_28.pdf


def build_model(size=512, pad='same', n_channels=1, n_classes=2, bn=True):
    """
    :param size: Size of input image
    :param pad: Padding of the convolution operation (same=padding, valid=no padding)
    :param n_channels: Number of channels of the input image
    :param n_classes: Number of classes to predict
    :param bn: Whether to perform batch normalization after each convolution

    Builds the Unet model

    :return: model
    """
    # Input might not fit depending on size due to cropping
    inputs = Input(shape=(size, size, n_channels), name='input')

    # Output
    outputs = Conv2D(filters=n_classes, kernel_size=(1, 1), strides=1, activation='softmax', name='output')(inputs)

    return keras.Model(inputs=inputs, outputs=outputs)


if __name__ == '__main__':
    model = build_model()
    print(model.summary())
