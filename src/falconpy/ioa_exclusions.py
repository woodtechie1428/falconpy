"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

ioa_exclusions - Falcon Machine Learning Exclusions API Interface Class

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""
# pylint: disable=C0103  # Aligning method names to API operation IDs
from ._util import service_request, force_default, args_to_params
from ._service_class import ServiceClass
from ._endpoint._ioa_exclusions import _ioa_exclusions_endpoints as Endpoints


class IOA_Exclusions(ServiceClass):
    """The only requirement to instantiate an instance of this class
       is a valid token provided by the Falcon API SDK OAuth2 class, a
       existing instance of the authentication class as an object or a
       valid set of credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def getIOAExclusionsV1(self: object, parameters: dict = None, **kwargs) -> dict:
        """Get a set of IOA Exclusions by specifying their IDs"""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/getIOAExclusionsV1
        # id_list = str(parse_id_list(ids)).replace(",", "&ids=")
        # target_url = f"{self.base_url}/policy/entities/ioa-exclusions/v1?ids={id_list}"
        operation_id = "getIOAExclusionsV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def createIOAExclusionsV1(self: object, body: dict) -> dict:
        """Create the IOA exclusions"""
        # [POST] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/createIOAExclusionsV1
        operation_id = "createIOAExclusionsV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="POST",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def deleteIOAExclusionsV1(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103
        """Delete the IOA Exclusions by ID."""
        # [DELETE] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/deleteIOAExclusionsV1
        operation_id = "deleteIOAExclusionsV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="DELETE",
                                   endpoint=target_url,
                                   params=parameter_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    def updateIOAExclusionsV1(self: object, body: dict) -> dict:
        """Update the IOA Exclusions"""
        # [PATCH] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/updateIOAExclusionsV1
        operation_id = "updateIOAExclusionsV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}".replace("?ids={}", "")
        header_payload = self.headers
        body_payload = body
        returned = service_request(caller=self,
                                   method="PATCH",
                                   endpoint=target_url,
                                   body=body_payload,
                                   headers=header_payload,
                                   verify=self.ssl_verify
                                   )
        return returned

    @force_default(defaults=["parameters"], default_types=["dict"])
    def queryIOAExclusionsV1(self: object, parameters: dict = None, **kwargs) -> dict:  # pylint: disable=C0103
        """Search for IOA Exclusions."""
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/ioa-exclusions/queryIOAExclusionsV1
        operation_id = "queryIOAExclusionsV1"
        target_url = f"{self.base_url}{[ep[2] for ep in Endpoints if operation_id in ep[0]][0]}"
        header_payload = self.headers
        parameter_payload = args_to_params(parameters, kwargs, Endpoints, operation_id)
        returned = service_request(caller=self,
                                   method="GET",
                                   endpoint=target_url,
                                   headers=header_payload,
                                   params=parameter_payload,
                                   verify=self.ssl_verify
                                   )
        return returned
