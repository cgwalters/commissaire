# Copyright (C) 2016  Red Hat, Inc
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Authentication related code for commissaire.
"""

import logging

import falcon


class Authenticator:
    """
    Base class for authentication implementations.
    """

    #: Logger for authenticators
    logger = logging.getLogger('authentication')

    def process_request(self, req, resp):
        """
        Falcon hook to inject authentication before the requests is
        processed.

        :param req: Request instance that will be passed through.
        :type req: falcon.Request
        :param resp: Response instance that will be passed through.
        :type resp: falcon.Response
        :raises: falcon.HTTPForbidden
        """
        self.authenticate(req, resp)

    def authenticate(self, req, resp):
        """
        Method should be overriden with specific a specific authentication
        call for an implementation.

        :param req: Request instance that will be passed through.
        :type req: falcon.Request
        :param resp: Response instance that will be passed through.
        :type resp: falcon.Response
        :raises: falcon.HTTPForbidden
        """
        raise falcon.HTTPForbidden('Forbidden', 'Forbidden')
