Changelog
=========

[1.2.0] - 2024-07-15
--------------------

### New Features

- feat: add support for transactional update (#53)

[1.1.5] - 2024-07-02
--------------------

### Bug Fixes

- fix: add support for EL10 (#51)

### Other Changes

- ci: ansible-lint action now requires absolute directory (#50)

[1.1.4] - 2024-06-11
--------------------

### Other Changes

- ci: use tox-lsr 3.3.0 which uses ansible-test 2.17 (#45)
- ci: tox-lsr 3.4.0 - fix py27 tests; move other checks to py310 (#47)
- ci: Add supported_ansible_also to .ansible-lint (#48)

[1.1.3] - 2024-04-04
--------------------

### Other Changes

- ci: Bump codecov/codecov-action from 3 to 4 (#40)
- ci: fix python unit test - copy pytest config to tests/unit (#41)
- ci: Bump ansible/ansible-lint from 6 to 24 (#42)
- ci: Bump mathieudutour/github-tag-action from 6.1 to 6.2 (#43)

[1.1.2] - 2024-01-16
--------------------

### Other Changes

- ci: Bump github/codeql-action from 2 to 3 (#35)
- ci: support ansible-lint and ansible-test 2.16 (#37)
- ci: Use supported ansible-lint action; run ansible-lint against the collection (#38)

[1.1.1] - 2023-12-08
--------------------

### Other Changes

- ci: Bump actions/github-script from 6 to 7 (#32)
- refactor: get_ostree_data.sh use env shebang - remove from .sanity* (#33)

[1.1.0] - 2023-11-29
--------------------

### New Features

- feat: support for ostree systems (#29)

### Other Changes

- build(deps): Bump actions/checkout from 3 to 4 (#19)
- ci: ensure dependabot git commit message conforms to commitlint (#22)
- docs: Docs fixes (#28)

[1.0.2] - 2023-09-08
--------------------

### Other Changes

- ci: Add markdownlint, test_converting_readme, and build_docs workflows (#15)

  - markdownlint runs against README.md to avoid any issues with
    converting it to HTML
  - test_converting_readme converts README.md > HTML and uploads this test
    artifact to ensure that conversion works fine
  - build_docs converts README.md > HTML and pushes the result to the
    docs branch to publish dosc to GitHub pages site.
  - Fix markdown issues in README.md
  
  Signed-off-by: Sergei Petrosian <spetrosi@redhat.com>

- docs: Make badges consistent, run markdownlint on all .md files (#16)

  - Consistently generate badges for GH workflows in README RHELPLAN-146921
  - Run markdownlint on all .md files
  - Add custom-woke-action if not used already
  - Rename woke action to Woke for a pretty badge
  
  Signed-off-by: Sergei Petrosian <spetrosi@redhat.com>

- ci: Remove badges from README.md prior to converting to HTML (#17)

  - Remove thematic break after badges
  - Remove badges from README.md prior to converting to HTML
  
  Signed-off-by: Sergei Petrosian <spetrosi@redhat.com>

[1.0.1] - 2023-07-26
--------------------

### Bug Fixes

- fix: allow .j2 suffix for templates, strip off for file/service names (#12)

### Other Changes

- ci: systemd is a python role (#13)

[1.0.0] - 2023-07-20
--------------------

### New Features

- feat: initial import of systemd role content (#9)
