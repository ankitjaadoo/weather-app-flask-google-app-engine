# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/appengine_v1beta/proto/firewall.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/appengine_v1beta/proto/firewall.proto',
  package='google.appengine.v1beta',
  syntax='proto3',
  serialized_options=b'\n$com.google.appengine.v1beta.firewallB\rFirewallProtoP\001Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengine',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n2google/cloud/appengine_v1beta/proto/firewall.proto\x12\x17google.appengine.v1beta\x1a\x1cgoogle/api/annotations.proto\"\xc0\x01\n\x0c\x46irewallRule\x12\x10\n\x08priority\x18\x01 \x01(\x05\x12<\n\x06\x61\x63tion\x18\x02 \x01(\x0e\x32,.google.appengine.v1beta.FirewallRule.Action\x12\x14\n\x0csource_range\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\"5\n\x06\x41\x63tion\x12\x16\n\x12UNSPECIFIED_ACTION\x10\x00\x12\t\n\x05\x41LLOW\x10\x01\x12\x08\n\x04\x44\x45NY\x10\x02\x42y\n$com.google.appengine.v1beta.firewallB\rFirewallProtoP\x01Z@google.golang.org/genproto/googleapis/appengine/v1beta;appengineb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_FIREWALLRULE_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='google.appengine.v1beta.FirewallRule.Action',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED_ACTION', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ALLOW', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DENY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=249,
  serialized_end=302,
)
_sym_db.RegisterEnumDescriptor(_FIREWALLRULE_ACTION)


_FIREWALLRULE = _descriptor.Descriptor(
  name='FirewallRule',
  full_name='google.appengine.v1beta.FirewallRule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='priority', full_name='google.appengine.v1beta.FirewallRule.priority', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='action', full_name='google.appengine.v1beta.FirewallRule.action', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source_range', full_name='google.appengine.v1beta.FirewallRule.source_range', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='google.appengine.v1beta.FirewallRule.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FIREWALLRULE_ACTION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=110,
  serialized_end=302,
)

_FIREWALLRULE.fields_by_name['action'].enum_type = _FIREWALLRULE_ACTION
_FIREWALLRULE_ACTION.containing_type = _FIREWALLRULE
DESCRIPTOR.message_types_by_name['FirewallRule'] = _FIREWALLRULE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FirewallRule = _reflection.GeneratedProtocolMessageType('FirewallRule', (_message.Message,), {
  'DESCRIPTOR' : _FIREWALLRULE,
  '__module__' : 'google.cloud.appengine_v1beta.proto.firewall_pb2'
  ,
  '__doc__': """A single firewall rule that is evaluated against incoming traffic and
  provides an action to take on matched requests.
  
  Attributes:
      priority:
          A positive integer between [1, Int32.MaxValue-1] that defines
          the order of rule evaluation. Rules with the lowest priority
          are evaluated first.  A default rule at priority
          Int32.MaxValue matches all IPv4 and IPv6 traffic when no
          previous rule matches. Only the action of this rule can be
          modified by the user.
      action:
          The action to take on matched requests.
      source_range:
          IP address or range, defined using CIDR notation, of requests
          that this rule applies to. You can use the wildcard character
          "*" to match all IPs equivalent to “0/0” and “::/0” together.
          Examples: ``192.168.1.1`` or ``192.168.0.0/16`` or
          ``2001:db8::/32`` or
          ``2001:0db8:0000:0042:0000:8a2e:0370:7334``.  .. raw:: html
          <p>  Truncation will be silently performed on addresses which
          are not properly truncated. For example, ``1.2.3.4/24`` is
          accepted as the same address as ``1.2.3.0/24``. Similarly, for
          IPv6, ``2001:db8::1/32`` is accepted as the same address as
          ``2001:db8::/32``.
      description:
          An optional string description of this rule. This field has a
          maximum length of 100 characters.
  """,
  # @@protoc_insertion_point(class_scope:google.appengine.v1beta.FirewallRule)
  })
_sym_db.RegisterMessage(FirewallRule)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
