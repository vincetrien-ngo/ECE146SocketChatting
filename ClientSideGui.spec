# -*- mode: python -*-

block_cipher = None


a = Analysis(['ClientSideGui.py'],
             pathex=['C:\\Users\\Hannselthill Camacho\\Desktop\\ugoChat\\ECE146SocketChatting'],
             binaries=[],
             datas=[],
             hiddenimports=['pyqt5'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='ClientSideGui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='ClientSideGui')
