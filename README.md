# join-lines
A simple neovim's plugin for joining lines with a delimiter

## Dependencies
It makes use of `neovim`'s remote plugin architecture through which plug-n-play plugins can be written in any languages.
`neovim`, `python3` and `pip3` is required.

```bash
sudo add-apt-repository ppa:neovim-ppa/stable
sudo apt-get update
sudo apt-get install neovim
```

```bash
sudo pip3 install neovim
```
-----

## Installation

- Clone this repository
- Put the folder to `vim-plugs` to plugin directory.
- Update the remote plugins using `UpdateRemotePlugins`
- Reload vim configurations

## Usage
In normal mode, enter vim commands with `exec` function.  

Eg:
```bash
:exec Join(3, 6, ",")
```
It joins lines from 3 to 6 with comma

