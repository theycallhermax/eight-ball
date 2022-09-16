import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
import random

class AboutDialog(Gtk.AboutDialog):
    def __init__(self, parent):
        Gtk.AboutDialog.__init__(self)
        self.props.program_name = "Eight Ball"
        self.props.version = "1.3.2"
        self.props.authors = ["M.D. Walters"]
        self.props.copyright = "2022 M.D. Walters"
        self.props.logo_icon_name = "ml.mdwalters.EightBall"
        self.props.modal = True

class EightBall(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_size_request(640, 360)
        self.set_border_width(10)

        eightBall = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful.", "No.", "Maybe."]
        header = Gtk.HeaderBar()
        label = Gtk.Label()
        popover = Gtk.Popover()
        newPrediction = Gtk.Button()
        menu = Gtk.MenuButton(popover=popover)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        menuButton = Gtk.ModelButton(label="About Eight Ball")

        def roll(self):
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
        newPrediction.connect("clicked", roll)
        header.pack_start(newPrediction)

        icon = Gio.ThemedIcon(name="open-menu")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        menu.add(image)
        menuButton.connect("clicked", about)
        header.pack_end(menu)

        label.set_line_wrap(True)
        roll(self)
        self.add(label)

window = EightBall()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
