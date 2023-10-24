from unittest import IsolatedAsyncioTestCase

from slardar.utils import map_and_gather
from .utils import simple_func


class TestMap(IsolatedAsyncioTestCase):
    async def test_map(self) -> None:
        r = await map_and_gather(
            simple_func,
            [3, 6, 9]
        )

        self.assertEqual(r, ['p', 'n', 'L'])
