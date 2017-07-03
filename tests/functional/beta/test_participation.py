# -*- coding: utf-8 -*-
"""Functional tests using WebTest.

See: http://webtest.readthedocs.org/
"""
import pytest
from flex.core import validate_api_call

class TestParticipationEndpoint:
    def test_national_participation_endpoint(self, testapp, swagger_beta):
        res = testapp.get('/participation/national')
        assert res.status_code == 200
        validate_api_call(swagger_beta, raw_request=res.request, raw_response=res)

    def test_state_participation_endpoint(self, testapp, swagger_beta):
        res = testapp.get('/participation/states/NY')
        assert res.status_code == 200
        validate_api_call(swagger_beta, raw_request=res.request, raw_response=res)

        res = testapp.get('/participation/states/ny')
        assert res.status_code == 200

    def test_agencies_endpoint(self, testapp, swagger_beta):
        res = testapp.get('/participation/agencies?year=2014')
        assert res.status_code == 200
        validate_api_call(swagger_beta, raw_request=res.request, raw_response=res)

    @pytest.mark.parametrize('filter,value', [
        ('year', 2014),
        ('state_name', 'Rhode Island'),
        ('state_abbr', 'RI'),
        ('agency_ori', 'RI0010100'),
        ('reported', 0),
        ('nibrs_reported', 0),
    ])
    def test_agencies_endpoint_with_filter(self, testapp, swagger_beta, filter, value):
        res = testapp.get('/participation/agencies?{}={}'.format(filter, value))
        assert res.status_code == 200
        assert res.json['results'][0][filter] == value
        validate_api_call(swagger_beta, raw_request=res.request, raw_response=res)

    @pytest.mark.parametrize('filter,value', [
        ('year', 2014),
        ('months_reported', 12),
        ('nibrs_months_reported', 0)
    ])
    def test_agencies_endpoint_with_filter_comparison(self, testapp, swagger_beta, filter, value):
        res = testapp.get('/participation/agencies?{}<={}'.format(filter, value))
        assert res.status_code == 200
        assert int(res.json['results'][0][filter]) <= value
        validate_api_call(swagger_beta, raw_request=res.request, raw_response=res)

        res = testapp.get('/participation/agencies?{}={}'.format(filter, value))
        assert res.status_code == 200
        assert int(res.json['results'][0][filter]) == value
        validate_api_call(swagger_beta, raw_request=res.request, raw_response=res)

        res = testapp.get('/participation/agencies?{}>={}'.format(filter, value))
        assert res.status_code == 200
        assert int(res.json['results'][0][filter]) >= value
        validate_api_call(swagger_beta, raw_request=res.request, raw_response=res)
