# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class FlowspeedrenamePlugin(octoprint.plugin.SettingsPlugin,
                            octoprint.plugin.AssetPlugin,
                            octoprint.plugin.TemplatePlugin):


	def get_settings_defaults(self):
		return dict(
			flowname='<i class="fa fa-sort-amount-asc"></i> Flow',
			feedname='<i class="fa fa-arrows"></i> Speed'
		)

	def get_assets(self):
		return dict(
			js=["js/flowspeedrename.js"],
		)

	def get_template_configs(self):
		return [
			dict(type="settings", name="Rename Feed & Flow", template="flowspeedrename_settings.jinja2", custom_bindings=False)
			]

	def get_update_information(self):
		return dict(
			flowspeedrename=dict(
				displayName="Flowspeedrename Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="ntoff",
				repo="OctoPrint-Flowspeedrename",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/ntoff/OctoPrint-Flowspeedrename/archive/{target_version}.zip"
			)
		)


__plugin_name__ = "Rename Flowspeed & Feedrate"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = FlowspeedrenamePlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

