# (C) Datadog, Inc. 2010-2017
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

import random

from requests import HTTPError

from datadog_checks.checks import AgentCheck
from datadog_checks.utils.containers import hash_mutable

@pytest.fixture
def aggregator():
    from datadog_checks.stubs import aggregator
    aggregator.reset()
    return aggregator


def test_get_nodes_with_service(monkeypatch):
    check = AgentCheck
