#!/usr/bin/env python
import pandas as pd
import numpy as np

# read the log file
df = pd.read_table('tasks-fingerfootlips_events.tsv')

groups = df.groupby(df['trial_type'])
times = groups['onset'].unique()

# save times
for condition in times.index:
	onsets = np.array(times[condition])
	np.savetxt(condition + '.txt', onsets[np.newaxis], fmt='%0.2f')
