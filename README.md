<!--
SPDX-FileCopyrightText: 2019, 2020, Alex Willmer <alex@moreati.org.uk>
SPDX-License-Identifier: Apache-2.0
-->

jq-filter
=========

This Ansible collection provides `jq()`, a filter that slices and dices JSON
just like the [jq] command. It's particularly good with deeply nested lists
of dicts, and dicts of lists.

Example
-------

A list of databases & nested users such as

```yaml
databases:
  - {name: db1, users: [{username: alice}, {username: alex}]}
  - {name: db2, users: [{username: bob}, {username: brienne}]}
```

can be transformed by a template expression such as

```jinja
{{ databases | moreati.jq.jq('map({db: .name, user: .users[].username}) }}

```

into a flat list

```
[
  {"db": "db1", "user": "alice"},
  {"db": "db1", "user": "alex"},
  {"db": "db2", "user": "bob"},
  {"db": "db2", "user": "brienne"}
]
```

You can try out jq expressions at [jqplay.org], starting with this [example].

[jq]: https://stedolan.github.io/jq/
[jq expression language]: https://stedolan.github.io/jq/manual/#Basicfilters
[jqplay.org]: https://jqplay.org
[example]: https://jqplay.org/s/zg_l3ZoT6C

Installation
------------

To install this collection run

```
ansible-galaxy collection install moreati.jq
```

Requirements
------------

This collection requires

- [Ansible] >= 2.8
- [Python jq] >= 1.0

To install Python jq run

```
python -m pip jq
```

Python jq is only needed on the Ansible controller (the host your playbooks
run _from_). It's not needed on Ansible targets (hosts your playbooks run
_against_). The `jq` command isn't needed.

pre-compiled wheels have been published for CPython 2.7, and 3.x on MacOS,
and Linux (x86, x86_64). Other Python version, and pltforms will need to build
the module from source.

[ansible]: https://ansible.com
[Python jq]: https://pypi.org/project/jq

Role Variables
--------------

None.

Dependencies
------------

No dependencies on other roles.

Example Playbook
----------------

- [playbooks/demo.yml]

[playbooks/demo.yml]: https://github.com/moreati/jq-filter/blob/master/playbooks/demo.yml
License
-------

Apache 2.0
