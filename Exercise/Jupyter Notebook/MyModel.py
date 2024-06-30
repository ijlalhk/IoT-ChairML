try:
    from time import ticks_us, ticks_diff
except ImportError:
    from time import time_ns

    def ticks_us(): return int(time_ns() * 1000)
    def ticks_diff(a, b): return a - b

class RandomForestClassifier:
    """
    # RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_name=RandomForestClassifier, class_weight={0: 0.875, 1: 0.9655172413793104, 2: 1.2173913043478262}, criterion=gini, estimator=DecisionTreeClassifier(), estimator_params=('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha', 'monotonic_cst'), max_depth=5, max_features=sqrt, max_leaf_nodes=None, max_samples=None, min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, monotonic_cst=None, n_estimators=10, n_jobs=None, num_outputs=3, oob_score=False, package_name=everywhereml.sklearn.ensemble, random_state=42, template_folder=everywhereml/sklearn/ensemble, verbose=0, warm_start=False)
    """

    def __init__(self):
        """
        Constructor
        """
        self.latency = 0
        self.predicted_value = -1

        self.votes = [0.00000000000, 0.00000000000, 0.00000000000]

    def predict(self, x):
        """
        Predict output from input vector
        """
        self.predicted_value = -1
        started_at = ticks_us()

        self.votes = [0.00000000000, 0.00000000000, 0.00000000000]

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
        
        idx, score = self.tree5(x)
        self.votes[idx] += score
        
        idx, score = self.tree6(x)
        self.votes[idx] += score
        
        idx, score = self.tree7(x)
        self.votes[idx] += score
        
        idx, score = self.tree8(x)
        self.votes[idx] += score
        
        idx, score = self.tree9(x)
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
        if x[1] < 2.531999945640564:
            if x[0] < 3049.5999755859375:
                return 2, 0.33048433048433046
            else:
                if x[1] < -5.443000078201294:
                    if x[1] < -5.858500003814697:
                        return 0, 0.24786324786324784
                    else:
                        return 2, 0.33048433048433046
                else:
                    return 0, 0.24786324786324784
        else:
            if x[1] < 2.8959999084472656:
                return 1, 0.42165242165242156
            else:
                return 1, 0.42165242165242156

    def tree1(self, x):
        """
        Random forest's tree #1
        """
        if x[0] < 3591.199951171875:
            if x[0] < 2251.199951171875:
                if x[0] < 2090.4000244140625:
                    if x[1] < -7.54449987411499:
                        return 2, 0.4245002515895888
                    else:
                        return 1, 0.2805605111080614
                else:
                    if x[1] < 2.45550000667572:
                        if x[0] < 2104.0:
                            return 2, 0.4245002515895888
                        else:
                            return 2, 0.4245002515895888
                    else:
                        return 1, 0.2805605111080614
            else:
                if x[1] < -0.01399993896484375:
                    return 2, 0.4245002515895888
                else:
                    return 1, 0.2805605111080614
        else:
            if x[0] < 5509.0:
                if x[1] < 2.6095000505447388:
                    return 0, 0.29493923730234967
                else:
                    return 1, 0.2805605111080614
            else:
                if x[0] < 5794.60009765625:
                    return 2, 0.4245002515895888
                else:
                    return 0, 0.29493923730234967

    def tree2(self, x):
        """
        Random forest's tree #2
        """
        if x[0] < 3591.199951171875:
            if x[1] < 0.0004999637603759766:
                return 2, 0.2511661970037095
            else:
                return 1, 0.3984015538679529
        else:
            if x[1] < 2.6985000371932983:
                if x[1] < -5.443000078201294:
                    if x[0] < 4634.10009765625:
                        return 0, 0.35043224912833737
                    else:
                        return 2, 0.2511661970037095
                else:
                    return 0, 0.35043224912833737
            else:
                return 1, 0.3984015538679529

    def tree3(self, x):
        """
        Random forest's tree #3
        """
        if x[0] < 3674.4000244140625:
            if x[0] < 2250.39990234375:
                if x[1] < -2.017500162124634:
                    return 2, 0.37305379037370306
                else:
                    return 1, 0.3072498724430631
            else:
                if x[1] < -2.400499939918518:
                    return 2, 0.37305379037370306
                else:
                    return 1, 0.3072498724430631
        else:
            if x[0] < 4679.35009765625:
                if x[0] < 4102.0999755859375:
                    return 0, 0.31969633718323354
                else:
                    if x[1] < -0.9615000486373901:
                        return 0, 0.31969633718323354
                    else:
                        return 1, 0.3072498724430631
            else:
                if x[1] < -5.443000078201294:
                    return 2, 0.37305379037370306
                else:
                    if x[0] < 5317.0:
                        if x[1] < 2.7265000343322754:
                            return 0, 0.31969633718323354
                        else:
                            return 1, 0.3072498724430631
                    else:
                        return 0, 0.31969633718323354

    def tree4(self, x):
        """
        Random forest's tree #4
        """
        if x[1] < 2.72599995136261:
            if x[1] < -5.443000078201294:
                if x[1] < -10.818000078201294:
                    return 2, 0.26339940394531436
                else:
                    if x[0] < 4634.10009765625:
                        return 0, 0.283977482378542
                    else:
                        return 2, 0.26339940394531436
            else:
                if x[1] < -1.6504999995231628:
                    if x[1] < -3.337999939918518:
                        return 0, 0.283977482378542
                    else:
                        return 2, 0.26339940394531436
                else:
                    return 0, 0.283977482378542
        else:
            if x[1] < 3.115000009536743:
                return 1, 0.4526231136761434
            else:
                return 1, 0.4526231136761434

    def tree5(self, x):
        """
        Random forest's tree #5
        """
        if x[1] < 2.531999945640564:
            if x[0] < 3181.85009765625:
                return 2, 0.32118809388962305
            else:
                if x[1] < -5.443000078201294:
                    return 2, 0.32118809388962305
                else:
                    return 0, 0.3777609967906361
        else:
            if x[1] < 2.9210000038146973:
                return 1, 0.3010509093197406
            else:
                return 1, 0.3010509093197406

    def tree6(self, x):
        """
        Random forest's tree #6
        """
        if x[0] < 3591.199951171875:
            if x[0] < 2250.39990234375:
                if x[0] < 2081.5999755859375:
                    if x[1] < -7.54449987411499:
                        return 2, 0.27962002632538807
                    else:
                        return 1, 0.35015937960892507
                else:
                    if x[0] < 2186.4000244140625:
                        if x[0] < 2166.4000244140625:
                            return 2, 0.27962002632538807
                        else:
                            return 2, 0.27962002632538807
                    else:
                        if x[0] < 2195.2000732421875:
                            return 1, 0.35015937960892507
                        else:
                            return 2, 0.27962002632538807
            else:
                if x[1] < -2.400499939918518:
                    return 2, 0.27962002632538807
                else:
                    return 1, 0.35015937960892507
        else:
            if x[1] < 2.7510000467300415:
                return 0, 0.3702205940656865
            else:
                return 1, 0.35015937960892507

    def tree7(self, x):
        """
        Random forest's tree #7
        """
        if x[0] < 3777.0:
            if x[1] < 0.0004999637603759766:
                return 2, 0.2790094153018434
            else:
                return 1, 0.3726877126354931
        else:
            if x[0] < 5229.0:
                return 0, 0.3483028720626631
            else:
                if x[1] < -5.394000053405762:
                    return 2, 0.2790094153018434
                else:
                    if x[1] < 2.7790000438690186:
                        return 0, 0.3483028720626631
                    else:
                        return 1, 0.3726877126354931

    def tree8(self, x):
        """
        Random forest's tree #8
        """
        if x[0] < 3674.4000244140625:
            if x[0] < 2138.4000244140625:
                if x[0] < 2081.5999755859375:
                    return 1, 0.2862565730109834
                else:
                    return 2, 0.3609322007529792
            else:
                if x[1] < 0.0004999637603759766:
                    return 2, 0.3609322007529792
                else:
                    return 1, 0.2862565730109834
        else:
            if x[0] < 5719.400146484375:
                if x[1] < -5.443000078201294:
                    if x[0] < 4634.10009765625:
                        return 0, 0.3528112262360371
                    else:
                        return 2, 0.3609322007529792
                else:
                    if x[1] < 1.2700000405311584:
                        return 0, 0.3528112262360371
                    else:
                        return 1, 0.2862565730109834
            else:
                return 0, 0.3528112262360371

    def tree9(self, x):
        """
        Random forest's tree #9
        """
        if x[1] < -5.443000078201294:
            return 2, 0.35862239535027524
        else:
            if x[0] < 4679.35009765625:
                if x[1] < 2.55649995803833:
                    return 0, 0.2886910282569715
                else:
                    return 1, 0.3526865763927533
            else:
                return 0, 0.2886910282569715