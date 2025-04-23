# Security Header Scanner

A simple Python tool to scan websites for common HTTP security headers.

## 🔐 Features

- Manual or bulk URL scanning
- Checks for key HTTP security headers:
  - Content-Security-Policy
  - Strict-Transport-Security
  - X-Frame-Options
  - X-Content-Type-Options
  - Referrer-Policy
  - Permissions-Policy
- Generates individual or bulk log files with scan results

## ⚙️ Requirements

- Python 3.6+
- `requests` library (install with `pip install requests`)

## 🚀 Installation

Clone the repo or download the `security_header_scanner_en.py` file and run:

```bash
python security_header_scanner_en.py
```

## 🧪 Usage

When prompted:

- Choose `m` for **manual mode** to scan a single URL
- Choose `f` for **bulk mode** to scan multiple URLs from a file

### ⚠️ Important for bulk usage:
- Create a file named `url_list.txt` in the same folder
- Add **one URL per line**
- **DO NOT leave a blank line at the end of the file**

Example `url_list.txt`:

```
https://example.com
https://github.com
https://google.com
```

The results will be saved to `bulk_scan_report.txt`.

## 📦 Output

- In manual mode: Results saved to `scan_log_<domain>.txt`
- In bulk mode: All results saved to `bulk_scan_report.txt`

## 👨‍💻 Author

Made with ❤️ by Džony
