import re

"""
	Eight levels of inclusivity:
	0	Not inclusive, literally Hitler!
	1	Replace one vowel
	2	Replace all vowels
	3	Replace all but the first and last letters, no vowels
	4	Replace all but the first letter, no vowels
	5	Only the first letter, and one censor if it is a 2+ letter word.  No vowels
	6	Only word-length censors
	7	One censor
	8	Nothing but punctuation
	9+	Ulimate inclusivity! Not even any triggering punctuation.

	from snowflake import protect
	for level in range(10): print(protect("Zhey went to the store today.",level))
"""
def protect(triggered,level=1,safe="*",triggering="aeiouAEIOU"):
	woke=""
	for word in re.split(r"([^\w]+)",triggered):
		if not re.match(r"[\w]+",word):
			woke+=word
			continue
		match level:
			case 0: return triggered
			case 1: pass
			case 2: pass
			case 3: word=(word[0]+safe*(len(word)-2)+word[-1])[0:len(word)]
			case 4: word=(word[0]+safe*(len(word)-1))[0:len(word)]
			case 5: word=(word[0]+safe)[0:len(word)]
			case 6: word=safe*len(word)
			case 7: word=safe
			case 8: word=""
			case _: return ""
		woke+=re.sub(f"[{triggering}]",safe,word,count=1 if level<2 else 0)
	return woke

for level in range(10): print(level,protect("Zhey went to the store today.",level))