from math import inf
from typing import (
    Iterator,
    Optional,
    Sequence,
    Set,
    Tuple,
    Type,
    TypeVar,
    Generic,
    overload,
    List,
    Any,
)
from random import Random, shuffle
from queue import PriorityQueue, Queue
from dataclasses import dataclass, field

T = TypeVar("T", int, float)
node_type = int
weight_type = TypeVar("weight_type")


@dataclass
class Edge(Generic[T]):
    from_: node_type
    to: node_type
    weight: T


edge_type = Edge[T]
edge_list = List[edge_type]
size_type = int


@dataclass
class Graph(Generic[T]):
    n: size_type
    begin_node: node_type
    edges: List[edge_list] = field(default_factory=list)
    m: size_type = 0
    __orig_class__: Any = None
    it: Any = None

    def __post_init__(self):
        if not self.edges:
            self.edges = [list() for _ in range(self.n)]

    class Config:
        arbitrary_types_allowed = True

    @dataclass
    class AllEdgeIterator(Iterator):
        graph: "Graph"
        node: node_type
        it: Optional[Any] = None
        # @validator("it", always=True)
        # def check_it(cls, v, values, **kwargs):
        #     if values["graph"].check_range(values["node"]):
        #         return iter(values["graph"][values["node"]])

        def __eq__(self, __o: Any) -> bool:
            return self.node == __o.node

        def __ne__(self, __o: object) -> bool:
            return not (self == __o)

        # def __next__(self):
        #     if self.it is not None:
        #         self.__find_next()
        #         return self.it
        #     raise StopIteration

        # def __repr__(self) -> str:
        #     if self.it is not None:
        #         return self.it.__repr__()
        #     else:
        #         return str(self)

        def __iter__(self):
            if self.node < self.graph.n:
                self.node += 1
                if self.node < self.graph.n:
                    self.it = iter(self.graph[self.node])
                    return self.it

        def __getitem__(self, pos: int):
            if self.it is not None:
                return self.it[pos]

        def __next__(self):
            if self.it is None:
                self.it = iter(self)
            return next(self.it)

    def __getitem__(self, i: size_type) -> edge_list:
        return self.edges[i]

    def size(self) -> size_type:
        return self.n

    def all_edges(self) -> edge_list:
        edges: edge_list = []
        for i in range(self.begin_node, self.n):
            edges.extend(self.edges[i])
        return edges

    def check_range(self, i: node_type) -> bool:
        return self.begin_node <= i and i < self.n

    def get_begin_node(self) -> node_type:
        return self.begin_node

    @overload
    def add_edge(self, *, from_: node_type, to: node_type, weight: T):
        ...

    @overload
    def add_edge(
        self,
        *,
        edge: Edge,
        directed: bool = True,
    ):
        ...

    def add_edge(
        self,
        from_: node_type = 0,
        to: node_type = 0,
        weight: T = Any,
        edge: Optional[Edge] = None,
        directed: bool = True,
    ) -> None:
        if edge:
            from_ = edge.from_
            to = edge.to
            weight = edge.weight
        self.__add_edge(from_, to, weight)
        if not directed and from_ != to:
            self.__add_edge(to, from_, weight)

    def __add_edge(self, from_: node_type, to: node_type, weight: T):
        if (not self.check_range(from_)) or (not self.check_range(to)):
            raise ValueError("Out of range")
        self.m += 1
        self.edges[from_].append(Edge(from_=from_, to=to, weight=weight))
        # x = self.edges[from_].__len__()
        # self.edges[from_][x] = Edge(from_, to, weight)

    def clear(self) -> None:
        self.m = 0
        self.edges.clear()

    def __iter__(self) -> AllEdgeIterator:
        self.it = self.AllEdgeIterator(graph=self, node=self.begin_node)
        return self.it

    def __next__(self) -> AllEdgeIterator:
        return next(self.it)

    def shuffle_nodes(self):
        new_order: List[node_type] = [i for i in range(self.n)]
        shuffle(new_order)
        for i in range(self.begin_node, self.n):
            for e in self.edges[i]:
                e.from_ = new_order[e.from_]
                e.to = new_order[e.to]
        new_edges: List[edge_list] = [list() * self.n] * self.n
        for i in range(self.n):
            new_edges[new_order[i]] = self.edges[i]
        self.edges = new_edges

    U = TypeVar("U", int, float)
    T = TypeVar("T", int, float)

    def dijkstra(self, start: node_type) -> Sequence["Graph.U"]:
        if not self.check_range(start):
            raise IndexError("Out of range")

        @dataclass
        class Dist(Generic[Graph.T]):
            node: node_type
            dist: Graph.T

            def __lt__(self, rhs: "Dist"):
                return self.dist > rhs.dist

        dist: Sequence[Graph.U] = [inf] * self.n
        pq: PriorityQueue = PriorityQueue()
        inq: Sequence[bool] = [bool()] * self.n
        dist[start] = 0
        pq.put(Dist(node=start, dist=0))
        while not pq.empty():
            cur: Dist = pq.get()
            inq[cur.node] = False
            for e in self.edges[cur.node]:
                if dist[e.to] > dist[cur.node] + e.weight:
                    dist[e.to] = dist[cur.node] + e.weight
                    if not inq[e.to]:
                        pq.put(Dist(node=e.to, dist=dist[e.to]))
                        inq[e.to] = True
        return dist

    def is_connected(self, start: node_type) -> bool:
        if not self.check_range(start):
            raise IndexError("Out of range")
        if self.m < self.n - self.begin_node - 1:
            return False
        inq: Sequence[bool] = [False] * self.n
        visited: Sequence[bool] = [False] * self.n
        q: Queue = Queue()
        q.put(start)
        inq[start] = True
        while not q.empty():
            u: node_type = q.get()
            visited[u] = True
            for e in self.edges[u]:
                if not inq[e.to]:
                    q.put(e.to)
                    inq[e.to] = True
        return all(visited[: self.n - self.begin_node])

    def is_tree(self) -> bool:
        if self.m != 2 * (self.n - self.begin_node - 1):
            return False
        visited: Sequence[bool] = []
        q: Queue = Queue()
        visited_count: size_type = 0
        q.put(self.begin_node)
        visited[self.begin_node] = True
        while not q.empty():
            u: node_type = q.get()
            for e in self.edges[u]:
                v = e.to
                if not visited[v]:
                    q.put(v)
                    visited[v] = True
                else:
                    visited_count += 1
        return visited_count == self.n - self.begin_node - 1 and all(
            visited[: self.n - self.begin_node]
        )

    # TODO
    def reachable(self, from_: node_type, to: node_type) -> bool:
        ...

    # TODO
    @property
    def degree(self) -> Sequence[Tuple[size_type, size_type]]:
        ...

    # TODO
    @property
    def udegree(self) -> Sequence[size_type]:
        ...


T = TypeVar("T", int, float)


@dataclass
class GraphGenerateInfo(Generic[T]):
    n: size_type
    m: size_type
    min_weight: T
    max_weight: T
    is_directed: bool = True
    begin_node: size_type = 0
    has_self_loop: bool = True
    has_parallel_edge: bool = True


G = TypeVar("G", bound=Graph)
result_type = Graph[T]


class Generator(Generic[G]):
    def generate(self, info: GraphGenerateInfo, rnd: Random) -> result_type:
        if not info.has_parallel_edge:
            edge_count: size_type = (info.n - info.begin_node) * (
                info.n - info.begin_node
            )
            if info.is_directed:
                edge_count *= 2
            if info.has_self_loop:
                edge_count += info.n - info.begin_node
            if edge_count < info.m:
                raise ValueError("invalid_argument: too many edges")
        g: result_type = result_type(n=info.n, begin_node=info.begin_node)
        generate_node = lambda: rnd.randint(info.begin_node, info.n - 1)
        generate_weight = lambda: rnd.randint(info.min_weight, info.max_weight)
        # TODO: check hashable
        edges: Set[Tuple[node_type, node_type]] = set()

        def check_edge(edge: edge_type) -> bool:
            if not info.has_self_loop and edge.from_ == edge.to:
                return False
            if not info.has_parallel_edge and (
                tuple(edges).count((edge.from_, edge.to))
            ):
                return False
            return True

        def generate_edge() -> edge_type:
            while True:
                e: edge_type = Edge(
                    from_=generate_node(), to=generate_node(), weight=generate_weight()
                )
                if not info.is_directed and e.from_ > e.to:
                    e.from_, e.to = e.to, e.from_
                if check_edge(e):
                    return e

        for _ in range(info.m):
            e = generate_edge()
            g.add_edge(edge=e, directed=info.is_directed)
            edges.add((e.from_, e.to))

        return g
