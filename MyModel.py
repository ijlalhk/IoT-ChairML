try:
    from time import ticks_us, ticks_diff
except ImportError:
    from time import time_ns

    def ticks_us(): return int(time_ns() * 1000)
    def ticks_diff(a, b): return a - b

class RandomForestClassifier:
    """
    # RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_name=RandomForestClassifier, class_weight={0: 1.0360696517412935, 1: 1.0734536082474226, 2: 0.9776995305164319, 3: 0.9255555555555556}, criterion=gini, estimator=DecisionTreeClassifier(), estimator_params=('criterion', 'max_depth', 'min_samples_split', 'min_samples_leaf', 'min_weight_fraction_leaf', 'max_features', 'max_leaf_nodes', 'min_impurity_decrease', 'random_state', 'ccp_alpha', 'monotonic_cst'), max_depth=5, max_features=sqrt, max_leaf_nodes=None, max_samples=None, min_impurity_decrease=0.0, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, monotonic_cst=None, n_estimators=10, n_jobs=None, num_outputs=4, oob_score=False, package_name=everywhereml.sklearn.ensemble, random_state=42, template_folder=everywhereml/sklearn/ensemble, verbose=0, warm_start=False)
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
        if x[1] < 16.85949993133545:
            if x[0] < 2701.5999755859375:
                return 2, 0.2180678710684776
            else:
                if x[0] < 5573.0:
                    if x[1] < 0.43749999068677425:
                        return 1, 0.2767547432541003
                    else:
                        if x[1] < 8.255500316619873:
                            return 0, 0.24102606773368795
                        else:
                            return 1, 0.2767547432541003
                else:
                    return 0, 0.24102606773368795
        else:
            if x[4] < 12.624999642372131:
                if x[2] < 8.404000282287598:
                    if x[0] < 2509.5999755859375:
                        return 3, 0.26415131794373803
                    else:
                        if x[0] < 2912.0:
                            return 1, 0.2767547432541003
                        else:
                            return 1, 0.2767547432541003
                else:
                    if x[0] < 2025.6000366210938:
                        return 3, 0.26415131794373803
                    else:
                        return 3, 0.26415131794373803
            else:
                if x[4] < 22.684499740600586:
                    return 1, 0.2767547432541003
                else:
                    return 1, 0.2767547432541003

    def tree1(self, x):
        """
        Random forest's tree #1
        """
        if x[2] < 9.302000045776367:
            if x[2] < 4.134500026702881:
                if x[0] < 4030.0999755859375:
                    return 3, 0.2453496280732461
                else:
                    if x[0] < 5865.0:
                        return 0, 0.23984844103196043
                    else:
                        return 0, 0.23984844103196043
            else:
                if x[0] < 5569.800048828125:
                    if x[0] < 2492.7999267578125:
                        if x[0] < 2224.7999267578125:
                            return 2, 0.25213579457530305
                        else:
                            return 3, 0.2453496280732461
                    else:
                        if x[1] < 0.2794999983161688:
                            return 1, 0.26266613631949426
                        else:
                            return 1, 0.26266613631949426
                else:
                    return 0, 0.23984844103196043
        else:
            if x[5] < 1.6455000042915344:
                if x[4] < 1.0374999642372131:
                    if x[2] < 19.57200050354004:
                        if x[2] < 15.313999652862549:
                            return 2, 0.25213579457530305
                        else:
                            return 3, 0.2453496280732461
                    else:
                        if x[5] < -1.7695000767707825:
                            return 3, 0.2453496280732461
                        else:
                            return 2, 0.25213579457530305
                else:
                    if x[1] < 11.276000022888184:
                        if x[3] < -8.000000476837158:
                            return 2, 0.25213579457530305
                        else:
                            return 3, 0.2453496280732461
                    else:
                        return 3, 0.2453496280732461
            else:
                if x[0] < 2100.0:
                    return 2, 0.25213579457530305
                else:
                    return 3, 0.2453496280732461

    def tree2(self, x):
        """
        Random forest's tree #2
        """
        if x[4] < -1.4164999723434448:
            if x[4] < -2.4984999895095825:
                if x[3] < 15.200000047683716:
                    if x[2] < 11.129500150680542:
                        return 1, 0.25768183229147024
                    else:
                        if x[1] < 23.58300018310547:
                            return 3, 0.23884242721949395
                        else:
                            return 3, 0.23884242721949395
                else:
                    return 3, 0.23884242721949395
            else:
                if x[0] < 2528.800048828125:
                    if x[4] < -1.9319999814033508:
                        return 3, 0.23884242721949395
                    else:
                        return 2, 0.2734209902168781
                else:
                    return 1, 0.25768183229147024
        else:
            if x[0] < 2659.199951171875:
                if x[2] < 19.691499710083008:
                    if x[1] < 13.133500337600708:
                        return 2, 0.2734209902168781
                    else:
                        return 3, 0.23884242721949395
                else:
                    if x[5] < 0.29600000381469727:
                        if x[2] < 24.201499938964844:
                            return 2, 0.2734209902168781
                        else:
                            return 2, 0.2734209902168781
                    else:
                        if x[1] < 11.189499855041504:
                            return 2, 0.2734209902168781
                        else:
                            return 3, 0.23884242721949395
            else:
                if x[1] < 0.43749999068677425:
                    return 1, 0.25768183229147024
                else:
                    if x[2] < 4.299000024795532:
                        return 0, 0.23005475027216105
                    else:
                        if x[3] < -281.6500015258789:
                            return 2, 0.2734209902168781
                        else:
                            return 0, 0.23005475027216105

    def tree3(self, x):
        """
        Random forest's tree #3
        """
        if x[2] < 8.270999908447266:
            if x[0] < 5515.35009765625:
                if x[4] < -0.009499999694527084:
                    if x[0] < 4463.300048828125:
                        if x[2] < 7.163500070571899:
                            return 1, 0.25655279841702094
                        else:
                            return 2, 0.22544833641062523
                    else:
                        if x[5] < 0.1665000021457672:
                            return 0, 0.25010674820553813
                        else:
                            return 1, 0.25655279841702094
                else:
                    if x[4] < 0.007499999832365489:
                        if x[3] < -290.5:
                            return 2, 0.22544833641062523
                        else:
                            return 1, 0.25655279841702094
                    else:
                        if x[1] < 8.723999977111816:
                            return 0, 0.25010674820553813
                        else:
                            return 1, 0.25655279841702094
            else:
                if x[1] < 2.126499881967902:
                    return 1, 0.25655279841702094
                else:
                    if x[3] < -420.8999938964844:
                        return 1, 0.25655279841702094
                    else:
                        return 0, 0.25010674820553813
        else:
            if x[2] < 19.577000617980957:
                if x[2] < 15.295000076293945:
                    if x[1] < 16.236499786376953:
                        if x[0] < 3995.699951171875:
                            return 2, 0.22544833641062523
                        else:
                            return 0, 0.25010674820553813
                    else:
                        return 3, 0.2678921169668206
                else:
                    if x[1] < 11.239499568939209:
                        return 2, 0.22544833641062523
                    else:
                        return 3, 0.2678921169668206
            else:
                if x[4] < -2.109000027179718:
                    return 3, 0.2678921169668206
                else:
                    if x[0] < 2244.0:
                        if x[2] < 23.812999725341797:
                            return 2, 0.22544833641062523
                        else:
                            return 2, 0.22544833641062523
                    else:
                        return 2, 0.22544833641062523

    def tree4(self, x):
        """
        Random forest's tree #4
        """
        if x[0] < 2665.5999755859375:
            if x[2] < 19.371000289916992:
                if x[2] < 15.445000171661377:
                    if x[1] < 14.2955002784729:
                        if x[3] < -84.79999923706055:
                            return 2, 0.21761309177619864
                        else:
                            return 2, 0.21761309177619864
                    else:
                        return 3, 0.28729633262388576
                else:
                    if x[0] < 2378.4000244140625:
                        if x[1] < 4.90749979019165:
                            return 2, 0.21761309177619864
                        else:
                            return 3, 0.28729633262388576
                    else:
                        if x[2] < 17.185999870300293:
                            return 2, 0.21761309177619864
                        else:
                            return 3, 0.28729633262388576
            else:
                if x[1] < 13.506500482559204:
                    return 2, 0.21761309177619864
                else:
                    if x[5] < -2.1015000343322754:
                        return 3, 0.28729633262388576
                    else:
                        return 3, 0.28729633262388576
        else:
            if x[2] < 4.836999893188477:
                if x[4] < 1.4005000293254852:
                    if x[1] < 6.565500020980835:
                        return 0, 0.23808399657741328
                    else:
                        if x[0] < 5039.300048828125:
                            return 1, 0.2570065790225064
                        else:
                            return 0, 0.23808399657741328
                else:
                    return 1, 0.2570065790225064
            else:
                if x[0] < 5439.39990234375:
                    if x[0] < 4561.699951171875:
                        if x[2] < 7.427999973297119:
                            return 1, 0.2570065790225064
                        else:
                            return 2, 0.21761309177619864
                    else:
                        if x[2] < 5.319499969482422:
                            return 1, 0.2570065790225064
                        else:
                            return 0, 0.23808399657741328
                else:
                    if x[0] < 5572.949951171875:
                        if x[2] < 4.9654998779296875:
                            return 1, 0.2570065790225064
                        else:
                            return 0, 0.23808399657741328
                    else:
                        if x[1] < 5.066999912261963:
                            return 0, 0.23808399657741328
                        else:
                            return 0, 0.23808399657741328

    def tree5(self, x):
        """
        Random forest's tree #5
        """
        if x[1] < 16.85949993133545:
            if x[2] < 8.962999820709229:
                if x[1] < 2.1450000405311584:
                    if x[1] < 0.2794999983161688:
                        return 1, 0.25661564101724216
                    else:
                        if x[3] < -148.04999387264252:
                            return 2, 0.26073849121972664
                        else:
                            return 1, 0.25661564101724216
                else:
                    if x[1] < 8.28600025177002:
                        if x[4] < -1.4514999985694885:
                            return 1, 0.25661564101724216
                        else:
                            return 0, 0.230254140256227
                    else:
                        if x[5] < -0.04050000011920929:
                            return 1, 0.25661564101724216
                        else:
                            return 1, 0.25661564101724216
            else:
                if x[1] < 4.067000150680542:
                    return 2, 0.26073849121972664
                else:
                    if x[2] < 10.607500076293945:
                        return 0, 0.230254140256227
                    else:
                        if x[5] < -0.8389999866485596:
                            return 2, 0.26073849121972664
                        else:
                            return 2, 0.26073849121972664
        else:
            if x[1] < 31.856499671936035:
                if x[2] < 7.291500091552734:
                    if x[2] < 5.835000038146973:
                        return 3, 0.2523917275068076
                    else:
                        if x[3] < -279.2499876022339:
                            return 1, 0.25661564101724216
                        else:
                            return 1, 0.25661564101724216
                else:
                    return 3, 0.2523917275068076
            else:
                if x[3] < 4.799999713897705:
                    return 1, 0.25661564101724216
                else:
                    if x[3] < 28.800000190734863:
                        return 3, 0.2523917275068076
                    else:
                        return 1, 0.25661564101724216

    def tree6(self, x):
        """
        Random forest's tree #6
        """
        if x[2] < 8.962999820709229:
            if x[0] < 5509.75:
                if x[1] < 0.2794999983161688:
                    return 1, 0.236249947527513
                else:
                    if x[0] < 4541.64990234375:
                        if x[1] < 6.129499912261963:
                            return 2, 0.2857255195449342
                        else:
                            return 1, 0.236249947527513
                    else:
                        if x[3] < -267.24999237060547:
                            return 2, 0.2857255195449342
                        else:
                            return 0, 0.23425245592321087
            else:
                if x[3] < -420.8999938964844:
                    return 1, 0.236249947527513
                else:
                    if x[1] < 2.126499881967902:
                        return 1, 0.236249947527513
                    else:
                        if x[1] < 4.273999929428101:
                            return 0, 0.23425245592321087
                        else:
                            return 0, 0.23425245592321087
        else:
            if x[5] < 0.08549999818205833:
                if x[2] < 19.322999954223633:
                    if x[2] < 13.947500228881836:
                        if x[5] < -0.1664999984204769:
                            return 2, 0.2857255195449342
                        else:
                            return 0, 0.23425245592321087
                    else:
                        if x[3] < 36.0:
                            return 3, 0.2437720770043454
                        else:
                            return 3, 0.2437720770043454
                else:
                    if x[4] < -0.6299999952316284:
                        if x[4] < -0.6969999969005585:
                            return 2, 0.2857255195449342
                        else:
                            return 3, 0.2437720770043454
                    else:
                        if x[2] < 19.854000091552734:
                            return 2, 0.2857255195449342
                        else:
                            return 2, 0.2857255195449342
            else:
                if x[1] < 11.381500005722046:
                    return 2, 0.2857255195449342
                else:
                    if x[5] < 0.159000001847744:
                        return 3, 0.2437720770043454
                    else:
                        return 3, 0.2437720770043454

    def tree7(self, x):
        """
        Random forest's tree #7
        """
        if x[0] < 2659.199951171875:
            if x[2] < 20.01300048828125:
                if x[1] < 12.280999660491943:
                    if x[1] < 4.874499797821045:
                        return 2, 0.2534601603193454
                    else:
                        if x[2] < 17.11549949645996:
                            return 2, 0.2534601603193454
                        else:
                            return 3, 0.25105072422742125
                else:
                    return 3, 0.25105072422742125
            else:
                if x[5] < 1.621999979019165:
                    if x[5] < -1.7695000767707825:
                        return 3, 0.25105072422742125
                    else:
                        if x[1] < 13.698999881744385:
                            return 2, 0.2534601603193454
                        else:
                            return 3, 0.25105072422742125
                else:
                    return 3, 0.25105072422742125
        else:
            if x[2] < 4.836999893188477:
                if x[4] < -1.4880000352859497:
                    return 1, 0.26668842899580664
                else:
                    if x[5] < -0.057500001043081284:
                        if x[0] < 4641.7998046875:
                            return 1, 0.26668842899580664
                        else:
                            return 0, 0.22880068645743085
                    else:
                        if x[1] < 10.111500263214111:
                            return 0, 0.22880068645743085
                        else:
                            return 1, 0.26668842899580664
            else:
                if x[0] < 5506.599853515625:
                    if x[2] < 5.3459999561309814:
                        if x[1] < 3.4809999465942383:
                            return 1, 0.26668842899580664
                        else:
                            return 1, 0.26668842899580664
                    else:
                        if x[1] < 8.371999740600586:
                            return 0, 0.22880068645743085
                        else:
                            return 1, 0.26668842899580664
                else:
                    if x[1] < 2.0520000364631414:
                        return 1, 0.26668842899580664
                    else:
                        if x[2] < 4.957499980926514:
                            return 0, 0.22880068645743085
                        else:
                            return 0, 0.22880068645743085

    def tree8(self, x):
        """
        Random forest's tree #8
        """
        if x[2] < 10.431000232696533:
            if x[0] < 5458.60009765625:
                if x[1] < 0.2794999983161688:
                    return 1, 0.24125871557898695
                else:
                    if x[0] < 4510.4501953125:
                        if x[2] < 7.427999973297119:
                            return 1, 0.24125871557898695
                        else:
                            return 2, 0.24441444329901982
                    else:
                        if x[1] < 8.946000099182129:
                            return 0, 0.25402545900853996
                        else:
                            return 1, 0.24125871557898695
            else:
                if x[1] < 2.0459999945014715:
                    return 1, 0.24125871557898695
                else:
                    if x[1] < 11.949999809265137:
                        return 0, 0.25402545900853996
                    else:
                        return 1, 0.24125871557898695
        else:
            if x[1] < 11.964499950408936:
                if x[4] < 2.0415000319480896:
                    return 2, 0.24441444329901982
                else:
                    return 3, 0.26030138211345677
            else:
                return 3, 0.26030138211345677

    def tree9(self, x):
        """
        Random forest's tree #9
        """
        if x[4] < 1.456999957561493:
            if x[4] < 0.002000000094996679:
                if x[1] < 17.175999641418457:
                    if x[0] < 2756.7999267578125:
                        return 2, 0.2577455291884071
                    else:
                        if x[0] < 5508.949951171875:
                            return 1, 0.233885594944233
                        else:
                            return 0, 0.24320090312911513
                else:
                    if x[2] < 7.870000123977661:
                        if x[4] < -0.5019999966025352:
                            return 1, 0.233885594944233
                        else:
                            return 3, 0.2651679727382477
                    else:
                        return 3, 0.2651679727382477
            else:
                if x[4] < 0.22450000047683716:
                    if x[2] < 10.90500020980835:
                        if x[3] < -56.0:
                            return 0, 0.24320090312911513
                        else:
                            return 0, 0.24320090312911513
                    else:
                        if x[5] < 0.08000000193715096:
                            return 3, 0.2651679727382477
                        else:
                            return 2, 0.2577455291884071
                else:
                    if x[0] < 4876.849853515625:
                        if x[1] < 7.259999990463257:
                            return 2, 0.2577455291884071
                        else:
                            return 3, 0.2651679727382477
                    else:
                        if x[2] < 3.712499976158142:
                            return 0, 0.24320090312911513
                        else:
                            return 0, 0.24320090312911513
        else:
            if x[2] < 10.869999885559082:
                return 1, 0.233885594944233
            else:
                if x[0] < 2204.0:
                    return 3, 0.2651679727382477
                else:
                    if x[3] < -22.40000057220459:
                        return 2, 0.2577455291884071
                    else:
                        return 3, 0.2651679727382477