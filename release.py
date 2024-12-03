from os import listdir, mkdir, path
from shutil import copytree, move, rmtree
import subprocess

from source.py.utils import joinPaths

output_base = "fonts"
output_release = "release"


def move_and_log(file_path: str, target_path: str):
    print(f"Move {file_path} -> {target_path}")
    move(file_path, target_path)

def build(normal: bool, hinted: bool, cache: bool = False):
    args = [
        "python",
        "build.py",
        "--archieve",
        "--cn-both",
    ]

    if cache:
        args.append("--cache")

    if normal:
        args.append("--normal")

    if hinted:
        args.append("--hinted")
    else:
        args.append("--no-hinted")

    print(" ".join(args))
    subprocess.run(args)

    build_archieve_dir = f"{output_base}/archieve"

    for file_name in listdir(build_archieve_dir):
        file_path = joinPaths(build_archieve_dir, file_name)
        if path.isfile(file_path):
            if not hinted:
                name, ext = path.splitext(file_name)
                file_name = f"{name}-unhinted{ext}"

            move_and_log(file_path, joinPaths(output_release, file_name))


# clear old releases
rmtree(output_base, ignore_errors=True)
mkdir(output_base)
rmtree(output_release, ignore_errors=True)
mkdir(output_release)

# build all formats
build(normal=True, hinted=True)
build(normal=True, hinted=False, cache=True)
build(normal=False, hinted=True)
build(normal=False, hinted=False, cache=True)

# copy woff2 to root
rmtree("woff2", ignore_errors=True)
copytree(f"{output_base}/woff2", "woff2")
print("Copy woff2 to root")

subprocess.run(f"ftcli converter ft2wf -out woff2/var -f woff2 {output_base}/variable")

target_dir = "website/public-dev/fonts"
rmtree(target_dir, ignore_errors=True)
copytree("woff2/var", target_dir)
