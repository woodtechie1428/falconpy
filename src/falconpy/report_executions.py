"""
 _______                        __ _______ __        __ __
|   _   .----.-----.--.--.--.--|  |   _   |  |_.----|__|  |--.-----.
|.  1___|   _|  _  |  |  |  |  _  |   1___|   _|   _|  |    <|  -__|
|.  |___|__| |_____|________|_____|____   |____|__| |__|__|__|_____|
|:  1   |                         |:  1   |
|::.. . |   CROWDSTRIKE FALCON    |::.. . |    FalconPy
`-------'                         `-------'

OAuth2 API - Customer SDK

report_executions - Falcon Report Executions API Interface Class

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
from ._util import force_default, process_service_request, handle_single_argument
from ._service_class import ServiceClass
from ._endpoint._report_executions import _report_executions_endpoints as Endpoints


class ReportExecutions(ServiceClass):
    """
    The only requirement to instantiate an instance of this class
    is a valid token provided by the Falcon API SDK OAuth2 class, an
    authorization object (oauth2.py) or a credential dictionary with
    client_id and client_secret containing valid API credentials.
    """
    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_download(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Get report entity download
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#
        #           /report-executions/report-executions-download.get
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="report_executions_download_get",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def get_reports(self: object, *args, parameters: dict = None, **kwargs) -> dict:
        """
        Retrieve report details for the provided report IDs.
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/report-executions/report-executions.get
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="report_executions_get",
            keywords=kwargs,
            params=handle_single_argument(args, parameters, "ids")
            )

    @force_default(defaults=["parameters"], default_types=["dict"])
    def query_reports(self: object, parameters: dict = None, **kwargs) -> dict:
        """
        Find all report execution IDs matching the query with filter
        """
        # [GET] https://assets.falcon.crowdstrike.com/support/api/swagger.html#/report-executions/report-executions.query
        return process_service_request(
            calling_object=self,
            endpoints=Endpoints,
            operation_id="report_executions_query",
            keywords=kwargs,
            params=parameters
            )

    # These method names align to the operation ID in the
    # API and are defined here for ease of use purposes
    report_executions_download_get = get_download
    report_executions_get = get_reports
    scheduled_reports_query = query_reports
