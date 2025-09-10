#method resolution order
class A: pass
class B(A): pass
class C(B,A): pass
print(C.mro())
print(B.mro())