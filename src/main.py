import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gio
import random

class EightBall(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_size_request(500, 500)
        self.set_border_width(10)

        eightBall = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        header = Gtk.HeaderBar()
        button = Gtk.Button()
        label = Gtk.Label()

        def roll(self):
            label.set_markup(f"<big>{random.choice(eightBall)}</big>")

        header.set_show_close_button(True)
        header.props.title = "Eight Ball"
        self.set_titlebar(header)

        icon = Gio.ThemedIcon(name="view-refresh")
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        button.add(image)
        button.connect("clicked", roll)
        header.pack_start(button)

        label.set_line_wrap(True)
        roll(self)
        self.add(label)

window = EightBall()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
