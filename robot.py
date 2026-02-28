
import requests
import re

def clean_playlist(input_file='playlist.m3u', output_file='playlist.m3u'):
    with open(input_file, 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()

    cleaned_lines = []
    for i in range(len(lines)):
        line = lines[i]
        # Filtering Logic (Strict): Remove lines/channels containing keywords
        if re.search(r'4k|2k|uhd|4К|2К', line, re.IGNORECASE):
            continue

        # Perform connection test for HTTP/HTTPS links
        if line.startswith('http://') or line.startswith('https://'):
            url = line.strip()
            try:
                response = requests.get(url, timeout=10, stream=True)
                response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
                cleaned_lines.append(line)
            except requests.exceptions.RequestException as e:
                print(f"Skipping unresponsive or error link: {url} - {e}")
        else:
            cleaned_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.writelines(cleaned_lines)

if __name__ == '__main__':
    clean_playlist()
