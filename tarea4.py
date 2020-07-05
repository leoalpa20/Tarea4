### Tarea 4 ####
# Created by Leonardo Alfaro on 02/06/2020
# Finished on 05/07/2020

# Imports

import numpy as np
from scipy import stats
from scipy import signal
from scipy import integrate
import matplotlib.pyplot as plt

# Punto 1

frequency = 5000 # frequency is 5 kHz

bits = np.genfromtxt("bits10k.csv", dtype=int, delimiter=",", skip_header=False) # getting the bits
amountBits = len(bits)

T = 1/frequency # Period of the signal

resolution = 1000 # Number of points for the signals gives us the "resolution"

pointsPerPeriod = np.linspace(0, T, resolution) # linspace from zero to period with 100 points per space

# Carrier signals
#BPSK modulation uses sine when one and minus sine when zero
sine = np.sin(2*np.pi * frequency * pointsPerPeriod)
minusSine = -(np.sin(2*np.pi * frequency * pointsPerPeriod))


# Sampling frequency (Nyquist theorem)

samplingFrequency = resolution/T # 500 kHz

# storing all of the values for the modulated signal

tempLine = np.linspace(0, amountBits*T, amountBits*resolution) # size 100*10000

# Vector that will hold the modulated signal

modulatedSignal = np.zeros(tempLine.shape)

# Creation of the modulated signal


for k, b in enumerate(bits):
    if b == 1:
        modulatedSignal[k*resolution:(k+1)*resolution] = b * sine
    else:
        modulatedSignal[k * resolution:(k + 1) * resolution] = minusSine

pb = 5
plt.plot(modulatedSignal[0: pb*resolution])
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Modulated signal showing first 5 bits")
plt.show()


# Punto 2

instantPower = modulatedSignal**2

averagePower = integrate.trapz(instantPower, tempLine) / (amountBits * T)
print("The average power is", averagePower)

# Punto 3

for n in range(0, 5):
    SNR = range(-2, 3)

    noise_power = averagePower / (10**(SNR[n]/10))
    print("SNR is", SNR[n])

    sigma = np.sqrt(noise_power) # standard noise deviation

    noise = np.random.normal(0, sigma, modulatedSignal.shape) # Creating the noise

    received_signal = modulatedSignal + noise # received signal always has some noise

    pb = 8
    plt.plot(received_signal[0:pb*resolution])
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title("Noisy signal with a SNR ranging from -2 to 3 dB")
    plt.show()

# Punto 4

#Before adding the noise
#Spectral plot of the power using scipy

fw, PSD = signal.welch(modulatedSignal, samplingFrequency, nperseg=1024)
plt.plot(fw, PSD)
plt.semilogy(fw, PSD)
#Labels
plt.xlabel("Frequency/Hz")
plt.ylabel("Spectral plot of power / V**2/Hz")
plt.show()

#After adding the noise

fw, PSD = signal.welch(received_signal, samplingFrequency, nperseg=1024)
plt.semilogy(fw, PSD)

#Labels
plt.xlabel("Frequency/Hz")
plt.ylabel("Spectral plot of power / V**2/Hz")
plt.show()

# Punto 5
# Demodulating the signal and doing a BER (bit error rate)

#pseudo-energy of the original wave, sum not integrated

sine_energy = np.sum(sine**2) #Same for the -sine

received_bits_vector = np.zeros(bits.shape) # vector of zeros to receive the signal with the shape of bits

vector = np.zeros(5)
#Decodifying the signal by energy detection

for n in range(0, 5):
    for k, b in enumerate(bits):
        received_signal_energy = np.sum(received_signal[k*resolution:(k+1)*resolution] * sine)
        if received_signal_energy > sine_energy/2:
            received_bits_vector[k] = 1
        else:
            received_bits_vector[k] = 0


    errors = np.sum(np.abs(bits-received_bits_vector))

    BER = errors/amountBits #Bit error rate


    BER = vector[n]

    print("There is a total of {} errors in {} bits for an "
        "error rate of {}".format(errors, amountBits, BER))


# Punto 6


plt.plot(vector, SNR)
plt.xlabel("BER")
plt.ylabel("SNR")
plt.title("BER vs SNR")
plt.show()

