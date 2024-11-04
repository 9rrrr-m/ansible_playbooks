Changelog
=========

[1.1.7] - 2024-08-29
--------------------

### Bug Fixes

- fix: use journalctl -t fapolicyd to get fapolicyd log messages (#41)

### Other Changes

- ci: Add tags to TF workflow, allow more [citest bad] formats (#40)

[1.1.6] - 2024-08-21
--------------------

### Other Changes

- test: use ansible_python_interpreter (#38)

[1.1.5] - 2024-08-20
--------------------

### Other Changes

- ci: Add tft plan and workflow (#30)
- ci: Update fmf plan to add a separate job to prepare managed nodes (#32)
- ci: Bump sclorg/testing-farm-as-github-action from 2 to 3 (#33)
- ci: Add workflow for ci_test bad, use remote fmf plan (#34)
- ci: Fix missing slash in ARTIFACTS_URL (#35)
- test: make test_trusted_execution gather facts (#36)

[1.1.4] - 2024-07-02
--------------------

### Bug Fixes

- fix: add support for EL10 (#28)

### Other Changes

- ci: ansible-lint action now requires absolute directory (#27)

[1.1.3] - 2024-06-11
--------------------

### Other Changes

- ci: use tox-lsr 3.3.0 which uses ansible-test 2.17 (#22)
- ci: tox-lsr 3.4.0 - fix py27 tests; move other checks to py310 (#24)
- ci: Add supported_ansible_also to .ansible-lint (#25)

[1.1.2] - 2024-04-04
--------------------

### Other Changes

- ci: fix python unit test - copy pytest config to tests/unit (#15)
- ci: Bump ansible/ansible-lint from 6 to 24 (#18)
- test: Fix trusted test - use python script (#19)
- ci: Bump mathieudutour/github-tag-action from 6.1 to 6.2 (#20)

[1.1.1] - 2024-01-16
--------------------

### Other Changes

- ci: Use supported ansible-lint action; run ansible-lint against the collection (#12)
- ci: Use supported ansible-lint action; run ansible-lint against the collection (#13)

[1.1.0] - 2023-12-08
--------------------

### New Features

- feat: several role improvements (#8)

### Other Changes

- refactor: get_ostree_data.sh use env shebang - remove from .sanity* (#10)

[1.0.0] - 2023-11-27
--------------------

### New Features

- feat: New Role to manage fapolicyd
