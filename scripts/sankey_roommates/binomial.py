from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import UnivariateSpline, interp1d

n = 86
p = 0.051


k_range = 18
k_vals = list(range(k_range))

pmf = []
for k in k_vals:
    binomial = binom.pmf(k, n, p)
    print(f"{k}, {binomial}")
    pmf.append(binomial)


fine_k_vals = np.arange(0, k_range, 0.001)


# us = UnivariateSpline(k_vals, pmf, k=5)
# interpolated = us(fine_k_vals)
# interpolated = interp1d(k_vals, pmf, kind="linear")(pmf)

z = np.polyfit(k_vals, pmf, 10)
f = np.poly1d(z)
interpolated = f(fine_k_vals)


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel(r"Number of successes ($k$)", color="w")
ax.set_ylabel("Probability", color="w")
ax.set_ylim([-0.01, 0.20])
ax.plot(fine_k_vals, interpolated, color="lightgrey", zorder=1)
ax.scatter(k_vals, pmf, color="dodgerblue", zorder=100)

ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white')
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')
ax.xaxis.label.set_color('white')
ax.yaxis.label.set_color('white')
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

# plt.show()
plt.savefig("binomial.png", dpi=400, transparent=True)
