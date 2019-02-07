
jq-filter
=========

This role contains `jq()` filter, for using [jq] filter expressions in your
Ansible playbooks, roles, and templates. It's not really a role, it's just a
way to distrbute the `jq()` filter.

[jq]: https://stedolan.github.io/jq/

Requirements
------------

The jq filter requires the Python [jq module]  to be installed on the host
running your playbooks. Installing the module requires a build environment
with a C compiler.

[jq module]: https://pypi.org/project/jq/

For Debian, Ubuntu, etc

```sh
apt-get install autoconf automake build-essential libtool python-dev
```

For Red Hat, CentOS, Fedora, etc

```
yum groupinstall "Development Tools"
yum install autoconf automake libtool python
```

The jq command is not required. No libraries or modules are required on remote hosts.

Role Variables
--------------

None.

Dependencies
------------

No dependencies on other roles.

Example Playbook
----------------

```yaml
- hosts: localhost
  connection: local
  vars:
    domain_definition:
      domain:
        cluster:
          - name: "cluster1"
          - name: "cluster2"
        server:
          - name: "server11"
            cluster: "cluster1"
            port: "8080"
          - name: "server12"
            cluster: "cluster1"
            port: "8090"
          - name: "server21"
            cluster: "cluster2"
            port: "9080"
          - name: "server22"
            cluster: "cluster2"
            port: "9090"
        library:
          - name: "lib1"
            target: "cluster1"
          - name: "lib2"
            target: "cluster2"
  tasks:
    - name: Show cluster names
      debug:
        msg: "{{ domain_definition | jq('.domain.cluster[].name') }}"
```
License
-------

BSD
