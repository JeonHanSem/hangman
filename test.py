import unittest
import hangman

class hangmanTestCase(unittest.TestCase):
	def test_True(self):
		ret = hangman.checkCorrectAnswer("tac","cat")
		self.assertTrue(ref)
	def test_False(self):
		ret = hangman.checkCorrectAnswer("zebrio","zebra")
		self.asserTrue(answer)

if __name__ == "__main__":
	unittest.main()
