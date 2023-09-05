import json
import os

import jsonschema_rs
import requests
from enums import PRODUCT_STATS_RESPONSE_SCHEMA_JSON, DELIVERY_INFO_RESPONSE_SCHEMA_JSON

__author__ = "UniCourt Inc"
__version__ = "v1.0.0"
__maintainer__ = "Search - Core & API"
__email__ = "eng-search@unicourt.com"


class TestApi:
    """
    This class should have all test methods
    """

    def test_product_stats(self):
        """
        Checks whether ProductStats API returns valid response with status code 200
        :return:
        """
        headers = {"Content-Type": "application/json"}
        post_data = {'product_id': 'e83ded7d97b96d338c4e72bb1ff7676c'}
        response = requests.post(url=f'http://{os.environ["API_HOST"]}:5000/ProductStats',
                                 headers=headers,
                                 data=json.dumps(post_data))

        assert response.status_code == 200

        validator = jsonschema_rs.JSONSchema(PRODUCT_STATS_RESPONSE_SCHEMA_JSON)
        assert validator.is_valid(response.json())

    def test_delivery_info(self):
        """
        Checks whether DeliveryInfo API returns valid response with status code 200
        :return:
        """
        headers = {"Content-Type": "application/json"}
        post_data = {'order_id': '47770eb9100c2d0c44946d9cf07ec65d'}
        response = requests.post(url=f'http://{os.environ["API_HOST"]}:5000/DeliveryInfo',
                                 headers=headers,
                                 data=json.dumps(post_data))

        assert response.status_code == 200

        validator = jsonschema_rs.JSONSchema(DELIVERY_INFO_RESPONSE_SCHEMA_JSON)
        assert validator.is_valid(response.json())
