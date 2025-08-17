Eight levels of inclusivity:  
- 0	Not inclusive, literally Hitler!
- 1	Replace one vowel
- 2	Replace all vowels
- 3	Replace all but the first and last letters, no vowels
- 4	Replace all but the first letter, no vowels
- 5	Only the first letter, and one censor if it is a 2+ letter word.  No vowels
- 6	Only word-length censors
- 7	One censor
- 8	Nothing but punctuation
- 9+	Ulimate inclusivity! Not even any triggering punctuation.

```python
from snowflake import protect
for fragility in range(10):
  print(fragility,protect("Zhey went to the store for zher medication today.",fragility))
```
