## typed-ffmpeg

[![CI Package](https://github.com/livingbio/typed-ffmpeg/actions/workflows/ci-package.yml/badge.svg)](https://github.com/livingbio/typed-ffmpeg/actions?query=workflow%3Aci-package)
[![Documentation](https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat)](https://livingbio.github.io/typed-ffmpeg/)
[![PyPI Version](https://img.shields.io/pypi/v/typed-ffmpeg.svg)](https://pypi.org/project/typed-ffmpeg/)

**typed-ffmpeg** offers a modern, Pythonic interface to FFmpeg, providing extensive support for complex filters with detailed typing and documentation. Inspired by `ffmpeg-python`, this package enhances functionality by addressing common limitations, such as lack of IDE integration and comprehensive typing, while also introducing new features like JSON serialization of filter graphs and automatic FFmpeg validation.

---

### Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Quick Usage](#quick-usage)
- [Documentation](https://livingbio.github.io/typed-ffmpeg/)
- [Acknowledgements](#acknowledgements)

---

## Features

![typed-ffmpeg](https://raw.githubusercontent.com/livingbio/typed-ffmpeg/main/docs/media/autocomplete.png)


- **Zero Dependencies:** Built purely with the Python standard library, ensuring maximum compatibility and security.
- **User-Friendly:** Simplifies the construction of filter graphs with an intuitive Pythonic interface.
- **Comprehensive FFmpeg Filter Support:** Out-of-the-box support for most FFmpeg filters, with IDE auto-completion.
- **Integrated Documentation:** In-line docstrings provide immediate reference for filter usage, reducing the need to consult external documentation.
- **Robust Typing:** Offers static and dynamic type checking, enhancing code reliability and development experience.
- **Filter Graph Serialization:** Enables saving and reloading of filter graphs in JSON format for ease of use and repeatability.
- **Graph Visualization:** Leverages `graphviz` for visual representation, aiding in understanding and debugging.
- **Validation and Auto-correction:** Assists in identifying and fixing errors within filter graphs.

### Planned Features

Please note that the following features are under consideration or development for future releases:

- **Partial Evaluation:** Enhance the flexibility of filter graphs by enabling partial evaluation, allowing for modular construction and reuse.
- **Extended FFmpeg Version Support:** While `typed-ffmpeg` is currently built with FFmpeg version 6.0 in mind, we are working to ensure compatibility across different FFmpeg versions. Feedback and issue reports are welcome to improve version support.
- **Additional Filter Support:** We aim to expand the range of FFmpeg filters supported by `typed-ffmpeg`. Continuous updates will be made to include more complex and varied filters.
- **Input and Output Options Support:** Provide a more comprehensive interface for input and output options, including support for additional codecs and formats.

---

## Installation

To install `typed-ffmpeg`, simply use pip:

```bash
pip install typed-ffmpeg
```

Note: FFmpeg must be installed on your system.

### Visualization Support

To enable graph visualization features:

```bash
pip install 'typed-ffmpeg[graph]'
```

Note: This requires Graphviz to be installed on your system.

---

## Quick Usage

Here's how to quickly start using `typed-ffmpeg`:

```python
import ffmpeg

# Flip video horizontally and output
f = (
    ffmpeg
    .input(filename='input.mp4')
    .hflip()
    .output(filename='output.mp4')
)
f.run()
```

![](https://raw.githubusercontent.com/livingbio/typed-ffmpeg/main/docs/media/quick-usage.png)

For a more complex example:

```python
import ffmpeg

# Complex filter graph example
in_file = ffmpeg.input("input.mp4")
overlay_file = ffmpeg.input("overlay.png")

f = (
    ffmpeg
    .concat(
        in_file.trim(start_frame=10, end_frame=20),
        in_file.trim(start_frame=30, end_frame=40),
    )
    .overlay(overlay_file.hflip())
    .drawbox(x="50", y="50", width="120", height="120", color="red", thickness="5")
    .output(filename="out.mp4")
)
f.run()
```

![](https://raw.githubusercontent.com/livingbio/typed-ffmpeg/main/docs/media/quick-usage-complex.png)

See the [Usage](https://livingbio.github.io/typed-ffmpeg/usage/typed/) section in our documentation for more examples and detailed guides.

---

## Acknowledgements

This project was initially inspired by the capabilities of GPT-3, with the original concept focusing on using GPT-3 to generate an FFmpeg filter SDK directly from the FFmpeg documentation. However, during the development process, I encountered limitations with GPT-3's ability to fully automate this task.

As a result, I shifted to traditional code generation methods to complete the SDK, ensuring a more robust and reliable tool. Despite this change in approach, both GitHub Copilot and GPT-3 were instrumental in accelerating the development process, providing valuable insights and saving significant time.

This project is dedicated to my son, Austin, on his seventh birthday (February 24, 2024), whose curiosity and zest for life continually inspire me.

---

Feel free to check the [Documentation](https://livingbio.github.io/typed-ffmpeg/) for detailed information and more advanced features.
