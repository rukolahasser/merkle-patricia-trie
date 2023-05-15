import sys
sys.path.append('../src')
import trie, utils, rlp

#initialize trie from previous hash; add new [key, value] where key has common prefix
state = trie.Trie('triedb', '4161fc351963df5d93bb2d8b05f1ccb76a25de0a6ea0e9293aa139822bd2e876'.decode('hex'))
print state.root_hash.encode('hex')
print state.root_node
print ''
state.update('\x01\x01\x02\x55', rlp.encode(['hellothere']))
print 'root hash:', state.root_hash.encode('hex')
print 'root node:', state.root_node
print 'branch node it points to:', state._decode_to_node(state.root_node[1])
print ''
state.update('\x01\x01\x02\x57', rlp.encode(['jimbojones']))
print 'root hash:', state.root_hash.encode('hex')
print 'root node:', state.root_node
branch_node = state._decode_to_node(state.root_node[1])
print 'branch node it points to:', branch_node
next_hash = branch_node[5]
print 'hash stored in branch node:', next_hash.encode('hex')
print 'branch node it points to:', state._decode_to_node(next_hash)
