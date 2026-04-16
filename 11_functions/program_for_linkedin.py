from playwright.sync_api import sync_playwright
import time
import os
import subprocess
from pathlib import Path

def close_chrome():
    """Close all Chrome processes"""
    print("Closing Chrome processes...")
    try:
        subprocess.run(['taskkill', '/F', '/IM', 'chrome.exe'], capture_output=True)
        time.sleep(2)
        print("✓ Chrome processes closed")
    except Exception as e:
        print(f"Note: {e}")

def get_chrome_profile_path():
    """Get the default Chrome profile directory path"""
    username = os.getenv('USERNAME')
    user_data_dir = Path(f"C:/Users/{username}/AppData/Local/Google/Chrome/User Data")
    print(f"Looking for Chrome profile in: {user_data_dir}")
    
    if not user_data_dir.exists():
        print(f"✗ Chrome User Data directory not found")
        return None
    
    # Prefer the Default profile folder, otherwise use the first Profile X folder
    default_profile = user_data_dir / "Default"
    if default_profile.exists():
        print(f"✓ Found Default Chrome profile")
        return str(default_profile)
    
    for profile in user_data_dir.iterdir():
        if profile.is_dir() and profile.name.startswith("Profile"):
            print(f"✓ Found Chrome profile: {profile.name}")
            return str(profile)
    
    print("✗ No Chrome profile folder found inside User Data")
    return None

def send_connection_requests(page, num_requests=10):
    """Send connection requests from the grow network page"""
    print(f"\nNavigating to grow network page...")
    page.goto("https://www.linkedin.com/mynetwork/grow/")
    
    try:
        page.wait_for_load_state("networkidle", timeout=20000)
    except:
        print("⚠ Page load timeout (continuing anyway)")
    
    time.sleep(3)
    
    if page.url.startswith("https://www.linkedin.com/login") or page.locator("input[name='session_key']").count() > 0:
        print("⚠ Detected LinkedIn login page. Please log in manually in the browser window.")
        page.wait_for_selector("a[data-control-name='identity_welcome_message']", timeout=60000)
        print("✓ Login detected. Continuing...")
    
    # Check if already logged in by detecting the top profile menu
    if page.locator("button[aria-label*='Me']").count() > 0 or page.locator("img[alt*='Profile photo']").count() > 0:
        print("✓ Already logged into LinkedIn!")
    else:
        print("⚠ Could not verify login by profile icon. Proceeding anyway.")
    
    sent_count = 0
    attempt = 0
    
    while sent_count < num_requests and attempt < num_requests * 4:
        try:
            attempt += 1
            
            # Find connect buttons
            connect_buttons = page.locator("button:has-text('Connect')")
            button_count = connect_buttons.count()
            
            if button_count > 0:
                print(f"Found {button_count} Connect button(s)")
                connect_buttons.first.click()
                print(f"✓ Connection request {sent_count + 1} sent!")
                sent_count += 1
                time.sleep(2)
                
                # Dismiss invitation modal if present
                if page.locator("button:has-text('Send now')").count() > 0:
                    page.locator("button:has-text('Send now')").first.click()
                    time.sleep(1)
                
                # Scroll down to load more profiles
                page.evaluate("window.scrollBy(0, 400)")
                time.sleep(2)
            else:
                print("No 'Connect' buttons found. Scrolling to load more...")
                page.evaluate("window.scrollBy(0, 700)")
                time.sleep(3)
                
        except Exception as e:
            print(f"Error during attempt {attempt}: {e}")
            time.sleep(2)
    
    return sent_count

def main():
    """Main function to run LinkedIn connection automation using existing Chrome profile"""
    print("=" * 70)
    print("LinkedIn Connection Automation (Using Existing Chrome Profile)")
    print("=" * 70)
    
    # Close Chrome first
    close_chrome()
    
    # Get Chrome profile path
    profile_path = get_chrome_profile_path()
    if not profile_path:
        print("\n✗ Could not find Chrome profile.")
        print("Make sure Chrome is installed at: C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome")
        return
    
    try:
        num_requests = int(input("\nHow many connection requests to send? (default: 10): ") or "10")
    except ValueError:
        num_requests = 10
    
    print("\n" + "=" * 70)
    print("Starting browser automation with your Chrome profile...")
    print(f"Profile path: {profile_path}")
    print("=" * 70)
    
    try:
        with sync_playwright() as p:
            print("\nLaunching Chrome with your profile...")
            
            # Launch browser with existing Chrome profile
            context = p.chromium.launch_persistent_context(
                user_data_dir=profile_path,
                headless=False,
                channel="chrome",  # Use system Chrome
                args=[
                    '--disable-dev-shm-usage',
                    '--disable-gpu'
                ]
            )
            
            print("✓ Chrome launched successfully!")
            page = context.new_page()
            
            # Open LinkedIn after the browser is ready
            page.goto("https://www.linkedin.com/mynetwork/grow/")
            print("Waiting for LinkedIn page to load...")
            
            sent = send_connection_requests(page, num_requests)
            
            print("\n[2/2] Completed!")
            print("=" * 70)
            print(f"✓ Successfully sent {sent} connection requests!")
            print("=" * 70)
            
            # Keep browser open for a few seconds so user can review result
            time.sleep(5)
            
            context.close()
            print("\nBrowser closed. Script completed.")
            
    except Exception as e:
        print(f"\n✗ An error occurred: {e}")
        print(f"\nTroubleshooting tips:")
        print("1. Make sure Chrome is completely closed before running the script")
        print("2. Make sure your LinkedIn session is active in that profile")
        print("3. If the page opens on the login screen, sign in manually and wait")
        print("4. If 'chrome' channel is unavailable, remove channel='chrome' from launch_persistent_context")
        print("5. Install Playwright browsers: python -m playwright install")

if __name__ == "__main__":
    main()
