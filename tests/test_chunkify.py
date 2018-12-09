from ethinjest.util import chunkify

def test_chunkify_ok():
    l = [1, 2, 3, 4, 5, 6]
    chunks = chunkify(l, 3)
    assert len(chunks) == 3
    assert chunks[0] == [1,4]
    assert all([i in chunks[0] or i in chunks[1] or i in chunks[2] for i in l])
