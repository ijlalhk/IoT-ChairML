try:
    from time import ticks_us, ticks_diff
except ImportError:
    from time import time_ns

    def ticks_us(): return int(time_ns() * 1000)
    def ticks_diff(a, b): return a - b

class RandomForestClassifier:
    """
    # RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_name=RandomForestClassifier, class_weight=None, criterion=gini, estimator=DecisionTreeClassifier(), estimator_params=('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha', 'monotonic_cst'), max_depth=5, max_features=sqrt, max_leaf_nodes=20, max_samples=None, min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, monotonic_cst=None, n_estimators=10, n_jobs=None, num_outputs=3, oob_score=False, package_name=everywhereml.sklearn.ensemble, random_state=None, template_folder=everywhereml/sklearn/ensemble, verbose=0, warm_start=False)
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
        if x[1] < 0.029000000562518835:
            if x[4] < -0.03800000064074993:
                return 2, 0.31100478468899523
            else:
                if x[5] < 0.004500000039115548:
                    if x[2] < -0.0025000000605359674:
                        if x[4] < 0.1730000004172325:
                            return 1, 0.3014354066985646
                        else:
                            return 2, 0.31100478468899523
                    else:
                        if x[1] < 0.0035000001080334187:
                            return 0, 0.3875598086124402
                        else:
                            return 1, 0.3014354066985646
                else:
                    if x[4] < 0.07450000382959843:
                        if x[5] < 0.02449999935925007:
                            return 1, 0.3014354066985646
                        else:
                            return 0, 0.3875598086124402
                    else:
                        return 2, 0.31100478468899523
        else:
            return 2, 0.31100478468899523

    def tree1(self, x):
        """
        Random forest's tree #1
        """
        if x[2] < -0.02000000048428774:
            return 2, 0.31100478468899523
        else:
            if x[2] < 0.030499999411404133:
                if x[3] < 0.004500000039115548:
                    if x[1] < 0.0035000001080334187:
                        if x[4] < -0.005499999970197678:
                            return 1, 0.3253588516746411
                        else:
                            return 0, 0.36363636363636365
                    else:
                        if x[4] < 0.005000000121071935:
                            return 1, 0.3253588516746411
                        else:
                            return 1, 0.3253588516746411
                else:
                    if x[4] < 0.14049999322742224:
                        if x[5] < 0.004500000039115548:
                            return 1, 0.3253588516746411
                        else:
                            return 1, 0.3253588516746411
                    else:
                        return 2, 0.31100478468899523
            else:
                return 2, 0.31100478468899523

    def tree2(self, x):
        """
        Random forest's tree #2
        """
        if x[3] < -0.019500000402331352:
            return 2, 0.35406698564593303
        else:
            if x[3] < 0.011500000022351742:
                if x[0] < -0.001500000071246177:
                    if x[4] < -0.0020000000367872417:
                        return 1, 0.36363636363636365
                    else:
                        if x[5] < 0.006000000052154064:
                            return 1, 0.36363636363636365
                        else:
                            return 0, 0.2822966507177033
                else:
                    if x[4] < 0.004500000039115548:
                        if x[3] < 0.003999999957159162:
                            return 0, 0.2822966507177033
                        else:
                            return 1, 0.36363636363636365
                    else:
                        if x[4] < 0.005499999970197678:
                            return 1, 0.36363636363636365
                        else:
                            return 1, 0.36363636363636365
            else:
                return 2, 0.35406698564593303

    def tree3(self, x):
        """
        Random forest's tree #3
        """
        if x[2] < -0.020500000566244125:
            return 2, 0.32057416267942584
        else:
            if x[2] < 0.01699999999254942:
                if x[4] < 0.005499999970197678:
                    if x[2] < 0.001500000071246177:
                        if x[2] < -0.0025000000605359674:
                            return 1, 0.3397129186602871
                        else:
                            return 0, 0.3397129186602871
                    else:
                        if x[3] < -0.004000000073574483:
                            return 1, 0.3397129186602871
                        else:
                            return 1, 0.3397129186602871
                else:
                    if x[5] < -0.11049999669194221:
                        return 2, 0.32057416267942584
                    else:
                        if x[5] < -0.0020000000367872417:
                            return 1, 0.3397129186602871
                        else:
                            return 1, 0.3397129186602871
            else:
                if x[0] < 0.4594999924302101:
                    if x[1] < 0.014000000897794962:
                        if x[2] < 0.030499999411404133:
                            return 0, 0.3397129186602871
                        else:
                            return 2, 0.32057416267942584
                    else:
                        return 2, 0.32057416267942584
                else:
                    return 0, 0.3397129186602871

    def tree4(self, x):
        """
        Random forest's tree #4
        """
        if x[3] < -0.024999999441206455:
            return 2, 0.291866028708134
        else:
            if x[1] < 0.07550000352784991:
                if x[0] < -0.0025000000605359674:
                    if x[4] < 0.0005000000237487257:
                        return 1, 0.36363636363636365
                    else:
                        if x[5] < -0.004000000131782144:
                            return 1, 0.36363636363636365
                        else:
                            return 1, 0.36363636363636365
                else:
                    if x[4] < 0.004500000039115548:
                        if x[5] < 0.004500000039115548:
                            return 0, 0.3444976076555024
                        else:
                            return 1, 0.36363636363636365
                    else:
                        return 1, 0.36363636363636365
            else:
                return 2, 0.291866028708134

    def tree5(self, x):
        """
        Random forest's tree #5
        """
        if x[3] < -0.019500000402331352:
            return 2, 0.35406698564593303
        else:
            if x[1] < 0.07550000352784991:
                if x[1] < -0.029000000562518835:
                    return 2, 0.35406698564593303
                else:
                    if x[1] < 0.0025000000605359674:
                        if x[5] < -0.0035000001080334187:
                            return 1, 0.3827751196172249
                        else:
                            return 0, 0.2631578947368421
                    else:
                        if x[4] < 0.006500000134110451:
                            return 1, 0.3827751196172249
                        else:
                            return 1, 0.3827751196172249
            else:
                return 2, 0.35406698564593303

    def tree6(self, x):
        """
        Random forest's tree #6
        """
        if x[1] < 0.02800000086426735:
            if x[5] < 0.03349999990314245:
                if x[0] < -0.038999998942017555:
                    return 2, 0.37320574162679426
                else:
                    if x[4] < 0.004500000039115548:
                        if x[5] < -0.007500000298023224:
                            return 1, 0.3492822966507177
                        else:
                            return 0, 0.27751196172248804
                    else:
                        if x[4] < 0.006500000134110451:
                            return 1, 0.3492822966507177
                        else:
                            return 1, 0.3492822966507177
            else:
                return 2, 0.37320574162679426
        else:
            return 2, 0.37320574162679426

    def tree7(self, x):
        """
        Random forest's tree #7
        """
        if x[1] < 0.07550000352784991:
            if x[1] < -0.040499999653548:
                return 2, 0.31100478468899523
            else:
                if x[5] < -0.0025000000605359674:
                    if x[3] < -0.0005000000237487257:
                        return 1, 0.3923444976076555
                    else:
                        if x[0] < 0.0005000000237487257:
                            return 0, 0.2966507177033493
                        else:
                            return 1, 0.3923444976076555
                else:
                    if x[2] < 0.0005000000237487257:
                        if x[1] < -0.0025000000605359674:
                            return 1, 0.3923444976076555
                        else:
                            return 0, 0.2966507177033493
                    else:
                        if x[4] < -0.004500000039115548:
                            return 1, 0.3923444976076555
                        else:
                            return 1, 0.3923444976076555
        else:
            return 2, 0.31100478468899523

    def tree8(self, x):
        """
        Random forest's tree #8
        """
        if x[1] < 0.029000000562518835:
            if x[1] < -0.03299999935552478:
                return 2, 0.36363636363636365
            else:
                if x[0] < 0.0025000000605359674:
                    if x[1] < -0.0025000000605359674:
                        if x[5] < 0.019499999471008778:
                            return 1, 0.291866028708134
                        else:
                            return 0, 0.3444976076555024
                    else:
                        if x[5] < 0.004500000039115548:
                            return 0, 0.3444976076555024
                        else:
                            return 1, 0.291866028708134
                else:
                    if x[1] < -0.0005000000237487257:
                        if x[5] < 0.003499999991618097:
                            return 0, 0.3444976076555024
                        else:
                            return 1, 0.291866028708134
                    else:
                        if x[5] < -0.0025000000605359674:
                            return 0, 0.3444976076555024
                        else:
                            return 1, 0.291866028708134
        else:
            return 2, 0.36363636363636365

    def tree9(self, x):
        """
        Random forest's tree #9
        """
        if x[0] < -0.010499999858438969:
            return 2, 0.3157894736842105
        else:
            if x[0] < 0.012000000104308128:
                if x[4] < 0.006500000134110451:
                    if x[3] < -0.0025000000605359674:
                        if x[5] < -0.0020000000367872417:
                            return 1, 0.3397129186602871
                        else:
                            return 1, 0.3397129186602871
                    else:
                        if x[5] < 0.004500000039115548:
                            return 0, 0.3444976076555024
                        else:
                            return 1, 0.3397129186602871
                else:
                    if x[1] < 0.3819999936968088:
                        return 1, 0.3397129186602871
                    else:
                        return 2, 0.3157894736842105
            else:
                if x[0] < 0.5419999957084656:
                    return 2, 0.3157894736842105
                else:
                    return 0, 0.3444976076555024