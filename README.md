## typed-ffmpeg

Modern Python FFmpeg wrappers offer comprehensive support for complex filters, complete with detailed typing and documentation.

This API design is based on the helpful `ffmpeg-python` package, which serves as a Python binding for FFmpeg. Acting as a wrapper around the FFmpeg command line utility, it provides a Pythonic interface for accessing FFmpeg functionality. However, the `ffmpeg-python` package lacks some crucial features, including:

- Documentation for filters
- Comprehensive typing and type checking
- Support for serialization and deserialization of filter graphs
- Support for partial evaluation of filter graphs


[![ci](https://github.com/livingbio/typed-ffmpeg/workflows/ci/badge.svg)](https://github.com/livingbio/typed-ffmpeg/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://livingbio.github.io/typed-ffmpeg/)
[![pypi version](https://img.shields.io/pypi/v/typed-ffmpeg.svg)](https://pypi.org/project/typed-ffmpeg/)

---

**[Features](#features)** - **[Requirements](#requirements)** - **[Installation](#installation)** - **[Quick usage](#quick-usage)**

![mkdocstrings_gif1](https://user-images.githubusercontent.com/3999221/77157604-fb807480-6aa1-11ea-99e0-d092371d4de0.gif)

## Features
- [**Built-in Documentation:**](https://mkdocstrings.github.io/theming/)
  Checking the FFmpeg documentation every time you want to use a filter can be cumbersome. typed-ffmpeg utilizes docstrings to provide comprehensive documentation for all filters. IDEs and text editors can display this documentation as a tooltip when you hover over a filter.

- [**Typed:**](https://mkdocstrings.github.io/handlers/overview/)
  This package offers comprehensive typing for all filters, including both input and output types. For non-dynamic inputs/outputs, typing is checked by static type checkers such as mypy; for dynamic inputs/outputs, typing is checked at runtime. This can help catch errors early and make your code more robust.

- [**No Dependency:**](https://mkdocstrings.github.io/usage/#cross-references-to-other-projects-inventories)
  typed-ffmpeg is a pure Python package and has no dependency on the FFmpeg command line utility. This allows you to use typed-ffmpeg in a platform-independent manner.

- [**Serialization:**](https://mkdocstrings.github.io/usage/#cross-references-to-other-projects-inventories)
  typed-ffmpeg provides a way to serialize and deserialize filter graphs. This allows you to save the filter graph to a file and load it later.

- [**Validate and Auto Fix:**](https://mkdocstrings.github.io/usage/#cross-references)
  typed-ffmpeg offers a feature to automatically fix the filter graph. This can help fix the filter graph when it is not valid.

    **Note**: This feature can be turned off by setting `auto_fix` to `False` during `compile` or `run`.
    [Opt-in](https://mkdocstrings.github.io/usage/#cross-references-to-any-markdown-heading).

- [**Partial Evaluation (Coming Soon):**](https://mkdocstrings.github.io/usage/)
  typed-ffmpeg provides a way to partially evaluate the filter graph. This can help evaluate the filter graph step by step.

## Installation

With `pip`:

```bash
pip install typed-ffmpeg
```

You can also install support for visualizing filter graphs with `graphviz`:

```bash
pip install 'typed-ffmpeg[graph]'
```

**Note**: You need to install FFmpeg / Graphviz to your system.

## Quick Usage

```python
import ffmpeg

f = (
    ffmpeg
    .input(filename='input.mp4')
    .hflip()
    .output(filename='output.mp4')
)

f.run()
```
![quickstart](media/quickstart.png)

NOTE: you can get the graph easily by using `f.view()`

See the [Usage](https://mkdocstrings.github.io/usage) section of the docs for more examples!

## Acknowledgements

This project was initially conceived upon the release of GPT-3. I embarked on this endeavor to test GPT-3's capability to generate a functional SDK for FFmpeg by providing it with FFmpeg documentation. However, I soon realized that it remained a challenging task for GPT to create a truly usable SDK for FFmpeg. Therefore, I opted to develop an SDK for FFmpeg using traditional code generation methods. Nevertheless, without the assistance of Copilot and GPT, I would not have had the time to complete this project.

I have decided to release this open-source project on February 24, 2024, to commemorate the seventh birthday of my son, Austin. His curiosity and enthusiasm for exploring the world have been a constant source of inspiration throughout this journey.
