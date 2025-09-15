import numpy as np
from typing import Tuple, Any, Type

class Value:
    def __init__(self, 
                data: float, 
                _children: tuple[Any, ...] = (), 
                _op: str='', 
                label: str=''):
        self.data = data
        self.grad = 0.0
        self._prev = set(_children)
        self._op = _op
        self.label = label
        self._backward = lambda: None

    def __repr__(self):
        return f"Value(data={self.data})"

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), '+')
        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward

        return out
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other): # a - b
        return self.__add__(-1 * other)
    
    def __rsub__(self, other): # -a + b
        return (-1 * self).__add__(other)
    
    def __neg__(self): # -a
        return self.__mul__(-1)

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), '*')
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return self.__mul__(other**-1)

    def __pow__(self, other: int):
        assert isinstance(other, (int, float))
        out = Value(self.data**other, (self, ), f"**{other}")
        def _backward():
            # example: x^5, derivative 5x^4
            self.grad += other * self.data**(other-1) * out.grad
        out._backward = _backward
        return out

    def exp(self):
        out = Value(np.exp(self.data), (self, ), "exp")

        def backward():
            self.grad += out.data * out.grad
        out._backward = backward
        return out

    def backward(self):
        self.grad = 1.0

        topo = []
        visited = set()
        def build_topo(v):
            if v not in visited:
                visited.add(v)
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        build_topo(self)

        for node in reversed(topo):
            node._backward()

    def relu(self):
        # def _backward():
        #     pass
        # out._backward = _backward
        pass

    def tanh(self):
        # (e^2x - 1) / (e^2x + 1) / 
        epow2x = np.exp(2*self.data)
        tanh = (epow2x - 1) / (epow2x + 1)
        out = Value(tanh, (self, ), 'tanh')

        def _backward():
            self.grad += (1 - tanh**2) * out.grad
        out._backward = _backward
        # print(f"{epow2x=}\n{tanh=}")
        
        return out
