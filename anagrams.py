
from collections import Counter, defaultdict
user_input = ["eat", "tea", "tan", "ate", "nat", "bat"]
			
def solve(words: list) -> list:
	m = defaultdict(list)
	for word in words:
		m[frozenset(dict(Counter(word)).items())].append(word)
	return [v for k, v in m.items()]
print(solve(user_input))
