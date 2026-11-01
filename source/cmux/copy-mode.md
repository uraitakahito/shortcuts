# Selecting text with the keyboard (copy mode)

This guide shows how to select text in a cmux terminal with the keyboard only and copy it to the clipboard, using cmux's copy mode. For selecting with the mouse, see [Copying text from the terminal](copy.md).

:::{admonition} In short
:class: tip

1. Press {kbd}`⌘+⇧+M` to enter copy mode. The pane shows "vim" at the top right.
2. Move the cursor with {kbd}`h` {kbd}`j` {kbd}`k` {kbd}`l`, as in vim.
3. Press {kbd}`v` to select by character, or {kbd}`V` to select whole lines. Moving the cursor then extends the selection.
4. Press {kbd}`y` to copy. The text goes to the clipboard, and copy mode ends. To copy only the cursor line, press {kbd}`y` {kbd}`y` without selecting.
5. Press {kbd}`Esc` or {kbd}`q` to leave without copying.
:::

## How copy mode works

To select without the mouse, use cmux's copy mode. You move around the screen with keys like vim's, select a range, and copy it. Lines that have scrolled out of view can be selected too. Text copied in copy mode always goes to the clipboard, whatever the copy on select setting.

:::{figure} figures/copy-mode.svg
:alt: Command Shift M enters copy mode, v or V starts a selection, and y copies and leaves. yy copies the cursor line. Esc or q quits.

How copy mode works. {kbd}`⌘+⇧+M` enters it, {kbd}`v` or {kbd}`V` starts a selection, and {kbd}`y` copies. Copying ends copy mode. While copy mode is on, the pane shows "vim" at the top right.
:::

| Keys | What it does |
| --- | --- |
| {kbd}`⌘+⇧+M` | Enters copy mode. Press it again to leave. |
| {kbd}`Esc` {kbd}`q` | Leaves without copying. The selection is cleared. |

### Example: copying two lines a little higher up

1. Press {kbd}`⌘+⇧+M`. The pane shows "vim" at the top right, and a box marks the cursor.
2. Press {kbd}`k` to go up to the first line you want. Typing a number first, as in {kbd}`5` {kbd}`k`, moves five lines at once.
3. Press {kbd}`V` ({kbd}`⇧+V`) to start selecting by line.
4. Press {kbd}`j` to extend the selection to the second line.
5. Press {kbd}`y`. The two lines go to the clipboard, and copy mode ends.

## Moving the cursor

The box that copy mode draws is the cursor. The keys are vim's: {kbd}`h` {kbd}`j` {kbd}`k` {kbd}`l` move one step, and other keys go further. While you are selecting, the box is hidden, and the same keys move the end of the selection.

:::{figure} figures/copy-mode-moves.svg
:alt: k, Control U, Control B, and gg go up by one line, half a screen, one screen, and to the very top. j, Control D, Control F, and G go down the same way. h and l move one character, 0 goes to the start of the line, and $ to the end.

Where the movement keys go. Up and down on the left, along a line on the right. A number typed first repeats the key.
:::

| Keys | What it does |
| --- | --- |
| {kbd}`h` {kbd}`j` {kbd}`k` {kbd}`l` | One step left, down, up, or right. The arrow keys do the same. |
| {kbd}`0` {kbd}`^` / {kbd}`$` | To the start of the line / to the end of the line |
| {kbd}`g` {kbd}`g` / {kbd}`G` | To the very top, the first line that has scrolled out of view / to the bottom. {kbd}`Home` / {kbd}`End` do the same. |
| {kbd}`{` / {kbd}`}` | Scrolls up to the previous prompt / down to the next prompt. |
| {kbd}`⌃+U` / {kbd}`⌃+D` | Scrolls half a screen up / down. |
| {kbd}`⌃+B` / {kbd}`⌃+F` | Scrolls a full screen up / down. {kbd}`PageUp` / {kbd}`PageDown` do the same. |
| {kbd}`⌃+Y` / {kbd}`⌃+E` | Scrolls one line up / down. |
| A number | Repeats the next key that many times. {kbd}`5` {kbd}`j` moves down five lines. |

- **At the edge of the pane**: moving the cursor past the top or bottom of the pane scrolls the screen with it.
- **Keys that scroll**: keys such as {kbd}`⌃+U` and {kbd}`{` keep the cursor on the same text while that text is still in view. Otherwise the cursor moves to the top or bottom edge of the pane.
- **While selecting**: {kbd}`⌃+U` and {kbd}`⌃+D` move a full screen, like {kbd}`⌃+B` and {kbd}`⌃+F`.
- **0 in a number**: {kbd}`0` alone goes to the start of the line. After another digit it is part of the number, so {kbd}`1` {kbd}`0` {kbd}`k` moves up ten lines.

## Selecting by character or by line

There are two ways to select. {kbd}`v` selects from the character where you started to the cursor. {kbd}`V` selects whole lines, from the line where you started to the cursor line. Use {kbd}`V` for lines of output, and {kbd}`v` for part of a line, such as a path or a commit ID.

:::{figure} figures/copy-mode-select.svg
:alt: With v, the selection runs from Fix on the second line to Add on the third. With V, the second and third lines are selected whole.

The same start point and cursor, selected with {kbd}`v` and with {kbd}`V`. The selection was started at "Fix", and the cursor is on "Add".
:::

| Keys | What it does |
| --- | --- |
| {kbd}`v` | Starts selecting by character. Press it again to stop selecting; copy mode stays on. |
| {kbd}`V` | Starts selecting by line. |

- **Switching to lines**: pressing {kbd}`V` while selecting by character starts a new line selection at the cursor line. The earlier start point is dropped.
- **Several lines at once**: {kbd}`3` {kbd}`V` selects the cursor line and the two lines below it.

## Copying

| Keys | What it does |
| --- | --- |
| {kbd}`y` | Copies the selection and leaves copy mode. |
| {kbd}`y` {kbd}`y` | With nothing selected, copies the line with the cursor and leaves. {kbd}`3` {kbd}`y` {kbd}`y` copies the cursor line and the two lines below it. |
| {kbd}`Y` | Same as {kbd}`y` with a selection, and as {kbd}`y` {kbd}`y` without one. |
| {kbd}`⌘+C` | Copies the selection. Copy mode stays on. |

Paste with {kbd}`⌘+V`, in cmux or in any other app.

## Searching

| Keys | What it does |
| --- | --- |
| {kbd}`/` | Opens the search bar. |
| {kbd}`n` / {kbd}`N` | To the next match / to the previous match |

## Common tasks

### Copying one line

1. Press {kbd}`⌘+⇧+M`.
2. Go to the line with {kbd}`k` or {kbd}`j`.
3. Press {kbd}`y` {kbd}`y`.

### Copying part of a line, such as a path

1. Press {kbd}`⌘+⇧+M`, and move the cursor to the first character you want. {kbd}`0` goes to the start of the line, and a number such as {kbd}`8` {kbd}`l` moves eight characters at once.
2. Press {kbd}`v`.
3. Move to the last character with {kbd}`l`, or to the end of the line with {kbd}`$`.
4. Press {kbd}`y`.

### Copying lines further up

1. Press {kbd}`⌘+⇧+M`.
2. Scroll up with {kbd}`⌃+U` or {kbd}`⌃+B` until the lines are in view. {kbd}`{` goes back one prompt at a time, and {kbd}`g` {kbd}`g` goes to the very top.
3. Move the cursor to the first line, and press {kbd}`V`.
4. Extend the selection with {kbd}`j`, and press {kbd}`y`.

## Good to know

- **Not available**: vim's {kbd}`w` {kbd}`b` {kbd}`e` (moving by word) and rectangular selection. For a rectangle, use {kbd}`⌥` + drag with the mouse.
- **Other keys**: keys not in the tables above are ignored. {kbd}`⌃+C` is ignored too, so copy mode never stops a running command by accident. Keys with {kbd}`⌘` work as usual.
- **Japanese input**: even with Japanese input on, keys are read by their position on the keyboard.
- **Caps Lock**: Caps Lock is ignored, so {kbd}`V` {kbd}`Y` {kbd}`G` {kbd}`N` typed with it work as {kbd}`v` {kbd}`y` {kbd}`g` {kbd}`n`. Hold {kbd}`⇧` for the capital letters.
- **Other ways in**: copy mode is not in the menu bar. Besides the key, you can enter it with Toggle terminal copy mode in the command palette ({kbd}`⌘+⇧+P`). To change {kbd}`⌘+⇧+M`, set `shortcuts.bindings.toggleTerminalCopyMode` in `cmux.json`.

## About this guide

Checked with cmux 0.65.2 (build 113) on macOS. The keys and what they do were checked in the cmux source at tag v0.65.2 and in the source of the Ghostty that cmux uses (`cb1ef7091c`). The keys were not pressed to confirm.

- [cmux keyboard shortcuts](https://cmux.com/docs/keyboard-shortcuts)
- [cmux configuration](https://cmux.com/docs/configuration)
