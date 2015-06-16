import sublime, sublime_plugin
import webbrowser

search_engine = None

url = {
    'Bing': 'https://www.bing.com/search?q=',
    'DuckDuckGo': 'https://duckduckgo.com/?q=',
    'Google': 'https://www.google.com/search?q=',
    'Yahoo': 'https://search.yahoo.com/search?p='
}

def plugin_loaded():
    global search_engine
    settings = sublime.load_settings('Search.sublime-settings')
    search_engine = settings.get('search_engine', 'Google')

class SearchCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = self.get_text()
        webbrowser.open_new_tab(
            url[search_engine] + text
        )

    def is_visible(self):
        return bool(self.get_text())

    def get_text(self):
        sel = self.view.sel()
        reg = sel[0]
        return self.view.substr(reg).strip()

    def description(self):
        text = "%s for '%s'" % (search_engine, self.get_text())
        if len(text) > 32:
            text = text[0: 32] + '...'
        return 'Search ' + text
