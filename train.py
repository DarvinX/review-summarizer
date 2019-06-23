import numpy as np
import pandas as pd
import re
from pickle import dump, load

reviews = pd.read_csv("./dataset/Reviews.csv")

print(reviews.shape)
print(reviews.isnull().sum())
reviews = reviews.dropna()

reviews = reviews.drop(['Id',
                        'ProductId',
                        'UserId',
                        'ProfileName',
                        'HelpfulnessNumerator',
                        'HelpfulnessDenominator',
                        'Score',
                        'Time'
                        ], 1)

print(reviews.shape)
reviews = reviews.reset_index(drop=True)
print(reviews.head())
