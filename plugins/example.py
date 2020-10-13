""" An example of a plugin. """
from __future__ import print_function

from lib.common.plugins import Plugin
import lib.common.helpers as helpers

# anything you simply write out (like a script) will run immediately when the
# module is imported (before the class is instantiated)
print("Hello from your new plugin!")


# this class MUST be named Plugin
class Plugin(Plugin):
    description = "An example plugin."

    def onLoad(self):
        """ any custom loading behavior - called by init, so any
        behavior you'd normally put in __init__ goes here """
        print("Custom loading behavior happens now.")

        # you can store data here that will persist until the plugin
        # is unloaded (i.e. Empire closes)
        self.calledTimes = 0
        self.commands = {'do_test': {'Description': 'an example of a plugin function',
                                     'arg': 'the argument required and it''s description'
                                     }
                         }

    def execute(self, dict):
        # This is for parsing commands through the api

        try:
            # essentially switches to parse the proper command to execute
            if dict['command'] == 'do_test':
                results = self.do_test(dict['arguments']['arg'])
            return results
        except:
            return False

    def get_commands(self):
        return self.commands

    def register(self, mainMenu):
        """ any modifications to the mainMenu go here - e.g.
        registering functions to be run by user commands """
        mainMenu.__class__.do_test = self.do_test

    def do_test(self, args):
        "An example of a plugin function."
        print("This is executed from a plugin!")
        print(helpers.color("[*] It can even import Empire functionality!"))

        # you can also store data in the plugin (see onLoad)
        self.calledTimes += 1
        print("This function has been called {} times.".format(self.calledTimes))

    def shutdown(self):
        """if the plugin spawns a process provide a shutdown method for when Empire exits else leave it as pass"""
        return
