class StorageNode:
    data = {}
    def __init__(self, id):
        self.id = id

    def put_file(self, name: str, content: str):
        self.data[name] = content

    def get_file(self, name: str):
        return self.data[name]
    
# Initially we have 5 nodes in our storage node pool
storage_nodes = [StorageNode(1), StorageNode(2), StorageNode(3), StorageNode(4), StorageNode(5)]

def hash_fn(name: str):
    return sum(bytearray(name.encode('utf-8'))) % len(storage_nodes)    # %<total number of storage nodes>

files_to_put = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt"]

# Putting all files to their respenctive hashed nodes
print("With storage node pool as 5 :")
for i in range(5):
    current_file = files_to_put[i]
    hash_value = hash_fn(current_file)
    node_to_put = storage_nodes[hash_value]
    node_to_put.put_file(current_file, current_file)
    print("{} -> storage node {}".format(current_file, hash_value + 1))
print("\n")
# Lets scale up storage nodes to 7

storage_nodes.append([StorageNode(6), StorageNode(7)])
# Now we have 7 storage nodes

print("Adding 2 more storage nodes, now those same files belong to")
for i in range(5):
    current_file = files_to_put[i]
    hash_value = hash_fn(current_file)
    print("{} -> storage node {}".format(current_file, hash_value + 1))
print("\n")
print("Now we can see, we have to move all files to their new respentive storage nodes, which makes the whole process costier")








