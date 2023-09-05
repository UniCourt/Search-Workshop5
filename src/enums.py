__author__ = "UniCourt Inc"
__version__ = "v1.0.0"
__maintainer__ = "Search - Core & API"
__email__ = "eng-search@unicourt.com"

PRODUCT_STATS_RESPONSE_SCHEMA_JSON = {
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "OrderStats": {
                    "type": "object",
                    "properties": {
                        "maxPrice": {
                            "type": "number"
                        },
                        "minPrice": {
                            "type": "number"
                        },
                        "orderCount": {
                            "type": "integer"
                        }
                    },
                    "required": [
                        "maxPrice",
                        "minPrice",
                        "orderCount"
                    ]
                },
                "productCategory": {
                    "type": "string"
                },
                "productId": {
                    "type": "string"
                }
            },
            "required": [
                "OrderStats",
                "productCategory",
                "productId"
            ]
        },
        "message": {
            "type": "string"
        },
        "status": {
            "type": "string"
        }
    },
    "required": [
        "data",
        "message",
        "status"
    ]
}

DELIVERY_INFO_RESPONSE_SCHEMA_JSON = {
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "customer_city": {
                    "type": "string"
                },
                "customer_id": {
                    "type": "string"
                },
                "customer_state": {
                    "type": "string"
                },
                "customer_zip_code_prefix": {
                    "type": "integer"
                },
                "order_approved_at": {
                    "type": "string"
                },
                "order_delivered_carrier_date": {
                    "type": "string"
                },
                "order_delivered_customer_date": {
                    "type": "string"
                },
                "order_id": {
                    "type": "string"
                },
                "order_purchase_timestamp": {
                    "type": "string"
                },
                "order_status": {
                    "type": "string"
                }
            },
            "required": [
                "customer_city",
                "customer_id",
                "customer_state",
                "customer_zip_code_prefix",
                "order_approved_at",
                "order_delivered_carrier_date",
                "order_delivered_customer_date",
                "order_id",
                "order_purchase_timestamp",
                "order_status"
            ]
        },
        "message": {
            "type": "string"
        },
        "status": {
            "type": "string"
        }
    },
    "required": [
        "data",
        "message",
        "status"
    ]
}
