"""."""

import yaml
from evaluation.static_evaluation.nuscenes.eval import eval_nusc


if __name__ == "__main__":
    cfg = yaml.load(open("./config/nuscenes.yaml", "r"), Loader=yaml.Loader)
    cfg["SAVE_PATH"] = "results/nuscenes/20250818_163644"
    eval_nusc(cfg)
