#!/usr/bin/python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0-or-later

# Get state of systemd units and export it as facts data
# Copyright (C) 2023  Michal Sekletar

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: systemd_units
author: Michal Sekletar (@msekletar)
short_description: Return systemd units status as fact data
requirements: [systemd]
description:
  - This module gathers state of systemd units and exposes it as facts data
options: {}
"""

RETURN = r"""
---
ansible_facts:
  description: Facts about systemd units
  returned: always
  type: complex
  contains:
    systemd_units:
      type: list
      elements: dict
      description: State of systemd units
      returned: always
      contains:
        name:
            description: Name of the unit.
            returned: always
            type: str
            sample: cups.service
        load_state:
          description: Load state of the unit file.
          returned: always
          type: str
          sample: loaded
        active_state:
          description: Main active state of the unit.
          returned: always
          type: str
          sample: active
        sub_state:
          description: Sub state of the unit.
          returned: always
          type: str
          sample: listening
        description:
          description: Description of the unit.
          returned: always
          type: str
          sample: Journal Service
"""

EXAMPLES = r"""
---
- hosts: all
  name: Gather systemd_units facts
  roles:
    - linux-system-roles.systemd
  tasks:
    - name: Print units facts
      debug:
        msg: "{{ systemd_units }}"
"""

from ansible.module_utils.basic import AnsibleModule


class SystemdUnitsFacts:
    def __init__(self, module):
        self.module = module

    def units(self):
        systemctl = self.module.get_bin_path(
            "systemctl", opt_dirs=["/usr/bin", "/usr/local/bin"]
        )

        units = {}
        rc, stdout, stderr = self.module.run_command(
            "%s list-units --no-pager --no-legend" % systemctl, use_unsafe_shell=True
        )
        if rc != 0:
            self.module.warn("Could not list units: %s" % stderr)
            return {}

        for line in stdout.splitlines():
            f = line.split()
            if len(f) >= 5:
                units[f[0]] = {
                    "name": f[0],
                    "load_state": f[1],
                    "active_state": f[2],
                    "sub_state": f[3],
                    "description": " ".join(f[4:]),
                }

        return units


def main():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    systemd_facts_module = SystemdUnitsFacts(module)

    units = systemd_facts_module.units()

    results = dict(ansible_facts={"systemd_units": units})
    module.exit_json(**results)


if __name__ == "__main__":
    main()
