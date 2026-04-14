import os
import glob
import shutil

docs_dir = 'tutorials/docs'
files = glob.glob(os.path.join(docs_dir, '**', '*.md'), recursive=True)

for file in files:
    filename = os.path.basename(file)
    dirname = os.path.dirname(file)
    
    if filename.endswith('_ENG.md'):
        base = filename[:-7]
        new_en = os.path.join(dirname, base + '.en.md')
        new_pt = os.path.join(dirname, base + '.pt.md')
        os.rename(file, new_en)
        # Ensure a pt version exists, even if it's just english content
        if not os.path.exists(new_pt):
            shutil.copy(new_en, new_pt)
    elif filename.endswith('_ptbr.md'):
        base = filename[:-8]
        new_pt = os.path.join(dirname, base + '.pt.md')
        os.rename(file, new_pt)
    elif filename.endswith('-ptbr.md'):
        base = filename[:-8]
        new_pt = os.path.join(dirname, base + '.pt.md')
        os.rename(file, new_pt)
    elif filename == 'STR5-Model3.mkdocs gh-deploy --forcemd':
        pass # this was already fixed in yml but file doesn't exist
    elif not filename.endswith('.pt.md') and not filename.endswith('.en.md') and not filename.endswith('.es.md'):
        # Normal .md file, rename to .pt.md
        base = filename[:-3]
        new_pt = os.path.join(dirname, base + '.pt.md')
        os.rename(file, new_pt)

