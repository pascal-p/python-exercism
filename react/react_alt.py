from typing import Union, List, Callable, Dict

Number = Union[int, float]
Vector = List


class ComputeCell:
    pass  # trick to get the type for the observer


class InputCell:
    def __init__(self, init_val: Number):
        self._id = id(self)
        self._value = init_val
        self._observers = set()

    @property
    def value(self):
        return self._value

    @property
    def id(self):
        return self._id

    @value.setter
    def value(self, val: Number):
        """
        only propagate if the value actually changes
        """
        if self.value != val:
            self._value = val  # yes, use ._value
            self._propagate()

    def _propagate(self):
        """
        Propagate the change down the dependency tree.
        The nodes(ccells) are visited in breadth-first, by using a queue to
        guarantee that all inputs of a node(ccell) are updated before any
        given node(ccell) is updated.
        """
        q_ccells = list(self._observers)
        while len(q_ccells) > 0:
            ccell = q_ccells[0]
            q_ccells = q_ccells[1:]
            ccell.re_calc()
            q_ccells = [
                *q_ccells,
                *ccell._observers
            ]

    def __repr__(self):
        ids = list(map(lambda x: str(x._id), self._observers))
        s_ids = ','.join(ids)
        return f"<id: {self._id} , value: {self._value} / observers: [{s_ids}]>"


class ComputeCell:
    def __init__(self, inputs: Vector, compute_fn: Callable):
        self._id = id(self)
        self._inputs = inputs
        self._fn = compute_fn
        self._callbacks = set()
        self._observers = set()
        for inp in inputs:
            inp._observers.add(self)
        self.calc()

    def add_callback(self, callback: Callable):
        self._callbacks.add(callback)

    def remove_callback(self, callback: Callable):
        if callback in self._callbacks:
            self._callbacks.remove(callback)

    def calc(self):
        self._value = self._fn([x.value for x in self._inputs])

    def re_calc(self):
        ex_val = self._value
        self.calc()  # calc new value - did it change?
        if self._value != ex_val:  # yes
            self._call_callbacks()

    def _call_callbacks(self):
        for cb in self._callbacks:
            cb(self._value)

    def __getattr__(self, attr: str):
        if attr == 'value':
            return self._value
        raise NotImplementedError(
            f"this method: {attr} is not (yet) implemented")
