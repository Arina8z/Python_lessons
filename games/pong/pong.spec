# pong.spec
import os
import sys
from PyInstaller.utils.hooks import collect_data_files

# Функция для добавления папок рекурсивно
def get_resources(path):
    data = []
    for root, _, files in os.walk(path):
        if not files:
            continue
        # Получаем относительный путь от текущей директории
        target_path = os.path.relpath(root)
        data += [(os.path.join(root, f), target_path) for f in files]
    return data

# Путь к ресурсам
resources = get_resources('resources')

a = Analysis(
    ['pong.py'],
    pathex=[os.getcwd()],
    binaries=[],
    datas=resources,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='pong',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    clean=False,
#    icon='resources/images/icon.ico'  # если есть иконка
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='pong'
)