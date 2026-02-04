"""10. Regular Expression Matching.

Hard
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 

Constraints:

1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match."""


class Solution:

	def isMatch(self, s: str, p: str) -> bool:
		lastPChar = ""
		lastSChar = ""
		sTracker = 0
		for pIndex, pChar in enumerate(p):
			if pChar == ".":
				sTracker += 1
				lastPChar = pChar
			elif pChar == "*":
				if lastPChar == ".":
					if pIndex == len(p) - 1:
						return True
					nextSTracker = s.find(pChar, sTracker)
					if nextSTracker == -1:
						return False
					sTracker = nextSTracker
				else:
					for nextSTracker, c in enumerate(s[sTracker :]):
						if c != lastSChar:
							sTracker = nextSTracker
							break
			else:
				sTracker += 1
		return False


if __name__ == "__main__":
	print("Solution.isMatch(None, \"aa\", \"a\"):", Solution.isMatch(None, "aa", "a"))
	print("Solution.isMatch(None, \"aa\", \"a*\"):", Solution.isMatch(None, "aa", "a*"))
	print("Solution.isMatch(None, \"ab\", \".*\"):", Solution.isMatch(None, "ab", ".*"))
