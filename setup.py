from cream.dist import setup

setup('src/manifest.xml',
    data_files = [
        ('{module_dir}', ['src/watcher.py', 'src/manifest.xml'])
        ]
    )
