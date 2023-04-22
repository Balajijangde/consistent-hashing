import hashlib
from bisect import bisect, bisect_left, bisect_right

class StorageNode:
    files = {}
    def __init__(self, host: str):
        self.host = host

    def put_file(self, name: str, content: str):
        self.files[name] = content

    def get_file(self, name: str):
        self.files[name]


keys = []
nodes = []
total_slots = 50

def hash_fn(key: str, total_slots: int) -> int:
    hsh = hashlib.sha256()
    hsh.update(bytes(key.encode('utf-8')))
    #print(hsh.hexdigest())
    return int(hsh.hexdigest(), 16) % total_slots

def add_node(storageNode: StorageNode) -> int:
    #adds a storage node to the storage pool and returns its key in hash space where it is placed
    if(len(nodes) == total_slots):
        raise Exception("Hash space is full")
    key = hash_fn(storageNode.host, total_slots)
    index = bisect(keys, key)
    #check for collision

    if(index > 0 and keys[index-1] == key):
        raise Exception("collision occured")
    
    #Perform data migration
    keys.insert(index, key)
    nodes.insert(index, storageNode)

    return key

def remove_node(storageNode: StorageNode) -> int:
    #removes a storage node from the storage pool and returns its key in hash space from where its removed

    if(len(nodes) == 0):
        raise Exception("storage pool empty")
    
    key = hash_fn(storageNode.host, total_slots)
    index = bisect_left(keys, key)

    if index >= len(nodes) or keys[index] != key:
        raise Exception("storage node doesn't exist")
    
    # Perform data migration
    keys.pop(index)
    nodes.pop(index)

    return key

def assign(name: str) -> str:
    #Given a file name, it will return the storage node file is associated with
    key = hash_fn(name, total_slots)
    index = bisect_right(keys, key) % len(keys)
    print("file {} is assigned to host {}".format(name, nodes[index].host))
    return nodes[index].host

node1 = StorageNode("192.168.80.101")
node2 = StorageNode("192.168.80.104")
node3 = StorageNode("192.168.80.210")
node4 = StorageNode("192.168.80.345")
node5 = StorageNode("192.168.80.502")
add_node(node1)
add_node(node2)
add_node(node3)
add_node(node4)
add_node(node5)

print(keys)

remove_node(node1)
remove_node(node2)

print(keys)

files_to_put = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]
for i in range(5):
    assign(files_to_put[i])


