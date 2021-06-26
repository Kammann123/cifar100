"""
    helper.py
    
    Helper with utility functions
"""

# Python modules
import tensorflow as tf
import pandas as pd


def generate_submission(predictions, filepath='submission.csv'):
    """ Generate the .csv file to submit in the challenge
        @param predictions Predictions made by the model from the test dataset
        @param filepath Filepath for the file generated
    """
    df = pd.DataFrame(predictions, columns=['label'])
    df.index.name = 'Id'
    df.to_csv(filepath)


def resize_images(images, height, width):
  """ Resizes images using the bicubic interpolation method and returns them in a
      [0, 255] value mode.
      @param images Group of images
      @param height Height of the output image
      @param width Width of the output image
  """
  resized = tf.image.resize(images / 255, (width, height), method=tf.image.ResizeMethod.BICUBIC) * 255
  resized = tf.cast(resized, tf.int32)
  return resized
  