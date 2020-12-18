"""Generated client library for servicenetworking version v1beta."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.servicenetworking.v1beta import servicenetworking_v1beta_messages as messages


class ServicenetworkingV1beta(base_api.BaseApiClient):
  """Generated client library for service servicenetworking version v1beta."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://servicenetworking.googleapis.com/'
  MTLS_BASE_URL = ''

  _PACKAGE = 'servicenetworking'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform', 'https://www.googleapis.com/auth/service.management']
  _VERSION = 'v1beta'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'ServicenetworkingV1beta'
  _URL_VERSION = 'v1beta'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new servicenetworking handle."""
    url = url or self.BASE_URL
    super(ServicenetworkingV1beta, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.operations = self.OperationsService(self)
    self.services_connections = self.ServicesConnectionsService(self)
    self.services = self.ServicesService(self)

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = 'operations'

    def __init__(self, client):
      super(ServicenetworkingV1beta.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (ServicenetworkingOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/operations/{operationsId}',
        http_method='GET',
        method_id='servicenetworking.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta/{+name}',
        request_field='',
        request_type_name='ServicenetworkingOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ServicesConnectionsService(base_api.BaseApiService):
    """Service class for the services_connections resource."""

    _NAME = 'services_connections'

    def __init__(self, client):
      super(ServicenetworkingV1beta.ServicesConnectionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""To connect service to a VPC network peering connection.
must be established prior to service provisioning.
This method must be invoked by the consumer VPC network administrator
It will establish a permanent peering connection with a shared
network created in the service producer organization and register a
reserved IP range(s) to be used for service subnetwork provisioning.
This connection will be used for all supported services in the service
producer organization, so it only needs to be invoked once.
Operation<response: Connection>.

      Args:
        request: (ServicenetworkingServicesConnectionsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/services/{servicesId}/connections',
        http_method='POST',
        method_id='servicenetworking.services.connections.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1beta/{+parent}/connections',
        request_field='connection',
        request_type_name='ServicenetworkingServicesConnectionsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Service consumer use this method to list configured peering connection for.
the given service and consumer network.

      Args:
        request: (ServicenetworkingServicesConnectionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListConnectionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/services/{servicesId}/connections',
        http_method='GET',
        method_id='servicenetworking.services.connections.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['network'],
        relative_path='v1beta/{+parent}/connections',
        request_field='',
        request_type_name='ServicenetworkingServicesConnectionsListRequest',
        response_type_name='ListConnectionsResponse',
        supports_download=False,
    )

  class ServicesService(base_api.BaseApiService):
    """Service class for the services resource."""

    _NAME = 'services'

    def __init__(self, client):
      super(ServicenetworkingV1beta.ServicesService, self).__init__(client)
      self._upload_configs = {
          }

    def AddSubnetwork(self, request, global_params=None):
      r"""Service producers use this method to provision a new subnet in.
peered service shared VPC network.
It will validate previously provided reserved ranges, find
non-conflicting sub-range of requested size (expressed in
number of leading bits of ipv4 network mask, as in CIDR range
notation). It will then create a subnetwork in the request
region. Operation<response: Subnetwork>

      Args:
        request: (ServicenetworkingServicesAddSubnetworkRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('AddSubnetwork')
      return self._RunMethod(
          config, request, global_params=global_params)

    AddSubnetwork.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta/services/{servicesId}/{servicesId1}/{servicesId2}:addSubnetwork',
        http_method='POST',
        method_id='servicenetworking.services.addSubnetwork',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1beta/{+parent}:addSubnetwork',
        request_field='addSubnetworkRequest',
        request_type_name='ServicenetworkingServicesAddSubnetworkRequest',
        response_type_name='Operation',
        supports_download=False,
    )
