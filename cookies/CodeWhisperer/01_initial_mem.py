import tracemalloc
tracemalloc.start()

from typing import List

# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], 
# we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i

g1 = [5840,6515,9482,7301,3097,9823,3459,8020,3972,3662,1292,8590,2533,2130,9371,1712,5803,8059,2490,1170,4058,6614,184,4208,5347,2828,6242,2287,5132,7138,5218,5472,2350,2823,2599,4148,9233,8088,4868,1883,7803,5534,646,5498,4040,6928,6991,9636,6325,5480,6408,762,9140,3998,4792,626,8588,5838,3384,2556,4601,5306,6759,7763,3309,166,1416,1822,9295,524,7229,8296,700,6274,449,8147,3468,6518,3088,132,214,3357,1615,2928,9026,4941,1292,9498,1384,9051,4846,5539,3071,657,2594,3106,7341,1511,9001,1131,596,4851,1441,5016,325,5536,8855,7233,7910,80,8276,6928,5131,5621,9834,9041,1732,1361,5441,9346,364,4563,2387,8890,3479,7952,9104,3400,4410,2875,2318,6035,79,8143,5909,5704,7414,3164,6189,7952,1624,6092,1614,8703,7582,5728,7813,5042,2392,7889,7210,9691,1777,9411,7088,2322,1345,237,2128,6219,1187,6823,3063,5782,7971,8566,2475,9600,612,6906,3996,2353,5504,1675,9490,6916,7782,5727,1660,7327,5324,3550,7485,6836,6389,244,2582,3216,2801,6411,1682,3048,798,7364,4561,2275,8638,9317,1656,2423,1782,6438,1308,5719,1632,3385,6942,2016,5539,8379,6016,3967,4050,5597,7825,5692,1005,5128,3797,4844,3294,1065,8405,9326,4200,8773,8687,7117,9080,4081,2597,166,8927,374,9711,7460,6065,5682,3258,4362,6195,9393,8178,2548,5157,7455,5747,7316,36,4879,6174,61,7506,6980,1058,4532,3959,1436,3301,8249,6422,3819,7499,2590,958,9787,5913,4211,6593,3941,770,4355,1859,3835,5581,3743,1576,5710,2994,1307,1165,3314,961,3493,3947,6433,9727,7453,2781,1230,6704,9526,9927,4746,3600,6931,1182,3005,2515,6787,2084,3348,3985,3608,7821,4452,7022,9923,6933,2989,2087,7211,7115,363,4649,1904,1460,6948,543,1800,7129,240,7316,2894,6120,5945,6118,7624,61,8217,3437,7464,368,4213,4113,6363,9007,7393,2655,1877,3864,3728,4269,5240,1592,6446,7139,3800,433,5510,8570,4328,882,1821,2117,5885,371,7074,7652,9777,5220,8154,1636,130,4296,9317,2638,7789,3251,1436,4193,1580,3860,6499,1326,8293,4433,4986,7084,6721,373,3169,1507,6425,9219,6654,3528,2252,244,375,4162,2513,6515,6000,6342,8994,5251,4472,3984,4936,2029,6942,1444,2786,946,849,320,7641,9659,5371,4670,3179,7442,2094,5089,9791,3095,7783,1357,760,4497,3388,1341,5786,5263,878,7998,82,2247,4595,4275,3671,6326,9995,9631,5948,9359,4729,1081,4546,1897,8824,3050]
s1 = [6433,2979,5662,6196,7642,8630,5313,3964,2203,9685,2438,7001,2322,2361,338,74,741,3249,740,5391,4670,8609,8605,4268,179,5961,2470,8978,4240,708,9558,5617,3166,5331,7688,9016,5147,8837,8282,3696,5716,4755,2657,9600,5613,8580,1683,8398,5779,2317,6768,8008,6958,3793,2137,6446,6528,6364,166,435,1969,1229,9221,5105,5044,1199,7580,3407,4967,5518,3589,4823,5392,7198,9167,7339,1228,7388,2583,7279,1493,3768,1155,7834,9854,1665,3424,185,7279,5075,7727,5210,2766,1677,6463,294,4052,4984,8093,9577,7770,3870,9269,3797,5394,8833,1507,8386,7214,1147,2738,5631,1346,1366,2483,9543,7076,8677,2200,2171,2131,5223,90,8943,3186,8348,8022,1538,2314,1874,5185,2296,5956,3578,8247,1317,8212,1008,3782,4821,6782,5290,209,2705,2234,2327,1417,4927,1194,8295,9821,2157,908,5027,92,1842,9640,1098,1881,2793,9442,4815,9221,1717,3912,7534,3334,8744,8528,663,9434,5012,7999,8990,9994,6244,3795,7753,256,8036,6771,6386,9528,9739,5401,5472,1678,5071,4152,6150,8600,6187,5736,1382,9804,1910,7097,4249,3410,6111,3219,5466,1566,7462,2994,5289,4594,7392,4200,3340,8505,8182,7616,6287,9505,6338,5242,374,834,6181,2074,6217,2969,6539,6664,949,2505,5348,2258,1176,5750,1206,4621,5550,5552,8872,5780,1259,1902,5043,2988,595,1487,102,4281,6835,987,8716,2669,3212,6565,3967,3250,4045,6098,5344,4043,5937,4683,5667,3533,2802,7464,9739,8963,9594,5104,76,1967,3124,6645,4091,3716,2321,7950,3879,4357,9108,4690,3217,2431,8857,9484,8343,3645,9436,4739,5001,5193,6439,1589,2393,2464,8948,3735,9515,6332,311,6090,5914,5946,7366,6490,302,1340,1965,1179,3705,2678,4730,8609,5775,3400,1726,514,3575,7549,2414]

g2 = [3989,2503,3517,2672,2388,5395,3442,8011,1964,5764,2957,7397,3899,3970,7297,4904,8891,293,9030,4100,5347,7034,4777,7453,6981,4123,737,4462,1972,8390,1672,607,2121,6997,9352,1732,7789,3396,6247,8021,8788,5344,2305,3420,1132,2004,7645,1708,9775,8193,7529,692,2548,2684,8536,6996,6863,6177,6599,5986,4525,828,6835,3205,94,2468,3779,405,5038,9402,376,3946,498,7667,7374,9631,8931,4516,6730,3291,1563,8653,3124,1839,9661,6960,4737,3467,4044,6030,4703,5639,7854,5535,6311,2988,4691,3293,2882,5802,7283,8527,8934,9436,8293,2464,7677,8367,8798,7795,3746,4877,3809,9962,9041,9283,5577,2174,9355,4721,6875,1180,8889,7289,2497,2758,7459,4048,2052,6845,3311,7846,1748,7829,9095,3869,4724,4999,4931,605,8157,3687,9062,3452,3782,9546,101,4791,9038,6038,5628,8864,3666,3108,8430,6911,9498,22,6574,1254,6103,8593,9199,3192,9894,8064,1735,6541,3419,8779,5047,7247,9023,9801,3206,5291,4548,6283,4851,1338,3548,388,5246,3923,1222,1925,7186,8902,8640,351,8857,3716,8617,4261,7739,9394,3512,674,1939,8034,8946,7304,1974,8530,5278,7971,116,5720,8044,8170,5697,3405,4243,2821,1800,2692,9265,6438,9710,9777,6254,4079,5406,4612,8267,6635,6008,3605,3281,5163,5619,29,1435,2904,3253,6449,9831,8970,7427,9078,613,4187,9285,8810,9739,4109,5737,4264,9121,9595,9115,100,7386,2355,5909,1609,5395,9113,7720,285,1,4804,5852,2964,9379,2099,4967,2069,6828,5605,6510,7875,8418,7821,1808,3191,1933,3974,267,5383,8807,9558,2419,6835,7501,4766,5642,8820,9161,4486,6773,8374,2284,4290,6733,121,8718,223,3677,4333,3633,9769,9115,7327,7558,2545,6433,63,6491,2024,8343,8596,2438,2853,128,1509,9990,2509,7323,9300,2023,9352,3253,593,6558,1025,3800,4670,2372,9674,7765,117,8934,7936,825,7097,6705,5266,8122,3594,5311,8935,7375,8610,2277,1864,7487,8200,6654,8983,1891,9975,1617,9372,4592,627,6104,5967,8991,2139,6820,7240,7022,4518,8630,6246,7009,1746,8293,1410,766,5278,4998,8145,4327,6057,2711,3103,6676,9989,4757,7019,2635,124,6461,1630,5673,9426,1321,2539,9695,2590,7775,7407,4479,7012,7336,7838,8701,3138,1409,1112,3878,5488,4826,1528,9318,1322,3953,3116,1135,3526,4471,2964,6896,8076,8072,4379,8753,2743,4705,4453,6744,9622,5631]
s2 = [7435,3367,7079,8805,4546,9846,572,3749,902,2310,6183,6233]

g3 = [9846,3265,4860,9226,7892,4374,5875,6745,3469,706,2600,2223,7769,2898,9894,538,6217,6922,6037,2164,5073,4852,7878,2047,1872,7600,2497,8292,756,798,660,3220,8616,7457,3338,2746,4736,8737,6688,715,2293,8344,1208,6173,8995,7222,6022,3623,3561,8949,1642,4985,4354,8623,7251,4188,2660,9782,2957,2252,4421,7109,1072,5252,7013,9397,3919,9360,1685,7099,2958,4470,8753,9798,5796,1473,7264,7366,8449,6002,3763,9009,2436,1635,974,4465,8394,2419,3456,6168,5820,6522,6243,7743,9124,6739,2788,7317,4306,2611,5532,6927,7205,6923,4183,308,5303,1153,6951,8468,5295,1209,2493,8830,771,8287,5996,2345,3092,3913,1435,6595,5369,8373,7149,7998,3855,8033,8132,4846,5117,3534,2938,9838,4940,9745,3225,5022,1135,26,9681,957,1914,2935,9662,2722,929,5628,6266,5447,470,8718,1864,1721,5273,592,6186,2323,208,4263,3422,5250,8409,8217,5104,7940,2283,1741,6119,5847,3782,2776,2604,7180,6357,1163,624,8963,4052,1242,9014,4404]
s3 = [2998,5662,808,2122,8068,3887,8923,6067,9988,1824,200,1448,5182,5209,6178,4864,6181,1793,1484,8390,895,5375,137,6274,9585,3420,169,6005,2853,9754,4420,8040,8701,3187,5919,5150,1778,3362,8339,5394,4318,4606,2563,6214,9101,4653,6236,424,6855,968,4371,9053,6188,5204,434,6238,1430,2547,330,3613,8402,6762,3969,8151,1041,6251,8357,8799,7705,6773,5312,9412,9524,9145,6012,2799,8353,2196,4681,6600,9304,3086,5714,5241,733,5029,8474,7595,4567,9501,7445,3397,5348,7035,596,648,574,6798,5638,8449,5260,9221,6568,4445,2990,587,5103,7602,740,4883,5411,438,3899,1848,9725,1021,6931,942,8642,5611,9009,2108,9883,4260,946,8394,7469,1806,1863,8743,3752,9865,2041,904,8697,8016,5897,7943,7378,9672,5594,3129,7027,3822,2712,8473,1029,2661,2354,5663,7735,8346,7522,1054,2978,5492,3894,2680,4951,2666,3058,6839,3969,852,9593,5029,3794,7317,8054,7153,3332,8319,5931,8770,5653,805,5445,3025,113,1968,651,4334,1385,64]


s = Solution()

s.findContentChildren([*g1], [*s1])
s.findContentChildren([*g2], [*s2])
s.findContentChildren([*g3], [*s3])

# for i in range(100000):
#     s.findContentChildren([*g1], [*s1])
#     s.findContentChildren([*g2], [*s2])
#     s.findContentChildren([*g3], [*s3])

curr, peak = tracemalloc.get_traced_memory()
peak /= 1024
curr /= 1024
print(f"{peak=}")
print(f"{curr=}")