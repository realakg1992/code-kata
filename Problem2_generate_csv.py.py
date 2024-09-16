#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
from faker import Faker

# Instantiate Faker for random data generation
fake = Faker()

# Number of rows to generate
rows = 10**3  # We can Adjust this to generate large files

# Generate data
data = {
    'first_name': [fake.first_name() for _ in range(rows)],
    'last_name': [fake.last_name() for _ in range(rows)],
    'address': [fake.address().replace('\n', ', ') for _ in range(rows)],
    'date_of_birth': [fake.date_of_birth(minimum_age=18, maximum_age=90) for _ in range(rows)]
}

# Convert to DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv('large_dataset.csv', index=False)


# In[ ]:





# In[ ]:




