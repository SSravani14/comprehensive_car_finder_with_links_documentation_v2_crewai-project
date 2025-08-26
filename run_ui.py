#!/usr/bin/env python3
"""
UI Runner Script for Comprehensive Car Finder
Choose between demo mode (simulated) or full CrewAI mode
"""

import sys
import os
import subprocess

def check_crewai_available():
    """Check if CrewAI is available in the environment"""
    try:
        import crewai
        return True
    except ImportError:
        return False

def main():
    print("🚗 Comprehensive Car Finder - UI Launcher")
    print("=" * 50)
    
    crewai_available = check_crewai_available()
    
    if crewai_available:
        print("✅ CrewAI is available!")
        print("\nChoose your mode:")
        print("1. Demo Mode (Simulated results - Fast)")
        print("2. Full CrewAI Mode (Real AI agents - Slower)")
        print("3. Exit")
        
        while True:
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == "1":
                print("\n🚀 Starting Demo Mode...")
                print("Access the UI at: http://localhost:5000")
                print("Press Ctrl+C to stop the server")
                subprocess.run([sys.executable, "app_demo.py"])
                break
                
            elif choice == "2":
                print("\n🤖 Starting Full CrewAI Mode...")
                print("Access the UI at: http://localhost:5000")
                print("Press Ctrl+C to stop the server")
                subprocess.run([sys.executable, "app.py"])
                break
                
            elif choice == "3":
                print("👋 Goodbye!")
                break
                
            else:
                print("❌ Invalid choice. Please enter 1, 2, or 3.")
    
    else:
        print("⚠️  CrewAI is not available in your environment.")
        print("This could be due to:")
        print("  - Python version < 3.10 (CrewAI requires Python 3.10+)")
        print("  - CrewAI not installed")
        print("  - Missing dependencies")
        
        print("\nOptions:")
        print("1. Run Demo Mode (Simulated results)")
        print("2. Install CrewAI (requires Python 3.10+)")
        print("3. Exit")
        
        while True:
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == "1":
                print("\n🚀 Starting Demo Mode...")
                print("Access the UI at: http://localhost:5000")
                print("Press Ctrl+C to stop the server")
                subprocess.run([sys.executable, "app_demo.py"])
                break
                
            elif choice == "2":
                print("\n📦 Installing CrewAI...")
                print("Note: This requires Python 3.10 or higher")
                print("Current Python version:", sys.version)
                
                if sys.version_info >= (3, 10):
                    try:
                        subprocess.run([sys.executable, "-m", "pip", "install", "crewai[tools]>=0.150.0,<1.0.0"])
                        print("✅ CrewAI installed successfully!")
                        print("You can now run the full version.")
                    except Exception as e:
                        print(f"❌ Failed to install CrewAI: {e}")
                else:
                    print("❌ Python 3.10+ required for CrewAI")
                    print("Please upgrade your Python version first.")
                break
                
            elif choice == "3":
                print("👋 Goodbye!")
                break
                
            else:
                print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
