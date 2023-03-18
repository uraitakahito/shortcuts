.. shortcuts documentation master file, created by
   sphinx-quickstart on Tue Dec 27 00:20:48 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Keyboard shortcuts for Mac
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Visual Studio Code
==================

General
-------

``⌘ + ⇧ + p``
   show Command Palette

``⌘ + p``
   Quick Open, Go to File...

``⌘ + Left``
   jump to the start of the line

``⌘ + Right``
   jump to the end of the line

``⌃ + Left(Right)``
   move by word

``⌘ + \``
   split editor

``⌃ + ⌘ + Left(Right)``
   move a tab from one of two split editors to another

``⌃ + ```
   focus the terminal

``⌃ + 1``
   focus the editor

Navigation
----------

``⌃ + g``
   go to line

multi-cursor / Selection
------------------------

``⌘ + d``
   select current word

``⌘ + l``
   select current line

``⇧ + ⌥ + Left(Right)``
   extend selection by word

``⇧ + ⌘ + l``
   select all occurrences of current selection

``⇧ + ⌥ + ⌘ + Up/Down/Left/Right``
   column box selection

Editing
-------

``⌘ + x``
   Cut line(empty selection)

``⌘ + c``
   Copy line(empty selection)

``⌘ + /``
   Toggle line comment

``⇧ + ⌘ + /``
   delete line

``⌘ + ⏎``
   insert line below

``⇧ + ⌘ + ⏎``
   insert line above

``⌥ + Up/Down``
   move line up/down

Panel
-----

``⌘ + j``
   toggle panel

``⌘ + ⇧ + u``
   output

``⌘ + ⇧ + y``
   debug console

Sidebars
--------

``⌘ + b``
   toggle sidebar

``⌘ + ⇧ + e``
   explorer

``⌘ + ⇧ + f``
   search

``⌘ + k, e``
   Explorer: Focus on Open Editors View

Window Management
-----------------

``⌘ + w``
   close editor/window

File Management
---------------

``⌘ + s``
   save

Command Palette
---------------

``Preferences: Open Keyboard Shortcuts``
   edit and find available key bindings

``Split Editor XXX``
   split an editor

``View: Move Editor Group XXX``
   move a tab from A to B

.. note::
   `vscode cheat sheet <https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf>`_


Slack
======

``⌘ + ⇧ + a``
   Open the "All unreads" dialog

.. note::
   `84 Slack Keyboard Shortcuts: Your Cheat Sheet <https://dispatch.m.io/slack-keyboard-shortcuts-cheat-sheet/>`_

Google Chrome
=============

Tab & window shortcuts
----------------------

``⌘ + ⇧ + n``
   open a new window in incognito mode

``⌘ + ⇧ + t``
   reopen the last tab you've closed

``⌘ + 1-8``
   switch to the tab at the specified position number

``⌘ + 9``
   switch to the last tab

``⌃ + tab``
   switch to the next tab

``⌘ + ⇧ + tab``
   switch to the previous tab

``⌘ + w``
   close the current tab or pop up

``⌘ + [/] or ⌘ + Left/Right``
   open the previous/next page in your browsing history for the current tab

``⌘ + ⇧ + a``
   search your tabs

Google Chrome feature shortcuts
-------------------------------

``⌘ + y``
   open the history page in a new tab

``⌘ + g``
   jump to the next match to your Find Bar search

``⌘ + ⇧ + g``
   jump to the previous match to your Find Bar search

``⌘ + ⌥ + i``
   open Developer Tools

``⌘ + ⇧ + delete``
   open the Clear Browsing Data options

Address bar shorcuts
--------------------

``⌘ + l``
   highlight content in the web address area

Site shortcuts
--------------------

@bookmarks, @history and @tabs

.. note::
   `Google Chrome Help <https://support.google.com/chrome/answer/157179>`_

Vim
=============

Editing
--------------------

``i``
   Insert text before the cursor [count] times.

``I``
   Insert text before the first non-blank in the line [count] times.

``a``
   Appent text after the cursor [count] times. If the cursor is in the first column of an empty line Insert starts there.

``A``
   Appent text at the end of the line [count] times.

``o``
   Begin a new line below the cursor and insert text, repeat [count] times.

``O``
   Begin a new line above the cursor and insert text, repeat [count] times.

``u``
   Undo [count] changes.

``CTRL-r``
   Redo [count] changes which were undone.

Insert Mode
--------------------

``CTRL-w``
   `Delete word before the cursor during insert mode. <https://knowledge.sakura.ad.jp/22465/>`_

``CTRL-o``
   Execute one command, return to Insert mode.

``CTRL-t``
   indent (move right) line one shiftwidth during insert mode.

``CTRL-d``
   Delete one shiftwidth of indent at the start of the current line.

``CTRL-u``
   Delete all entered characters before the cursor in the current line.

Operator
--------------------

``["x]c{motion}``
   Delete {motion} text [into register x] and start insert.

``["x]d{motion}``
   Delete text that {motion} moves over [into register x].

``["x]y{motion}``
   Yank(copy) {motion} text [into register x].

``["x]yy``
   Yank(copy) [count] lines [into register x].

``gU{motion}``
   Make {motion} text uppercase.

``gu{motion}``
   Make {motion} text lowercase.

``>{motion}``
   Shift {motion} lines one 'shiftwidth' rightwards.

``<{motion}``
   Shift {motion} lines one 'shiftwidth' leftwards.

Motion
--------------------

``0``
   To the first character of the line.

``^``
   Start of line(after whitespace)

``$``
   End of line

``gg``
   Goto line [count], default first line.

``G``
   Goto line [count], default last line.

``b/w/B/W``
   Previous/next word

``f{char}/F{char}``
   Go forward/backward to character {char}

``;``
   Repeat latest f, t, F or T [count] times.

``,``
   Repeat latest f, t, F or T in opposite direction [count] times.

``%``
   Find the next item in this line after or under the cursor and ump to its match. Items can be: ([{}])

Visual mode
--------------------

``[count]v``
   Start Visual mode per character.

``[count]V``
   Start Visual mode per linewise.

``[count]Ctrl-V``
   Start Visual mode blockwise.

Clipboard
--------------------

``["x]y{motion}``
   Yank {motion} text [into register x ].

``["x]yy``
   Yank [count] lines [into register x ] linewise.

Text objects
--------------------

Usage
~~~~~~~~~~~~~~~~~~~~~~

Text objects let you operate (with an operator) in or aound text blocks(objects).

======== ==================== ===========
v        i                    p
Operator [i]nside or [a]round Text object
======== ==================== ===========

``p``
   Paragraph

``w``
   Word

``s``
   Sentence

``[({<``
   A [], (), {} or <>  block

``'"``
   A quoted string

Window commands
--------------------

``C-w w``
   Go to N next window (wrap around)

Misc
--------------------

``:h[elp] {subject}``
   Open a window and display the help file in read-only, additionally jump to the tag {subject}. `Prepend something to specify the context. e.g. Insert mode command is :help i_<Esc> <https://vimhelp.org/>`_

``.``
   Simple changes can be repeated with the "." command. Without a count, the count of the last change is used.
``:%s/foo/bar/g``
   Replace foo with bar in whole document.

.. note::
   `Vim cheatsheet <https://devhints.io/vim>`_


