# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .copy_source_py3 import CopySource


class AmazonRedshiftSource(CopySource):
    """A copy activity source for Amazon Redshift Source.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param source_retry_count: Source retry count. Type: integer (or
     Expression with resultType integer).
    :type source_retry_count: object
    :param source_retry_wait: Source retry wait. Type: string (or Expression
     with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type source_retry_wait: object
    :param max_concurrent_connections: The maximum concurrent connection count
     for the source data store. Type: integer (or Expression with resultType
     integer).
    :type max_concurrent_connections: object
    :param type: Required. Constant filled by server.
    :type type: str
    :param query: Database query. Type: string (or Expression with resultType
     string).
    :type query: object
    :param redshift_unload_settings: The Amazon S3 settings needed for the
     interim Amazon S3 when copying from Amazon Redshift with unload. With
     this, data from Amazon Redshift source will be unloaded into S3 first and
     then copied into the targeted sink from the interim S3.
    :type redshift_unload_settings:
     ~azure.mgmt.datafactory.models.RedshiftUnloadSettings
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'source_retry_count': {'key': 'sourceRetryCount', 'type': 'object'},
        'source_retry_wait': {'key': 'sourceRetryWait', 'type': 'object'},
        'max_concurrent_connections': {'key': 'maxConcurrentConnections', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'query': {'key': 'query', 'type': 'object'},
        'redshift_unload_settings': {'key': 'redshiftUnloadSettings', 'type': 'RedshiftUnloadSettings'},
    }

    def __init__(self, *, additional_properties=None, source_retry_count=None, source_retry_wait=None, max_concurrent_connections=None, query=None, redshift_unload_settings=None, **kwargs) -> None:
        super(AmazonRedshiftSource, self).__init__(additional_properties=additional_properties, source_retry_count=source_retry_count, source_retry_wait=source_retry_wait, max_concurrent_connections=max_concurrent_connections, **kwargs)
        self.query = query
        self.redshift_unload_settings = redshift_unload_settings
        self.type = 'AmazonRedshiftSource'