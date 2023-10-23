from unittest import IsolatedAsyncioTestCase

from slardar.utils import map_and_gather


async def simple_func(num: int) -> str:
    sequence = 'elephant_liu'

    return sequence[num % len(sequence)]


class TestMap(IsolatedAsyncioTestCase):
    async def test_map(self) -> None:
        r = await map_and_gather(
            simple_func,
            [3, 6, 9]
        )

        self.assertEqual(r, ['p', 'n', 'l'])
