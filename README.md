## typed-ffmpeg

[![ci-pacakge](https://github.com/livingbio/typed-ffmpeg/actions/workflows/ci-package.yml/badge.svg)](https://github.com/livingbio/typed-ffmpeg/actions?query=workflow%3Aci)
[![documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://livingbio.github.io/typed-ffmpeg/)
[![pypi version](https://img.shields.io/pypi/v/typed-ffmpeg.svg)](https://pypi.org/project/typed-ffmpeg/)

Modern Python FFmpeg wrappers provide extensive support for complex filters, accompanied by detailed typing and documentation.

This API design draws inspiration from the user-friendly `ffmpeg-python` package, which offers an easy-to-use Pythonic interface for accessing FFmpeg functionality. However, the `ffmpeg-python` package lacks certain features that I require, including:

- IDE friendly
- Built-in documentation for FFmpeg filters
- Comprehensive typing and type checking
- Support for JSON serialization and deserialization of filter graphs
- FFmpeg validation and automatic correction
- Support for partial evaluation of filter graphs

---

**[Features](#features)** - **[Installation](#installation)** - **[Quick Usage](#quick-usage)**

![typed-ffmpeg](https://raw.githubusercontent.com/livingbio/typed-ffmpeg/main/docs/media/autocomplete.png)

## Features
- **No Dependency:**
  typed-ffmpeg is a pure Python package only build on python std library. Relying solely on the Python standard library for a package ensures portability, as it doesn't require additional dependencies for installation. It also minimizes maintenance overhead and security risks while providing stable functionality.

- **Easy to Use:**
  typed-ffmpeg is designed to be user-friendly and easy to use. It provides a Pythonic interface for constructing filter graphs, making it simple to use and understand.
  see Example

- **Support FFMpeg Complex Filter**
  typed-ffmpeg supports all FFmpeg filters, including video, audio, and dynamic filters. This allows you to construct complex filter graphs with ease.

- [**Built-in Documentation:**](https://livingbio.github.io/typed-ffmpeg/usage/doc/)
  Checking the FFmpeg documentation every time you want to use a filter can be cumbersome. typed-ffmpeg utilizes docstrings to provide comprehensive documentation for all filters. IDEs and text editors can display this documentation as a tooltip when you hover over a filter.

- [**Typed:**](https://livingbio.github.io/typed-ffmpeg/usage/typed/)
  This package offers comprehensive typing for all filters, including both input and output types. For non-dynamic inputs/outputs, typing is checked by static type checkers such as mypy; for dynamic inputs/outputs, typing is checked at runtime. This can help catch errors early and make your code more robust.

![typed-ffmpeg](https://raw.githubusercontent.com/livingbio/typed-ffmpeg/main/docs/media/typed.png)


- [**Serialization:**](https://livingbio.github.io/typed-ffmpeg/usage/serialize/)
  typed-ffmpeg offers the capability to serialize and deserialize filter graphs to JSON format, enabling you to save the filter graph to a file and reload it for future use.

- [**Validate and Auto Fix:**](https://livingbio.github.io/typed-ffmpeg/usage/validate/)
  The FFMpeg filter graph can be intricate and challenging to construct accurately. typed-ffmpeg provides a functionality to validate and even automatically correct these filter graphs, aiding in rectifying any inconsistencies or errors present within the graph.

- **Graph Visualization:**
  typed-ffmpeg supports visualizing filter graphs using `graphviz`. This can help you understand the filter graph better and debug any issues.


!!! tip "Note"
    This feature can be turned off by setting relate flags during `compile` or `run`.

### Coming Soon
- **Partial Evaluation:**
  typed-ffmpeg provides a way to partially evaluate the filter graph. This can help evaluate the filter graph step by step.
- **FFmpeg Version Support:**
  typed-ffmpeg is built based on FFmpeg version 6.0. If you encounter any issues with typed-ffmpeg in different FFmpeg versions, please open an issue in the GitHub repository.
- **Support for More Filters:**
  typed-ffmpeg currently supports a subset of FFmpeg filters. We are working to support more filters in the future.

## Help

See [documentation](https://livingbio.github.io/typed-ffmpeg/) for more details.

## Installation

!!! tip "Note"
    FFmpeg installation is required on your system.

With `pip`:

```bash
pip install typed-ffmpeg
```

You can also install support for visualizing filter graphs with `graphviz`:

!!! tip "Note"
    Graphviz must be installed on your system.

```bash
pip install 'typed-ffmpeg[graph]'
```


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
![quickstart](https://raw.githubusercontent.com/livingbio/typed-ffmpeg/main/docs/media/quickstart.png)

!!! tip "Note"
    Obtaining the graph is simple; just utilize `f.view()`.

See the [Usage](https://mkdocstrings.github.io/usage) section of the docs for more examples!

## Acknowledgements

This project was initially conceived upon the release of GPT-3. I embarked on this endeavor to test GPT-3's capability to generate a functional SDK for FFmpeg by providing it with FFmpeg documentation. However, I soon realized that it remained a challenging task for GPT to create a truly usable SDK for FFmpeg. Therefore, I opted to develop an SDK for FFmpeg using traditional code generation methods. Nevertheless, without the assistance of Copilot and GPT, I would not have had the time to complete this project.

I have decided to release this open-source project on February 24, 2024, to commemorate the seventh birthday of my son, Austin. His curiosity and enthusiasm for exploring the world have been a constant source of inspiration throughout this journey.
