import sys
sys.path.append('../src')
import trie, utils, rlp

#initialize trie from previous hash; add new [key, value] where key has common prefix
state = trie.Trie('triedb', '4161fc351963df5d93bb2d8b05f1ccb76a25de0a6ea0e9293aa139822bd2e876'.decode('hex'))
print 'using root hash from ex2b'
print rlp.decode(state.get('\x01\x01\x03'))
print ''
state = trie.Trie('triedb', '5b4700cc8b3d5b39e61ef4d22ae9ddb62916dc30d4cac7d5f043bd2b1ee84f07'.decode('hex'))
print 'using root hash from ex3'
print rlp.decode(state.get('\x01\x01\x02'))
print rlp.decode(state.get('\x01\x01\x02\x55'))
print rlp.decode(state.get('\x01\x01\x02\x57'))
