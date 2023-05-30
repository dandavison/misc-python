class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self._refs = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        for ref in self._refs:
            ref._evaluate()
        for ref in self._refs:
            ref._call_callbacks()

    def _evaluate(self):
        return self.value


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        for i in self.inputs:
            i._refs.append(self)
        self.compute_function = compute_function
        self._callbacks = set()
        self._evaluate()
        self._call_callbacks()
        self._refs = []

    def _evaluate(self):
        for i in self.inputs:            
            i._evaluate()
        self.value = self.compute_function([i.value for i in self.inputs])

    def _call_callbacks(self):
        for cb in self._callbacks:
            cb(self.value)

    def add_callback(self, callback):
        self._callbacks.add(callback)

    def remove_callback(self, callback):
        self._callbacks.remove(callback)
