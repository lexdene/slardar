from asyncio import gather
from typing import TypeVar
from collections.abc import Callable, Awaitable, Iterable

InputType = TypeVar('InputType')
OutputType = TypeVar('OutputType')
NormalFunc = Callable[[InputType], Awaitable[OutputType]]


async def map_and_gather(
    func: NormalFunc[InputType, OutputType], input_data: Iterable[InputType]
) -> Iterable[Awaitable[OutputType]]:
    return await gather(*[
        func(i)
        for i in input_data
    ])
