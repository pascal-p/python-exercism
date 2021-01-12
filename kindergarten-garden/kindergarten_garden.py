class KClass:
    PUPIL = [ 'Ayumi', 'Bob', 'Charlie', 'David',
              'Eve', 'Fred', 'Ginny', 'Harriet',
              'Ileana', 'Joseph', 'Kincaid', 'Larry' ]

    PLANTS = {
        'C': 'Clover', 'G': 'Grass', 'R': 'Radishes', 'V': 'Violets'
    }


class Garden:
    def __init__(self, diagram, pupil=KClass.PUPIL):
        self.diagram = diagram
        self.pupil = sorted(pupil)
        self.assign = self.assign()

    def plants(self, name):
        if name in self.pupil:
            return self.assign[name]
        raise(ValueError(f"pupil: {name} is not in this class"))

    # Helper
    def assign(self):
        ary = self.diagram.split('\n')
        hsh = {}

        for (ix, name) in enumerate(self.pupil):
            # hsh[name] = []
            jx = 2 * (ix + 1) - 2
            hsh[name] = [
                KClass.PLANTS[ary[0][kx]] for kx in range(jx, jx + 2) \
                if ary[0][kx] in KClass.PLANTS
            ] + [
                KClass.PLANTS[ary[1][kx]] for kx in range(jx, jx + 2) \
                if ary[1][kx] in KClass.PLANTS
            ]
            if jx+2 >= len(ary[0]):
                break

        return hsh
