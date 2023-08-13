# baking-pis

Benchmarking passively and actively cooled Raspberry Pis with automated analytics.

## Dependencies

### Raspberry Pi:

- [`stress-ng`](https://wiki.ubuntu.com/Kernel/Reference/stress-ng)

```bash
# To install on Raspberry Pi OS
sudo apt install stress-ng
```

- Jeff Geerling's [`pi-cpu-stress.sh`](https://gist.github.com/geerlingguy/91d4736afe9321cbfc1062165188dda4) (modified)

```bash
# To download and review the code on your own
wget https://gist.githubusercontent.com/geerlingguy/91d4736afe9321cbfc1062165188dda4/raw/f6cbb1c540405fc677e8f530d878f72d7b7dd226/pi-cpu-stress.sh
```

### Python:

```bash
# Tested on Python 3.11.x
pip install -r requirements.txt
```

## Results

#### Passive Cooling

```
Raspberry Pi 4 Model B 2GB
Armor Passive Heatsink Case
Thermal paste
```

![Raspberry Pi 4 Model B Passive Cooling](./out/cpu_temp_1.png)

#### Active Cooling

```
Raspberry Pi 4 Model B 4GB
Armor Heatsink Case w/ Fan
Thermal pads
```

![Raspberry Pi 4 Model B Active Cooling](./out/cpu_temp_2.png)
