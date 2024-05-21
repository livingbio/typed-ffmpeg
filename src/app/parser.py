import shlex
from scripts.cache import load
from ffmpeg.common.schema import FFMpegOptionList, FFMpegOptionType, FFMpegOption
from ffmpeg.base import input, output
from typing import Any

option_list = load(FFMpegOptionList, "list")



def parse(cmd: str) -> Any:
    """
    Parse the command line arguments and return the options.
    Options has Input Option, Output Option, Global Option, and Filter Option.
    """

    option_dict = {
        k.name: k for k in option_list.options
    }

    arguments = shlex.split(cmd)

    assert arguments.pop(0) == "ffmpeg"

    parsed_options: dict[str, tuple[FFMpegOption, str | bool]] = {}
    
    nodes = []
    while arguments:
        arg = arguments.pop(0)
        if arg == "-i":
            filename = arguments.pop(0)

            nodes.append(input(filename=filename, **{k: parsed_options[k] for k in parsed_options if parsed_options[k][0].is_input_option}))
            parsed_options = {k: parsed_options[k] for k in parsed_options if not parsed_options[k][0].is_input_option}

            assert not {k: parsed_options[k] for k in parsed_options if parsed_options[k][0].is_output_option}, f"Output options must not be specified before input files, {parsed_options}"

        elif arg.startswith("-"):
            arg = arg.lstrip("-")
            arg_name = arg.split(":")[0]
            assert arg_name in option_dict, f"Unknown option {arg_name}"

            option = option_dict[arg_name]

            arg_value: str | bool
            if option.type == FFMpegOptionType.OPT_TYPE_BOOL:
                arg_value = True
            else:
                arg_value = arguments.pop(0)

            # option is not exclusive, for example -c are both input and output options
            parsed_options[arg] = (option, arg_value)
        else:
            # should be output file
            nodes.append(output(filename=arg, **{k: parsed_options[k][1] for k in parsed_options if parsed_options[k][0].is_output_option}))
            parsed_options = {k: parsed_options[k] for k in parsed_options if not parsed_options[k][0].is_output_option}

            assert not {k: parsed_options[k] for k in parsed_options if parsed_options[k][0].is_input_option}, f"Input options must not be specified after output files, {parsed_options}"

    if parsed_options:
        # handle globla nodes
        ...

    print(nodes)

parse("ffmpeg -i input.mp4 -c:v libx264 -c:a aac output.mp4")
parse("ffmpeg -i input.mp4 -c:a aac output.mp4 -c:v libx264 -c:a aac output.mp4")