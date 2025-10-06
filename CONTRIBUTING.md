# Contributing to StreamForge-Pro

## How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Development Setup

```bash
git clone https://github.com/rajsaraswati/streamforge-pro.git
cd streamforge-pro
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

## Code Style

- Follow PEP 8
- Add type hints
- Write docstrings
- Add tests for new features

## Testing

```bash
pytest tests/
```

## Questions?

Open an issue or discussion on GitHub.
