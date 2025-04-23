from urllib.parse import urlparse
import requests

choice = input("Do you want to enter a URL manually (m) or use a file (f)? ").strip().lower()

if choice == "f":
    try:
        with open("url_list.txt", "r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip()]
        if not urls:
            print("⚠️ File 'url_list.txt' found but contains no URLs.")
            exit()
    except FileNotFoundError:
        print("⚠️ File 'url_list.txt' not found.")
        exit()

    with open("bulk_scan_report.txt", "a", encoding="utf-8") as bulk_log:
        for url in urls:
            print(f"\n🔍 Scanning: {url}")
            try:
                response = requests.get(url)
                bulk_log.write(f"\nURL: {url}\n")
                bulk_log.write(f"Status Code: {response.status_code}\n")

                if response.status_code == 200:
                    headers = {
                        "Content-Security-Policy": response.headers.get("Content-Security-Policy"),
                        "Strict-Transport-Security": response.headers.get("Strict-Transport-Security"),
                        "X-Frame-Options": response.headers.get("X-Frame-Options"),
                        "X-Content-Type-Options": response.headers.get("X-Content-Type-Options"),
                        "Referrer-Policy": response.headers.get("Referrer-Policy"),
                        "Permissions-Policy": response.headers.get("Permissions-Policy")
                    }
                    bulk_log.write("Security Headers:\n")
                    for key, val in headers.items():
                        bulk_log.write(f"- {key}: {val if val else 'N/A'}\n")
                else:
                    bulk_log.write("❌ No successful response\n")
                bulk_log.write("-" * 40 + "\n")

            except requests.exceptions.RequestException as e:
                print(f"⚠️ Error for {url}: {e}")
                bulk_log.write(f"⚠️ Error for {url}: {e}\n")
                bulk_log.write("-" * 40 + "\n")

else:
    while True:
        url = input("Enter the URL to scan (e.g., https://example.com): ")
        if url.startswith("http://") or url.startswith("https://"):
            break
        else:
            print("❌ Invalid input. URL must start with http:// or https://. Please try again.\n")

    while True:
        try:
            response = requests.get(url)
            print(f"\nStatus code: {response.status_code}")

            if response.status_code == 200:
                print("\nSecurity-related HTTP headers found in the response:")

                csp = response.headers.get("Content-Security-Policy")
                print(f"- Content-Security-Policy: {csp}" if csp else "- Content-Security-Policy not found ❌")

                hsts = response.headers.get("Strict-Transport-Security")
                print(f"- Strict-Transport-Security: {hsts}" if hsts else "- Strict-Transport-Security not found ❌")

                xfo = response.headers.get("X-Frame-Options")
                print(f"- X-Frame-Options: {xfo}" if xfo else "- X-Frame-Options not found ❌")

                xcto = response.headers.get("X-Content-Type-Options")
                print(f"- X-Content-Type-Options: {xcto}" if xcto else "- X-Content-Type-Options not found ❌")

                refpol = response.headers.get("Referrer-Policy")
                print(f"- Referrer-Policy: {refpol}" if refpol else "- Referrer-Policy not found ❌")

                perm = response.headers.get("Permissions-Policy")
                print(f"- Permissions-Policy: {perm}" if perm else "- Permissions-Policy not found ❌")

                parsed_url = urlparse(url)
                domain = parsed_url.netloc.replace("www.", "")
                filename = f"scan_log_{domain}.txt"

                with open(filename, "a", encoding="utf-8") as log:
                    log.write(f"URL: {url}\n")
                    log.write(f"Status Code: {response.status_code}\n")
                    log.write("Security Headers:\n")
                    log.write(f"- Content-Security-Policy: {csp if csp else 'N/A'}\n")
                    log.write(f"- Strict-Transport-Security: {hsts if hsts else 'N/A'}\n")
                    log.write(f"- X-Frame-Options: {xfo if xfo else 'N/A'}\n")
                    log.write(f"- X-Content-Type-Options: {xcto if xcto else 'N/A'}\n")
                    log.write(f"- Referrer-Policy: {refpol if refpol else 'N/A'}\n")
                    log.write(f"- Permissions-Policy: {perm if perm else 'N/A'}\n")
                    log.write("-" * 40 + "\n")

        except requests.exceptions.RequestException as e:
            print(f"⚠️ An error occurred: {e}")

        print("\nScan complete.")
        again = input("Do you want to scan another URL? (yes/no): ").strip().lower()
        if again != "yes":
            print("👋 Thank you for using the scanner!")
            break
