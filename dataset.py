from typing import Generator
from pathlib import Path

import pickle
import random
import pandas as pd

import tensorflow as tf
import numpy as np

import tensorflow as tf

# TODO: try chaing into an iterative loader to lower the peak RAM usage
def loadDataset(data: pd.DataFrame, labels: list, classes: list) -> tf.data.Dataset:

    n, m = data.shape

    def generatorFunc() -> Generator:
        
        for i in range(n):
            y = labels[i]
            x = data.iloc[i]
            # print(f"Reading {i}...")
            yield {
                "features": tf.convert_to_tensor(x, dtype = tf.float64),
                "labels": tf.convert_to_tensor(y, dtype = tf.int32)
            }

    return tf.data.Dataset.from_generator(
        generator = generatorFunc,
        output_signature = {
            "features": tf.TensorSpec(shape = (m, ), dtype = tf.float64),
            "labels": tf.TensorSpec(shape = (len(classes), ), dtype = tf.int32)
        }
    )


def createBatches(
    dataset: tf.data.Dataset,
    count: int,
    validationSplit: float,
    bufferSize: int,
    batchSize: int
) -> tuple[tf.data.Dataset, int, tf.data.Dataset, int]:
    
    trainCount = int((1 - validationSplit) * count)
    testCount = count - trainCount

    trainData = dataset.take(trainCount)
    testData = dataset.skip(trainCount).take(testCount)

    trainBatches = (
        trainData
        .cache()
        .shuffle(bufferSize)
        .batch(batchSize)
        .repeat()
        .prefetch(buffer_size = tf.data.AUTOTUNE)
    )
    testBatches = testData.batch(batchSize)

    return trainBatches, trainCount // batchSize, testBatches, count - trainCount
