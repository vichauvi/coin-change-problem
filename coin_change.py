def make_change_rec (denom, target, memo = {}, solns = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        memo[0] = 0
        solns[0] = []
        return 0
    if target < 0:
        memo[target] = None
        solns[target] = None
        return None
    min_coins = np.inf
    min_soln = None
    for d in denom:
        if target - d >= 0:
            cur_min = make_change_rec(denom, target-d, memo, solns) + 1
            if cur_min <min:
                min_coins = cur_min
                min_soln = solns[target-d] + [d] 
    memo[target] = min_coins
    solns[target] = min_soln
    return min_coins