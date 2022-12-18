class Layer:
    def __init__(self):
        self.next_layer = None
        self.name = 'Layer'

    def __call__(self, next_obj):
        self.next_layer = next_obj
        return next_obj


class Input(Layer):
    def __init__(self, inp):
        super().__init__()
        self.inputs = inp
        self.name = 'Input'


class Dense(Layer):
    def __init__(self, inputs, outputs, activation):
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation
        super().__init__()
        self.name = 'Dense'


class NetworkIterator:
    def __init__(self, layer: Layer):
        self._iter = [layer]
        while layer.next_layer:
            layer = layer.next_layer
            self._iter.append(layer)

    def __iter__(self):
        return self._iter
