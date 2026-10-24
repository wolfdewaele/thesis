"""Build a mixture set from a data config; key=value pairs override config entries.

python scripts/make_mixtures.py configs/data/pilot_v0.yaml
python scripts/make_mixtures.py configs/data/pilot_v0.yaml n_scenes=5 seed=1 out_dir=data/processed/try
"""

import argparse

import yaml

from hased.data.mixtures import make_mixtures

parser = argparse.ArgumentParser()
parser.add_argument("config", help="configs/data/<name>.yaml")
parser.add_argument("overrides", nargs="*", help="key=value, value parsed as YAML")
args = parser.parse_args()
with open(args.config) as f:
    cfg = yaml.safe_load(f)
for item in args.overrides:
    key, value = item.split("=", 1)
    if key not in cfg:
        parser.error(f"unknown config key: {key}")
    cfg[key] = yaml.safe_load(value)
make_mixtures(cfg)
