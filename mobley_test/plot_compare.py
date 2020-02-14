import numpy
from matplotlib import pyplot

bem = numpy.loadtxt('energy_bem.txt')
mobley = numpy.loadtxt('mobley_results_clean.txt')

index_clean = numpy.where(abs(bem)>1e-12)[0]

fig,ax = pyplot.subplots()
ax.scatter(bem[index_clean], mobley[index_clean])

lims = [
    numpy.min([ax.get_xlim(), ax.get_ylim()]),  # min of both axes
    numpy.max([ax.get_xlim(), ax.get_ylim()]),  # max of both axes
]

ax.plot(numpy.array([lims[0],lims[1]]), numpy.array([lims[0],lims[1]]), c='k')

ax.set_aspect('equal')
ax.set_xlim(lims)
ax.set_ylim(lims)
ax.set_xlabel('BEM')
ax.set_ylabel('Mobley')

fig.savefig('energy_compare.png')

