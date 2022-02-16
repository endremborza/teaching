from pathlib import Path
import json

import boto3

bucket = "borza-public-data"
subdir = "swimming-pool-packs"


def load_pack(pack_id="S-10", out_path="./pack.zip"):
    s3_client = boto3.client("s3")
    s3_client.download_file(bucket, f"{subdir}/{pack_id}.zip", out_path)


def evaluate(solution_dir, true_results):
    out = json.loads((Path(solution_dir) / "output.json").read_text())
    if out == true_results:
        return True

    msg = f"len(true_results)={len(true_results)}, len(output)={len(out)}"
    for i, (res, calc) in enumerate(zip(true_results, out)):
        if res != calc:
            msg += f"\nTRUE RESULT != OUTPUT at {i}:\n{res} != {calc}"
            break
    print(f"-------" * 10, "EVALUATION ERROR", msg, f"-------" * 10, sep="\n")
    return False
