#!/usr/bin/env python3
"""Keep the reviewable patch and the self-contained build workflow identical."""
import argparse
import base64
import hashlib
from pathlib import Path
import re
import textwrap
import zlib

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--check', action='store_true', help='validate without modifying the workflow')
args = parser.parse_args()
root = Path(__file__).resolve().parent.parent
patch = (root / 'patches/ventura-1.5.5.patch').read_bytes()
workflow = root / '.github/workflows/ventura-build.yml'
text = workflow.read_text()
payload_pattern = r'          encoded = """\n(.*?)\n          """'
digest_pattern = r'assert hashlib.sha256\(patch\).hexdigest\(\) == "([0-9a-f]{64})"'
payload = re.search(payload_pattern, text, re.S)
digest = re.search(digest_pattern, text)
if payload is None or digest is None:
    raise SystemExit('Expected embedded patch and checksum were not found.')
expected = hashlib.sha256(patch).hexdigest()
if args.check:
    if zlib.decompress(base64.b64decode(payload.group(1))) != patch or digest.group(1) != expected:
        raise SystemExit('Readable patch and workflow differ. Review changes and run without --check to sync.')
    print(f'PASS: readable and embedded patches match ({expected}).')
else:
    encoded = base64.b64encode(zlib.compress(patch, 9)).decode()
    replacement = '          encoded = """\n' + '\n'.join('          ' + line for line in textwrap.wrap(encoded, 100)) + '\n          """'
    text = re.sub(payload_pattern, lambda _: replacement, text, count=1, flags=re.S)
    text = re.sub(digest_pattern, lambda _: f'assert hashlib.sha256(patch).hexdigest() == "{expected}"', text, count=1)
    workflow.write_text(text)
    print(f'Updated workflow patch ({expected}).')
