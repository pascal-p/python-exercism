from typing import Union, List, Callable, Dict

Number = Union[int, float]
Vector = List


class ComputeCell:
    pass  # trick to get the type for the observer


class Cell:
    def __init__(self, init_val: Number):
        self._id = id(self)
        self._value = init_val
        self._observers = set()

    def add_observer(self, observer: ComputeCell):
        self._observers.add(observer)

    def remove_observer(self, observer: ComputeCell):
        self._observers.remove(observer)

    def notify_observers(self, changed: Dict):
        for obs in self._observers:
            obs.re_calc(changed)  # NOTE observers are ComputeCell instances

    @property
    def value(self):
        return self._value

    @property
    def id(self):
        return self._id

    def __repr__(self):
        ids = list(map(lambda x: str(x._id), self._observers))
        s_ids = ','.join(ids)
        return f"<id: {self._id} , value: {self._value} / observers: [{s_ids}]>"


class InputCell(Cell):
    def __init__(self, init_val: Number):
        super().__init__(init_val)

    @Cell.value.setter
    def value(self, val: Number):
        """
        only propagate if the value actually changes
        """
        if self.value != val:
            self._value = val  # yes, use ._value
            changed = {}
            self.notify_observers(changed)  # propagate...
            for cell, orig_val in changed.items():
                if cell.value != orig_val:
                    cell.call_callbacks()  # as the cell's value actually changed, invoke callback


class ComputeCell(Cell):
    def __init__(self, inputs: Vector[Cell], compute_fn: Callable):
        self._inputs = inputs
        self._fn = compute_fn
        self._callbacks = set()
        for inp in inputs:
            inp.add_observer(self)
        super().__init__(init_val=self.calc())

    def add_callback(self, callback: Callable):
        self._callbacks.add(callback)

    def remove_callback(self, callback: Callable):
        if callback in self._callbacks:
            self._callbacks.remove(callback)

    def calc(self):
        return self._fn([x.value for x in self._inputs])

    def re_calc(self, changed: Dict):
        val = self.calc()  # calc new value - did it change?
        if self._value != val:  # yes
            changed.setdefault(self, self._value)  # current value
            self._value = val  # update
            self.notify_observers(changed)  # notify (cascade) dependent cells

    def call_callbacks(self):
        for cb in self._callbacks:
            cb(self.value)

    def __getattr__(self, attr: str):
        if attr == 'value':
            return self._value
        raise NotImplementedError(
            f"this method: {attr} is not (yet) implemented")
