"""
Advanced Visual Effects System
Created by RAJSARASWATI JATAV
"""
import time
import random
import sys
from colorama import Fore, Back, Style, init

init(autoreset=True)

class VisualEffects:
    """Next-level visual effects"""
    
    COLORS = {
        'neon_green': '\033[38;5;46m',
        'neon_pink': '\033[38;5;201m',
        'neon_blue': '\033[38;5;51m',
        'neon_yellow': '\033[38;5;226m',
        'neon_purple': '\033[38;5;165m',
        'neon_orange': '\033[38;5;208m',
        'neon_cyan': '\033[38;5;87m',
        'electric_blue': '\033[38;5;27m',
        'hot_pink': '\033[38;5;198m',
        'lime': '\033[38;5;118m',
        'reset': '\033[0m'
    }
    
    @staticmethod
    def rainbow_text(text):
        """Rainbow colored text"""
        colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
        result = ""
        for i, char in enumerate(text):
            result += colors[i % len(colors)] + char
        return result + Style.RESET_ALL
    
    @staticmethod
    def glitch_effect(text, duration=0.5):
        """Glitch animation effect"""
        glitch_chars = ['█', '▓', '▒', '░', '▄', '▀']
        for _ in range(5):
            glitched = ''.join(random.choice(glitch_chars) if random.random() > 0.7 else c for c in text)
            print(f"\r{Fore.CYAN}{glitched}{Style.RESET_ALL}", end='', flush=True)
            time.sleep(duration / 5)
        print(f"\r{Fore.GREEN}{text}{Style.RESET_ALL}")
    
    @staticmethod
    def matrix_rain(lines=10):
        """Matrix-style falling characters"""
        chars = "01アイウエオカキクケコサシスセソタチツテト"
        for _ in range(lines):
            line = ''.join(random.choice(chars) for _ in range(80))
            print(f"{Fore.GREEN}{line}{Style.RESET_ALL}")
            time.sleep(0.05)
    
    @staticmethod
    def pulse_text(text, times=3):
        """Pulsing text effect"""
        for _ in range(times):
            print(f"\r{Fore.GREEN}{Style.BRIGHT}{text}{Style.RESET_ALL}", end='', flush=True)
            time.sleep(0.3)
            print(f"\r{Fore.GREEN}{Style.DIM}{text}{Style.RESET_ALL}", end='', flush=True)
            time.sleep(0.3)
        print()
    
    @staticmethod
    def neon_box(title, content, color='neon_green'):
        """Neon-style box"""
        c = VisualEffects.COLORS[color]
        width = max(len(title), len(content)) + 4
        print(f"{c}╔{'═' * width}╗")
        print(f"║ {title.center(width-2)} ║")
        print(f"╠{'═' * width}╣")
        print(f"║ {content.center(width-2)} ║")
        print(f"╚{'═' * width}╝{VisualEffects.COLORS['reset']}")
    
    @staticmethod
    def loading_bar(duration=2, color='neon_cyan'):
        """Animated loading bar"""
        c = VisualEffects.COLORS[color]
        width = 50
        for i in range(width + 1):
            bar = '█' * i + '░' * (width - i)
            percent = int((i / width) * 100)
            print(f"\r{c}[{bar}] {percent}%{VisualEffects.COLORS['reset']}", end='', flush=True)
            time.sleep(duration / width)
        print()
    
    @staticmethod
    def typewriter(text, speed=0.05, color='neon_green'):
        """Typewriter effect"""
        c = VisualEffects.COLORS[color]
        for char in text:
            print(f"{c}{char}{VisualEffects.COLORS['reset']}", end='', flush=True)
            time.sleep(speed)
        print()
    
    @staticmethod
    def cyber_banner():
        """Cyberpunk-style banner"""
        banner = f"""
{Fore.CYAN}╔═══════════════════════════════════════════════════════════════════════════╗
{Fore.MAGENTA}║{Fore.YELLOW}                    ⚡ STREAMFORGE-PRO v2.2.0 ⚡                          {Fore.MAGENTA}║
{Fore.CYAN}╠═══════════════════════════════════════════════════════════════════════════╣
{Fore.GREEN}║  {Fore.WHITE}🎬 Advanced Multi-Platform Media Downloader                            {Fore.GREEN}║
{Fore.GREEN}║  {Fore.CYAN}👨💻 Created by: {Fore.YELLOW}RAJSARASWATI JATAV                                   {Fore.GREEN}║
{Fore.GREEN}║  {Fore.MAGENTA}📍 Location: {Fore.WHITE}Gwalior, Madhya Pradesh, India                       {Fore.GREEN}║
{Fore.CYAN}╚═══════════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
        return banner
    
    @staticmethod
    def success_animation(message):
        """Success animation"""
        frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        for _ in range(10):
            for frame in frames:
                print(f"\r{Fore.GREEN}{frame} {message}{Style.RESET_ALL}", end='', flush=True)
                time.sleep(0.1)
        print(f"\r{Fore.GREEN}✓ {message}{Style.RESET_ALL}")
    
    @staticmethod
    def error_shake(message):
        """Error shake effect"""
        for _ in range(3):
            print(f"\r  {Fore.RED}✗ {message}{Style.RESET_ALL}", end='', flush=True)
            time.sleep(0.1)
            print(f"\r{Fore.RED}✗ {message}{Style.RESET_ALL}", end='', flush=True)
            time.sleep(0.1)
        print()
    
    @staticmethod
    def gradient_text(text, start_color, end_color):
        """Gradient colored text"""
        # Simple gradient simulation
        mid = len(text) // 2
        result = start_color + text[:mid] + end_color + text[mid:] + Style.RESET_ALL
        return result
    
    @staticmethod
    def sparkle_effect(text):
        """Sparkle animation"""
        sparkles = ['✨', '⭐', '🌟', '💫', '✨']
        for sparkle in sparkles:
            print(f"\r{sparkle} {Fore.YELLOW}{text}{Style.RESET_ALL} {sparkle}", end='', flush=True)
            time.sleep(0.2)
        print()
