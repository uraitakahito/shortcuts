==================
cmux
==================

.. Source: manaflow-ai/cmux web/data/cmux-shortcuts.ts at 12023d89f (release v0.65.2.2).
   Numbered keys (9 = last) and Esc, Esc: AppDelegate.swift, WorkspaceShortcutMapper and
   BrowserPanel.swift at the same commit.
   Copy and Paste: Ghostty 1.3.2 bundled with cmux (ghostty +list-keybinds --default).
   Copy Mode: TerminalKeyboardCopyModeKeyResolution.swift at the same commit.
   Claude Code: https://code.claude.com/docs/en/fullscreen
   Update by diffing these against the next release.

Default shortcuts of cmux 0.65.2 (113).
See `Keyboard Shortcuts <https://cmux.com/docs/keyboard-shortcuts>`_ for the full list.

App
=========================

``⌘ + ,``
   settings

``⌘ + ⇧ + ,``
   reload configuration

``⌃ + ⌘ + ⌥ + .``
   show/hide all cmux windows (system-wide hotkey)

``⌘ + ⌥ + f``
   global search (when cmux is active)

``⌘ + ⇧ + p``
   command palette

``⌘ + ⇧ + i``
   show agent inbox

``⌃ + n``
   command palette next result (in the command palette)

``⌃ + p``
   command palette previous result (in the command palette)

``⌘ + ⇧ + n``
   new window

``⌃ + ⌘ + w``
   close window

``⌃ + ⌘ + f``
   toggle full screen

``⌘ + ⇧ + o``
   reopen previous session

``⌘ + q``
   quit cmux

Workspaces
=========================

``⌘ + b``
   toggle left sidebar

``⌘ + ⌥ + b``
   toggle right sidebar

``⌘ + n``
   new local workspace

``⌘ + ⌥ + n``
   new browser workspace (the first surface is a browser pane)

``⌃ + ⌘ + s``
   save current workspace layout as a template

``⌘ + o``
   open folder

``⌘ + p``
   go to workspace (workspace switcher)

``⌃ + ⌘ + ]``
   next workspace

``⌃ + ⌘ + [``
   previous workspace

``⌃ + ⌘ + ⌥ + [``
   move workspace up

``⌃ + ⌘ + ⌥ + ]``
   move workspace down

``⌘ + [``
   focus back (outside browser panes)

``⌘ + ]``
   focus forward (outside browser panes)

``⌘ + 1-8``
   select workspace 1-8

``⌘ + 9``
   select the last workspace

``⌘ + ⇧ + r``
   rename workspace

``⌘ + ⌥ + e``
   edit workspace description

``⌘ + ;``
   mark workspace as done

``⌘ + ⇧ + ;``
   cycle workspace status one lane forward

``⌃ + ⌘ + g``
   new empty workspace group

``⌘ + ⇧ + g``
   group selected workspaces

``⌃ + ⌘ + .``
   collapse or expand focused workspace group

``⌃ + ⌘ + e``
   focus the workspace sidebar (↑/↓ select, Return or Esc goes back to the terminal)

``⌘ + ⇧ + e``
   toggle right-sidebar focus

``⌘ + ⇧ + w``
   close workspace

Surfaces
=========================

``⌘ + t``
   new surface

``⌘ + ⇧ + ]``
   next surface

``⌘ + ⇧ + [``
   previous surface

``⌘ + ⌥ + ⇧ + [``
   reorder surface left

``⌘ + ⌥ + ⇧ + ]``
   reorder surface right

``⌃ + ⌘ + ⇧ + [``
   move surface to previous pane

``⌃ + ⌘ + ⇧ + ]``
   move surface to next pane

``⌘ + ⌥ + ⇧ + Left/Right/Up/Down``
   move the surface to the pane in that direction

``⌃ + 1-8``
   select surface 1-8

``⌃ + 9``
   select the last surface

``⌘ + r``
   rename tab

``⌘ + w``
   close tab

``⌘ + ⌥ + t``
   close other tabs in pane

``⌘ + ⇧ + t``
   reopen last closed

``⌘ + ⇧ + m``
   toggle terminal copy mode

``⌘ + ⇧ + k``
   clear screen (keep scrollback)

Split Panes
=========================

``⌘ + ⌥ + Left/Right/Up/Down``
   focus the pane in that direction

``⌃ + ⌘ + 1-8``
   focus pane 1-8

``⌃ + ⌘ + 9``
   focus the last pane

``⌘ + d``
   split right

``⌘ + ⇧ + d``
   split down

``⌃ + ⌘ + n``
   new pane with auto layout (retiles all panes)

``⌘ + ⌥ + d``
   split browser right

``⌘ + ⌥ + ⇧ + d``
   split browser down

``⌘ + ⇧ + ↩``
   toggle pane zoom

``⌃ + ⌘ + =``
   increase font size for every terminal in the selected workspace

``⌃ + ⌘ + -``
   decrease font size for every terminal in the selected workspace

``⌃ + ⌘ + 0``
   reset font size for every terminal in the selected workspace

``⌃ + ⌘ + ⇧ + =``
   equalize split sizes

``⌃ + ⇧ + h/l/k/j``
   resize the pane left, right, up, or down

Browser
=========================

``⌘ + ⇧ + l``
   open browser

``⌘ + l``
   focus address bar

``⌘ + [``
   back (in a browser pane)

``⌘ + ]``
   forward (in a browser pane)

``⌘ + r``
   reload page (in a browser pane)

``⌘ + ⇧ + r``
   hard refresh page (in a browser pane)

``⌘ + =``
   zoom in

``⌘ + -``
   zoom out

``⌘ + 0``
   actual size

``⌘ + ⌥ + i``
   toggle browser developer tools

``⌘ + ⌥ + c``
   show browser JavaScript console

``⌘ + ⌥ + ↩``
   enter browser focus mode (the page gets shortcuts first)

``Esc, Esc``
   leave browser focus mode (press twice within 1.6 seconds; the first Esc also reaches the page)

``⌃ + ⌘ + ⌥ + d``
   toggle browser design mode (select and edit elements visually)

``⌘ + ⇧ + g``
   toggle React Grab (in a browser pane)

Find
=========================

``⌘ + f``
   find

``⌘ + ⇧ + f``
   find in directory

``⌘ + g``
   find next

``⌘ + ⌥ + g``
   find previous

``⌘ + ⌥ + ⇧ + f``
   hide find bar

``⌘ + e``
   use selection for find

Notifications
=========================

``⌘ + i``
   show notifications

``⌘ + ⇧ + u``
   jump to latest unread

``⌘ + ⇧ + b``
   jump to the surface where you last sent an agent prompt

``⌘ + ⌥ + u``
   toggle current item unread state

``⌃ + ⌘ + u``
   mark current item as oldest unread and jump to the next latest unread

``⌘ + ⇧ + h``
   flash focused panel

Copy and Paste
=========================

``⌘ + c``
   copy the selection to the clipboard (selecting alone does not copy; ``⌃ + c`` stops the running command instead)

``⌘ + ⇧ + v``
   paste the last selection inside cmux (middle click does the same; other apps cannot paste it)

``double-click``
   select a word (``/`` and ``.`` do not split words, so a path such as ``src/todo.ts`` is one word)

``triple-click``
   select a line

``⌘ + triple-click``
   select the whole output of one command (needs shell integration, which cmux sets up for zsh)

``⌥ + drag``
   select a rectangle, such as one column of a table

``⇧ + click``
   extend or shrink the selection to the clicked point

``⇧ + Left/Right/Up/Down``
   move the end of the selection (only while text is selected)

``⇧ + drag``
   select with cmux inside apps that use the mouse, such as Claude Code, vim, and tmux

Claude Code
-------------------------

``drag``
   select text; it is copied to the clipboard when you release the mouse button (Copy on select in /config)

``⌃ + c``
   copy the selection; with nothing selected, interrupt as usual

``⌃ + o, [``
   write the whole conversation into the terminal as plain text, so cmux selection and copy mode can reach it

Copy Mode
=========================

``⌘ + ⇧ + m``
   enter or leave copy mode

``Esc/q``
   leave copy mode without copying

``h/j/k/l``
   move left, down, up, or right (arrow keys also work)

``0/^``
   move to the start of the line

``$``
   move to the end of the line

``gg``
   move to the top of the scrollback (``Home`` also works)

``G``
   move to the bottom (``End`` also works)

``{``
   move to the previous prompt

``}``
   move to the next prompt

``⌃ + u/d``
   scroll half a page up or down

``⌃ + b/f``
   scroll a page up or down (``PageUp`` and ``PageDown`` also work)

``⌃ + y/e``
   scroll a line up or down

``[count]{motion}``
   repeat a motion (``5j`` moves down five lines)

``v``
   start selecting by character (press again to stop selecting)

``V``
   start selecting by line

``y``
   copy the selection and leave copy mode

``yy``
   copy the current line and leave copy mode when nothing is selected (``3yy`` copies three lines)

``Y``
   same as ``y`` with a selection, otherwise same as ``yy``

``⌘ + c``
   copy the selection and stay in copy mode

``/``
   open the search bar

``n/N``
   move to the next or previous match
