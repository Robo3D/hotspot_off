# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin
import subprocess

class Hotspot_offPlugin(octoprint.plugin.SettingsPlugin, octoprint.plugin.AssetPlugin, octoprint.plugin.TemplatePlugin, octoprint.plugin.StartupPlugin):

    def on_startup(self, host, port):
        args = ['netconnectcli', 'stop_ap']
        try:
            r = subprocess.check_output(args)
        except Exception as e:
            r = 'Failed to run stop command.'
        finally:
            self._logger.info('### Stop Hotspot Results: {}'.format(r))

    def get_update_information(self):
        return dict(
                hotspot_off=dict(
                displayName="Hotspot_off Plugin",
                displayVersion=self._plugin_version,
                type="github_release",
                user="Robo3D",
                repo="hotspot_off",
                current=self._plugin_version,
                pip="https://github.com/Robo3D/hotspot_off/archive/{target_version}.zip"
            )
        )


__plugin_name__ = "Hotspot_off Plugin"

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = Hotspot_offPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
