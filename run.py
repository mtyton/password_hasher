import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from GUI.main_window import PassWindow


if __name__ == "__main__":
    window = PassWindow()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()