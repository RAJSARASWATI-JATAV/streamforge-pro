#!/usr/bin/env python3
"""
Visual Effects Demo - StreamForge-Pro
Created by RAJSARASWATI JATAV
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from streamforge.utils.visual_effects import VisualEffects
import time

def demo():
    """Demonstrate all visual effects"""
    
    # Cyber banner
    print(VisualEffects.cyber_banner())
    time.sleep(1)
    
    # Rainbow text
    print("\n" + VisualEffects.rainbow_text("🌈 RAINBOW TEXT EFFECT"))
    time.sleep(1)
    
    # Glitch effect
    print("\n⚡ GLITCH EFFECT:")
    VisualEffects.glitch_effect("STREAMFORGE-PRO v2.2.0")
    time.sleep(1)
    
    # Matrix rain
    print("\n💚 MATRIX RAIN:")
    VisualEffects.matrix_rain(5)
    time.sleep(1)
    
    # Pulse text
    print("\n💓 PULSE EFFECT:")
    VisualEffects.pulse_text(">>> DOWNLOADING <<<")
    time.sleep(1)
    
    # Neon boxes
    print("\n📦 NEON BOXES:")
    VisualEffects.neon_box("INSTAGRAM PRO", "Zero Compression Technology", "neon_pink")
    time.sleep(0.5)
    VisualEffects.neon_box("TIKTOK PRO", "No Watermark Downloads", "neon_blue")
    time.sleep(0.5)
    VisualEffects.neon_box("AI OPTIMIZER", "Machine Learning Powered", "neon_purple")
    time.sleep(1)
    
    # Loading bar
    print("\n⏳ LOADING BAR:")
    VisualEffects.loading_bar(2, "neon_cyan")
    time.sleep(1)
    
    # Typewriter
    print("\n⌨️  TYPEWRITER EFFECT:")
    VisualEffects.typewriter("Created by RAJSARASWATI JATAV from Gwalior, India", 0.03, "neon_yellow")
    time.sleep(1)
    
    # Success animation
    print("\n✅ SUCCESS ANIMATION:")
    VisualEffects.success_animation("Download completed successfully!")
    time.sleep(1)
    
    # Error shake
    print("\n❌ ERROR ANIMATION:")
    VisualEffects.error_shake("Connection failed!")
    time.sleep(1)
    
    # Sparkle effect
    print("\n✨ SPARKLE EFFECT:")
    VisualEffects.sparkle_effect("STREAMFORGE-PRO")
    time.sleep(1)
    
    # Final message
    print("\n" + VisualEffects.rainbow_text("=" * 80))
    VisualEffects.neon_box("DEMO COMPLETE", "All Visual Effects Showcased!", "neon_green")
    print(VisualEffects.rainbow_text("=" * 80))

if __name__ == "__main__":
    demo()
