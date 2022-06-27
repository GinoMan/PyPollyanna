# main.py File Notes #

## Summary ##

This file contains the main method as well as some miscellaneous methods and a global that is used by the main function and its ancillary functions. Other files are reserved for particular classes within a domain and are documented in their respective markdown files.

## Imports ##

This program imports several standard as well as external libraries:

### Standard Library ###

`argparse`: `ArgumentParser`, `Namespace`, `RawTextHelpFormatter`
`datetime`: `datetime`
`os`: `path`, `system`, `get_terminal_size`
`pathlib`: `Path`
`random`: `choice`
`tempfile`: `gettempdir`

### Packages ###

`colorama`: `Back`, `Fore`, `Style`, `deinit`, `init`
`minify_html`: `minify` <- PyLance cannot find this function
`progress.bar`: `IncrementalBar`

### Custom Classes ###

`Person`: `Person`, `PollyannaGroup`
`SendEmail`: `Email`, `TXTHandler`
`Templates`: `ContestSettings`, `EmailTemplate`

## app_description ##

This variable contains a detailed description of the app used in the help text.

## reset_terminal_colors() -> None ##

## show_header() -> None ##

## display_example(person: Person, template: EmailTemplate, txtTemplate: EmailTemplate) -> None ##

## display_group(group: PollyannaGroup) -> None ##

## display_associations(group: PollyannaGroup) -> None ##

## negative_answer(prompt_str: str, pos_answer:str='Y') -> bool ##

## parse_arguments() -> Namespace ##

## save_csv(group: PollyannaGroup) -> None ##

## email_group(group: PollyannaGroup, template: EmailTemplate, txtTemplate: EmailTemplate, is_test: bool) -> None ##

## main() -> None ##

## if __name__ == '__main__' invocation ##