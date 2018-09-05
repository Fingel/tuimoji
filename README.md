# tuimoji

tuimoji is a terminal based emoji chooser for \*nix. With tuimoji you
can search and browse emojis and copy them to your clipboard without ever
leaving the comfort of your terminal!

![Tuimoji main window](https://s3-us-west-2.amazonaws.com/pedaldp/images/2018-09-04-tuimoji/people.png)

* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
    * [Skin tone modifier](#skin-tone-modifier)
    * [Change the clipboard](#change-the-clipboard)
* [Acknowledgements](#acknowledgements)

## Features

* Browse emojis by category.
* Search emojis by name.
* Supports [skin tone modifiers](https://emojipedia.org/modifiers/).

## Installation

tuimoji requires Python3 and xclip to be installed. xclip can be installed
via your favorite package manager (if it is not already).

To install tuimoji, use pip:

    pip3 install --user tuimoji

## Usage

Launch tuimoji with the `tuimoji` command. By default, the search input is
focused, allowing you to type to search immediately:

![Tuimoji search](https://s3-us-west-2.amazonaws.com/pedaldp/images/2018-09-04-tuimoji/poo.png)

Press Enter to highlight the first result, and use the cursor keys to navigate
to the desired emoji. Pressing Enter again will copy the emoji to your
clipboard and exit the program.

Alternatively you may browse emojis using the named categories. Use the cursor
keys to navigate and press Enter to select a category.

### Skin tone modifier

tuimoji defaults to `0` which is the original Simpsons skin tone (no modifier).

To change the tone launch tuimoji with the `-t` or `--tone` command line argument:

    tuimoji -t 6


The available skin tone modifiers are:

| Tone | Result |
| ---- | ------ |
| 0    | 👊     |
| 1_2  | 👊🏻   |
| 3    | 👊🏼   |
| 4    | 👊🏽   |
| 5    | 👊🏾   |
| 6    | 👊🏿   |


### Change the clipboard

By default tuimoji will copy characters to the clipboard, which is the usual
selection when using copy and paste operations (ctrl+c/ctrl+v). You can also
tell tuimoji to place the character on the primary (middle click paste) or
secondary (unused?) selections.

Launch tuimoji with the `-s` or `--selection` command line argument:

    tuimoji -s primary


## Acknowledgements

Thanks to [shanraisshan/EmojiCodeSheet](https://github.com/shanraisshan/EmojiCodeSheet)
for the contents of the .json data file in this project.
