# SPDX-FileCopyrightText: 2019, 2020, Alex Willmer <alex@moreati.org.uk>
# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible.errors import AnsibleError, AnsibleFilterError
from ansible.module_utils._text import to_native

try:
    import jq
except ImportError:
    jq = None


def jq_filter(data, expr):
    if not jq:
        raise AnsibleError("You must install the Python jq module to use jq filter")

    try:
        program = jq.jq(expr)
    except ValueError as e:
        raise AnsibleFilterError("Error compiling jq expression: %s" % to_native(e))
    except Exception as e:
        raise AnsibleFilterError("Unknown error with jq expression: %s" % to_native(e))

    return program.transform(data)


class FilterModule(object):
    def filters(self):
        return {
            'jq': jq_filter,
        }
