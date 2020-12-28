# window.py
#
# Copyright 2020 Stephan Verbücheln
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk
import subprocess



@Gtk.Template(resource_path='/de/ccc/streamlauncher/window.ui')
class StreamlauncherWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'StreamlauncherWindow'

    en_player = Gtk.Template.Child()
    bn_hd = Gtk.Template.Child()
    bn_translated = Gtk.Template.Child()

    @Gtk.Template.Callback('on_button_clicked')
    def _on_button_clicked(self, button):
        room = button.get_label()
        if self.bn_hd.get_active():
            definition = 'hd'
        else:
            definition = 'sd'
        if self.bn_translated.get_active():
            translated = 'translated'
        else:
            translated = 'native'
        url = 'https://cdn.c3voc.de/' + room + '_' + translated + '_' + definition + '.webm'
        print('Opening URL:' + url)
        subprocess.Popen([self.en_player.get_text(), url])


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
