import urwid
import json
from subprocess import Popen, PIPE

DEFAULT_TONE = '0'


class CustomEdit(urwid.Edit):
    def __init__(self, label, on_enter, *args, **kwargs):
        self.on_enter = on_enter
        return super().__init__(label, *args, **kwargs)

    def keypress(self, size, key):
        if key == 'enter':
            return self.on_enter()
        else:
            return super().keypress(size, key)


class CustomSelectableIcon(urwid.SelectableIcon):

    def keypress(self, size, key):
        if key == 'enter':
            self.paste(self.get_text()[0].split(' ')[0].encode('utf-8'))
            raise urwid.ExitMainLoop()
        return key

    def paste(self, contents):
        p = Popen(['xclip', '-selection', 'clipboard'], stdin=PIPE)
        p.communicate(contents)


def all_emojis():
    with open('categories/all.json', 'r') as f:
        emoji_dict = json.loads(f.read())

    if DEFAULT_TONE != '0':
        for cat, cat_list in emoji_dict.items():
            bases = {}
            for i in cat_list:
                if '_type_' + DEFAULT_TONE in i['key']:
                    base = i['key'][:i['key'].index('_type_')]
                    bases[base] = i.copy()
                    bases[base]['key'] = base

            for n, i in enumerate(cat_list):
                if i['key'] in bases:
                    emoji_dict[cat][n] = bases[i['key']]

    all_emojis = []
    for cat in emoji_dict.keys():
        cleaned = [k for k in emoji_dict[cat] if '_type_' not in k['key']]
        emoji_dict[cat] = cleaned
        all_emojis += cleaned
    emoji_dict['_all'] = all_emojis

    return emoji_dict


class App():
    def __init__(self):
        self.emoji_bank = all_emojis()
        self.pane = urwid.GridFlow([], 21, 1, 1, 'left')
        self.edit = CustomEdit('Filter: ', on_enter=self.focus_results)
        self.menu = self.category_menu
        self.columns = urwid.Columns([(12, self.menu), self.pane], 2)
        self.pile = urwid.Pile([self.edit, ('weight', 1, self.columns)])

        urwid.connect_signal(self.edit, 'change', self.filter_emojis)
        self.show_emojis(None, self.emoji_bank['People'])
        self.pane.focus_position = 0

    @property
    def category_menu(self):
        body = [urwid.Divider()]
        for cat in [c for c in self.emoji_bank.keys() if c != '_all']:
            button = urwid.AttrMap(
                urwid.Button(cat, self.show_emojis, self.emoji_bank[cat]),
                '', 'reveal focus')
            body.append(button)
        return urwid.BoxAdapter(
            urwid.ListBox(urwid.SimpleFocusListWalker(body)), 10
        )

    @property
    def widget(self):
        return urwid.Filler(
            self.pile,
            'top'
        )

    def focus_results(self):
        self.pile.focus_position = 1
        self.columns.focus_position = 1
        self.pane.focus_position = 0

    def filter_emojis(self, widget, text):
        if not text:
            self.show_emojis(None, self.emoji_bank['_all'])
        else:
            filtered = [e for e in self.emoji_bank['_all'] if text in e['key']]
            self.show_emojis(None, filtered)

    def show_emojis(self, widget, emojis):
        cells = []
        for emoji in emojis:
            name = emoji['key'][:15] + (emoji['key'][15:] and '..')
            text = CustomSelectableIcon(
                '{} {}'.format(emoji['value'], name),
                0
            )
            mapped = urwid.AttrMap(
                text,
                '', 'reveal focus'
            )

            widget = (mapped, ('given', 21))
            cells.append(widget)
        self.pane.contents = cells


palette = [
    ('reveal focus', 'black', 'dark blue', 'standout')
]


def handle_keys(key):
    if key == 'esc':
        raise urwid.ExitMainLoop()


def main():
    app = App()
    widget = app.widget
    loop = urwid.MainLoop(widget, palette=palette, unhandled_input=handle_keys)
    loop.run()


if __name__ == '__main__':
    main()
