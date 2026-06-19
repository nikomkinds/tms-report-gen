# tms-report-gen

Модуль генерации PDF и DOCX отчётов из TMS CSV файлов.

Поддерживает:
- генерацию отдельных отчётов для каждого тест-кейса
- PDF (WeasyPrint)
- DOCX (python-docx)
- базовую HTML-разметку

---

# Установка

## 1. Клонирование проекта

```bash
git clone https://github.com/nikomkinds/tms-report-gen.git
cd tms-report-gen
```

---

## 2. Создание виртуального окружения

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

### Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Установка Python зависимостей

```bash
pip install -r requirements.txt
```

---

# Установка GTK для работы WeasyPrint

## Windows

1. Скачать GTK runtime:

https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases

2. Установить:
- gtk3-runtime-*-x64.exe

3. Перезапустить терминал.

---

## Linux (Debian/Ubuntu)

```bash
sudo apt install \
    libpango-1.0-0 \
    libcairo2 \
    libgdk-pixbuf-2.0-0 \
    libffi-dev
```

---

# Использование

```python
from tms_report_gen import generate_reports


generate_reports(
    cases_csv_path="case_case.csv",         # Cases CSV file path
    steps_csv_path="case_casestep.csv",     # Case steps CSV file path
    output_dir="reports",                   # Output directory path
    report_format=None,                     # Report format: "pdf", "docx" or None for both
)
```

---

# Поддерживаемые HTML теги

- p
- b
- i
- pre
- code
- br

---

# Версия python
- 3.11+