import click
import os

colors = {"ERROR": "red", "FILE": "blue", "DIR": "yellow"}
indent = 4

# ? it is a important deccorator for lunching click!
@click.command()
def hello():
    path = os.getcwd()
    if not path:
        click.echo(click.style("permission denied!", colors["ERROR"]))
    in_dir_file_list = os.listdir(path)
    max_char_len = max([len(i) for i in in_dir_file_list])
    for directory in in_dir_file_list:
        abs_dir = os.path.join(path, directory)
        current_len = len(directory)
        indent_needed = max_char_len - current_len + indent
        if os.path.isfile(abs_dir):
            # ? it is a important to add colorama for color styling!
            click.echo(click.style(
                " ".join([directory, " "*indent_needed,    "--file--"]), fg=colors["DIR"]))
        else:
            click.echo(click.style(
                " ".join([directory,  " "*indent_needed,  "--dir--"]), fg=colors["FILE"]))


if __name__ == '__main__':
    hello()
