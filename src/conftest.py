import sys
import os
from os.path import dirname, abspath

from pytest_snapshot.plugin import Snapshot
sys.path.append("./src")
sys.path.append("./src/proto")
import asyncio
import pytest
from google.protobuf.json_format import MessageToDict
import json
sys.path.append("./src")
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

def process_snapshot(file_name: str, snapshot: Snapshot, result):
    snapshot.snapshot_dir = (
        f"{dirname(dirname(abspath(__file__)))}/snapshot"
    )
    snapshot.assert_match(''.join(result), f"{file_name}.txt")


@pytest.yield_fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()