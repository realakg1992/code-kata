#!/usr/bin/env python
# coding: utf-8

# In[2]:


import hashlib
import pandas as pd

# Function to anonymize data
def anonymize_string(value):
    return hashlib.sha256(value.encode()).hexdigest()

# Process CSV in chunks to avoid memory overload
chunk_size = 10**6  # Process 100,000 rows at a time
chunks = pd.read_csv('large_dataset.csv', chunksize=chunk_size)

for chunk in chunks:
    # Apply anonymization to the required columns
    chunk['first_name'] = chunk['first_name'].apply(anonymize_string)
    chunk['last_name'] = chunk['last_name'].apply(anonymize_string)
    chunk['address'] = chunk['address'].apply(anonymize_string)
    
    # Save the anonymized chunk to a new CSV file
    chunk.to_csv('anonymized_large_dataset.csv', mode='a', index=False, header=False)


# In[ ]:




