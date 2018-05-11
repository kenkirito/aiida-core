# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida_core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################
from aiida.restapi.translator.base import BaseTranslator
from aiida.restapi.common.config import custom_schema

class UserTranslator(BaseTranslator):
    """
    Translator relative to resource 'users' and aiida class User
    """

    # A label associated to the present class (coincides with the resource name)
    __label__ = "users"
    # The AiiDA class one-to-one associated to the present class
    from aiida.orm.user import User
    _aiida_class = User
    # The string name of the AiiDA class
    _aiida_type = "user.User"
    # The string associated to the AiiDA class in the query builder lexicon
    _qb_type = 'user'

    # If True (False) the corresponding AiiDA class has (no) uuid property
    _has_uuid = False

    _result_type = __label__

    _default_projections = None

    # Extract the default projections from custom_schema if they are defined
    if custom_schema is not None:
        try:
            # check if schema is defined for given node type
            if __label__ in custom_schema['columns'].keys():
                _default_projections = custom_schema['columns'][__label__]
        except KeyError:
            pass

    if _default_projections is None:
        # send only white listed keys in default response for user for security reasons
        _default_projections = ['id', 'first_name', "last_name", 'institution', 'date_joined']


    def __init__(self, **kwargs):
        """
        Initialise the parameters.
        Create the basic query_help
        """
        super(UserTranslator, self).__init__(Class=self.__class__, **kwargs)

