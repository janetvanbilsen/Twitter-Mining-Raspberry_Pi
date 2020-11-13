#!/usr/bin/env python3

import pandas as pd
import time

# Importing dataset
dataset = pd.read_csv('Dataset.csv')

# Saving date of backup
current_date = time.strftime('%Y%m%d')

# Saving to backup folder
dataset.to_csv('Dataset_backup_' + current_date + '.csv', index=False)
