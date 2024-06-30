try:
    from time import ticks_us, ticks_diff
except ImportError:
    from time import time_ns

    def ticks_us(): return int(time_ns() * 1000)
    def ticks_diff(a, b): return a - b

class RandomForestClassifier:
    """
    # RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_name=RandomForestClassifier, class_weight={0: 1.05, 1: 1.0, 2: 1.0, 3: 0.9545454545454546}, criterion=gini, estimator=DecisionTreeClassifier(), estimator_params=('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha', 'monotonic_cst'), max_depth=5, max_features=sqrt, max_leaf_nodes=None, max_samples=None, min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, monotonic_cst=None, n_estimators=10, n_jobs=None, num_outputs=4, oob_score=False, package_name=everywhereml.sklearn.ensemble, random_state=42, template_folder=everywhereml/sklearn/ensemble, verbose=0, warm_start=False)
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
        if x[1] < 2.573499917984009:
            return 0, 0.1259541984732825
        else:
            if x[0] < 2554.4000244140625:
                if x[1] < 17.814000129699707:
                    if x[1] < 10.732500076293945:
                        if x[1] < 7.736500024795532:
                            return 3, 0.28625954198473297
                        else:
                            return 3, 0.28625954198473297
                    else:
                        if x[0] < 2243.199951171875:
                            return 2, 0.2639040348964014
                        else:
                            return 3, 0.28625954198473297
                else:
                    return 2, 0.2639040348964014
            else:
                if x[0] < 5509.0:
                    if x[1] < 4.0375001430511475:
                        if x[1] < 3.168000102043152:
                            return 1, 0.3238822246455835
                        else:
                            return 0, 0.1259541984732825
                    else:
                        return 1, 0.3238822246455835
                else:
                    return 0, 0.1259541984732825

    def tree1(self, x):
        """
        Random forest's tree #1
        """
        if x[0] < 2690.4000244140625:
            if x[0] < 2251.199951171875:
                if x[0] < 2169.5999755859375:
                    if x[0] < 2138.4000244140625:
                        if x[1] < 13.986999988555908:
                            return 3, 0.23864927755830956
                        else:
                            return 2, 0.30954055955408855
                    else:
                        if x[1] < 18.244500160217285:
                            return 3, 0.23864927755830956
                        else:
                            return 2, 0.30954055955408855
                else:
                    if x[0] < 2216.7999267578125:
                        return 2, 0.30954055955408855
                    else:
                        if x[1] < 14.976000308990479:
                            return 3, 0.23864927755830956
                        else:
                            return 2, 0.30954055955408855
            else:
                if x[0] < 2468.0:
                    return 3, 0.23864927755830956
                else:
                    return 2, 0.30954055955408855
        else:
            if x[1] < 4.0375001430511475:
                if x[0] < 4469.4998779296875:
                    return 1, 0.21429731046052286
                else:
                    return 0, 0.23751285242707953
            else:
                if x[0] < 5509.0:
                    return 1, 0.21429731046052286
                else:
                    return 0, 0.23751285242707953

    def tree2(self, x):
        """
        Random forest's tree #2
        """
        if x[0] < 2679.199951171875:
            if x[1] < 10.91100025177002:
                return 3, 0.3430064790112703
            else:
                if x[1] < 17.814000129699707:
                    if x[1] < 17.291500091552734:
                        if x[0] < 2240.7999267578125:
                            return 2, 0.16769205640550988
                        else:
                            return 3, 0.3430064790112703
                    else:
                        return 3, 0.3430064790112703
                else:
                    if x[1] < 20.18899917602539:
                        if x[0] < 2266.4000244140625:
                            return 2, 0.16769205640550988
                        else:
                            return 3, 0.3430064790112703
                    else:
                        return 2, 0.16769205640550988
        else:
            if x[0] < 4990.550048828125:
                if x[0] < 4834.550048828125:
                    return 1, 0.2754940926661948
                else:
                    if x[0] < 4906.550048828125:
                        return 0, 0.21380737191702512
                    else:
                        return 1, 0.2754940926661948
            else:
                if x[1] < 4.427000045776367:
                    return 0, 0.21380737191702512
                else:
                    if x[1] < 5.25:
                        return 1, 0.2754940926661948
                    else:
                        return 0, 0.21380737191702512

    def tree3(self, x):
        """
        Random forest's tree #3
        """
        if x[0] < 2690.4000244140625:
            if x[0] < 2250.39990234375:
                if x[1] < 10.91100025177002:
                    return 3, 0.19220415634758273
                else:
                    if x[1] < 17.291500091552734:
                        return 2, 0.2724238182405514
                    else:
                        if x[0] < 2147.199951171875:
                            return 2, 0.2724238182405514
                        else:
                            return 2, 0.2724238182405514
            else:
                if x[0] < 2485.5999755859375:
                    return 3, 0.19220415634758273
                else:
                    return 2, 0.2724238182405514
        else:
            if x[1] < 2.7925000190734863:
                if x[1] < 1.9355000257492065:
                    return 0, 0.298481748680952
                else:
                    if x[0] < 4489.4500732421875:
                        return 1, 0.23689027673091423
                    else:
                        return 0, 0.298481748680952
            else:
                if x[1] < 5.858500003814697:
                    if x[1] < 5.443000078201294:
                        if x[0] < 5208.199951171875:
                            return 1, 0.23689027673091423
                        else:
                            return 1, 0.23689027673091423
                    else:
                        return 0, 0.298481748680952
                else:
                    return 1, 0.23689027673091423

    def tree4(self, x):
        """
        Random forest's tree #4
        """
        if x[1] < 7.59850001335144:
            if x[1] < 4.427000045776367:
                if x[1] < 2.531499981880188:
                    if x[0] < 4469.4998779296875:
                        return 1, 0.2998255560401222
                    else:
                        return 0, 0.17629742695159184
                else:
                    if x[1] < 3.9549999237060547:
                        if x[1] < 3.565500020980835:
                            return 3, 0.33198866114260805
                        else:
                            return 3, 0.33198866114260805
                    else:
                        return 0, 0.17629742695159184
            else:
                if x[1] < 5.443000078201294:
                    return 1, 0.2998255560401222
                else:
                    if x[0] < 4634.10009765625:
                        return 1, 0.2998255560401222
                    else:
                        return 0, 0.17629742695159184
        else:
            if x[1] < 16.291500091552734:
                if x[0] < 2873.5999755859375:
                    if x[0] < 2200.800048828125:
                        if x[0] < 2161.5999755859375:
                            return 3, 0.33198866114260805
                        else:
                            return 2, 0.1918883558656782
                    else:
                        return 3, 0.33198866114260805
                else:
                    return 1, 0.2998255560401222
            else:
                if x[1] < 29.163500785827637:
                    if x[0] < 2269.5999755859375:
                        if x[1] < 18.04300022125244:
                            return 2, 0.1918883558656782
                        else:
                            return 2, 0.1918883558656782
                    else:
                        if x[1] < 21.790499687194824:
                            return 3, 0.33198866114260805
                        else:
                            return 2, 0.1918883558656782
                else:
                    return 1, 0.2998255560401222

    def tree5(self, x):
        """
        Random forest's tree #5
        """
        if x[1] < 2.572999954223633:
            if x[0] < 4548.75:
                return 1, 0.2375296912114015
            else:
                return 0, 0.29928741092636596
        else:
            if x[1] < 11.503499984741211:
                if x[1] < 7.653500080108643:
                    if x[1] < 2.9210000038146973:
                        return 3, 0.2494061757719716
                    else:
                        if x[1] < 5.364000082015991:
                            return 1, 0.2375296912114015
                        else:
                            return 2, 0.21377672209026136
                else:
                    return 3, 0.2494061757719716
            else:
                if x[0] < 2504.800048828125:
                    if x[0] < 2244.0:
                        return 2, 0.21377672209026136
                    else:
                        if x[0] < 2247.199951171875:
                            return 2, 0.21377672209026136
                        else:
                            return 2, 0.21377672209026136
                else:
                    return 1, 0.2375296912114015

    def tree6(self, x):
        """
        Random forest's tree #6
        """
        if x[0] < 2690.4000244140625:
            if x[0] < 2250.39990234375:
                if x[0] < 2166.4000244140625:
                    if x[1] < 17.814000129699707:
                        if x[0] < 2138.4000244140625:
                            return 3, 0.24970273483947691
                        else:
                            return 3, 0.24970273483947691
                    else:
                        return 2, 0.21403091557669449
                else:
                    if x[0] < 2186.4000244140625:
                        return 2, 0.21403091557669449
                    else:
                        if x[0] < 2195.2000732421875:
                            return 3, 0.24970273483947691
                        else:
                            return 2, 0.21403091557669449
            else:
                if x[1] < 7.488999843597412:
                    return 3, 0.24970273483947691
                else:
                    if x[1] < 7.679999828338623:
                        return 2, 0.21403091557669449
                    else:
                        return 3, 0.24970273483947691
        else:
            if x[1] < 4.0375001430511475:
                if x[1] < 1.4739999771118164:
                    return 0, 0.27467300832342467
                else:
                    if x[0] < 4940.949951171875:
                        return 1, 0.2615933412604044
                    else:
                        return 0, 0.27467300832342467
            else:
                return 1, 0.2615933412604044

    def tree7(self, x):
        """
        Random forest's tree #7
        """
        if x[0] < 2690.4000244140625:
            if x[1] < 11.372000217437744:
                if x[0] < 2485.5999755859375:
                    if x[1] < 6.447999954223633:
                        if x[1] < 4.677999973297119:
                            return 3, 0.2843832945127567
                        else:
                            return 2, 0.2025892421862305
                    else:
                        return 3, 0.2843832945127567
                else:
                    return 2, 0.2025892421862305
            else:
                if x[0] < 2169.5999755859375:
                    if x[0] < 2131.199951171875:
                        return 2, 0.2025892421862305
                    else:
                        return 3, 0.2843832945127567
                else:
                    if x[1] < 16.034500122070312:
                        if x[0] < 2225.60009765625:
                            return 2, 0.2025892421862305
                        else:
                            return 3, 0.2843832945127567
                    else:
                        return 2, 0.2025892421862305
        else:
            if x[0] < 5477.0:
                if x[1] < 4.0375001430511475:
                    if x[0] < 4405.4500732421875:
                        return 1, 0.2502572991712259
                    else:
                        return 0, 0.26277016412978726
                else:
                    return 1, 0.2502572991712259
            else:
                return 0, 0.26277016412978726

    def tree8(self, x):
        """
        Random forest's tree #8
        """
        if x[0] < 2812.7999267578125:
            if x[0] < 2138.4000244140625:
                if x[0] < 2081.5999755859375:
                    return 3, 0.26088365561196936
                else:
                    return 2, 0.2495408879766663
            else:
                if x[1] < 10.91100025177002:
                    if x[0] < 2468.0:
                        return 3, 0.26088365561196936
                    else:
                        return 2, 0.2495408879766663
                else:
                    if x[1] < 13.068000316619873:
                        return 2, 0.2495408879766663
                    else:
                        if x[0] < 2269.5999755859375:
                            return 2, 0.2495408879766663
                        else:
                            return 3, 0.26088365561196936
        else:
            if x[1] < 4.427000045776367:
                if x[1] < 2.7925000190734863:
                    return 0, 0.2994490655719996
                else:
                    if x[0] < 5041.75:
                        return 1, 0.1901263908393648
                    else:
                        return 0, 0.2994490655719996
            else:
                if x[1] < 5.443000078201294:
                    return 1, 0.1901263908393648
                else:
                    if x[1] < 5.858500003814697:
                        return 0, 0.2994490655719996
                    else:
                        return 1, 0.1901263908393648

    def tree9(self, x):
        """
        Random forest's tree #9
        """
        if x[1] < 2.7674999237060547:
            if x[0] < 4405.4500732421875:
                return 1, 0.16702819956616058
            else:
                return 0, 0.25054229934924094
        else:
            if x[1] < 11.372000217437744:
                if x[1] < 6.5269999504089355:
                    if x[1] < 5.443000078201294:
                        if x[0] < 3502.050048828125:
                            return 3, 0.29609544468546656
                        else:
                            return 1, 0.16702819956616058
                    else:
                        return 0, 0.25054229934924094
                else:
                    if x[0] < 2453.5999755859375:
                        if x[1] < 7.653500080108643:
                            return 2, 0.28633405639913245
                        else:
                            return 3, 0.29609544468546656
                    else:
                        if x[1] < 8.04200005531311:
                            return 2, 0.28633405639913245
                        else:
                            return 1, 0.16702819956616058
            else:
                if x[0] < 2269.5999755859375:
                    if x[0] < 2147.199951171875:
                        return 2, 0.28633405639913245
                    else:
                        if x[1] < 17.291500091552734:
                            return 2, 0.28633405639913245
                        else:
                            return 2, 0.28633405639913245
                else:
                    if x[1] < 22.477999687194824:
                        if x[0] < 2797.6500244140625:
                            return 3, 0.29609544468546656
                        else:
                            return 1, 0.16702819956616058
                    else:
                        return 2, 0.28633405639913245