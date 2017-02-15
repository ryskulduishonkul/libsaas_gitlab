# coding: utf-8
# Copyright © 2016 Bytedance.com All Rights Reserved.
# Wang Jing (wangjing@bytedance.com)

from libsaas import http, parsers
from libsaas.services import base

from . import resource

__author__ = 'wangjing'

class DeployKeysBase(resource.GitlabResource):
    path = 'deploy_keys'

    @base.apimethod
    def update(self, obj):
        raise base.MethodNotSupported()

class DeployKeys(DeployKeysBase):
    @base.apimethod
    def delete(self):
        raise base.MethodNotSupported()

class DeployKey(DeployKeysBase):

    @base.apimethod
    def create(self, obj):
        raise base.MethodNotSupported()

    @base.apimethod
    def enable(self):
        """
        Tree
        """
        url = '{0}/enable'.format(self.get_url())

        return http.Request('POST', url), parsers.parse_json

    @base.apimethod
    def disable(self):
        """
        Tree
        """
        url = '{0}/disable'.format(self.get_url())

        return http.Request('DELETE', url), parsers.parse_json
