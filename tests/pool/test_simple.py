from asyncio import get_running_loop
from unittest import IsolatedAsyncioTestCase

from slardar.utils import map_and_gather
from slardar.pool import run_in_pool
from ..utils import simple_func


class TestSimplePool(IsolatedAsyncioTestCase):
    async def test_simple(self) -> None:
        loop = get_running_loop()
        pooled_func = run_in_pool(
            max_worker_count=10,
            loop=loop
        )(
            simple_func
        )

        it = await map_and_gather(
            pooled_func,
            list(range(20))
        )
        r = list(it)

        self.assertEqual(len(r), 20)
        self.assertEqual(r[15], 'p')
