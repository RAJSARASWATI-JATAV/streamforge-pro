"""
StreamForge-Pro: Advanced Multi-Platform Media Downloader

Created by: Raj Saraswati (@rajsaraswati)
GitHub: github.com/RAJSARASWATI-JATAV/streamforge-pro
Copyright © 2025 Raj Saraswati - All Rights Reserved

This is a proprietary software created by Raj Saraswati.
Educational and ethical use only.
"""

__version__ = "2.0.0"
__author__ = "Raj Saraswati"
__email__ = "raj@streamforge.pro"
__license__ = "MIT with Additional Restrictions"
__copyright__ = "Copyright © 2025 Raj Saraswati. All Rights Reserved."
__github__ = "github.com/RAJSARASWATI-JATAV/streamforge-pro"
__creator__ = "Raj Saraswati"
__maintainer__ = "Raj Saraswati"

# Core exports
__all__ = [
    "__version__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
    "__github__",
    "__creator__",
]

# Display creator info
def show_credits():
    """Display creator information"""
    print(f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                    StreamForge-Pro v{__version__}                              ║
║                                                                           ║
║                    👨💻 Created by: {__author__}                        ║
║                    📧 Email: {__email__}                      ║
║                    🌐 GitHub: {__github__[:40]}    ║
║                                                                           ║
║                    {__copyright__}              ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
    """)
