# Ansible role: prometheus-postgres-exporter

[![Build Status](https://travis-ci.org/mbaran0v/ansible-role-prometheus-postgres-exporter.svg?branch=master)](https://travis-ci.org/mbaran0v/ansible-role-prometheus-postgres-exporter) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![GitHub tag](https://img.shields.io/github/tag/mbaran0v/anansible-role-prometheus-postgres-exporter.svg)](https://github.com/mbaran0v/ansible-role-prometheus-postgres-exporter/tags) [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Ansible role for install and configure [Prometheus Postgres Exporter](https://github.com/wrouesnel/postgres_exporter). Currently this works on Debian and RedHat based linux systems. Tested platforms are:

* Ubuntu 16.04
* Debian 9
* CentOS 7

Requirements
------------

No special requirements; note that this role requires root access, so either run it in a playbook with a global become: yes

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows. (For all variables, take a look at defaults/main.yml)

```yaml
postgres_exporter_version: 0.29.0
```
version for installation

```yaml
postgres_exporter_listen_address: "0.0.0.0"
postgres_exporter_listen_port: 9419
```
listen address and port

```yaml
postgres_exporter_root_dir: /opt/postgres_exporter
```
directory for installation

```yaml
postgres_exporter_system_group: "rabbitmq-exp"
postgres_exporter_system_user: "{{ postgres_exporter_system_group }}"
```
user and group for service

```yaml
# see https://github.com/kbudde/postgres_exporter#configuration
postgres_exporter_config_vars: |
  RABBIT_URL=http://127.0.0.1:15672
  RABBIT_USER=guest
  RABBIT_PASSWORD=guest
```
config variables

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: app
  become: yes
  roles:
      - mbaran0v.prometheus-postgres-exporter
```

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2018 by Maxim Baranov.
