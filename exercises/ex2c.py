import sys
sys.path.append('../src')
import trie, utils, rlp

#initialize trie from previous hash; add new [key, value] where key has common prefix
state = trie.Trie('triedb', 'bd177d2f9a593cc26c3b918dfcffb74fd03cdca47ee1e962b80555cf1f5f4fda'.decode('hex'))
print state.root_hash.encode('hex')
print state.root_node
print ''
state.update('\x01\x01', rlp.encode(['hellothere']))
print 'root hash:', state.root_hash.encode('hex')
print 'root node:', state.root_node
print state._decode_to_node(state.root_node[1])
