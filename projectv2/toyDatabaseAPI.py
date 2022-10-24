from random import randint

class ToyDatabaseApi:
    def __init__(self):
        self.arr = [{"RU-AMU": 3218, "RU-ARK": 3682, "RU-AST": 3704, "RU-BEL": 3922, "RU-BRY": 2995, "RU-VLA": 6984,
                     "RU-VGG": 7666, "RU-VLG": 4269, "RU-VOR": 9167, "RU-YEV": 470, "RU-ZAB": 2875, "RU-IVA": 3629,
                     "RU-IRK": 8142, "RU-KB": 2014, "RU-KGD": 2651, "RU-KLU": 4784, "RU-KAM": 1484, "RU-KC": 1754,
                     "RU-KEM": 8652, "RU-KIR": 4181, "RU-KOS": 2028, "RU-KDA": 21230, "RU-KYA": 10314, "RU-KGN": 2890,
                     "RU-KRS": 4661, "RU-LEN": 8483, "RU-LIP": 4399, "RU-MAG": 543, "RU-MOW": 27998, "RU-MOS": 19255,
                     "RU-MUR": 2300, "RU-NEN": 67, "RU-NIZ": 14815, "RU-NGR": 2890, "RU-NVS": 6900, "RU-OMS": 8230,
                     "RU-ORE": 6175, "RU-ORL": 2737, "RU-PNZ": 5528, "RU-PRI": 7386, "RU-PSK": 2338, "RU-AD": 1714,
                     "RU-AL": 590, "RU-BA": 3808, "RU-BU": 2528, "RU-DA": 5427, "RU-IN": 705, "RU-KL": 1309,
                     "RU-KR": 1757, "RU-KO": 2735, "RU-ME": 1913, "RU-MO": 2833, "RU-SA": 2194, "RU-SE": 2514,
                     "RU-TA": 13643, "RU-TY": 909, "RU-KK": 1681, "RU-ROS": 12007, "RU-RYA": 5590, "RU-SAM": 10821,
                     "RU-SPE": 17209, "RU-SAR": 9554, "RU-SAK": 1631, "RU-SVE": 8621, "RU-SMO": 2853, "RU-STA": 9488,
                     "RU-TAM": 4752, "RU-TVE": 5211, "RU-TOM": 1932, "RU-TUL": 6496, "RU-TYU": 8973, "RU-UD": 4786,
                     "RU-ULY": 4216, "RU-KHA": 5253, "RU-KHM": 6190, "RU-CHE": 13038, "RU-CE": 1047, "RU-CU": 3640,
                     "RU-CHU": 13, "RU-YAN": 1400, "RU-YAR": 5448},
                    {"RU-AMU": 5380, "RU-ARK": 6072, "RU-AST": 5804, "RU-BEL": 5484, "RU-BRY": 4842, "RU-VLA": 10169,
                     "RU-VGG": 10922, "RU-VLG": 6662, "RU-VOR": 12519, "RU-YEV": 973, "RU-ZAB": 5422, "RU-IVA": 5876,
                     "RU-IRK": 14058, "RU-KB": 2446, "RU-KGD": 5277, "RU-KLU": 6633, "RU-KAM": 2290, "RU-KC": 2059,
                     "RU-KEM": 12825, "RU-KIR": 7054, "RU-KOS": 3314, "RU-KDA": 27663, "RU-KYA": 16340, "RU-KGN": 4623,
                     "RU-KRS": 6860, "RU-LEN": 12557, "RU-LIP": 6598, "RU-MAG": 1054, "RU-MOW": 37041, "RU-MOS": 24723,
                     "RU-MUR": 3422, "RU-NEN": 105, "RU-NIZ": 22207, "RU-NGR": 4972, "RU-NVS": 10568, "RU-OMS": 12997,
                     "RU-ORE": 9359, "RU-ORL": 3796, "RU-PNZ": 7951, "RU-PRI": 12808, "RU-PSK": 4441, "RU-AD": 2058,
                     "RU-AL": 1322, "RU-BA": 5749, "RU-BU": 5082, "RU-DA": 5637, "RU-IN": 632, "RU-KL": 1886,
                     "RU-KR": 3067, "RU-KO": 4293, "RU-ME": 2935, "RU-MO": 4111, "RU-SA": 4133, "RU-SE": 2867,
                     "RU-TA": 19614, "RU-TY": 2016, "RU-KK": 2699, "RU-ROS": 15661, "RU-RYA": 7393, "RU-SAM": 16519,
                     "RU-SPE": 27344, "RU-SAR": 13503, "RU-SAK": 3020, "RU-SVE": 12869, "RU-SMO": 4441, "RU-STA": 12234,
                     "RU-TAM": 6108, "RU-TVE": 8218, "RU-TOM": 3232, "RU-TUL": 9483, "RU-TYU": 11904, "RU-UD": 8317,
                     "RU-ULY": 6089, "RU-KHA": 8167, "RU-KHM": 7017, "RU-CHE": 19440, "RU-CE": 1054, "RU-CU": 5372,
                     "RU-CHU": 105, "RU-YAN": 1861, "RU-YAR": 8077},
                    {"RU-AMU": 6043, "RU-ARK": 5924, "RU-AST": 4848, "RU-BEL": 4273, "RU-BRY": 3638, "RU-VLA": 9229,
                     "RU-VGG": 8244, "RU-VLG": 6786, "RU-VOR": 10247, "RU-YEV": 922, "RU-ZAB": 4441, "RU-IVA": 6256,
                     "RU-IRK": 12439, "RU-KB": 1164, "RU-KGD": 4680, "RU-KLU": 7008, "RU-KAM": 2034, "RU-KC": 1296,
                     "RU-KEM": 11191, "RU-KIR": 8189, "RU-KOS": 3485, "RU-KDA": 15849, "RU-KYA": 15580, "RU-KGN": 3930,
                     "RU-KRS": 6814, "RU-LEN": 9610, "RU-LIP": 5097, "RU-MAG": 1032, "RU-MOW": 43367, "RU-MOS": 15576,
                     "RU-MUR": 3756, "RU-NEN": 83, "RU-NIZ": 24783, "RU-NGR": 4836, "RU-NVS": 8478, "RU-OMS": 14323,
                     "RU-ORE": 6817, "RU-ORL": 3858, "RU-PNZ": 7463, "RU-PRI": 11572, "RU-PSK": 4108, "RU-AD": 1590,
                     "RU-AL": 1024, "RU-BA": 3753, "RU-BU": 4595, "RU-DA": 3118, "RU-IN": 316, "RU-KL": 1734,
                     "RU-KR": 2493, "RU-KO": 4314, "RU-ME": 2658, "RU-MO": 3888, "RU-SA": 3325, "RU-SE": 2323,
                     "RU-TA": 20251, "RU-TY": 1248, "RU-KK": 2017, "RU-ROS": 13925, "RU-RYA": 8091, "RU-SAM": 14065,
                     "RU-SPE": 26287, "RU-SAR": 9526, "RU-SAK": 2296, "RU-SVE": 9310, "RU-SMO": 3621, "RU-STA": 7528,
                     "RU-TAM": 5627, "RU-TVE": 7137, "RU-TOM": 1955, "RU-TUL": 8129, "RU-TYU": 14618, "RU-UD": 8590,
                     "RU-ULY": 5158, "RU-KHA": 8244, "RU-KHM": 7152, "RU-CHE": 17583, "RU-CE": 370, "RU-CU": 5445,
                     "RU-CHU": 76, "RU-YAN": 1804, "RU-YAR": 7849},
                    {"RU-AMU": 711, "RU-ARK": 634, "RU-AST": 532, "RU-BEL": 910, "RU-BRY": 856, "RU-VLA": 1494,
                     "RU-VGG": 1546, "RU-VLG": 620, "RU-VOR": 2253, "RU-YEV": 146, "RU-ZAB": 1102, "RU-IVA": 504,
                     "RU-IRK": 1913, "RU-KB": 696, "RU-KGD": 713, "RU-KLU": 956, "RU-KAM": 295, "RU-KC": 389,
                     "RU-KEM": 1620, "RU-KIR": 836, "RU-KOS": 330, "RU-KDA": 5049, "RU-KYA": 2029, "RU-KGN": 719,
                     "RU-KRS": 962, "RU-LEN": 2346, "RU-LIP": 1072, "RU-MAG": 150, "RU-MOW": 2885, "RU-MOS": 5579,
                     "RU-MUR": 301, "RU-NEN": 22, "RU-NIZ": 2285, "RU-NGR": 620, "RU-NVS": 1554, "RU-OMS": 1048,
                     "RU-ORE": 1385, "RU-ORL": 568, "RU-PNZ": 1029, "RU-PRI": 1548, "RU-PSK": 655, "RU-AD": 510,
                     "RU-AL": 228, "RU-BA": 1596, "RU-BU": 720, "RU-DA": 1607, "RU-IN": 307, "RU-KL": 312, "RU-KR": 406,
                     "RU-KO": 453, "RU-ME": 451, "RU-MO": 647, "RU-SA": 517, "RU-SE": 513, "RU-TA": 2024, "RU-TY": 487,
                     "RU-KK": 432, "RU-ROS": 2798, "RU-RYA": 1094, "RU-SAM": 1781, "RU-SPE": 1508, "RU-SAR": 1596,
                     "RU-SAK": 497, "RU-SVE": 2157, "RU-SMO": 713, "RU-STA": 2064, "RU-TAM": 745, "RU-TVE": 1118,
                     "RU-TOM": 483, "RU-TUL": 1499, "RU-TYU": 1015, "RU-UD": 892, "RU-ULY": 796, "RU-KHA": 884,
                     "RU-KHM": 769, "RU-CHE": 2096, "RU-CE": 493, "RU-CU": 798, "RU-CHU": 22, "RU-YAN": 247,
                     "RU-YAR": 930},
                    {"RU-AMU": 6103, "RU-ARK": 7310, "RU-AST": 6375, "RU-BEL": 6249, "RU-BRY": 5777, "RU-VLA": 11122,
                     "RU-VGG": 12501, "RU-VLG": 7762, "RU-VOR": 14625, "RU-YEV": 1102, "RU-ZAB": 6231, "RU-IVA": 6957,
                     "RU-IRK": 16311, "RU-KB": 3062, "RU-KGD": 6357, "RU-KLU": 7647, "RU-KAM": 2475, "RU-KC": 2273,
                     "RU-KEM": 13898, "RU-KIR": 8532, "RU-KOS": 3968, "RU-KDA": 32152, "RU-KYA": 18936, "RU-KGN": 5310,
                     "RU-KRS": 7825, "RU-LEN": 13540, "RU-LIP": 7516, "RU-MAG": 1237, "RU-MOW": 52344, "RU-MOS": 29725,
                     "RU-MUR": 4365, "RU-NEN": 177, "RU-NIZ": 27308, "RU-NGR": 5624, "RU-NVS": 12524, "RU-OMS": 15217,
                     "RU-ORE": 10234, "RU-ORL": 4397, "RU-PNZ": 8940, "RU-PRI": 14812, "RU-PSK": 4983, "RU-AD": 2394,
                     "RU-AL": 1499, "RU-BA": 5884, "RU-BU": 5833, "RU-DA": 6526, "RU-IN": 626, "RU-KL": 2123,
                     "RU-KR": 3535, "RU-KO": 5231, "RU-ME": 3413, "RU-MO": 4610, "RU-SA": 4502, "RU-SE": 3455,
                     "RU-TA": 24190, "RU-TY": 2189, "RU-KK": 3159, "RU-ROS": 18681, "RU-RYA": 8465, "RU-SAM": 18514,
                     "RU-SPE": 35508, "RU-SAR": 15548, "RU-SAK": 3390, "RU-SVE": 14318, "RU-SMO": 5027, "RU-STA": 13971,
                     "RU-TAM": 6731, "RU-TVE": 9244, "RU-TOM": 3835, "RU-TUL": 10654, "RU-TYU": 13253, "RU-UD": 9828,
                     "RU-ULY": 6683, "RU-KHA": 9658, "RU-KHM": 8421, "RU-CHE": 21515, "RU-CE": 978, "RU-CU": 6580,
                     "RU-CHU": 143, "RU-YAN": 2465, "RU-YAR": 9573},
                    {"RU-AMU": 1099, "RU-ARK": 1031, "RU-AST": 692, "RU-BEL": 949, "RU-BRY": 787, "RU-VLA": 1699,
                     "RU-VGG": 1602, "RU-VLG": 958, "RU-VOR": 2110, "RU-YEV": 296, "RU-ZAB": 1313, "RU-IVA": 799,
                     "RU-IRK": 2315, "RU-KB": 516, "RU-KGD": 895, "RU-KLU": 1204, "RU-KAM": 406, "RU-KC": 522,
                     "RU-KEM": 1765, "RU-KIR": 1187, "RU-KOS": 591, "RU-KDA": 4386, "RU-KYA": 2522, "RU-KGN": 732,
                     "RU-KRS": 1297, "RU-LEN": 2553, "RU-LIP": 1051, "RU-MAG": 322, "RU-MOW": 2647, "RU-MOS": 3449,
                     "RU-MUR": 530, "RU-NEN": 46, "RU-NIZ": 3364, "RU-NGR": 1039, "RU-NVS": 944, "RU-OMS": 1293,
                     "RU-ORE": 1572, "RU-ORL": 667, "RU-PNZ": 1154, "RU-PRI": 2333, "RU-PSK": 1159, "RU-AD": 324,
                     "RU-AL": 407, "RU-BA": 1435, "RU-BU": 926, "RU-DA": 1052, "RU-IN": 176, "RU-KL": 424, "RU-KR": 540,
                     "RU-KO": 815, "RU-ME": 545, "RU-MO": 795, "RU-SA": 671, "RU-SE": 522, "RU-TA": 2359, "RU-TY": 291,
                     "RU-KK": 604, "RU-ROS": 2189, "RU-RYA": 1240, "RU-SAM": 1638, "RU-SPE": 1799, "RU-SAR": 1873,
                     "RU-SAK": 621, "RU-SVE": 1669, "RU-SMO": 864, "RU-STA": 2155, "RU-TAM": 974, "RU-TVE": 1566,
                     "RU-TOM": 407, "RU-TUL": 1841, "RU-TYU": 1627, "RU-UD": 1123, "RU-ULY": 779, "RU-KHA": 998,
                     "RU-KHM": 1071, "RU-CHE": 2440, "RU-CE": 233, "RU-CU": 834, "RU-CHU": 52, "RU-YAN": 446,
                     "RU-YAR": 1239},
                    {"RU-AMU": 240, "RU-ARK": 453, "RU-AST": 122, "RU-BEL": 262, "RU-BRY": 260, "RU-VLA": 387,
                     "RU-VGG": 497, "RU-VLG": 416, "RU-VOR": 584, "RU-YEV": 62, "RU-ZAB": 345, "RU-IVA": 295,
                     "RU-IRK": 706, "RU-KB": 112, "RU-KGD": 227, "RU-KLU": 276, "RU-KAM": 117, "RU-KC": 88,
                     "RU-KEM": 650, "RU-KIR": 361, "RU-KOS": 189, "RU-KDA": 682, "RU-KYA": 892, "RU-KGN": 265,
                     "RU-KRS": 402, "RU-LEN": 529, "RU-LIP": 171, "RU-MAG": 98, "RU-MOW": 963, "RU-MOS": 425,
                     "RU-MUR": 291, "RU-NEN": 21, "RU-NIZ": 1145, "RU-NGR": 296, "RU-NVS": 321, "RU-OMS": 701,
                     "RU-ORE": 346, "RU-ORL": 159, "RU-PNZ": 234, "RU-PRI": 462, "RU-PSK": 269, "RU-AD": 74,
                     "RU-AL": 92, "RU-BA": 385, "RU-BU": 318, "RU-DA": 345, "RU-IN": 38, "RU-KL": 133, "RU-KR": 187,
                     "RU-KO": 251, "RU-ME": 176, "RU-MO": 159, "RU-SA": 290, "RU-SE": 86, "RU-TA": 776, "RU-TY": 67,
                     "RU-KK": 208, "RU-ROS": 838, "RU-RYA": 470, "RU-SAM": 505, "RU-SPE": 756, "RU-SAR": 599,
                     "RU-SAK": 83, "RU-SVE": 965, "RU-SMO": 216, "RU-STA": 520, "RU-TAM": 309, "RU-TVE": 283,
                     "RU-TOM": 158, "RU-TUL": 439, "RU-TYU": 671, "RU-UD": 403, "RU-ULY": 184, "RU-KHA": 202,
                     "RU-KHM": 497, "RU-CHE": 1141, "RU-CE": 52, "RU-CU": 255, "RU-CHU": 16, "RU-YAN": 168,
                     "RU-YAR": 439},
                    {"RU-AMU": 1121, "RU-ARK": 868, "RU-AST": 531, "RU-BEL": 650, "RU-BRY": 509, "RU-VLA": 1317,
                     "RU-VGG": 1583, "RU-VLG": 511, "RU-VOR": 1661, "RU-YEV": 196, "RU-ZAB": 1873, "RU-IVA": 585,
                     "RU-IRK": 1941, "RU-KB": 165, "RU-KGD": 225, "RU-KLU": 844, "RU-KAM": 378, "RU-KC": 299,
                     "RU-KEM": 1447, "RU-KIR": 985, "RU-KOS": 314, "RU-KDA": 2728, "RU-KYA": 1719, "RU-KGN": 736,
                     "RU-KRS": 1099, "RU-LEN": 1377, "RU-LIP": 764, "RU-MAG": 265, "RU-MOW": 742, "RU-MOS": 1847,
                     "RU-MUR": 337, "RU-NEN": 54, "RU-NIZ": 2236, "RU-NGR": 732, "RU-NVS": 908, "RU-OMS": 1120,
                     "RU-ORE": 1616, "RU-ORL": 531, "RU-PNZ": 999, "RU-PRI": 1774, "RU-PSK": 852, "RU-AD": 163,
                     "RU-AL": 441, "RU-BA": 1697, "RU-BU": 1125, "RU-DA": 1207, "RU-IN": 108, "RU-KL": 609,
                     "RU-KR": 374, "RU-KO": 801, "RU-ME": 558, "RU-MO": 719, "RU-SA": 1045, "RU-SE": 330, "RU-TA": 2401,
                     "RU-TY": 760, "RU-KK": 568, "RU-ROS": 1643, "RU-RYA": 968, "RU-SAM": 1198, "RU-SPE": 380,
                     "RU-SAR": 1501, "RU-SAK": 582, "RU-SVE": 1064, "RU-SMO": 656, "RU-STA": 1554, "RU-TAM": 880,
                     "RU-TVE": 841, "RU-TOM": 334, "RU-TUL": 1384, "RU-TYU": 801, "RU-UD": 1003, "RU-ULY": 503,
                     "RU-KHA": 730, "RU-KHM": 817, "RU-CHE": 1605, "RU-CE": 108, "RU-CU": 748, "RU-CHU": 49,
                     "RU-YAN": 389, "RU-YAR": 795},
                    {"RU-AMU": 3, "RU-BEL": 5, "RU-BRY": 4, "RU-VLA": 1, "RU-VGG": 6, "RU-VLG": 6, "RU-VOR": 9,
                     "RU-YEV": 2, "RU-ZAB": 4, "RU-IVA": 3, "RU-IRK": 11, "RU-KB": 5, "RU-KGD": 1, "RU-KLU": 4,
                     "RU-KAM": 1, "RU-KC": 2, "RU-KEM": 8, "RU-KIR": 10, "RU-KOS": 2, "RU-KDA": 31, "RU-KYA": 5,
                     "RU-KGN": 8, "RU-KRS": 3, "RU-LEN": 7, "RU-LIP": 4, "RU-MAG": 2, "RU-MOW": 34, "RU-MOS": 5,
                     "RU-MUR": 2, "RU-NIZ": 16, "RU-NGR": 8, "RU-NVS": 5, "RU-OMS": 5, "RU-ORE": 4, "RU-ORL": 4,
                     "RU-PNZ": 9, "RU-PRI": 20, "RU-PSK": 5, "RU-AL": 1, "RU-BU": 2, "RU-DA": 15, "RU-IN": 3,
                     "RU-KL": 3, "RU-KR": 2, "RU-KO": 5, "RU-ME": 3, "RU-MO": 2, "RU-SA": 1, "RU-SE": 10, "RU-TA": 7,
                     "RU-ROS": 21, "RU-RYA": 12, "RU-SAM": 13, "RU-SPE": 27, "RU-SAR": 18, "RU-SAK": 1, "RU-SVE": 11,
                     "RU-SMO": 2, "RU-STA": 12, "RU-TAM": 13, "RU-TVE": 1, "RU-TOM": 3, "RU-TUL": 2, "RU-TYU": 2,
                     "RU-UD": 1, "RU-ULY": 2, "RU-KHA": 7, "RU-KHM": 8, "RU-CHE": 15, "RU-CE": 7, "RU-CU": 6,
                     "RU-YAN": 1, "RU-YAR": 7},
                    {"RU-AMU": 63, "RU-ARK": 27, "RU-AST": 121, "RU-BEL": 22, "RU-BRY": 42, "RU-VLA": 49, "RU-VGG": 55,
                     "RU-VLG": 10, "RU-VOR": 68, "RU-YEV": 16, "RU-ZAB": 32, "RU-IVA": 34, "RU-IRK": 134, "RU-KB": 23,
                     "RU-KGD": 38, "RU-KLU": 46, "RU-KAM": 19, "RU-KC": 95, "RU-KEM": 56, "RU-KIR": 101, "RU-KOS": 75,
                     "RU-KDA": 84, "RU-KYA": 282, "RU-KGN": 54, "RU-KRS": 100, "RU-LEN": 102, "RU-LIP": 24,
                     "RU-MAG": 12, "RU-MOW": 60, "RU-MOS": 176, "RU-MUR": 38, "RU-NIZ": 300, "RU-NGR": 50, "RU-NVS": 30,
                     "RU-OMS": 55, "RU-ORE": 90, "RU-ORL": 30, "RU-PNZ": 15, "RU-PRI": 90, "RU-PSK": 63, "RU-AD": 12,
                     "RU-AL": 26, "RU-BA": 27, "RU-BU": 87, "RU-DA": 21, "RU-IN": 3, "RU-KL": 61, "RU-KR": 51,
                     "RU-KO": 28, "RU-ME": 52, "RU-MO": 37, "RU-SA": 101, "RU-SE": 60, "RU-TA": 92, "RU-TY": 42,
                     "RU-KK": 96, "RU-ROS": 116, "RU-RYA": 25, "RU-SAM": 169, "RU-SPE": 155, "RU-SAR": 109,
                     "RU-SAK": 24, "RU-SVE": 81, "RU-SMO": 41, "RU-STA": 67, "RU-TAM": 29, "RU-TVE": 57, "RU-TOM": 30,
                     "RU-TUL": 69, "RU-TYU": 36, "RU-UD": 62, "RU-ULY": 18, "RU-KHA": 53, "RU-KHM": 85, "RU-CHE": 139,
                     "RU-CE": 2, "RU-CU": 49, "RU-CHU": 5, "RU-YAN": 66, "RU-YAR": 78}
                    ]

    def __del__(self):
        pass

    def __select_random(self, value):
        return self.arr[value % 10]

    def select_rta_count(self):
        return 1000

    def select_vehicles_count(self):
        return 1600


    def select_participants_count(self):
        return 2600

    def select_count_rta_by_region(self):
        return self.__select_random(0)

    def select_count_rta_by_key_value(self, key, value):
        return self.__select_random(value)

    def select_count_rta_by_key_values(self, key, values):
        return self.__select_random(values)

    def select_count_rta_by_keys_values(self, keys, values):
        return self.__select_random(values)

    def select_count_vehicles_by_key_value(self, key, value):
        return self.__select_random(value)

    def select_count_vehicles_by_key_values(self, key, values):
        return self.__select_random(values)

    def select_count_vehicles_by_keys_values(self, keys, values):
        return self.__select_random(values)

    def select_count_participants_by_key_value(self, key, value):
        return self.__select_random(value)

    def select_count_participants_by_key_values(self, key, values):
        return self.__select_random(values)

    def select_count_participants_by_keys_values(self, keys, values):
        return self.__select_random(values)

