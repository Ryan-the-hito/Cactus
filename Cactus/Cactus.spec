# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

__version__ = '1.0.4'

info_plist = {
    'LSUIElement': True,
    #'LSBackgroundOnly': True,
}

a = Analysis(
    ['Cactus.py'],
    pathex=['/Users/ryanshenefield/Downloads/Cactus.py'],
    binaries=[],
    datas=[('cactus-desk.icns', '.'), ('cactus-tray.icns', '.'), ('cactus.png', '.'), ('wechat50.png', '.'), ('wechat20.png', '.'), 
              ('wechat10.png', '.'), ('wechat5.png', '.'), ('alipay50.png', '.'), ('alipay20.png', '.'), ('alipay10.png', '.'), 
              ('alipay5.png', '.'), ('SetTime.txt', '.'), ('BetTime.txt', '.'), ('TetTime.txt', '.')],
    hiddenimports=['pyautogui'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Cactus',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Cactus',
)
app = BUNDLE(
    coll,
    name='Cactus.app',
    icon='cactus-desk.icns',
    info_plist=info_plist,
    bundle_identifier=None,
    version=__version__,
)
