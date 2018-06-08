from TrieTree import Trie

test = Trie()
test.AddWord("Hollo")
test.AddWord("Hoola")

print test.FindLike("H")
