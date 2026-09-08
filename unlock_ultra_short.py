import os
import sys
import subprocess

# Ensure pyzipper is available
try:
    import pyzipper
except ImportError:
    print("[*] Installing required decryption dependency (pyzipper)...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyzipper"])
    import pyzipper

ZIP_FILE = "ultra_short_locked.zip"
OUTPUT_DIR = "ultra_short"

def unlock():
    if not os.path.exists(ZIP_FILE):
        print(f"[-] Error: '{ZIP_FILE}' not found in current directory.")
        return

    print("=" * 60)
    print("[LOCKED ARCHIVE] ULTRA-SHORT NUMERICAL COMPUTING CODES")
    print("=" * 60)
    
    passcode = input("Enter Unique Passcode to Unlock: ").strip()

    try:
        with pyzipper.AESZipFile(ZIP_FILE) as zf:
            zf.setpassword(passcode.encode("utf-8"))
            # Test password validity by reading first file
            test_file = zf.namelist()[0]
            zf.read(test_file)

            os.makedirs(OUTPUT_DIR, exist_ok=True)
            zf.extractall(OUTPUT_DIR)

        print("\n" + "=" * 60)
        print(f"[+] Access Granted! Successfully unlocked to folder: '{OUTPUT_DIR}/'")
        print("=" * 60)

    except Exception:
        print("\n" + "=" * 60)
        print("[-] Access Denied: Invalid Passcode!")
        print("=" * 60)

if __name__ == "__main__":
    unlock()
