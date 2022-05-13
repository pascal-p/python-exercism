from typing import List


def tree_from_traversals(pre_o: List, in_o: List):
    """
    Pre-order: root, left subtree, right subtree
    In-order: left subtree, root, right right subtree
    """
    if has_repeated_items(pre_o) or has_repeated_items(in_o):
        raise ValueError("repeated values detected")
    return tree_from_trav_fn(pre_o, in_o)


def tree_from_trav_fn(pre_o: List, in_o: List):
    n_pre, n_ino = len(pre_o), len(in_o)

    if n_pre != n_ino:
        raise ValueError("preorder and inorder should have the same length")
    if n_pre == 0:
        return {}  # assert n_ino == 0

    root = pre_o[0]
    rix = find_root_inorder(in_o, root)  # root index inorder
    lst = tree_from_trav_fn(pre_o[1:rix+1], in_o[0:rix])
    rst = tree_from_trav_fn(pre_o[rix+1:n_pre], in_o[rix+1:n_ino])
    return node(root, l=lst, r=rst)


def find_root_inorder(in_o: List, root):
    ix, lim = 0, len(in_o)
    while ix < lim and in_o[ix] != root:
        ix += 1
    if ix == lim:
        # inconsistency between in-order and pre-order
        raise ValueError("Could not find the root in the in-order array")
    assert in_o[ix] == root
    return ix


def node(v, l={}, r={}):
    return {'v': v, 'l': l, 'r': r}


def has_repeated_items(a: List) -> bool:
    """
    Build hash from list, if all keys are unique (assoc. with value 1)
    """
    d, res = {}, False
    for x in a:
        if x in d.keys():
            res = True
            break
        d[x] = 1
    return res

##
# def tree_from_traversals(pre_o: List, in_o: List):
#     """
#     Pre-order: root, left subtree, right subtree

#     In-order: left subtree, root, right right subtree
#     """
#     if len(pre_o) != len(in_o):
#         raise ValueError("preorder and inorder should have the same length")

#     if len(pre_o) == 0:
#         assert len(in_o) == 0
#         return {}

#     root = pre_o[0]
#     # ll == left low ix, lh == left high ix ; rl == right low ix, rh == right high ix
#     ((ll, lh), (rl, rh)) = find_lr_subtree(in_o, root)

#     jx = lh - ll + 2
#     lst = tree_from_traversals(pre_o[1:jx], in_o[ll:lh + 1])
#     rst = tree_from_traversals(pre_o[jx:rh + 1], in_o[rl:rh + 1])
#     return node(root, l=lst, r=rst)

# def find_lr_subtree(in_o: List, root):
#     ix, lim = 0, len(in_o)
#     while ix < lim and in_o[ix] != root:
#         ix += 1

#     if ix == lim:
#         # inconsistency between in-order and pre-order
#         raise ValueError("Could not find the root in the in-order array")

#     assert in_o[ix] == root
#     return ((0, ix - 1), (ix + 1, lim - 1))
