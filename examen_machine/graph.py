import matplotlib.pyplot as plt

# Résultats notés à la main après les 4 lancements
temps = {1: 56.5, 2: 55.4, 4: 57.4, 8: 54.4}  # en ms

threads  = list(temps.keys())
speedups = [585/temps[n] for n in threads]

plt.plot(threads, speedups, 'o-', label='mesuré')
plt.plot(threads, threads,  '--', label='idéal')
plt.xlabel("Threads") ; plt.ylabel("Speedup")
plt.legend() ; plt.grid(True) ; plt.show()