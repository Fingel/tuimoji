import urwid
import json
from subprocess import Popen, PIPE


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
        emoji_dict['_all'] = [item for sublist in emoji_dict.values() for item in sublist]
        return emoji_dict


class App():
    def __init__(self):
        self.emoji_bank = all_emojis()
        self.edit = urwid.Edit('Filter: ')
        self.menu = self.category_menu
        self.pane = urwid.GridFlow([], 21, 1, 1, 'left')
        self.show_emojis(None, 'People')
        self.pane.focus_position = 0

    @property
    def category_menu(self):
        body = [urwid.Divider()]
        for cat in [c for c in self.emoji_bank.keys() if c != '_all']:
            button = urwid.AttrMap(
                urwid.Button(cat, self.show_emojis, cat),
                '', 'reveal focus')
            body.append(button)
        return urwid.BoxAdapter(
            urwid.ListBox(urwid.SimpleFocusListWalker(body)), 10
        )

    @property
    def widget(self):
        return urwid.Filler(
            urwid.Pile([
                self.edit,
                ('weight', 1, urwid.Columns([
                    (15, self.menu),
                    self.pane
                ]))
            ])
        )

    def show_emojis(self, widget, category):
        cells = []
        for emoji in self.emoji_bank[category]:
            if 'type' not in emoji['key'] and 'family' not in emoji['key']:
                name = emoji['key'][:15] + (emoji['key'][15:] and '..')
                text = CustomSelectableIcon('{} {}'.format(emoji['value'], name), 0)
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


def main():
    app = App()
    widget = app.widget
    loop = urwid.MainLoop(widget, palette=palette)
    loop.run()


if __name__ == '__main__':
    main()
