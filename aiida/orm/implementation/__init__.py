from __future__ import absolute_import
from aiida import settings

STORAGE_BACKEND = getattr(settings, "STORAGE_BACKEND", "django")

from aiida.orm.implementation.general.group import get_group_type_mapping

if STORAGE_BACKEND == "sqlalchemy":
    from aiida.orm.implementation.sqlalchemy.node import Node
    from aiida.orm.implementation.sqlalchemy.computer import Computer
    from aiida.orm.implementation.sqlalchemy.group import Group
    from aiida.orm.implementation.sqlalchemy.lock import Lock, LockManager
    # from aiida.orm.implementation.sqlalchemy.querytool import QueryTool
    from aiida.orm.implementation.sqlalchemy.workflow import Workflow, kill_all, get_workflow_info
    from aiida.orm.implementation.sqlalchemy.code import Code, delete_code
    from aiida.orm.implementation.sqlalchemy.utils import delete_computer
elif STORAGE_BACKEND == "django":
    from aiida.orm.implementation.django.node import Node
    from aiida.orm.implementation.django.computer import Computer
    from aiida.orm.implementation.django.group import Group
    from aiida.orm.implementation.django.lock import Lock, LockManager
    from aiida.orm.implementation.django.querytool import QueryTool
    from aiida.orm.implementation.django.workflow import Workflow, kill_all, get_workflow_info
    from aiida.orm.implementation.django.code import Code, delete_code
    from aiida.orm.implementation.django.utils import delete_computer

    from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned