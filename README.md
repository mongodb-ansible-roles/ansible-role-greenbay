Ansible role for greenbay
==================================

Installs greenbay

[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-greenbay/workflows/Molecule%20Test/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-greenbay/actions?query=workflow%3A%22Molecule+Test%22)
[![GitHub Actions](https://github.com/mongodb-ansible-roles/ansible-role-greenbay/workflows/Release/badge.svg)](https://github.com/mongodb-ansible-roles/ansible-role-greenbay/actions?query=workflow%3A%22Molecule+Test%22)


Requirements
------------

None

Role Variables
--------------

| Name | Description | Type | Default | Required |
|------|-------------|:----:|:-------:|:--------:|
| `greenbay_sha` | SHA of the version of greenbay you want to install | string | `""` | yes |
| `greenbay_package_url` | You may specify a custom URL to download greenbay from | string | `""` | no |

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: all
  roles:
    - role: ansible-role-greenbay
      vars:
        greenbay_sha: 88bd85f71f7425da94dc5c0f8809f38c24226c16
```

Development
-----------

Testing this role locally requires the CircleCI [Local CLI](https://circleci.com/docs/2.0/local-cli/).

To install the CLI for macOS and Linux, invoke the following command:

    $ curl -fLSs https://circle.ci/cli | DESTDIR=/usr/local/bin bash

After installing the CLI, invoke the following command to run the Molecule tests:

    $ make test

License
-------

[Apache License](LICENSE)
