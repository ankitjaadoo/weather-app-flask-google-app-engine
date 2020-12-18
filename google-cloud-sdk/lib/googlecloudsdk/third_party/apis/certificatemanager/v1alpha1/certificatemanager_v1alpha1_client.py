"""Generated client library for certificatemanager version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.certificatemanager.v1alpha1 import certificatemanager_v1alpha1_messages as messages


class CertificatemanagerV1alpha1(base_api.BaseApiClient):
  """Generated client library for service certificatemanager version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://certificatemanager.googleapis.com/'
  MTLS_BASE_URL = 'https://certificatemanager.mtls.googleapis.com/'

  _PACKAGE = 'certificatemanager'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'CertificatemanagerV1alpha1'
  _URL_VERSION = 'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new certificatemanager handle."""
    url = url or self.BASE_URL
    super(CertificatemanagerV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_certificateMaps_certificateMapEntries = self.ProjectsLocationsCertificateMapsCertificateMapEntriesService(self)
    self.projects_locations_certificateMaps = self.ProjectsLocationsCertificateMapsService(self)
    self.projects_locations_certificates = self.ProjectsLocationsCertificatesService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsCertificateMapsCertificateMapEntriesService(base_api.BaseApiService):
    """Service class for the projects_locations_certificateMaps_certificateMapEntries resource."""

    _NAME = 'projects_locations_certificateMaps_certificateMapEntries'

    def __init__(self, client):
      super(CertificatemanagerV1alpha1.ProjectsLocationsCertificateMapsCertificateMapEntriesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new CertificateMapEntry in a given project and location.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificateMapsCertificateMapEntriesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificateMaps/{certificateMapsId}/certificateMapEntries',
        http_method='POST',
        method_id='certificatemanager.projects.locations.certificateMaps.certificateMapEntries.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['certificateMapEntryId'],
        relative_path='v1alpha1/{+parent}/certificateMapEntries',
        request_field='certificateMapEntry',
        request_type_name='CertificatemanagerProjectsLocationsCertificateMapsCertificateMapEntriesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single CertificateMapEntry.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificateMapsCertificateMapEntriesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificateMaps/{certificateMapsId}/certificateMapEntries/{certificateMapEntriesId}',
        http_method='DELETE',
        method_id='certificatemanager.projects.locations.certificateMaps.certificateMapEntries.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='CertificatemanagerProjectsLocationsCertificateMapsCertificateMapEntriesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single CertificateMapEntry.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificateMapsCertificateMapEntriesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CertificateMapEntry) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificateMaps/{certificateMapsId}/certificateMapEntries/{certificateMapEntriesId}',
        http_method='GET',
        method_id='certificatemanager.projects.locations.certificateMaps.certificateMapEntries.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='CertificatemanagerProjectsLocationsCertificateMapsCertificateMapEntriesGetRequest',
        response_type_name='CertificateMapEntry',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists CertificateMapEntries in a given project and location.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificateMapsCertificateMapEntriesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListCertificateMapEntriesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificateMaps/{certificateMapsId}/certificateMapEntries',
        http_method='GET',
        method_id='certificatemanager.projects.locations.certificateMaps.certificateMapEntries.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+parent}/certificateMapEntries',
        request_field='',
        request_type_name='CertificatemanagerProjectsLocationsCertificateMapsCertificateMapEntriesListRequest',
        response_type_name='ListCertificateMapEntriesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a CertificateMapEntry.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificateMapsCertificateMapEntriesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificateMaps/{certificateMapsId}/certificateMapEntries/{certificateMapEntriesId}',
        http_method='PATCH',
        method_id='certificatemanager.projects.locations.certificateMaps.certificateMapEntries.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1alpha1/{+name}',
        request_field='certificateMapEntry',
        request_type_name='CertificatemanagerProjectsLocationsCertificateMapsCertificateMapEntriesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsCertificateMapsService(base_api.BaseApiService):
    """Service class for the projects_locations_certificateMaps resource."""

    _NAME = 'projects_locations_certificateMaps'

    def __init__(self, client):
      super(CertificatemanagerV1alpha1.ProjectsLocationsCertificateMapsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new CertificateMap in a given project and location.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificateMapsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificateMaps',
        http_method='POST',
        method_id='certificatemanager.projects.locations.certificateMaps.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['certificateMapId'],
        relative_path='v1alpha1/{+parent}/certificateMaps',
        request_field='certificateMap',
        request_type_name='CertificatemanagerProjectsLocationsCertificateMapsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single CertificateMap. A Certificate Map can't be deleted if it contains Certificate Map Entries. Remove all the entries from the map before calling this method.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificateMapsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificateMaps/{certificateMapsId}',
        http_method='DELETE',
        method_id='certificatemanager.projects.locations.certificateMaps.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='CertificatemanagerProjectsLocationsCertificateMapsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single CertificateMap.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificateMapsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (CertificateMap) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificateMaps/{certificateMapsId}',
        http_method='GET',
        method_id='certificatemanager.projects.locations.certificateMaps.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='CertificatemanagerProjectsLocationsCertificateMapsGetRequest',
        response_type_name='CertificateMap',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists CertificateMaps in a given project and location.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificateMapsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListCertificateMapsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificateMaps',
        http_method='GET',
        method_id='certificatemanager.projects.locations.certificateMaps.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+parent}/certificateMaps',
        request_field='',
        request_type_name='CertificatemanagerProjectsLocationsCertificateMapsListRequest',
        response_type_name='ListCertificateMapsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a CertificateMap.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificateMapsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificateMaps/{certificateMapsId}',
        http_method='PATCH',
        method_id='certificatemanager.projects.locations.certificateMaps.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1alpha1/{+name}',
        request_field='certificateMap',
        request_type_name='CertificatemanagerProjectsLocationsCertificateMapsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsCertificatesService(base_api.BaseApiService):
    """Service class for the projects_locations_certificates resource."""

    _NAME = 'projects_locations_certificates'

    def __init__(self, client):
      super(CertificatemanagerV1alpha1.ProjectsLocationsCertificatesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Certificate in a given project and location.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificatesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificates',
        http_method='POST',
        method_id='certificatemanager.projects.locations.certificates.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['certificateId'],
        relative_path='v1alpha1/{+parent}/certificates',
        request_field='certificate',
        request_type_name='CertificatemanagerProjectsLocationsCertificatesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Certificate.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificatesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificates/{certificatesId}',
        http_method='DELETE',
        method_id='certificatemanager.projects.locations.certificates.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='CertificatemanagerProjectsLocationsCertificatesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Certificate.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificatesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Certificate) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificates/{certificatesId}',
        http_method='GET',
        method_id='certificatemanager.projects.locations.certificates.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='CertificatemanagerProjectsLocationsCertificatesGetRequest',
        response_type_name='Certificate',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificatesGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificates/{certificatesId}:getIamPolicy',
        http_method='GET',
        method_id='certificatemanager.projects.locations.certificates.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=['options_requestedPolicyVersion'],
        relative_path='v1alpha1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name='CertificatemanagerProjectsLocationsCertificatesGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists Certificates in a given project and location.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificatesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListCertificatesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificates',
        http_method='GET',
        method_id='certificatemanager.projects.locations.certificates.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+parent}/certificates',
        request_field='',
        request_type_name='CertificatemanagerProjectsLocationsCertificatesListRequest',
        response_type_name='ListCertificatesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates a Certificate.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificatesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificates/{certificatesId}',
        http_method='PATCH',
        method_id='certificatemanager.projects.locations.certificates.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1alpha1/{+name}',
        request_field='certificate',
        request_type_name='CertificatemanagerProjectsLocationsCertificatesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificatesSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificates/{certificatesId}:setIamPolicy',
        http_method='POST',
        method_id='certificatemanager.projects.locations.certificates.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1alpha1/{+resource}:setIamPolicy',
        request_field='setIamPolicyRequest',
        request_type_name='CertificatemanagerProjectsLocationsCertificatesSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

      Args:
        request: (CertificatemanagerProjectsLocationsCertificatesTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/certificates/{certificatesId}:testIamPermissions',
        http_method='POST',
        method_id='certificatemanager.projects.locations.certificates.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1alpha1/{+resource}:testIamPermissions',
        request_field='testIamPermissionsRequest',
        request_type_name='CertificatemanagerProjectsLocationsCertificatesTestIamPermissionsRequest',
        response_type_name='TestIamPermissionsResponse',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(CertificatemanagerV1alpha1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (CertificatemanagerProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='certificatemanager.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='CertificatemanagerProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (CertificatemanagerProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='certificatemanager.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='CertificatemanagerProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (CertificatemanagerProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='certificatemanager.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='CertificatemanagerProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/*/operations`. To override the binding, API services can add a binding such as `"/v1/{name=users/*}/operations"` to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

      Args:
        request: (CertificatemanagerProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='certificatemanager.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+name}/operations',
        request_field='',
        request_type_name='CertificatemanagerProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(CertificatemanagerV1alpha1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (CertificatemanagerProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='certificatemanager.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='CertificatemanagerProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (CertificatemanagerProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='certificatemanager.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'includeUnrevealedLocations', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+name}/locations',
        request_field='',
        request_type_name='CertificatemanagerProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(CertificatemanagerV1alpha1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
