# create the signal
import numpy.polynomial.polynomial as _Npp
import numpy as np
import matplotlib.pyplot as plt

####  Ken's build_signal   - allow for more variable oscillations.
####  neural oscillations aren't sinusoids, rather their periods
####  fluctuate.  Use AR(2) 
def build_signal(N, dt, comps, wgts):
    obsvd = np.zeros(N)
    ic = -1

    for comp in comps:
        ic += 1
        r_comp = comp[1]
        osc_comp = comp[0]

        l_alfa = []
        for thr in osc_comp:
            r = thr[1]
            hz= thr[0]
            th = 2*hz*dt

            l_alfa.append(r*(np.cos(np.pi*th) + 1j*np.sin(np.pi*th)))
            l_alfa.append(r*(np.cos(np.pi*th) - 1j*np.sin(np.pi*th)))
        for r in r_comp:
            l_alfa.append(r)

        alfa  = np.array(l_alfa)
        ARcoeff          = (-1*_Npp.polyfromroots(alfa)[::-1][1:]).real
        sgnlC, y = createDataAR(N, ARcoeff, 0.01, 0)
        obsvd += wgts[ic] * sgnlC

    return obsvd / np.std(obsvd)


def createDataAR(N, B, err, obsnz, trim=0):
    #  a[1]^2 + 4a[0]
    #  B[0] = -0.45
    #  B[1] =  0.9
    err = np.sqrt(err)
    obsnz  = np.sqrt(obsnz)
    p = len(B)
    BB = np.array(B[::-1])   #  B backwards

    x    = np.empty(N)
    y    = np.empty(N)

    #  initial few
    for i in range(p+1):
        x[i] = err*np.random.randn()
        y[i] = obsnz*np.random.randn()

    nzs = err*np.random.randn(N)
    for i in range(p+1, N):
        #x[i] = _N.dot(B, x[i-1:i-p-1:-1]) + nzs[i]
        x[i] = np.dot(BB, x[i-p:i]) + nzs[i]
        #  y = Hx + w   where w is a zero-mean Gaussian with cov. matrix R.
        #  In our case, H is 1 and R is 1x1
    onzs = obsnz*np.random.randn(N)
    y[p+1:N] = x[p+1:N] + onzs[p+1:N]

    return x[trim:N], y[trim:N]
