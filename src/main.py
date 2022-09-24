import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
import random

class AboutDialog(Gtk.AboutDialog):
    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self)
        self.props.program_name = "Eight Ball"
        self.props.version = "1.4.0"
        self.props.authors = ["M.D. Walters"]
        self.props.copyright = "This project is licenced under the MIT Licence"
        self.props.logo_icon_name = "ml.mdwalters.EightBall"
        self.props.comments = "Make decisions easily"
        self.props.license_type = 7
        self.props.license = """
MIT License

Copyright (c) 2022 M.D. Walters

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
        self.props.wrap_license = True
        self.props.modal = True

class EightBall(Gtk.ApplicationWindow):
    def __init__(self):
        super().__init__()

        self.set_default_size(800, 600)
        self.set_border_width(10)

        eightBall = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful.", "No.", "Maybe."]
        header = Gtk.HeaderBar()
        label = Gtk.Label()
        popover = Gtk.Popover()
        newPrediction = Gtk.Button()
        menu = Gtk.MenuButton(popover=popover)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        menuButton = Gtk.ModelButton(label="About Eight Ball")

        def predict(self):
            label.set_markup(f"<big><b>{random.choice(eightBall)}</b></big>")

        def about(self):
            about = AboutDialog(self)
            about.show_all()

        header.set_show_close_button(True)
        header.props.title = "Eight Ball"
        self.set_titlebar(header)

        vbox.pack_start(menuButton, False, True, 10)
        vbox.show_all()
        popover.add(vbox)
        popover.set_position(Gtk.PositionType.BOTTOM)

        icon = Gio.ThemedIcon(name="view-refresh")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        newPrediction.add(image)
        newPrediction.connect("clicked", predict)
        header.pack_start(newPrediction)

        icon = Gio.ThemedIcon(name="open-menu")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        menu.add(image)
        menuButton.connect("clicked", about)
        header.pack_end(menu)

        label.set_line_wrap(True)
        predict(self)
        self.add(label)

window = EightBall()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
