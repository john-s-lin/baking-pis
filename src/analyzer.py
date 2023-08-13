import datetime
import matplotlib.pyplot as plt
from metrics import Metrics
import numpy as np


class Analyzer:
    @classmethod
    def parse_metrics_to_numpy(
        cls, metrics: list[Metrics]
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        times = [metric.time for metric in metrics]
        time_delta = cls.convert_time_to_delta(times)
        cpu_temp = np.array([metric.cpu_temp for metric in metrics])
        clock_freq = np.array([metric.clock_freq for metric in metrics])
        return time_delta, cpu_temp, clock_freq

    @classmethod
    def convert_time_to_delta(cls, times: list[datetime.datetime]) -> np.ndarray:
        origin = times[0]
        delta = np.array([(time - origin).total_seconds() for time in times])
        return delta

    @classmethod
    def generate_plot(
        cls,
        filename: str,
        time_delta: np.ndarray,
        cpu_temp: np.ndarray,
        clock_freq: np.ndarray,
    ):
        fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
        ax[0].plot(time_delta, cpu_temp, color="red")
        ax[0].set_ylim([30, 60])
        ax[0].set_ylabel("CPU Temp (C)", color="red")

        ax[1].plot(time_delta, clock_freq, color="green")
        ax[1].set_ylabel("Clock Frequency (MHz)", color="green")
        ax[1].set_xlabel("Time (s)")

        title = (
            "RPi 4B 2GB Passive Cooling + Thermal Paste"
            if "cpu_temp_1" in filename
            else "RPi 4B 4GB Active Cooling + Thermal Pads"
        )
        fig.suptitle(title)
        plt.savefig(filename)
        plt.close()
