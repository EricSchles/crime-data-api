# -*- coding: utf-8 -*-
"""Functional tests using WebTest.

See: http://webtest.readthedocs.org/
"""

import pytest
from flex.core import validate_api_call


class TestEstimatesEndpoint:
    def test_national_estimates(self, testapp, swagger):
        res = testapp.get('/estimates/national?per_page=100')
        assert res.status_code == 200
        validate_api_call(swagger, raw_request=res.request, raw_response=res)
        assert len(res.json['results']) > 0

    def test_state_estimates(self, testapp, swagger):
        res = testapp.get('/estimates/states/NE?per_page=100')
        assert res.status_code == 200
        validate_api_call(swagger, raw_request=res.request, raw_response=res)
        assert len(res.json['results']) > 0

    def test_state_estimates_lowercase(self, testapp, swagger):
        res = testapp.get('/estimates/states/ne?per_page=100')
        assert res.status_code == 200
        validate_api_call(swagger, raw_request=res.request, raw_response=res)
        assert len(res.json['results']) > 0
