# coding: utf-8

"""
    Thingsboard REST API

    For instructions how to authorize requests please visit <a href='http://thingsboard.io/docs/reference/rest-api/'>REST API documentation page</a>.

    OpenAPI spec version: 2.0
    Contact: info@thingsboard.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.customer_controller_api import CustomerControllerApi


class TestCustomerControllerApi(unittest.TestCase):
    """ CustomerControllerApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.customer_controller_api.CustomerControllerApi()

    def tearDown(self):
        pass

    def test_delete_customer_using_delete(self):
        """
        Test case for delete_customer_using_delete

        deleteCustomer
        """
        pass

    def test_get_customer_by_id_using_get(self):
        """
        Test case for get_customer_by_id_using_get

        getCustomerById
        """
        pass

    def test_get_customer_title_by_id_using_get(self):
        """
        Test case for get_customer_title_by_id_using_get

        getCustomerTitleById
        """
        pass

    def test_get_customers_using_get(self):
        """
        Test case for get_customers_using_get

        getCustomers
        """
        pass

    def test_get_short_customer_info_by_id_using_get(self):
        """
        Test case for get_short_customer_info_by_id_using_get

        getShortCustomerInfoById
        """
        pass

    def test_save_customer_using_post(self):
        """
        Test case for save_customer_using_post

        saveCustomer
        """
        pass


if __name__ == '__main__':
    unittest.main()