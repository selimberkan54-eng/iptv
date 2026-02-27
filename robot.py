import requests

input_file = "playlist.m3u"
# Сохраняем в тот же файл, чтобы GitHub Actions увидел изменения
output_file = "playlist.m3u" 

try:
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"Ошибка: Файл {input_file} не найден!")
    exit(1)

clean_lines = []

for line in lines:
    line = line.strip()
    if not line:
        continue
        
    if line.startswith("http"):
        try:
            # Используем get вместо head, так как некоторые сервера блокируют head-запросы
            r = requests.get(line, timeout=10, stream=True)
            if r.status_code == 200:
                clean_lines.append(line + "\n")
            else:
                print(f"Мёртвый поток: {line}")
        except:
            print(f"Ошибка доступа: {line}")
    else:
        clean_lines.append(line + "\n")

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(clean_lines)

print("Очистка M3U завершена. Результат сохранен в playlist.m3u")
            
