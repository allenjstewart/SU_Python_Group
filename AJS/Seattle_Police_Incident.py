# -*- coding: utf-8 -*-
"""
Created on Tue May 15 10:18:20 2018

@author: allen
"""


import pandas as pd
from sodapy import Socrata
import matplotlib.pyplot as plt


client = Socrata("data.seattle.gov", None)

#
results = client.get("y7pv-r3kh", limit=2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
plt.figure();
sector=results_df.groupby('district_sector').summarized_offense_description.value_counts().sort_index()
sector.unstack().plot(kind='bar')