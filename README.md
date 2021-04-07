# FitSpectrum

This notebook shows fitting of power spectrum can be well approximated as 1/f decay plus some bumps representing oscillatory activity at certain frequency bands.

It shows fitting a model of the spectrum using pymc3 using simulated EEG data and real human EEG during simple behavioral task.

It also shows another complimentary approach called AR decomposition, where time-domain signal is fitted using an AR(p) with a specified structure consisting of R non-oscillatory
AR(1) roots and C oscillatory AR(2) roots.

Take open the Colab notebook to look at the data and fit it.
