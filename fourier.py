import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 96000
meander_freq = 100000
rise_fall_time = 20e-9

duty_cycles = [i / 100 for i in range(10, 61, 10)]
time = np.arange(0, 1e-3, 1 / sampling_rate)

for duty_cycle in duty_cycles:
    meander_signal = np.where(
        (time % (1 / meander_freq)) < (duty_cycle / meander_freq), 1, 0
    )

    spectrum = np.fft.fft(meander_signal)
    freqs = np.fft.fftfreq(len(meander_signal), 1 / sampling_rate)

    plt.figure(figsize=(10, 5))
    plt.plot(freqs[: len(freqs) // 2], np.abs(spectrum)[: len(freqs) // 2])
    plt.title(f"Спектр сигнала меандра, скважность {int(duty_cycle * 100)}%")
    plt.xlabel("Частота (Гц)")
    plt.ylabel("Амплитуда")
    plt.grid()
    plt.show()

    harmonics = freqs[np.abs(spectrum) > np.max(np.abs(spectrum)) * 0.1]
    print(f"Скважность {int(duty_cycle * 100)}%: Паразитные частоты (Гц): {harmonics[harmonics > 0]}")
