# FFmpeg Flow Editor

A visual flow editor for creating and managing FFmpeg command pipelines. This tool provides a user-friendly interface for building complex FFmpeg commands through a node-based visual editor.

## Live Demo

Check out the live demo at: [https://livingbio.github.io/typed-ffmpeg-playground/](https://livingbio.github.io/typed-ffmpeg-playground/)

## Features

- Visual node-based interface for building FFmpeg commands
- Support for various FFmpeg filters and options
- Real-time command preview
- Type-safe FFmpeg command generation
- Interactive flow diagram editing
- Support for complex filter chains and multiple inputs/outputs

## Prerequisites

- Node.js >= 18.0.0
- npm >= 8.0.0

## Installation

```bash
# Clone the repository
git clone https://github.com/livingbio/typed-ffmpeg-playground.git
cd typed-ffmpeg-playground

# Install dependencies
npm install
```

## Development

```bash
# Start the development server
npm run dev

# Run tests
npm test

# Build for production
npm run build
```

## Project Structure

```
├── src/
│   ├── components/     # React components
│   ├── types/         # TypeScript type definitions
│   ├── utils/         # Utility functions
│   └── config/        # Configuration files
├── public/            # Static assets
└── tests/            # Test files
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
