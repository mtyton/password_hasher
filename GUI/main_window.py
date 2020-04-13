import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from GUI.utils.main import excute
from GUI.utils.db import Password


class PassWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="ComPass")
        notebook = Gtk.Notebook()
        self.set_default_size(600, 600)
        notebook.append_page(self.get_save_notebook())
        notebook.append_page(self.load_options())
        self.add(notebook)
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

    def get_save_notebook(self):
        vb = Gtk.VBox()
        hb = Gtk.HBox()
        web_label = Gtk.Label("Website/program: ")
        web_entry = Gtk.Entry()
        phrase_label = Gtk.Label("Password: ")
        phrase_entry = Gtk.Entry()
        button = Gtk.Button(label="Save")
        button.connect("clicked", self.click_save, "save", web_entry.get_text, phrase_entry.get_text)
        hb.add(web_label)
        hb.add(web_entry)
        vb.add(hb)
        hb = Gtk.HBox()
        hb.add(phrase_label)
        hb.add(phrase_entry)
        vb.add(hb)
        vb.add(button)
        return vb

    def click_save(self, widget, command, get_web, get_pass):
        try:
            excute(command, get_web, get_pass)
        except ValueError:
            dialog = Gtk.MessageDialog(parent=self, flags=0,
                                       message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.CLOSE,
                                       text="Please fill in all data")
            dialog.run()
            dialog.destroy()

    def load_options(self):
        vb = Gtk.VBox()
        hb = Gtk.HBox()
        web_label = Gtk.Label("Website/program: ")
        box = self.get_websites_combo()
        load_button = Gtk.Button(label="load")
        copy_button = Gtk.Button(label="copy")
        load_button.connect("clicked", excute, "get", "facebook-test", None)
        copy_button.connect("clicked", self.copy_click, "copy", box)
        hb.add(web_label)
        hb.add(box)
        vb.add(hb)
        hb = Gtk.HBox()
        hb.add(load_button)
        hb.add(copy_button)
        vb.add(hb)
        password_output = Gtk.Entry()
        vb.add(password_output)
        return vb

    def get_websites_combo(self):
        websites = Password.get_website_names()
        store = Gtk.ListStore(str)
        for website in websites:
            store.append([website])
        box = Gtk.ComboBox.new_with_model_and_entry(store)
        box.set_entry_text_column(0)
        return box

    def copy_click(self, widget, command, box):
        entry = box.get_child()
        get_web = entry.get_text
        try:
            result = excute(command, get_web, None)
            self.clipboard.set_text(result, len(result))
        except ValueError:
            dialog = Gtk.MessageDialog(parent=self, flags=0,
                                       message_type=Gtk.MessageType.INFO, buttons=Gtk.ButtonsType.CLOSE,
                                       text="Please fill in all data")
            dialog.run()
            dialog.destroy()

    def show_click(self, widget, command, get_web):
        pass