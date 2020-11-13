#!/usr/bin/env python3

import pandas as pd

dataset = pd.read_csv('Dataset.csv')
dataset.to_csv('Dataset.csv', index=False)
