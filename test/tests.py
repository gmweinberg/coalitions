#!/usr/bin/env python
import sys
sys.path.append('../src')
from coalitions.util import *
from coalitions.coalition import *
from coalitions.typedcoalition import *

if __name__ == '__main__':
    # gloves game. Shapley and banzhaf values must be the same for Colition and TypedCoalition
    vals = {('L1', 'R'):1,('L2', 'R'):1}
    cgg =  CoalitionalGame(vals)
    print('coalitional gloves game shapeley', cgg.get_shapley_values())
    print('coalitional gloves game shapeley simulated ', cgg.simulate_shapley_values(10000))
    print('coalitional gloves games banzhaf', cgg.get_banzhaf_values())
    vals = {(('L', 1), ('R',1)):1}
    tgp = {'L':2, 'R':1}
    tgg = create_typed_game(player_types=tgp, coalition_values=vals)
    print('typed gloves game shapeley', tgg.get_shapley_values())
    print('typed gloves game shapeley simulated ', tgg.simulate_shapley_values(10000))
    print('typed gloves games banzhaf', tgg.get_banzhaf_values())

    # renormalized gloves game
    vals =  {('L1',): 3, ('L1', 'R'):6,('L2', 'R'):3}
    cggr =  CoalitionalGame(vals)
    cggn, _  = cggr.zero_normalize()
    print('gloves game zero nomalized', cggn.coalition_values)
    print('gloves equivalent?', cgg.is_equivalent(cggr))
    vals = {(('L', 1), ('R',1)):3, (('L', 1), ('R', 0)):1}
    tggr = create_typed_game(player_types=tgp, coalition_values=vals)
    print('typed gloves game renormalized valuaation', tggr.get_valuation())
    print('typed gloves equivalent?', tgg.is_equivalent(tggr))


