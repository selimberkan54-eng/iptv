import requests

input_file = "playlist.m3u"
output_file = "playlist_clean.m3u"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

clean_lines = []

for i, line in enumerate(lines):
    if line.startswith("http"):
        try:
            r = requests.head(line, timeout=5)
            if r.status_code == 200:
                clean_lines.append(line)
            else:
                print(f"Мёртвый поток: {line.strip()}")
        except:
            print(f"Ошибка доступа: {line.strip()}")
    else:
        clean_lines.append(line)

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(clean_lines)

print("Очистка M3U завершена")
