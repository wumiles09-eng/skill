#!/usr/bin/env python3
"""
Development Server Checker
Checks if a development server is running on common ports
"""

import socket
import subprocess
import sys
from typing import List, Tuple, Optional

# Common development server ports
COMMON_PORTS = [
    (3000, "React/Next.js (default)"),
    (3001, "React/Next.js (alternate)"),
    (5173, "Vite"),
    (8080, "Vue CLI"),
    (4200, "Angular"),
    (8000, "Python/Django"),
    (5000, "Flask/Express"),
    (8888, "Jupyter"),
]

def check_port(port: int, timeout: float = 0.5) -> bool:
    """Check if a port is open"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex(('localhost', port))
        return result == 0
    except socket.error:
        return False
    finally:
        sock.close()

def find_running_servers() -> List[Tuple[int, str]]:
    """Find all running development servers"""
    running = []
    for port, description in COMMON_PORTS:
        if check_port(port):
            running.append((port, description))
    return running

def get_process_on_port(port: int) -> Optional[str]:
    """Try to get process name running on port (Unix only)"""
    try:
        # lsof command to find process
        result = subprocess.run(
            ['lsof', '-i', f':{port}', '-sTCP:LISTEN', '-t'],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0 and result.stdout.strip():
            pid = result.stdout.strip()
            # Get process name
            ps_result = subprocess.run(
                ['ps', '-p', pid, '-o', 'comm='],
                capture_output=True,
                text=True,
                timeout=2
            )
            if ps_result.returncode == 0:
                return ps_result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None

def main():
    """Main entry point"""
    print("🔍 Checking for running development servers...\n")
    
    running_servers = find_running_servers()
    
    if not running_servers:
        print("❌ No development servers detected on common ports")
        print("\nCommon ports checked:")
        for port, desc in COMMON_PORTS:
            print(f"  - {port} ({desc})")
        print("\n💡 Start your development server first:")
        print("  npm run dev")
        print("  yarn dev")
        print("  python manage.py runserver")
        print("  etc.")
        sys.exit(1)
    
    print("✅ Found running development server(s):\n")
    for port, description in running_servers:
        process = get_process_on_port(port)
        process_info = f" [{process}]" if process else ""
        print(f"  • localhost:{port} - {description}{process_info}")
        print(f"    URL: http://localhost:{port}")
    
    print("\n🎯 Ready for visual testing!")
    
    # Output JSON for programmatic use
    if '--json' in sys.argv:
        import json
        print("\n" + json.dumps({
            "running": True,
            "servers": [{"port": p, "description": d} for p, d in running_servers]
        }))
    
    sys.exit(0)

if __name__ == "__main__":
    main()
