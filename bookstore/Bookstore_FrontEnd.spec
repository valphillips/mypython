# -*- mode: python -*-

block_cipher = None


a = Analysis(['Bookstore_FrontEnd.py'],
             pathex=['C:\\Users\\vmp2303\\Dropbox\\Val_Work\\Python\\Training\\Bookstore_ App'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Bookstore_FrontEnd',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
