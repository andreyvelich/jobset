# coding: utf-8

"""
    JobSet SDK

    Python SDK for the JobSet API

    The version of the OpenAPI document: v0.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from jobset.models.io_k8s_api_batch_v1_success_policy import IoK8sApiBatchV1SuccessPolicy

class TestIoK8sApiBatchV1SuccessPolicy(unittest.TestCase):
    """IoK8sApiBatchV1SuccessPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IoK8sApiBatchV1SuccessPolicy:
        """Test IoK8sApiBatchV1SuccessPolicy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IoK8sApiBatchV1SuccessPolicy`
        """
        model = IoK8sApiBatchV1SuccessPolicy()
        if include_optional:
            return IoK8sApiBatchV1SuccessPolicy(
                rules = [
                    jobset.models.io/k8s/api/batch/v1/success_policy_rule.io.k8s.api.batch.v1.SuccessPolicyRule(
                        succeeded_count = 56, 
                        succeeded_indexes = '', )
                    ]
            )
        else:
            return IoK8sApiBatchV1SuccessPolicy(
                rules = [
                    jobset.models.io/k8s/api/batch/v1/success_policy_rule.io.k8s.api.batch.v1.SuccessPolicyRule(
                        succeeded_count = 56, 
                        succeeded_indexes = '', )
                    ],
        )
        """

    def testIoK8sApiBatchV1SuccessPolicy(self):
        """Test IoK8sApiBatchV1SuccessPolicy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
