"""
    helper.py
    
    Helper with utility functions
"""

# Python modules
import pandas as pd


def generate_submission(predictions, filepath='submission.csv'):
    """ Generate the .csv file to submit in the challenge
        @param predictions Predictions made by the model from the test dataset
        @param filepath Filepath for the file generated
    """
    df = pd.DataFrame(predictions, columns=['label'])
    df.index.name = 'Id'
    df.to_csv(filepath)
