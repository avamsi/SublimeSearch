import sublime, sublime_plugin
import webbrowser

class GoogleSearchCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = self.get_text()
        webbrowser.open_new_tab(
            'https://www.google.com/search?q=' + text
        )

    def is_visible(self):
        return bool(self.get_text())

    def get_text(self):
        sel = self.view.sel()
        reg = sel[0]
        return self.view.substr(reg).strip()

    def description(self):
        text = self.get_text()
        if len(text) > 16:
            text = text[0: 16] + '...'
        return "Search Google for '" + text + "'"
