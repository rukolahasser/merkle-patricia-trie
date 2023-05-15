import sys
sys.path.append('../src')
import trie, utils, rlp

#initialize trie from previous hash; add new [key, value] where key has common prefix
state = trie.Trie('triedb', '6b33a82ce696a9a554b9e1e2ca5317e57e6aabd735f32534ea144a0a51097380'.decode('hex'))
print state.root_hash.encode('hex')
print state.root_node
print ''
state.update('\x01\x01\x02\x55', rlp.encode(['hellothere']))
print 'root hash:', state.root_hash.encode('hex')
print 'root node:', state.root_node
print state._decode_to_node(state.root_node[1])
