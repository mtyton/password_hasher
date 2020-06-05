import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from GUI.main_window import PassApp
import sys


if __name__ == "__main__":
    application = PassApp()
    exit_status = application.run()
    sys.exit(exit_status)