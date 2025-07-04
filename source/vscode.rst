==================
Visual Studio Code
==================

General
=========================

``⌥ + Left(Right)``
   move by word

``⌃ + ⌘ + Left(Right)``
   move a tab from one of two split editors to another

``⌃ + 1``
   focus the editor

``⌘ + k, ⌘ + ⇧ + Left(Right)``
   move tab

Navigation
=========================

``⌃ + g``
   go to line

``⇧ + ⌘ + \``
   `Bracket matching <https://code.visualstudio.com/docs/editor/editingevolved#_bracket-matching>`_

``⇧ + F12``
   go to references

multi-cursor / Selection
=========================

.. ``⌘ + d``
..    select current word

``⇧ + ⌥ + Left(Right)``
   extend selection by word

``⇧ + ⌥ + ⌘ + Up/Down/Left/Right``
   column box selection

``⌘ + ⇧ + l``
   Select all occurrences of current selection

Editing
=========================

.. ``⌘ + x``
..    Cut line(empty selection)

.. ``⌘ + c``
..    Copy line(empty selection)

``⌘ + ⏎``
   insert line below

``⇧ + ⌘ + ⏎``
   insert line above

``⌥ + Up/Down``
   move line up/down

``⌘ + ⇧ + h``
   Replace text in bulk

Window Management
=========================

``⌘ + 1/2``
   Focus into First/Second Editor Group

``⌘ + ⇧ + ]``
   Move to previous terminal

``⌥ + ⌘ + ⇦``
   Move to previous editor

``⌥ + ⌘ + ⇨``
   Move to next editor


Display
=========================

``⌃ + ⇧ + g``
   Show source control

``⌘ + k + v``
   Open Preview to the Side

``⌃ + ```
   Toggle integrated terminal


Development
=========================

``⇧ + ⌘ + O``
   You can navigate symbols inside a file with ⇧⌘O. By typing : the symbols will be grouped by category. Press Up or Down and navigate to the place you want. ( `See Also <https://code.visualstudio.com/docs/editor/editingevolved#_go-to-symbol>`_ )

``⌃ + ⌘ + i``
   Copilot Chat

``⌘ + k, ⌘ + l``
   Expand/Collapse current code block

Panel
----------------

``⌘ + ⇧ + u``
   output

``⌘ + ⇧ + y``
   debug console

Sidebars
=========================

``⌘ + k, e``
   Explorer: Focus on Open Editors View

``⌥ + ⌘ + f``
   `Search for files in the File Explorer <https://code.visualstudio.com/updates/v1_94#_find-in-explorer>`_

Extensions
=========================

Bookmarks
----------------

``⌘ + ⌥ + k``
   Mark/unmark positions in your code

``⌘ + ⌥ + j/l``
   Jump forward and backward between bookmarks

GitHub Copilot
=========================

``^ + /``
   Accept Panel Suggestion at the Cursor

``⌘ + ⇨``
   Accept suggestion word by word

``⌥ + ⌘ + .``
   Debug Last Terminal Command

``⌥ + ]``
   Navigate to the Next Panel Suggestion

``⌥ + [``
   Navigate to the Previous Panel Suggestion

``^ + ⌘ + I``
   Toggle Copilot Chat

``⌘ + Backspace``
   `Undo requests <https://code.visualstudio.com/updates/v1_101#_chat-ux-improvements>`_

Context Variables
-------------------

``#selection``
   Selected text in the editor

``#terminalSelection``
   Selected text in the terminal

``#terminalLastCommand``
   Last executed command and its result in the terminal

``#codebase``
   Analyzes highly relevant code and files from the entire current workspace and adds them as context for prompts.

``#fetch``
   Retrieves web page content from the specified URL and adds it to the context.

``#<file or folder name>``
   By entering a file or folder name after # (e.g., #src/main.js), you can explicitly add the contents of that file or folder as context for the chat.

``#<symbol name>``
   By entering a symbol name such as function name, class name, or variable name after # (e.g., #myFunction), it searches for the definition and reference locations of the corresponding symbol from files in the workspace and adds them as context.

``#testFailure``
   Adds information about tests that failed in the most recent test execution as context. This is useful for debugging test code and identifying areas that need fixing.

Command Palette
=========================

``Dev Containers: Attach to Running Container``
   Attach to a Docker container

``Preferences: Open Keyboard Shortcuts``
   edit and find available key bindings

``Split Editor XXX``
   split an editor

``View: Move Editor Group XXX``
   move a tab from A to B

Core CLI options
=========================

``-d or --diff <file1> <file2>``
   Open a file difference editor. Requires two file paths as arguments.

``-r or --reuse-window``
   Forces opening a file or folder in the last active window.

.. note::
   `vscode cheat sheet <https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf>`_

