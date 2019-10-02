# Ansible role: Alertmanager Bot

[![Build Status](https://travis-ci.org/mbaran0v/ansible-role-alertmanager-bot.svg?branch=master)](https://travis-ci.org/mbaran0v/ansible-role-alertmanager-bot) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![GitHub tag](https://img.shields.io/github/tag/mbaran0v/ansible-role-alertmanager-bot.svg)](https://github.com/mbaran0v/ansible-role-alertmanager-bot/tags/) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

Ansible role for [Alertmanager Bot](https://github.com/metalmatze/alertmanager-bot). Currently this works on Debian and RedHat based linux systems (only systemd support). Tested platforms are:

* Ubuntu 16.04
* CentOS 7
* Debian 9

Requirements
------------

No special requirements; note that this role requires root access, so either run it in a playbook with a global become: yes

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows. (For all variables, take a look at defaults/main.yml)

```yaml
alertmanager_bot_version: 0.4.0
```
version for installation

```yaml
alertmanager_bot_telegram_token: 123456
```
telegram bot token - is required

```yaml
alertmanager_bot_telegram_admins:
  - 1
  - 2
```
list of telegram user id for admin accounts - is required

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: alertmanager-bot
  roles:
      - role: mbaran0v.alertmanager-bot
```

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2018 by [Maxim Baranov](https://github.com/mbaran0v).
