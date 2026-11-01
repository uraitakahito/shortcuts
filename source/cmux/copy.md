# Copying text from the terminal

This guide shows how to select text in a cmux terminal and copy it to the clipboard in three ways: with the mouse, with the keyboard only (copy mode), and inside apps that use the mouse, such as Claude Code.

:::{admonition} In short
:class: tip

1. Drag over the text and press {kbd}`⌘+C`. Press {kbd}`⌘+V` in another app to paste it.
2. By default, selecting alone does not put the text on the clipboard. Do not forget {kbd}`⌘+C`.
3. To select with the keyboard only, press {kbd}`⌘+⇧+M` to enter copy mode. Start with {kbd}`v`, extend with {kbd}`h` {kbd}`j` {kbd}`k` {kbd}`l`, and copy with {kbd}`y`.
4. On the Claude Code screen, a drag is selected by Claude Code and copied when you release the mouse button. To select with cmux, hold {kbd}`⇧` while dragging.
:::

## Select with the mouse and press ⌘C

Dragging over text colors the range. That range is the selection. Press {kbd}`⌘+C` to put the selected text on the clipboard. It works the same as Edit > Copy in the menu bar, or Copy in the right-click menu.

Besides dragging, there are several ways to select. The figure compares the range each one selects on the same screen.

:::{figure} figures/copy-select.svg
:alt: The range selected by a drag, a double-click, a triple-click, Command with a triple-click, Option with a drag, and Shift with a click

The range each action selects, in blue. The screen shows the output of `wc -l src/*.ts`, and the pointer marks where the button was released or clicked.
:::

| Action | What it selects |
| --- | --- |
| Drag | From where you press to where you release. Dragging past the top or bottom of the pane scrolls as it selects. |
| Double-click | One word. Spaces and symbols such as `( ) [ ] { } : ; , \| $` separate words. `/` and `.` do not, so a path such as `src/todo.ts` is one word. A URL is selected whole. |
| Triple-click | One line. A line wrapped at the pane width counts as one line, and spaces at either end are left out. On a prompt line, only the command you typed is selected. |
| {kbd}`⌘` + triple-click | The whole output of one command around the click. This works when the shell tells cmux where its prompts are, and cmux sets this up for zsh. |
| {kbd}`⌥` + drag | A rectangle. Use it to take just one column of a table. |
| {kbd}`⇧` + click | Extends or shrinks the selection to the clicked point. The start of the selection stays where it is. |
| {kbd}`⇧` + arrow keys | Moves the end of the selection with the keyboard. With nothing selected, the keys go to the shell or app as usual. |

- **After copying**: the selection stays colored after you copy. One click or typing a character clears it, and so does starting to type with Japanese input.
- **What is copied**: spaces at the end of each line are trimmed, and a line wrapped at the pane width is joined back into one line.
- **Colors**: colors are copied along with the text, as HTML. Pasting into a mail or notes app may keep them. To paste only the text, use {kbd}`⌘+⌥+⇧+V` (Paste and Match Style) in the app you paste into.

:::{admonition} ⌘C and ⌃C are different keys
:class: warning

In a terminal, {kbd}`⌃+C` does not copy. It stops the running command. Use {kbd}`⌘+C` to copy.
:::

## Selecting alone does not reach other apps

By default, text you select with the mouse goes to cmux's selection clipboard, not to the clipboard. Inside cmux you can paste it with a middle click or {kbd}`⌘+⇧+V`, but {kbd}`⌘+V` in other apps cannot see it. To paste into another app, put the text on the clipboard with {kbd}`⌘+C`.

:::{figure} figures/copy-clipboard.svg
:alt: Selecting fills the cmux selection clipboard, which only cmux can paste from. Command C fills the clipboard that every app can paste from.

Where selected text goes. Selecting alone fills only the cmux selection clipboard. To fill the clipboard that other apps paste from, press {kbd}`⌘+C`.
:::

### Copying on selection

Turn on copy on select under Terminal in Settings ({kbd}`⌘+,`). Selected text then goes to both the clipboard and the selection clipboard. It is off by default.

Also turn on the copy confirmation in the same place, and a short message appears each time a mouse selection is copied.

To set it in `~/.config/cmux/cmux.json` instead, write the following, then run `cmux reload-config` to apply it.

```json
{
  "terminal": {
    "copyOnSelect": true
  }
}
```

## Selecting with the keyboard (copy mode)

To select without the mouse, use cmux's copy mode. You move around the screen with keys like vim's, select a range, and copy it. Lines that have scrolled out of view can be selected too. Text copied in copy mode always goes to the clipboard, whatever the copy on select setting.

:::{figure} figures/copy-mode.svg
:alt: Command Shift M enters copy mode, v or V starts a selection, and y copies and leaves. yy copies the cursor line. Esc or q quits.

How copy mode works. {kbd}`⌘+⇧+M` enters it, {kbd}`v` or {kbd}`V` starts a selection, and {kbd}`y` copies. Copying ends copy mode. While copy mode is on, the pane shows "vim" at the top right.
:::

### Example: copying two lines a little higher up

1. Press {kbd}`⌘+⇧+M`. The pane shows "vim" at the top right, and a box marks the cursor.
2. Press {kbd}`k` to go up to the first line you want. Typing a number first, as in {kbd}`5` {kbd}`k`, moves five lines at once.
3. Press {kbd}`V` ({kbd}`⇧+V`) to start selecting by line.
4. Press {kbd}`j` to extend the selection to the second line.
5. Press {kbd}`y`. The two lines go to the clipboard, and copy mode ends.

### Copy mode keys

Enter and leave:

| Keys | What it does |
| --- | --- |
| {kbd}`⌘+⇧+M` | Enters copy mode. Press it again to leave. |
| {kbd}`Esc` {kbd}`q` | Leaves without copying. The selection is cleared. |

Move. While you are selecting, the end of the selection moves:

| Keys | What it does |
| --- | --- |
| {kbd}`h` {kbd}`j` {kbd}`k` {kbd}`l` | One step left, down, up, or right. The arrow keys do the same. |
| {kbd}`0` {kbd}`^` / {kbd}`$` | To the start of the line / to the end of the line |
| {kbd}`g` {kbd}`g` / {kbd}`G` | To the very top, the first line that has scrolled out of view / to the bottom. {kbd}`Home` / {kbd}`End` do the same. |
| {kbd}`{` / {kbd}`}` | To the previous prompt / to the next prompt |
| {kbd}`⌃+U` / {kbd}`⌃+D` | Scrolls half a screen up / down. |
| {kbd}`⌃+B` / {kbd}`⌃+F` | Scrolls a full screen up / down. {kbd}`PageUp` / {kbd}`PageDown` do the same. |
| {kbd}`⌃+Y` / {kbd}`⌃+E` | Scrolls one line up / down. |
| A number | Repeats the next key that many times. {kbd}`5` {kbd}`j` moves down five lines. |

Select:

| Keys | What it does |
| --- | --- |
| {kbd}`v` | Starts selecting by character. Press it again to stop selecting; copy mode stays on. |
| {kbd}`V` | Starts selecting by line. |

Copy:

| Keys | What it does |
| --- | --- |
| {kbd}`y` | Copies the selection and leaves copy mode. |
| {kbd}`y` {kbd}`y` | With nothing selected, copies the line with the cursor and leaves. {kbd}`3` {kbd}`y` {kbd}`y` copies three lines. |
| {kbd}`Y` | Same as {kbd}`y` with a selection, and as {kbd}`y` {kbd}`y` without one. |
| {kbd}`⌘+C` | Copies the selection. Copy mode stays on. |

Search:

| Keys | What it does |
| --- | --- |
| {kbd}`/` | Opens the search bar. |
| {kbd}`n` / {kbd}`N` | To the next match / to the previous match |

- **Not available**: vim's {kbd}`w` {kbd}`b` {kbd}`e` (moving by word) and rectangular selection. For a rectangle, use {kbd}`⌥` + drag with the mouse.
- **Other keys**: keys not in the tables above are ignored. {kbd}`⌃+C` is ignored too, so copy mode never stops a running command by accident. Keys with {kbd}`⌘` work as usual.
- **Japanese input**: even with Japanese input on, keys are read by their position on the keyboard.
- **Other ways in**: copy mode is not in the menu bar. Besides the key, you can enter it with Toggle terminal copy mode in the command palette ({kbd}`⌘+⇧+P`). To change {kbd}`⌘+⇧+M`, set `shortcuts.bindings.toggleTerminalCopyMode` in `cmux.json`.

## Selecting inside apps that use the mouse, such as Claude Code

Some apps take mouse events themselves, such as Claude Code in fullscreen, vim with `set mouse=a`, and tmux with `set -g mouse on`. A plain drag then goes to the app, not to cmux.

In fullscreen (the `"tui": "fullscreen"` setting), Claude Code selects text itself when you drag on its screen.

:::{figure} figures/copy-claude-code.svg
:alt: A drag without Shift is selected by Claude Code and copied on release. A drag with Shift held is selected by cmux and copied with Command C.

Where a drag on the Claude Code screen goes. Without {kbd}`⇧`, Claude Code selects and copies automatically. With {kbd}`⇧` held, cmux selects.
:::

| How | Result |
| --- | --- |
| Drag | Claude Code selects, and the text goes to the clipboard when you release the mouse button. This is Copy on select in Claude Code's `/config`, which is on by default. A double-click selects a word and a triple-click a line. |
| {kbd}`⇧` + drag, then {kbd}`⌘+C` | cmux selects. Keep {kbd}`⇧` held until you release the mouse button. The same works in vim and tmux. |
| `/copy` | Copies Claude Code's last response. `/copy 2` copies the one before it. If the response has code blocks, a screen asks which part to copy. |
| {kbd}`⌃+O`, then {kbd}`[` | Writes the whole conversation out as ordinary terminal text. Fullscreen Claude Code draws only what fits on the screen, so use this to handle a long conversation with cmux selection or copy mode. {kbd}`Esc` or {kbd}`q` goes back. |
| Start with `CLAUDE_CODE_DISABLE_MOUSE=1` | Claude Code no longer takes the mouse, so a plain drag selects with cmux. Clicking and wheel scrolling stop working in Claude Code, while {kbd}`PageUp` and {kbd}`PageDown` still scroll. |

:::{admonition} ⌃C means something else in Claude Code
:class: warning

While something is selected in Claude Code, {kbd}`⌃+C` copies. With nothing selected, it interrupts as usual.
:::

## About this guide

Checked with cmux 0.65.2 (build 113), the Ghostty 1.3.2-HEAD (`cb1ef7091c`) built into cmux, Claude Code 2.1.316, and macOS. The default keys and settings come from `ghostty +list-keybinds --default` and `ghostty +show-config --default --docs` bundled with cmux. cmux's behavior, such as the copy mode keys, the selection clipboard, and the menus, comes from the cmux source at tag v0.65.2. The selection rules come from the Ghostty source that cmux uses, and Claude Code's behavior from its documentation. The keys were not pressed to confirm.

- [cmux keyboard shortcuts](https://cmux.com/docs/keyboard-shortcuts)
- [cmux configuration](https://cmux.com/docs/configuration)
- [Ghostty configuration reference](https://ghostty.org/docs/config/reference)
- [Claude Code fullscreen](https://code.claude.com/docs/en/fullscreen)
