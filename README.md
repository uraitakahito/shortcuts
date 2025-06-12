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
% uv run make html
```

Finally, open the `build/html/index.html`.
