from dataclasses import dataclass


@dataclass
class NumberNode:
    value: float

    def __repr__(self) -> str:
        return f"{self.value}"


@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f"({self.node_a}+{self.node_b})"


@dataclass
class SubstractNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f"({self.node_a}-{self.node_b})"


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f"({self.node_a}*{self.node_b})"


@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self) -> str:
        return f"({self.node_a}/{self.node_b})"


@dataclass
class PlusNode:
    node: any

    def __repr__(self) -> str:
        return f"(+{self.node})"


@dataclass
class MinusNode:
    node: any

    def __repr__(self) -> str:
        return f"(-{self.node})"

@dataclass
class FactorialNode:
    node: any

    def __repr__(self) -> str:
        return f"({self.node}!)"