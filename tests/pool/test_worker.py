from asyncio import get_running_loop
from unittest import IsolatedAsyncioTestCase

from slardar.utils import map_and_gather
from slardar.pool import WorkerBase, run_worker_in_pool
from ..utils import simple_func


class PrefixWorker(WorkerBase[int, str]):
    def __init__(self) -> None:
        self.prefix = 'hello '

    async def handle(self, job: int) -> str:
        r = await simple_func(job)
        return self.prefix + r


class TestWorkerPool(IsolatedAsyncioTestCase):
    async def test_simple(self) -> None:
        loop = get_running_loop()
        func = run_worker_in_pool(
            worker_cls=PrefixWorker,
            max_worker_count=10,
            loop=loop
        )

        it = await map_and_gather(
            func,
            list(range(20))
        )
        r = list(it)

        self.assertEqual(len(r), 20)
        self.assertEqual(r[15], 'hello p')
