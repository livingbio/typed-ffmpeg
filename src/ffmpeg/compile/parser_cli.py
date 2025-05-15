import enum  
import re  
from typing import Dict, List, Optional, Tuple, Union, Callable, Any  
  
# Option types  
class OptionType(enum.Enum):  
    BOOL = 1  
    INT = 2  
    FLOAT = 3  
    STRING = 4  
    FUNC = 5  
    FUNC_ARG = 6  # Function with argument  
  
# Stream list types  
class StreamList(enum.Enum):  
    ALL = 0  
    PROGRAM = 1  
    STREAM_GROUP = 2  
  
# Media types (simplified)  
class MediaType(enum.Enum):  
    UNKNOWN = -1  
    VIDEO = 0  
    AUDIO = 1  
    SUBTITLE = 2  
    DATA = 3  
    ATTACHMENT = 4  
  
class StreamSpecifier:  
    def __init__(self):  
        self.idx = -1  # Stream index  
        self.media_type = MediaType.UNKNOWN  
        self.stream_list = StreamList.ALL  
        self.list_id = -1  
        self.meta_key = None  
        self.meta_val = None  
  
    def __str__(self):  
        result = []  
        if self.media_type != MediaType.UNKNOWN:  
            result.append(f"media_type={self.media_type.name}")  
        if self.idx >= 0:  
            result.append(f"idx={self.idx}")  
        if self.stream_list != StreamList.ALL:  
            result.append(f"stream_list={self.stream_list.name}")  
            if self.list_id >= 0:  
                result.append(f"list_id={self.list_id}")  
        if self.meta_key:  
            result.append(f"meta_key={self.meta_key}")  
            if self.meta_val:  
                result.append(f"meta_val={self.meta_val}")  
        return ", ".join(result)  
  
class OptionDef:  
    def __init__(self, name, opt_type, flags=0, value=None, help_text="", arg_name=""):  
        self.name = name  
        self.type = opt_type  
        self.flags = flags  
        self.value = value  # Can be a variable reference or function  
        self.help_text = help_text  
        self.arg_name = arg_name  
  
class FFmpegParser:  
    def __init__(self):  
        self.options = {}  # Dictionary of options  
        self.global_options = {}  # Global options  
        self.input_files = []  
        self.output_files = []  
        self.current_file = None  # Current file being processed  
  
    def register_option(self, option_def):  
        """Register an option definition"""  
        self.options[option_def.name] = option_def  
  
    def register_options(self, option_defs):  
        """Register multiple option definitions"""  
        for opt in option_defs:  
            self.register_option(opt)  
  
    def parse_stream_specifier(self, spec, allow_remainder=False):  
        """Parse a stream specifier like 'v', 'a:1', 'p:1:v', etc."""  
        ss = StreamSpecifier()  
          
        if not spec:  
            return ss, ""  
          
        # Parse the specifier  
        remainder = spec  
          
        # Check for stream index  
        match = re.match(r'^(\d+)(.*)', remainder)  
        if match:  
            ss.idx = int(match.group(1))  
            remainder = match.group(2)  
            if not remainder or (remainder[0] != ':' and not allow_remainder):  
                return ss, remainder  
            if remainder[0] == ':':  
                remainder = remainder[1:]  
          
        # Check for media type  
        if remainder and remainder[0] in 'vasdtV':  
            media_type_map = {  
                'v': MediaType.VIDEO,  
                'a': MediaType.AUDIO,  
                's': MediaType.SUBTITLE,  
                'd': MediaType.DATA,  
                't': MediaType.ATTACHMENT,  
                'V': MediaType.VIDEO  # V is also video but with different meaning  
            }  
            ss.media_type = media_type_map[remainder[0]]  
            remainder = remainder[1:]  
            if not remainder or (remainder[0] != ':' and not allow_remainder):  
                return ss, remainder  
            if remainder[0] == ':':  
                remainder = remainder[1:]  
          
        # Check for program specifier  
        if remainder.startswith('p:'):  
            ss.stream_list = StreamList.PROGRAM  
            remainder = remainder[2:]  
            match = re.match(r'^(\d+)(.*)', remainder)  
            if match:  
                ss.list_id = int(match.group(1))  
                remainder = match.group(2)  
                if not remainder or (remainder[0] != ':' and not allow_remainder):  
                    return ss, remainder  
                if remainder[0] == ':':  
                    remainder = remainder[1:]  
            else:  
                raise ValueError(f"Expected program ID, got: {remainder}")  
          
        # Check for metadata specifier  
        if remainder.startswith('m:'):  
            remainder = remainder[2:]  
            parts = remainder.split(':', 2)  
              
            if len(parts) >= 1:  
                ss.meta_key = parts[0]  
                  
                if len(parts) >= 2:  
                    ss.meta_val = parts[1]  
                    remainder = parts[2] if len(parts) > 2 else ""  
                else:  
                    remainder = ""  
            else:  
                raise ValueError("Invalid metadata specifier")  
          
        return ss, remainder  
  
    def parse_option_value(self, opt_def, arg):  
        """Parse an option value based on its type"""  
        if opt_def.type == OptionType.BOOL:  
            return True  
        elif opt_def.type == OptionType.INT:  
            return int(arg)  
        elif opt_def.type == OptionType.FLOAT:  
            return float(arg)  
        elif opt_def.type == OptionType.STRING:  
            return arg  
        elif opt_def.type == OptionType.FUNC:  
            # In a real implementation, this would call the function  
            return f"Function call: {opt_def.value.__name__}()"  
        elif opt_def.type == OptionType.FUNC_ARG:  
            # In a real implementation, this would call the function with the arg  
            return f"Function call with arg: {opt_def.value.__name__}({arg})"  
        return None  
  
    def parse_options(self, args):  
        """Parse command line arguments"""  
        i = 0  
        current_options = self.global_options  
          
        while i < len(args):  
            arg = args[i]  
            i += 1  
              
            # Check if it's an option  
            if arg.startswith('-'):  
                opt_name = arg[1:]  # Remove the leading '-'  
                  
                # Handle long options with --  
                if opt_name.startswith('-'):  
                    opt_name = opt_name[1:]  
                  
                # Check if the option exists  
                if opt_name not in self.options:  
                    raise ValueError(f"Unknown option: {arg}")  
                  
                opt_def = self.options[opt_name]  
                  
                # Check if the option needs an argument  
                if opt_def.type not in [OptionType.BOOL, OptionType.FUNC]:  
                    if i >= len(args):  
                        raise ValueError(f"Option {arg} requires an argument")  
                    opt_value = self.parse_option_value(opt_def, args[i])  
                    i += 1  
                else:  
                    opt_value = self.parse_option_value(opt_def, None)  
                  
                # Handle special case for input file option  
                if opt_name == 'i':  
                    self.input_files.append(args[i-1])  
                    self.current_file = args[i-1]  
                    current_options = {}  # Reset options for the next file  
                else:  
                    # Store the option  
                    current_options[opt_name] = opt_value  
            else:  
                # Not an option, must be an output file  
                self.output_files.append(arg)  
                self.current_file = arg  
                current_options = {}  # Reset options for the next file  
          
        return self.input_files, self.output_files  
  
    def print_options(self):  
        """Print parsed options for debugging"""  
        print("Global options:", self.global_options)  
        print("Input files:", self.input_files)  
        print("Output files:", self.output_files)  
  
# Example usage  
if __name__ == "__main__":  
    # Define some example options similar to FFmpeg  
    options = [  
        OptionDef("i", OptionType.STRING, 0, None, "input file", "input_file"),  
        OptionDef("c", OptionType.STRING, 0, None, "codec name", "codec"),  
        OptionDef("f", OptionType.STRING, 0, None, "force format", "format"),  
        OptionDef("v", OptionType.INT, 0, None, "verbosity level", "level"),  
        OptionDef("version", OptionType.BOOL, 0, None, "show version"),  
    ]  
      
    parser = FFmpegParser()  
    parser.register_options(options)  
      
    # Example command: ffmpeg -i input.mp4 -c:v libx264 -c:a aac output.mkv  
    args = ["-i", "input.mp4", "-c:v", "libx264", "-c:a", "aac", "output.mkv"]  
      
    try:  
        parser.parse_options(args)  
        parser.print_options()  
          
        # Parse some stream specifiers for demonstration  
        specifiers = ["v", "a:1", "p:1:v", "m:language:eng"]  
        for spec in specifiers:  
            ss, remainder = parser.parse_stream_specifier(spec)  
            print(f"Specifier '{spec}' parsed as: {ss}, remainder: '{remainder}'")  
      
    except ValueError as e:  
        print(f"Error: {e}")