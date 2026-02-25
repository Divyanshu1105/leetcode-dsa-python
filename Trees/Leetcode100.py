def isSameTree(p, q):
    """
    Determines whether two binary trees are structurally identical
    with the same node values at every position.

    Uses depth-first (pre-order) recursion: compares the current nodes
    first, then recurses into left and right subtrees. Short-circuits
    on the first mismatch found.

    Base cases:
        - Both nodes are None  → True  (matching leaves / empty trees)
        - Exactly one is None  → False (structural mismatch)
        - Values differ        → False (value mismatch)

    Args:
        p: Root of the first binary tree.
        q: Root of the second binary tree.

    Returns:
        True if both trees are identical in structure and values,
        False otherwise.

    Time Complexity:  O(n) — visits each node pair at most once,
                      where n = min(nodes in p, nodes in q)
    Space Complexity: O(h) — call stack depth equals tree height h.
                      O(log n) for balanced, O(n) worst case (skewed).

    Example:
        p = [1, 2, 3], q = [1, 2, 3]  → True
        p = [1, 2],    q = [1, None, 2] → False  (structural mismatch)
    """
    if not p and not q: return True
    if not p or not q: return False
    if p.val != q.val: return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)