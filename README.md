# Ansible role: prometheus-postgres-exporter

[![Build Status](https://travis-ci.org/mbaran0v/ansible-role-prometheus-postgres-exporter.svg?branch=master)](https://travis-ci.org/mbaran0v/ansible-role-prometheus-postgres-exporter) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![GitHub tag](https://img.shields.io/github/tag/mbaran0v/ansible-role-prometheus-postgres-exporter.svg)](https://github.com/mbaran0v/ansible-role-prometheus-postgres-exporter/tags) [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Ansible role for install and configure [Prometheus Postgres Exporter](https://github.com/wrouesnel/postgres_exporter). Currently this works on Debian and RedHat based linux systems. Tested platforms are:

* Ubuntu 16.04
* CentOS 7

Requirements
------------

No special requirements; note that this role requires root access, so either run it in a playbook with a global become: yes

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows. (For all variables, take a look at defaults/main.yml)

```yaml
postgres_exporter_version: 0.4.7
```
version for installation

```yaml
postgres_exporter_web_listen_address: ":9187"
```
listen address and port

```yaml
postgres_exporter_root_dir: /opt/postgres_exporter
```
directory for installation

```yaml
postgres_exporter_user: postgres-exp
postgres_exporter_group: "{{ postgres_exporter_user }}"
```
user and group for service

```yaml
# see https://github.com/wrouesnel/postgres_exporter#environment-variables
postgres_exporter_env_vars: |
  DATA_SOURCE_NAME=postgresql://127.0.0.1:5432/?sslmode=disable
```
environment variables

Dependencies
------------

None

Example Playbook
----------------


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
