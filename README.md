Build your docker image:

```console
% PROJECT=$(basename `pwd`) && docker image build -t $PROJECT-image . --build-arg user_id=`id -u` --build-arg group_id=`id -g`
```

Run the Docker container:

```console
% docker container run -d --rm --init --mount type=bind,src=`pwd`,dst=/app --name $PROJECT-container $PROJECT-image
```

Use [fdshell](https://github.com/uraitakahito/dotfiles/blob/37c4142038c658c468ade085cbc8883ba0ce1cc3/zsh/myzshrc#L93-L101) to log in to Docker.

```console
% fdshell /bin/zsh
```

Run the following commands inside the Docker containers as needed:

```console
% uv sync
% uv run make site
```

Finally, open `build/html/index.html` (English) or `build/html/ja/index.html` (Japanese).

## Publishing

Merging into `main` runs
[`.github/workflows/pages.yml`](.github/workflows/pages.yml), which builds the
HTML with Sphinx in English and Japanese and deploys it to GitHub Pages:

- English: https://uraitakahito.github.io/shortcuts/
- Japanese: https://uraitakahito.github.io/shortcuts/ja/

Pull requests against `main` run the same build without deploying, so a
Sphinx warning, a broken toctree, or an untranslated message fails the check
before merge.

## Translating

English text lives in `source/*.rst`. Japanese text lives in
`source/locales/ja/LC_MESSAGES/*.po`, one file per page.

After editing a `.rst` file, refresh the catalogs and translate the new
`msgstr ""` entries:

```console
% uv run make po
```

Keys such as `⌘ + d` are left out of the catalogs; only the descriptions are
translated. Keep inline markup, such as literals and links, in the translation.

Run `uv run make clean` after changing a file in `source/_static`, because an
incremental build keeps the old copy.
