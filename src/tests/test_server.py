import sys
from src.conftest import process_snapshot
sys.path.append("..")
from typing import List
from src.services import GetNewsUrls
import pytest
from pytest_snapshot.plugin import Snapshot

@pytest.mark.asyncio
async def test_process_article(snapshot: Snapshot):
    result = await GetNewsUrls.GetUrls().get_urls()
    print(f'result is ', result)
    assert isinstance(result, List)
    file_name = 'urls'
    process_snapshot(file_name, snapshot, ''.join(result))
