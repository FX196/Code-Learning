class Node:
    def __init__(self, val, key=None):
        self.val = val
        self.key = key

# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    res=[]
    while s:
        res.append((s[0],s.count(s[0])))
        s=s.replace(s[0],"")
    return res


def dictionary(freqs):
    nodes = []
    for element in freqs:
        nodes.append(Node(element[1], element[0]))

    nodes.sort(key=lambda x: x.val)

    while len(nodes)>1:
        right = nodes.pop(0)
        left = nodes.pop(0)
        new_node = Node(left.val+right.val)
        for i in range(len(nodes)):
            if nodes[i].val>new_node.val:
                break
        if nodes[i].val>new_node.val:
            nodes.insert(i, new_node)
        else:
            nodes.append(new_node)



# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):
    return ""


# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):
    return ""

if __name__ == "__main__":
    print(frequencies("aaabbc"))