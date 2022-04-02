Role Name
=========

This role downloads extra tools which cannot be installed with apt from Github etc.

Role Variables
--------------

`h_tools_base` is path to folder in which the tools will be installed. Default is `/home/kali/hacking_tools`


Example Playbook
----------------
```yaml
    - hosts: servers
      roles:
        - {role: ext-tools, h_tools_base: "/home/kali/hacking_tools"}
```

License
-------

MIT
