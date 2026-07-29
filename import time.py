import time
import sys

while True:
    print("\nDownloadinf 10 terabytes of useless data...")
    time.sleep(1)
    
    for percent in range(1, 100):
        sys.stdout.write(f"\rProgress: [{percent}%] ")
        sys.stdout.flush()
        
        if percent == 99:
            time.sleep(1)
            print("\n\033[91m\033[1m[SYSTEM ERROR] Critical failure. Resetting...\033[0m")
            time.sleep(2)
            break
            
        if percent > 90:
            time.sleep(60)
        else:
            time.sleep(30)