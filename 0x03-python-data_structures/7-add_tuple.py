#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    A = list(tuple_a)
    B = list(tuple_b)
    A.append(0) if len(A) is 1 else A.extend([0, 0])
    B.append(0) if len(B) is 1 else B.extend([0, 0])
    return (A[0] + B[0], A[1] + B[1])
