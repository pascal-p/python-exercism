from typing import Dict, List

class CustomSet:
    @staticmethod
    def mapper(elements, init) -> Dict:
        """Beware trap if init is set to default: {} => shared reference"""
        init.update({ e: 1 for e in elements })
        return init

    def __init__(self, elements=[]):
        if elements is None or len(elements) == 0:
            self._set = dict()
        else:
            self._set = __class__.mapper(elements, {})

    def isempty(self) -> bool:
        return len(self._set) == 0

    def card(self) -> int:
        return len(self._set)

    def __contains__(self, element) -> bool:
        return element in self._set.keys()

    def issubset(self, other) -> bool:
        return len(list(filter(lambda elt: elt not in other,
                               self.elements()))) == 0

    def isdisjoint(self, other) -> bool:
        c1, c2 = self.card(), other.card()
        if c1 < c2:
            if c1 == 0: return True
            return len(list(filter(lambda elt: elt in other,
                                   self.elements()))) == 0
        else:
            if c2 == 0: return True
            return len(list(filter(lambda elt: elt in self,
                                   other.elements()))) == 0

    def __eq__(self, other) -> bool:
        return self.card() == other.card() and self.issubset(other)

    def add(self, element):
        self._set[element] = 1
        return self

    def intersection(self, other):
        if self.card() > other.card():
            ary = filter(lambda elt: elt in self, other.elements())
        else:
            ary = filter(lambda elt: elt in other, self.elements())
        return CustomSet(list(ary))

    def __sub__(self, other):
        "diff: element in self not in other"
        print("Called diff ")
        ary = list(filter(lambda elt: elt not in other.elements(),
                          self.elements()))
        print(ary)
        return CustomSet(ary)

    def __add__(self, other):
        "union: elements in both sets"
        # if self.card() > other.card():
        #     this = CustomSet(self.elements())
        #     this._set = __class__.mapper(other.elements(), this._set)
        # else:
        #     this = CustomSet(other.elements())
        #     this._set = __class__.mapper(self.elements(), this._set)
        # return this
        # or:
        return CustomSet([*self.elements(), *other.elements()])

    def __repr__(self):
        # string repr
        return ', '.join(map(lambda e: str(e), self._set.keys()))

    ## Extensions
    def elements(self) -> List:
        return list(self._set.keys())
