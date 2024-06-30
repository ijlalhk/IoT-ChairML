try:
    from time import ticks_us, ticks_diff
except ImportError:
    from time import time_ns

    def ticks_us(): return int(time_ns() * 1000)
    def ticks_diff(a, b): return a - b

class RandomForestClassifier:
    """
    # RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_name=RandomForestClassifier, class_weight=None, criterion=gini, estimator=DecisionTreeClassifier(), estimator_params=('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha', 'monotonic_cst'), max_depth=4, max_features=sqrt, max_leaf_nodes=None, max_samples=None, min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, monotonic_cst=None, n_estimators=5, n_jobs=None, num_outputs=4, oob_score=False, package_name=everywhereml.sklearn.ensemble, random_state=42, template_folder=everywhereml/sklearn/ensemble, verbose=0, warm_start=False)
    """

    def __init__(self):
        """
        Constructor
        """
        self.latency = 0
        self.predicted_value = -1

        self.votes = [0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000]

    def predict(self, x):
        """
        Predict output from input vector
        """
        self.predicted_value = -1
        started_at = ticks_us()

        self.votes = [0.00000000000, 0.00000000000, 0.00000000000, 0.00000000000]

        idx, score = self.tree0(x)
        self.votes[idx] += score
        
        idx, score = self.tree1(x)
        self.votes[idx] += score
        
        idx, score = self.tree2(x)
        self.votes[idx] += score
        
        idx, score = self.tree3(x)
        self.votes[idx] += score
        
        idx, score = self.tree4(x)
        self.votes[idx] += score

        # get argmax of votes
        max_vote = max(self.votes)
        self.predicted_value = next(i for i, v in enumerate(self.votes) if v == max_vote)

        self.latency = ticks_diff(ticks_us(), started_at)
        return self.predicted_value

    def latencyInMicros(self):
        """
        Get latency in micros
        """
        return self.latency

    def latencyInMillis(self):
        """
        Get latency in millis
        """
        return self.latency // 1000

    def tree0(self, x):
        """
        Random forest's tree #0
        """
        if x[1] < 4.620000004768372:
            if x[0] < 3296.0:
                if x[1] < -24.55500030517578:
                    if x[1] < -24.75:
                        return 2, 0.25
                    else:
                        return 3, 0.3
                else:
                    if x[1] < -18.0600004196167:
                        return 2, 0.25
                    else:
                        return 2, 0.25
            else:
                if x[0] < 5489.0:
                    if x[0] < 4761.0:
                        return 1, 0.18571428571428572
                    else:
                        return 1, 0.18571428571428572
                else:
                    if x[1] < -4.2200000286102295:
                        return 0, 0.2642857142857143
                    else:
                        return 0, 0.2642857142857143
        else:
            if x[1] < 7.710000038146973:
                if x[0] < 2072.0:
                    return 0, 0.2642857142857143
                else:
                    return 3, 0.3
            else:
                if x[0] < 3032.0:
                    return 3, 0.3
                else:
                    if x[1] < 11.414999961853027:
                        return 0, 0.2642857142857143
                    else:
                        return 1, 0.18571428571428572

    def tree1(self, x):
        """
        Random forest's tree #1
        """
        if x[0] < 3240.0:
            if x[0] < 2744.0:
                if x[0] < 2336.0:
                    if x[0] < 2200.0:
                        return 2, 0.21428571428571427
                    else:
                        return 2, 0.21428571428571427
                else:
                    if x[1] < -6.429999828338623:
                        return 2, 0.21428571428571427
                    else:
                        return 3, 0.24285714285714285
            else:
                return 2, 0.21428571428571427
        else:
            if x[1] < -4.134999990463257:
                if x[0] < 5537.0:
                    return 1, 0.2571428571428571
                else:
                    return 0, 0.2857142857142857
            else:
                if x[1] < 11.414999961853027:
                    return 0, 0.2857142857142857
                else:
                    return 1, 0.2571428571428571

    def tree2(self, x):
        """
        Random forest's tree #2
        """
        if x[0] < 3152.0:
            if x[1] < 1.8849999904632568:
                if x[1] < -18.0600004196167:
                    if x[1] < -24.55500030517578:
                        return 3, 0.2714285714285714
                    else:
                        return 2, 0.2357142857142857
                else:
                    if x[0] < 1856.0:
                        return 3, 0.2714285714285714
                    else:
                        return 2, 0.2357142857142857
            else:
                if x[1] < 7.759999990463257:
                    if x[0] < 2072.0:
                        return 0, 0.34285714285714286
                    else:
                        return 3, 0.2714285714285714
                else:
                    if x[0] < 2624.0:
                        return 3, 0.2714285714285714
                    else:
                        return 1, 0.15
        else:
            if x[0] < 4801.0:
                if x[0] < 3896.0:
                    if x[1] < 2.309999942779541:
                        return 1, 0.15
                    else:
                        return 0, 0.34285714285714286
                else:
                    if x[1] < -2.415000017732382:
                        return 1, 0.15
                    else:
                        return 0, 0.34285714285714286
            else:
                if x[1] < -4.090000033378601:
                    if x[1] < -5.070000171661377:
                        return 0, 0.34285714285714286
                    else:
                        return 1, 0.15
                else:
                    return 0, 0.34285714285714286

    def tree3(self, x):
        """
        Random forest's tree #3
        """
        if x[0] < 3096.0:
            if x[0] < 1880.0:
                return 3, 0.2857142857142857
            else:
                if x[1] < 1.8849999904632568:
                    if x[1] < -24.55500030517578:
                        return 3, 0.2857142857142857
                    else:
                        return 2, 0.2642857142857143
                else:
                    if x[0] < 2072.0:
                        return 3, 0.2857142857142857
                    else:
                        return 3, 0.2857142857142857
        else:
            if x[0] < 5537.0:
                if x[1] < -3.350000023841858:
                    if x[1] < -5.81000018119812:
                        return 1, 0.22857142857142856
                    else:
                        return 1, 0.22857142857142856
                else:
                    if x[0] < 4785.0:
                        return 1, 0.22857142857142856
                    else:
                        return 0, 0.22142857142857142
            else:
                return 0, 0.22142857142857142

    def tree4(self, x):
        """
        Random forest's tree #4
        """
        if x[1] < 7.710000038146973:
            if x[1] < -1.5850000381469727:
                if x[1] < -6.194999933242798:
                    if x[0] < 3776.5:
                        return 2, 0.2357142857142857
                    else:
                        return 0, 0.2571428571428571
                else:
                    if x[1] < -4.004999995231628:
                        return 1, 0.21428571428571427
                    else:
                        return 2, 0.2357142857142857
            else:
                if x[1] < 1.7450000047683716:
                    return 0, 0.2571428571428571
                else:
                    if x[1] < 2.060000002384186:
                        return 2, 0.2357142857142857
                    else:
                        return 0, 0.2571428571428571
        else:
            if x[0] < 2976.0:
                return 3, 0.29285714285714287
            else:
                return 1, 0.21428571428571427