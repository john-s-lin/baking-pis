from analyzer import Analyzer
from metrics_parser import MetricsParser
import os
import re
import sys


def generate_image_name(filename: str) -> str:
    return filename.replace(".log", ".png").replace("data", "out")

def make_output_dir():
    if not os.path.exists("out"):
        os.mkdir("out")


def main(argv: list[str]):
    target_log_file = argv[0]

    if not re.search(r"cpu_temp_\d+.log", target_log_file):
        print("Invalid file name, must match 'cpu_temp_{int}.log")
        exit(1)

    image_file = generate_image_name(target_log_file)
    make_output_dir()

    if not target_log_file.startswith("data/"):
        target_log_file = "data/" + target_log_file

    lines = MetricsParser.open_file_as_list(target_log_file)
    metrics = MetricsParser.generate_metrics_list(lines)
    np_metrics = Analyzer.parse_metrics_to_numpy(metrics)

    Analyzer.generate_plot(image_file, *np_metrics)


if __name__ == "__main__":
    main(sys.argv[1:])
