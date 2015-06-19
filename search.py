import sublime, sublime_plugin
import webbrowser

url = {
    'Bing': 'https://www.bing.com/search?q=',
    'DuckDuckGo': 'https://duckduckgo.com/?q=',
    'Google': 'https://www.google.com/search?q=',
    'Yahoo': 'https://search.yahoo.com/search?p='
}

class WebSearchCommand(sublime_plugin.TextCommand):
    def __init__(self):
        settings = sublime.load_settings('Search.sublime-settings')
        self.search_engine = settings.get('search_engine', 'Google')

    def run(self, edit):
        text = self.get_text()
        webbrowser.open_new_tab(
            url[self.search_engine] + text
        )

    def is_visible(self):
        return bool(self.get_text())

    def get_text(self):
        sel = self.view.sel()
        reg = sel[0]
        return self.view.substr(reg).strip()

    def description(self):
        text = "%s for '%s'" % (self.search_engine, self.get_text())
        if len(text) > 32:
            text = text[0: 32] + '...'
        return 'Search ' + text
