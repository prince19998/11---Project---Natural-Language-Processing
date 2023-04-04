#!/usr/bin/env python
# coding: utf-8

# # Project - Natural Language Processing
# - Can you determine who tweeted this?

# ### Description
# - We will analyze a collection of tweets from one tweet account
# - Can we figure out the person behind the account?

# ### Step 1: Import libraries

# In[2]:


import pandas as pd
from nltk import word_tokenize, ngrams
from collections import Counter
import nltk
nltk.download('punkt')


# ### Step 2: Import data
# - Use Pandas [read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) method to read files/tweets.csv

# In[3]:


data = pd.read_csv('files/tweets.csv')
data.head()


# In[ ]:





# ### Step 3: Convert content to a list of content
# - Use list on the column **content**
#     - You can also apply [to_list()](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html) on the column

# In[4]:


content = list(data['content'])


# In[5]:


len(content)


# ### Step 4: Create a corpus
# - Create an empty list called **corpus**
# - Iterate over **content**
#     - Extend **corpus** with all words in lowercase if any character is alpha in the word.
#         - HINT: To lowercase, call **lower()** on the word.
#         - HINT: To check if any character is alhpa, use **any(c.isalpha() for c in word)**

# In[6]:


corpus = []
for item in content:
  corpus.extend([word.lower() for word in word_tokenize(item) if any(c.isalpha() for c in word)])


# In[ ]:





# ### Step 5: Check corpus
# - Find the length of the corpus
# - Look at the first 10 words in the corpus

# In[7]:


len(corpus)


# In[8]:


corpus[:10]


# ### Step 6: Display all 3-grams
# - Use **Counter(ngrams(corpus, 3))** and assign it to a variable
# - List the 10 most common 3-grams
#     - HINT: call **most_common(10)** on the result from **Counter(...)**

# In[9]:


ngram = Counter(ngrams(corpus, 3))


# In[10]:


ngram.most_common(10)


# ### Step 7 (Optional): Pretty print
# - Iterate over the result with a for-loop
#     - HINT: Each loop gives a **ngram** and **frequency**

# In[11]:


for gram, freq in ngram.most_common(10):
  print(f'Frequency: {freq} -> {gram}')


# In[ ]:





# ### Step 8 (Optional): Try it with 4-grams

# In[12]:


ngram = Counter(ngrams(corpus, 4))


# In[13]:


ngram.most_common(10)


# In[14]:


ngram = Counter(ngrams(corpus, 5))
ngram.most_common(10)

