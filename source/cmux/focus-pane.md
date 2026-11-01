# Returning to the Claude Code pane

When a browser pane has focus, these keys bring focus back to the terminal where Claude Code runs, without the mouse. Figures show which key moves to which pane, and the end of the page covers what to check when a key does not work.

:::{admonition} In short
:class: tip

1. Press {kbd}`⌘+⌥+←` (Command, Option, and the left arrow). Focus moves to the pane on the left. Pressed in a browser on the right, it returns to Claude Code in the middle, and you can type right away.
2. {kbd}`⌃+⌘+1` (Control, Command, and 1) also works. It moves to pane 1 wherever focus is. In the layout below, pane 1 is the Claude Code terminal.
3. Both work even when focus is in a text field or the address bar of the browser. Only browser focus mode blocks them, so press {kbd}`Esc` twice to leave it first.
:::

## The keys

Both are three keys pressed together. {kbd}`⌥` and {kbd}`⌘` sit next to each other at the bottom left of the keyboard, and {kbd}`⌃` is further to the left.

:::{figure} figures/focus-keys.svg
:alt: Option, Command, and the left arrow move to the pane on the left. Control, Command, and 1 move to pane 1.

The keys. The top three move to the pane on the left, and the bottom three move to pane 1.
:::

## Which pane you move to

Take a window that shows, from left to right, the sidebar, a terminal running Claude Code, and a browser. The terminal and the browser are panes that split one workspace into left and right. The left one is pane 1 and the right one is pane 2.

:::{figure} figures/focus-panes.svg
:alt: With focus on the browser pane on the right, Command Option left arrow moves focus to the terminal pane on its left. The terminal is pane 1 and the browser is pane 2.

With focus on the browser (pane 2), {kbd}`⌘+⌥+←` moves to the terminal on its left (pane 1). {kbd}`⌃+⌘+1` moves to pane 1 from anywhere.
:::

| Keys | Moves to |
| --- | --- |
| {kbd}`⌘+⌥+←` {kbd}`⌘+⌥+→` {kbd}`⌘+⌥+↑` {kbd}`⌘+⌥+↓` | The next pane to the left, right, top, or bottom. At the edge nothing happens. Focus does not wrap around to the other side or move to the sidebar. |
| {kbd}`⌃+⌘+1` to {kbd}`⌃+⌘+8` | The pane with that number. Nothing happens for a number that has no pane. |
| {kbd}`⌃+⌘+9` | The last pane. |

- **After moving**: when the pane you move to is a terminal, you can type right away and keep writing to Claude Code. If you used the TextBox in that terminal before, focus goes back to the TextBox.
- **Works anywhere**: both keys work wherever focus is in the browser, whether on the page, in a text field on it, or in the address bar, because cmux receives the keys before the page does. They also work in the middle of Japanese input conversion.

## With three or more panes

Panes are numbered from the left (or top) side of each split. When a side is split again, its panes are numbered in the same order. For example, splitting the browser on the right into top and bottom gives the following.

:::{figure} figures/focus-numbers.svg
:alt: With three panes, the terminal on the left is 1, the browser at the top right is 2, and the terminal at the bottom right is 3. Control Command 9 moves to pane 3, the last one.

Pane numbers with three panes. The left group is 1, and the right group is 2 and 3 from the top. {kbd}`⌃+⌘+9` moves to the last pane. From either pane on the right, {kbd}`⌘+⌥+←` moves to the terminal on the left.
:::

## Keys that look alike

These keys look similar and are easy to press when you mean to move focus. This is what they do when the browser has focus.

| Keys | What it does |
| --- | --- |
| {kbd}`⌘+[` {kbd}`⌘+]` | Back and forward in the browser. Focus stays in the pane. In a terminal, they go back and forward through the workspaces you had open. |
| {kbd}`⌘+⇧+B` | Moves to the pane where you last sent a prompt. With Claude Code running in several workspaces, this may move to another workspace or window. |
| {kbd}`⌘+⌥+⇧+←` {kbd}`⌘+⌥+⇧+→` | Moves the open tab to the pane on the left or right. It does not move focus. |
| {kbd}`⌃+1` to {kbd}`⌃+9` | Selects a tab within the current pane. |
| {kbd}`⌘+1` to {kbd}`⌘+9` | Selects a workspace. |
| {kbd}`⌘+⌥+↩` | Enters browser focus mode. While it is on, cmux keys stop working, as the next section explains. |
| {kbd}`⌘+⇧+H` | Flashes the focused pane. Use it when you cannot tell where focus is. |

## When the keys do not work

### Browser focus mode

If a focus mode badge appears over the browser, browser focus mode is on. While it is on, every key goes to the page, and neither {kbd}`⌘+⌥+←` nor {kbd}`⌃+⌘+1` works.

To leave, press {kbd}`Esc` twice within 1.6 seconds. After the first press, the badge asks for one more {kbd}`Esc`, and the second press leaves. The first {kbd}`Esc` also reaches the page. Clicking the badge or another pane leaves too. {kbd}`⌘+⌥+↩` only enters focus mode and does not leave it.

### Already in the leftmost pane

In the leftmost pane, {kbd}`⌘+⌥+←` does nothing.

### Caps Lock

According to the cmux 0.65.2 source, shortcuts that use arrow keys also compare the Caps Lock state, so {kbd}`⌘+⌥+←` may not work while Caps Lock is on. Number shortcuts ignore Caps Lock, so use {kbd}`⌃+⌘+1` in that case. This was not confirmed by pressing the keys.

## Telling where focus is

- A terminal pane without focus is slightly dimmed. A browser pane is not dimmed even without focus.
- A pane without focus shows its tab bar in a lighter color.
- If you are not sure, press {kbd}`⌘+⇧+H` to flash the focused pane.

## Changing the keys

Change them under Keyboard Shortcuts in Settings ({kbd}`⌘+,`). The actions are Focus pane left for {kbd}`⌘+⌥+←` and Focus pane 1…9 for {kbd}`⌃+⌘+1`.

In `~/.config/cmux/cmux.json`, change `focusLeft` ({kbd}`⌘+⌥+←`) or `focusPaneByNumber` ({kbd}`⌃+⌘+1`) under `shortcuts.bindings`.

## About this guide

Checked with cmux 0.65.2 (build 113) on macOS. The default keys, where they work, how panes are numbered, and how to leave focus mode were checked in the cmux source at tag v0.65.2 and in the source of Bonsplit, the component that splits panes. The keys were not pressed to confirm.

- [cmux keyboard shortcuts](https://cmux.com/docs/keyboard-shortcuts)
- [cmux configuration](https://cmux.com/docs/configuration)
