import random
from value import Value

class Neuron:
    def __init__(self, nin): #nin = number of inputs
        # weights
        self.w = [Value(random.uniform(-1, 1)) for _ in range(nin)]
        # bias
        self.b = Value(random.uniform(-1, 1))

    def __call__(self, x): 
        # w*x + b
        act = sum(wi * xi for wi,xi in zip(self.w, x)) + self.b
        return act.tanh()
    
    def __repr__(self):
        return f"Neuron(w={self.w}, b={self.b})"
    
    def parameters(self):
        return self.w + [self.b]

class Layer:
    def __init__(self, nin, nout):
        self.neurons = [Neuron(nin) for _ in range(nout)]

    def __call__(self, x):
        out = [neuron(x) for neuron in self.neurons]
        return out
    
    def __repr__(self):
        return f"Layer(neurons={len(self.neurons)})"
    
    def parameters(self):
        return [p for n in self.neurons for p in n.parameters()]

class MLP:
    def __init__(self, nin, nouts):
        n = [nin] + nouts
        self.layers = [Layer(n[i], n[i+1]) for i in range(len(nouts))]
    
    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x[0] if len(x) == 1 else x
    
    def parameters(self):
        return [p for n in self.layers for p in n.parameters()] 