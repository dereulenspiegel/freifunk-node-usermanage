#!/usr/bin/python

import pwd
import json
from ansible.module_utils.basic import *

NOOP_SHELL = [
  "/usr/sbin/nologin",
  '/bin/nologin',
  '/bin/false'
]

class CheckUsers(object):
  def __init__(self, module):
    self.module = module
    self.cusers = self.module.params["users_var"]

  def main(self):
    #self.module.fail_json(msg="Cuser var '{}'".format(self.cusers['users_db'][0]['comment']))
    users = pwd.getpwall()
    for user in users:
      name = user.pw_name
      shell = user.pw_shell
      uid = user.pw_uid
      home_dir = user.pw_dir

      if uid > 999 and self.isValidShell(shell):
        if not name in self.cusers['users_db']:
          self.module.fail_json(msg="User {} not defined by ansible".format(name))

  def isValidShell(self, shell):
    if shell in NOOP_SHELL:
      return False
    return True

  def checkUsersKeys(self, user):
    usersKeys = None

    for keys in self.cusers['key_db']:
      if keys['user'] == user:
        userKeys = keys
        break

    if userKeys == None:
      self.module.fail_json(msg="User {} has no ansible defined SSH keys".format(name))
    

def main():
  module = AnsibleModule(
      argument_spec=dict(
          users_var=dict(default=None, required=True, type='dict')
      ),
      supports_check_mode=False
  )
  CheckUsers(module).main()

if __name__ == '__main__':
    main()