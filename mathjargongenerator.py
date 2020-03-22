import random
import numpy

#nouns = ['surfaces', 'manifolds', 'complexities', 'ideals', 'matrices', 'fractals', 'ranks', 'systems', 'curves', 'frames', 'maps', 'obstructions', 'ensembles', 'estimates', 'dimensions', 'forms', 'sigularities', 'differential equations', 'integrals', 'algorithms', 'calculi', 'equations', 'invariants', 'geometries', 'homomorphisms', 'spaces', 'fields', 'varieties', 'domains', 'characteristics', 'groups', 'generalizations', 'dynamics', 'moduli', 'measures', 'topologies', 'graphs', 'operators', 'series', 'extensions', 'metrics', 'truncations', 'expansions', 'limits', 'sequences', 'elements', 'sets', 'equations', 'polynomials', 'models', 'regularities', 'roots', 'homologies', 'complexes']

#adjectives = ['differentiable', 'elliptic', 'fractional', 'affine', 'abstract', 'ergodic', 'diagonal', 'iterated', 'stochastic', 'symplectic', 'degenerate', 'convex', 'discrete', 'infinite', 'modular', 'canonical', 'bounded', 'hypergeometric', 'unusual', 'irrational', 'inconsistent', 'constructive', 'congruent', 'supplementary', 'logarithmic', 'indefinite', 'maximal', 'ordered', 'uncountable', 'non-commutative', 'associative', 'general', 'bounded', 'continuous', 'idempotent', 'functional', 'generating', 'exponential', 'orthogonal', 'linear', 'cyclotomic', 'trivial', 'compact', 'representative', 'solvable', 'quadratic', 'projective', 'bipartite', 'positive', 'bilinear', 'partial', 'quantitative', 'reductive', 'normalisable', 'nilpotent', 'symmetric', 'analytic', 'algebraic', 'smooth', 'algorithmic', 'absolute', 'complex', 'multiplicative', 'birational', 'measurable', 'trivial', 'binary']
                
#premodifiers = ['non-', 'sub-', 'anti-']

#adverbs = ['locally', 'finitely', 'conditionally', 'trivially', 'uniformly', 'partially', 'orthogonally', 'axially']

nouns = numpy.loadtxt('nouns.txt', dtype='str')

adjectives = numpy.loadtxt('adjectives.txt', dtype='str')

padjectives = ['Abelian', 'Gaussian', 'semi-Riemannian', 'Eulerian', 'Galois', 'Cauchy', 'Cartesian', 'Markovian', 'Diophantine', 'Fourier', 'Monge-Ampere', 'Borel', 'Laurent', 'non-Euclidean', 'Newtonian', 'Hermitian', 'Calabi']

connectors = ['for', 'of', 'with', 'on', 'and', 'under', 'in', 'from'] 

# = {'Properties', 'Characterization', 'Uniqueness'}

def sentence():
    s = (random.choice(adjectives) + ' ') + (random.random() > 0.6)*(random.choice(adjectives) + ' ') + (random.random() > 0.7)*(random.choice(adjectives) + ' ') + (random.random() > 0.8)*(random.choice(padjectives) + ' ') + (random.choice(nouns) + ' ')

    if random.random() > 0.7:
        s += (random.choice(connectors) + ' ' + sentence())

    return s

for i in range(10):
    print(sentence(), "\n")
