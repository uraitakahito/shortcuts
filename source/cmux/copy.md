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

The keys, with figures and examples, are on their own page: [Selecting text with the keyboard (copy mode)](copy-mode.md).

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
