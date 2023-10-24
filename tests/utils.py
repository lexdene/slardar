async def simple_func(num: int) -> str:
    sequence = 'Elephant_Liu'

    return sequence[num % len(sequence)]
