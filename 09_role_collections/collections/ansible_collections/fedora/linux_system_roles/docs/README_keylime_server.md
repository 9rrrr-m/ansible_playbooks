# keylime_server

[![ansible-lint.yml](https://github.com/fedora.linux_system_roles.keylime_server/actions/workflows/ansible-lint.yml/badge.svg)](https://github.com/fedora.linux_system_roles.keylime_server/actions/workflows/ansible-lint.yml) [![ansible-test.yml](https://github.com/fedora.linux_system_roles.keylime_server/actions/workflows/ansible-test.yml/badge.svg)](https://github.com/fedora.linux_system_roles.keylime_server/actions/workflows/ansible-test.yml) [![markdownlint.yml](https://github.com/fedora.linux_system_roles.keylime_server/actions/workflows/markdownlint.yml/badge.svg)](https://github.com/fedora.linux_system_roles.keylime_server/actions/workflows/markdownlint.yml) [![shellcheck.yml](https://github.com/fedora.linux_system_roles.keylime_server/actions/workflows/shellcheck.yml/badge.svg)](https://github.com/fedora.linux_system_roles.keylime_server/actions/workflows/shellcheck.yml) [![woke.yml](https://github.com/fedora.linux_system_roles.keylime_server/actions/workflows/woke.yml/badge.svg)](https://github.com/fedora.linux_system_roles.keylime_server/actions/workflows/woke.yml)

Ansible role for configuring and deploying the server components for Keylime Remote Attestation.

## Supported Distributions

* RHEL-9.1+, CentOS Stream 9.1+
* Fedora 36+

## Requirements

See below

### Collection requirements

If you want to manage `rpm-ostree` systems with this role, you will need to
install additional collections.  Please run the following command line to
install the collection.

```bash
ansible-galaxy collection install -vv -r meta/collection-requirements.yml
```

## Role Variables

These are the variables that can be passed to the role.  *NOTE:* Use Ansible Vault to encrypt passwords, keys, and other secrets.

| **Variable** | **Default/Choices** | **Description** |
|----------|-------------|------|
`keylime_server_verifier_ip` |  127.0.0.1 | The IP address of the `verifier`
`keylime_server_verifier_port` | 8881 | The port of the `verifier`
`keylime_server_verifier_database_url` | sqlite / empty string (legacy Keylime) | The URL connection for the verifier database. If set to `sqlite`, it will use the configuration set by the file located at `/var/lib/keylime/cv_data.sqlite`. See <https://keylime.readthedocs.io/en/latest/installation.html#database-support> for instructions on using different database configurations. When using When using systems with legacy Keylime, e.g. Fedora 36 and/or Fedora 37, this should be set to an empty string, if one wants to use default sqlite configuration
`keylime_server_verifier_tls_dir` | generate | This option defines the directory where the keys and certificates are stored. If set to `generate`, it will automatically generate a CA, keys and certificates for the client and server in the `/var/lib/keylime/cv_ca` directory, if they are not yet present. If set as `default`, the `/var/lib/keylime/cv_ca` directory is used, and it should contain the files indicated by `keylime_server_verifier_server_key`, `keylime_server_verifier_server_cert`, `keylime_server_verifier_client_key`, `keylime_server_verifier_client_cert`, `keylime_server_verifier_trusted_client_ca` and `keylime_server_verifier_trusted_server_ca` options `keylime_server_verifier_server_key` |  default | The file containing the Keylime verifier server private key. This file should be stored in the directory set in the `keylime_server_verifier_tls_dir` option. If set as `default`, the value `server-private.pem` is used
`keylime_server_verifier_server_key_passphrase` | default | Set the password used to decrypt the server private key file. If `keylime_server_verifier_tls_dir` is set to `generate`, this password will also be used to protect the generated server private key. If left empty, the private key will not be encrypted
`keylime_server_verifier_server_cert` | default | The name of the file containing the Keylime verifier server certificate. The file should be stored in the directory set in the `keylime_server_verifier_tls_dir` option. If set as `default`, the value `server-cert.crt` is used
`keylime_server_verifier_trusted_client_ca` |  default | The list of trusted client CA certificates. The files in the list should be stored in the directory set in the `keylime_server_verifier_tls_dir` option. If set as `default`, the value is set as `[cacert.crt]`
`keylime_server_verifier_client_key` | default | The name of the file containing the Keylime verifier client private key. The file should be stored in the directory set in the `keylime_server_verifier_tls_dir` option. This private key is used by the Keylime verifier to connect to the other services using TLS. If set as `default`, the `client-private.pem` value is used
`keylime_server_verifier_client_key_passphrase` | default | Set the password used to decrypt the client private key file. If `keylime_server_verifier_tls_dir` is set to `generate`, this password will also be used to protect the generated client private key. If left empty, the private key will not be encrypted
`keylime_server_verifier_client_cert` | default | The name of the file containing the Keylime verifier client certificate, which should be stored in the directory set in the `keylime_server_verifier_tls_dir` option. This certificate is used by the Keylime verifier to connect to the other services using TLS. If set as `default`, the value `client-cert.crt` value is used
`keylime_server_verifier_trusted_server_ca` | default | The list of trusted server CA certificates. The files in the list should be stored in the directory set in the `keylime_server_verifier_tls_dir` option. If set as `default`, the value is set as `[cacert.crt]`
`keylime_server_registrar_ip` |  127.0.0.1 | The IP address of the `registrar`
`keylime_server_registrar_port` | 8891 | The port of the `registrar`
`keylime_server_registrar_database_url` | sqlite / empty string (legacy Keylime) |  The URL connection for the registrar database. If set to `sqlite`, it will the configuration set by the file located at `/var/lib/keylime/reg_data.sqlite`. See <https://keylime.readthedocs.io/en/latest/installation.html#database-support> for instructions on using different database configurations. When using When using systems with legacy Keylime, e.g. Fedora 36 and/or Fedora 37, this should be set to an empty string, if one wants to use default sqlite configuration
`keylime_server_registrar_tls_dir` | default | Similarly to `keylime_server_verifier_tls_dir`, the `keylime_server_registrar_tls_dir` option defines the directory where the keys and certificates are stored. If set as `generate`, it will automatically generate a CA, keys, and certificates for the registrar server in the `/var/lib/keylime/reg_ca` directory, if they are not yet present. The options `keylime_server_registrar_server_key`, `keylime_server_registrar_server_cert` and `keylime_server_registrar_trusted_client_ca` should all be set to `default`, when `generate` is used for the `keylime_server_registrar_tls_dir` option. If set as `default`, it shares files with the verifier by using the `var/lib/keylime/cv_ca` directory, which should contain the files indicated by the `keylime_server_registrar_server_key`, `keylime_server_registrar_server_cert` and `keylime_server_registrar_trusted_client_ca` options
`keylime_server_registrar_server_key` |  default | The name of the file containing the Keylime registrar server private key, and it should be stored in the directory set in the `keylime_server_registrar_tls_dir` option. If set as `default`, the value `server-private.pem` is used
`keylime_server_registrar_server_key_passphrase` | default | This option sets the password used to decrypt the private key file. If `keylime_server_registrar_tls_dir` is set to `generate`, this password will also be used to protect the generated server private key. If left empty, the private key will not be encrypted
`keylime_server_registrar_server_cert` | default | The name of the file containing the Keylime registrar server certificate, and this file should be stored in the directory specified in the `keylime_server_registrar_tls_dir` option. If set as `default`, the value `server-cert.crt` is used
`keylime_server_registrar_trusted_client_ca` | default | The list of trusted client CA certificates. The files in the list should be stored in the directory set in the `keylime_server_registrar_tls_dir` option. If set as `default`, the value is set as `[cacert.crt]`

## Example Playbooks

```yaml
- name: Manage keylime servers
  hosts: all

  vars:
    keylime_server_verifier_ip: "{{ ansible_host }}"
    keylime_server_registrar_ip: "{{ ansible_host }}"

  roles:
    - fedora.linux_system_roles.keylime_server
```

## rpm-ostree

See README-ostree.md

## License

MIT
