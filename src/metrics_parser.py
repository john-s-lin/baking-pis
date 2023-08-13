import datetime
from metrics import Metrics


class MetricsParser:
    @classmethod
    def open_file_as_list(cls, filename: str) -> list[str]:
        with open(filename, "r") as f:
            return f.readlines()

    @classmethod
    def generate_metrics_list(cls, lines: list[str]) -> list[Metrics]:
        metrics = []
        for line in lines:
            metrics.append(cls.generate_metrics_from_line(line))
        return metrics

    @classmethod
    def generate_metrics_from_line(cls, line: str) -> Metrics:
        elements = line.split("\t")
        datetime = cls.parse_date(elements[0])
        cpu_temp = float(elements[1])
        clock_freq = int(elements[3].strip("\n"))
        return Metrics(datetime, cpu_temp, clock_freq)

    @classmethod
    def parse_date(cls, date: str) -> datetime.datetime:
        return datetime.datetime.strptime(date, "%a %d %b %Y %I:%M:%S %p %Z")
