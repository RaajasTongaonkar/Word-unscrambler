import nltk.corpus as nl
import itertools

def wordSearch(scrambledString:str):
	"""Function to unscramble letters and print legitimate english words"""

	scrambledString = [i for i in scrambledString]
	permutations = [''.join(p) for p in itertools.permutations(scrambledString)]
	englishVocab = nl.words.words()
	reducedVocab = set()
	for word in englishVocab:
		if len(word)==len(scrambledString):
			"""To reduce the size of the search space, only consider those words from english vocabulary that are the same
			length as input scrambeld string"""
			reducedVocab.add(word)

	for word in permutations:
		if word in reducedVocab:
			"""If a permutation of the input characters is present in the reduced vocabulary, it is a legitimate word"""
			print(word)



if __name__ == "__main__":
	scrambled = input("Give letters - ")
	wordSearch(scrambled)