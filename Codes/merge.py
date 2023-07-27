import numpy as num
import math as mathpy
from matplotlib import pyplot as plt


Usum_2coop = [23.075143260708874, 17.239219205243742, 15.090512440771457, 12.510293987513794, 11.409280692421737, 10.350511655075298, 9.6435672759982, 9.240742981756746, 9.527731968600861, 10.28638634755034, 11.403983051763749, 12.550449322826543, 13.433718505406429, 14.214001469157182, 15.0327705768871, 15.502066268421903, 16.08487581630277, 16.561410424464896, 16.92962185505846, 17.18930815452055]

Usum_2Max = [25.986180234822022, 19.68653543628902, 16.071216840947287, 13.277821674221766, 11.931447775776775, 10.653451114327751, 9.73207167259628, 9.267492201951942, 9.527731968600861, 10.28638634755034, 11.403983051763753, 12.550449322826548, 13.433718505406432, 14.214001469157182, 15.0327705768871, 15.502066268421903, 16.08487581630277, 16.561410424464896, 16.92962185505846, 17.189308154520553]

Usum_3coop = [252.0981953065912, 253.07308983538405, 254.0090021675159, 254.8871477980487, 252.10616860119615, 252.73128292542796, 253.25701011071482, 253.6557122137014, 253.8970400362207, 253.94830968603281, 253.7750720227318, 246.7762914257464, 245.97221668463496, 244.89951977731027, 243.52916141434264, 241.83476925715735, 239.7938536311695, 237.3889674176466, 234.6087204995598, 231.44856228733653]

Usum_3max = [269.833204380438, 269.431253677952, 268.90266644507295, 268.227590568525, 267.3841209390642, 266.3483828850595, 265.0947196102385, 263.6316240502123, 262.40460792860864, 261.24631162583796, 260.0464644765731, 258.76232992287635, 257.1874311939959, 255.4125461481657, 253.36553357278098, 250.87050253153427, 248.0427815891765, 245.01037140401917, 241.51343364693156, 237.5563536339111]

Usum_original = [15.53688458678733, 12.10405900686531, 10.379458134161426, 9.260609589636635, 8.456408460545974, 7.852960315869295, 7.376841763550882, 7.184626565626969, 7.413891219100109, 7.952154394150617, 8.732154703557528, 9.69977425015854, 10.795741426791604, 12.216108224453908, 13.723350811220485, 15.356536525074311, 17.038605987571128, 18.587672532448263, 20.0923553375336, 21.101520942403013]

Gamma = [0.01, 0.060000000000000005, 0.11, 0.16000000000000003, 0.21000000000000002, 0.26000000000000001, 0.31000000000000005, 0.36000000000000004, 0.41000000000000003, 0.46000000000000002, 0.51000000000000001, 0.56000000000000005, 0.6100000000000001, 0.66000000000000003, 0.71000000000000008, 0.76000000000000001, 0.81000000000000005, 0.8600000000000001, 0.91000000000000003, 0.96000000000000008]





f, (ax, ax2) = plt.subplots(2, 1, sharex=True)

# plot the same data on both axes
#ax.plot(pts)
#ax2.plot(pts)
ax.plot(Gamma, Usum_2coop, '-r>', label = 'Usum_2coop')
ax.plot(Gamma, Usum_2Max, '-bD', label = 'Usum_2Max')
ax.plot(Gamma, Usum_original, '-kp', label = 'Usum_original')
ax.plot(Gamma, Usum_3coop, '-gx', label = 'Usum_3coop')
ax.plot(Gamma, Usum_3max, '-c<', label = 'Usum_3max')


ax2.plot(Gamma, Usum_2coop, '-r>', label = 'Usum_2coop')
ax2.plot(Gamma, Usum_2Max, '-bD', label = 'Usum_2Max')
ax2.plot(Gamma, Usum_original, '-kp', label = 'Usum_original')
ax2.plot(Gamma, Usum_3coop, '-gx', label = 'Usum_3coop')
ax2.plot(Gamma, Usum_3max, '-c<', label = 'Usum_3max')


# zoom-in / limit the view to different portions of the data
ax.set_ylim(220, 280)  # outliers only
ax2.set_ylim(5, 30)  # most of the data

# hide the spines between ax and ax2
ax.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax.xaxis.tick_top()
ax.tick_params(labeltop='off')  # don't put tick labels at the top
ax2.xaxis.tick_bottom()

# This looks pretty good, and was fairly painless, but you can get that
# cut-out diagonal lines look with just a bit more work. The important
# thing to know here is that in axes coordinates, which are always
# between 0-1, spine endpoints are at these locations (0,0), (0,1),
# (1,0), and (1,1).  Thus, we just need to put the diagonals in the
# appropriate corners of each of our axes, and so long as we use the
# right transform and disable clipping.

d = .005  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

# What's cool about this is that now if we vary the distance between
# ax and ax2 via f.subplots_adjust(hspace=...) or plt.subplot_tool(),
# the diagonal lines will move accordingly, and stay right at the tips
# of the spines they are 'breaking'
plt.xlabel(r'$\gamma$')
plt.xlim(0,0.97)
# plt.ylabel('utility', labelpad=5)
ax.set_ylabel('utility')
ax2.set_ylabel('utility')
plt.legend(loc=9, ncol=2, fontsize=10, bbox_to_anchor=(0, 0, 1, 1),
           fancybox=True,shadow=True)
plt.show()























#plt.plot(Gamma, Usum_2coop, '-r>', label = 'Usum_2coop')
#plt.plot(Gamma, Usum_2Max, '-bD', label = 'Usum_2Max')
#plt.plot(Gamma, Usum_3coop, '-gx', label = 'Usum_3coop')
#plt.plot(Gamma, Usum_3max, '-c<', label = 'Usum_3max')
#plt.plot(Gamma, Usum_original, '-kp', label = 'Usum_original')

#plt.show()











