NODE, EDGE, ATTR = range(3)


class Node:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs

    def __eq__(self, other):
        return self.name == other.name and self.attrs == other.attrs


class Edge:
    def __init__(self, src, dst, attrs):
        self.src = src
        self.dst = dst
        self.attrs = attrs

    def __eq__(self, other):
        return (self.src == other.src and
                self.dst == other.dst and
                self.attrs == other.attrs)


class Graph:
    def __init__(self, data=None):
        # data = array of tuples (NODE, name ,attrs)
        #      = array of tuples (EDGE, src, dst, attrs)
        #      = array of tuples (ATTR, key, value)
        self._nodes = []
        self._edges = []
        self._attrs = {}
        if data is not None:
            self._process_data(data)

    def __getattr__(self, attr):
        if attr == 'nodes':
            return self._nodes
        elif attr == 'edges':
            return self._edges
        elif attr == 'attrs':
            return self._attrs
        else:
            raise NotImplementedError("this method is not (yet) implemented")

    def _process_data(self, data):
        if isinstance(data, list) and len(data) > 0:
            for item in data:
                if not isinstance(item, tuple) or len(item) < 2:
                    raise TypeError("Graph item incomplete")
                typ_, *rest = item
                if typ_ == ATTR:
                    self._set_attrs(rest)
                elif typ_ == EDGE:
                    self._set_edge(rest)
                elif typ_ == NODE:
                    self._set_node(rest)
                else:
                    raise ValueError("Unknown item")
        else:
            raise TypeError("Graph data malformed")

    def _set_attrs(self, rest):
        k, *v = rest
        if len(v) == 1:
            self._attrs[k] = v[0]
        else:
            raise ValueError("Attribute is malformed")

    def _set_edge(self, rest):
        try:
            src, dst, attrs = rest
            self._edges.append(Edge(src, dst, attrs))
        except Exception:
            raise ValueError("Edge is malformed")

    def _set_node(self, rest):
        try:
            name, attrs = rest
            if isinstance(attrs, dict):
                self._nodes.append(Node(name, attrs))
            else:
                raise ValueError("Node is malformed")
        except Exception:
            raise ValueError("Node is malformed")
