from typing import Union, List
from src.tokens import Token


class Stack:

    def __init__(self) -> None:
        self.stack: List[Token] = []

    def push(self, element: Token) -> None:
        self.stack.append(element)

    def inverse(self) -> None:
        self.stack = self.stack[::-1]

    def pop_(self) -> Union[Token, None]:
        if self.stack:
            return self.stack.pop()

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def get_len(self) -> int:
        return len(self.stack)

    def top_element(self) -> Union[Token, None]:
        if len(self.stack) != 0:
            return self.stack[-1]

    def __repr__(self) -> str:
        return str(self.stack)
