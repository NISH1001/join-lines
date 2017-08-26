#!/usr/bin/env python3

import neovim

@neovim.plugin
class Main:
    def __init__(self, vim):
        self.vim = vim

    @neovim.function("Join")
    def join(self, args):
        args_str = list(map(str, args))
        command = join_lines(args_str[0], args_str[1], args_str[2])
        self.vim.command( command )


def join_lines(start, end, delimiter=" "):
    command = r":{},{}-1s/\n/{}/g".format(start, end, delimiter)
    return command
