from zipfile import ZipFile
from pathlib import Path
import json
import tempfile


def load_pack(pack_id="P-1", out_path="./pack.zip"):
    tmp_dir = tempfile.TemporaryDirectory()
    res_path, in_path, d_path = [Path(tmp_dir.name, k) for k in ["r", "i", "d"]]
    res_path.write_text(json.dumps({"A": 10}))
    in_path.write_text(json.dumps({"B": 10}))
    d_path.write_text(json.dumps({"C": 10}))
    with ZipFile(out_path, "w") as zip_path:
        zip_path.write(res_path, "results.json")
        zip_path.write(in_path, "input.json")
        zip_path.write(d_path, "data.json")

    tmp_dir.cleanup()

def evaluate(solution_dir, true_results):
    out = json.loads((Path(solution_dir) / "output.json").read_text())
    if out == true_results:
        return True
    return False
