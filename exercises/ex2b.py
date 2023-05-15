import sys

sys.path.append('../src')
import trie, utils, rlp

# initialize trie from previous hash; add new [key, value] where key has common prefix
state = trie.Trie('triedb', 'bc8cc99c4f4e19445ed73436f128f20b4c4020dcb88d28700b1006052f5229d8'.decode('hex'))
print state.root_hash.encode('hex')
print state.root_node
print ''
state.update('\x01\x01\x03', rlp.encode(['hellothere']))
print 'root hash:', state.root_hash.encode('hex')
k, v = state.root_node
print 'root node:', [k, v]
print 'hp encoded key, in hex:', k.encode('hex')
print state._get_node_type(state.root_node) == trie.NODE_TYPE_EXTENSION
common_prefix_key, node_hash = state.root_node
print state._decode_to_node(node_hash)
print state._get_node_type(state._decode_to_node(node_hash)) == trie.NODE_TYPE_BRANCH
