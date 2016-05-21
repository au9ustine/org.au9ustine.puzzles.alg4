class UF(object):
    def __init__(self, N):
        self.g = range(N)
        self.g_count = N

    def __repr__(self):
        return str((self.g, self.g_count))

    def count(self):
        return self.g_count

    def connected(self, p, q):
        return self.g[p] == g[q]

    def find(self, p):
        return self.g[p]

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id is not q_id:
            for i in range(len(self.g)):
                if self.g[i] is p_id:
                    self.g[i] = q_id
            self.g_count -= 1
    
    def quick_find(self, p):
        while p != self.g[p]:
            p = self.g[p]
        return p

    def quick_union(self, p, q):
        p_root = self.quick_find(p)
        q_root = self.quick_find(q)
        if p_root != q_root:
            self.g[p_root] = q_root
            self.g_count -= 1


def commons():
    uf = UF(10)
    connections = [
        (4, 3),
        (3, 8),
        (6, 5),
        (9, 4),
        (2, 1),
        (8, 9),
        (5, 0),
        (7, 2),
        (6, 1),
        (1, 0),
        (6, 7)
    ]
    return (uf, connections)

def test_uf_union():
    uf, connections = commons()
    for p, q in connections:
        uf.union(p, q)
    assert repr(uf) == "([1, 1, 1, 8, 8, 1, 1, 1, 8, 8], 2)"

def test_uf_quick_union():
    uf, connections = commons()
    for p, q in connections:
        uf.quick_union(p, q)
    assert repr(uf) == "([1, 1, 1, 8, 3, 0, 5, 1, 8, 8], 2)"

if __name__ == "__main__":
    test_uf_union()
    test_uf_quick_union()

