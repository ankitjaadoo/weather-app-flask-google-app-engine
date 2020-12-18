# Copyright 2020 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from googlecloudsdk.third_party.logging_v2.proto import logging_pb2 as googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2


class LoggingServiceV2Stub(object):
  """Service for ingesting and querying logs.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DeleteLog = channel.unary_unary(
        '/google.logging.v2.LoggingServiceV2/DeleteLog',
        request_serializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.DeleteLogRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.WriteLogEntries = channel.unary_unary(
        '/google.logging.v2.LoggingServiceV2/WriteLogEntries',
        request_serializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.WriteLogEntriesRequest.SerializeToString,
        response_deserializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.WriteLogEntriesResponse.FromString,
        )
    self.ListLogEntries = channel.unary_unary(
        '/google.logging.v2.LoggingServiceV2/ListLogEntries',
        request_serializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.ListLogEntriesRequest.SerializeToString,
        response_deserializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.ListLogEntriesResponse.FromString,
        )
    self.ListMonitoredResourceDescriptors = channel.unary_unary(
        '/google.logging.v2.LoggingServiceV2/ListMonitoredResourceDescriptors',
        request_serializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.ListMonitoredResourceDescriptorsRequest.SerializeToString,
        response_deserializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.ListMonitoredResourceDescriptorsResponse.FromString,
        )
    self.ListLogs = channel.unary_unary(
        '/google.logging.v2.LoggingServiceV2/ListLogs',
        request_serializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.ListLogsRequest.SerializeToString,
        response_deserializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.ListLogsResponse.FromString,
        )
    self.TailLogEntries = channel.stream_stream(
        '/google.logging.v2.LoggingServiceV2/TailLogEntries',
        request_serializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.TailLogEntriesRequest.SerializeToString,
        response_deserializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.TailLogEntriesResponse.FromString,
        )


class LoggingServiceV2Servicer(object):
  """Service for ingesting and querying logs.
  """

  def DeleteLog(self, request, context):
    """Deletes all the log entries in a log. The log reappears if it receives new
    entries. Log entries written shortly before the delete operation might not
    be deleted. Entries received after the delete operation with a timestamp
    before the operation will be deleted.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def WriteLogEntries(self, request, context):
    """Writes log entries to Logging. This API method is the
    only way to send log entries to Logging. This method
    is used, directly or indirectly, by the Logging agent
    (fluentd) and all logging libraries configured to use Logging.
    A single request may contain log entries for a maximum of 1000
    different resources (projects, organizations, billing accounts or
    folders)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListLogEntries(self, request, context):
    """Lists log entries.  Use this method to retrieve log entries that originated
    from a project/folder/organization/billing account.  For ways to export log
    entries, see [Exporting
    Logs](https://cloud.google.com/logging/docs/export).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListMonitoredResourceDescriptors(self, request, context):
    """Lists the descriptors for monitored resource types used by Logging.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListLogs(self, request, context):
    """Lists the logs in projects, organizations, folders, or billing accounts.
    Only logs that have entries are listed.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TailLogEntries(self, request_iterator, context):
    """Streaming read of log entries as they are ingested. Until the stream is
    terminated, it will continue reading logs.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LoggingServiceV2Servicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DeleteLog': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteLog,
          request_deserializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.DeleteLogRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'WriteLogEntries': grpc.unary_unary_rpc_method_handler(
          servicer.WriteLogEntries,
          request_deserializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.WriteLogEntriesRequest.FromString,
          response_serializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.WriteLogEntriesResponse.SerializeToString,
      ),
      'ListLogEntries': grpc.unary_unary_rpc_method_handler(
          servicer.ListLogEntries,
          request_deserializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.ListLogEntriesRequest.FromString,
          response_serializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.ListLogEntriesResponse.SerializeToString,
      ),
      'ListMonitoredResourceDescriptors': grpc.unary_unary_rpc_method_handler(
          servicer.ListMonitoredResourceDescriptors,
          request_deserializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.ListMonitoredResourceDescriptorsRequest.FromString,
          response_serializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.ListMonitoredResourceDescriptorsResponse.SerializeToString,
      ),
      'ListLogs': grpc.unary_unary_rpc_method_handler(
          servicer.ListLogs,
          request_deserializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.ListLogsRequest.FromString,
          response_serializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.ListLogsResponse.SerializeToString,
      ),
      'TailLogEntries': grpc.stream_stream_rpc_method_handler(
          servicer.TailLogEntries,
          request_deserializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.TailLogEntriesRequest.FromString,
          response_serializer=googlecloudsdk_dot_third__party_dot_logging__v2_dot_proto_dot_logging__pb2.TailLogEntriesResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.logging.v2.LoggingServiceV2', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
