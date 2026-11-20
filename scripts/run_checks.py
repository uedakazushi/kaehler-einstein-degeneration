"""Run recovered certificate scripts in build/, preserving original source files."""
from pathlib import Path
import subprocess
import shutil
import sys
import json
import hashlib

root = Path(__file__).resolve().parents[1]
out = root / 'build/certificate-runs'
out.mkdir(parents=True, exist_ok=True)
summary = []
for source in sorted((root / 'scripts').rglob('*.py')):
    if source.resolve() == Path(__file__).resolve():
        continue
    relative = source.relative_to(root / 'scripts')
    target = out / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    with target.with_suffix('.log').open('w') as log:
        result = subprocess.run([sys.executable, str(target)], cwd=target.parent,
                                stdout=log, stderr=subprocess.STDOUT)
    summary.append({'script': str(relative), 'exit_code': result.returncode,
                    'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest()})
    print(relative, result.returncode, flush=True)
(out / 'summary.json').write_text(json.dumps(summary, indent=2) + '\n')
raise SystemExit(any(row['exit_code'] for row in summary))
