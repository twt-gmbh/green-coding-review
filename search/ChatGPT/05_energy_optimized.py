# optimize solution based on energy consumption

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        
        return left

l1 = [-9967,-9949,-9926,-9866,-9850,-9770,-9743,-9705,-9692,-9615,-9561,-9557,-9523,-9425,-9376,-9337,-9283,-9237,-9232,-9225,-9114,-8987,-8867,-8850,-8806,-8711,-8647,-8576,-8575,-8563,-8562,-8486,-8450,-8443,-8431,-8414,-8376,-8289,-8274,-8249,-8168,-8154,-8116,-8115,-8079,-8057,-7983,-7949,-7876,-7821,-7810,-7802,-7778,-7728,-7715,-7709,-7702,-7690,-7664,-7651,-7541,-7539,-7465,-7406,-7272,-7209,-7186,-7105,-7094,-7024,-6988,-6977,-6967,-6922,-6852,-6780,-6769,-6766,-6716,-6681,-6669,-6626,-6625,-6590,-6521,-6486,-6410,-6359,-6348,-6335,-6294,-6281,-6278,-6134,-6093,-6087,-5992,-5987,-5982,-5975,-5965,-5964,-5937,-5900,-5856,-5654,-5621,-5596,-5587,-5520,-5513,-5396,-5377,-5332,-5251,-5227,-5173,-5128,-5019,-4977,-4933,-4931,-4922,-4864,-4828,-4827,-4826,-4789,-4772,-4726,-4717,-4694,-4682,-4630,-4513,-4500,-4493,-4338,-4323,-4274,-4262,-4261,-4247,-4238,-4182,-4052,-4040,-4039,-4013,-4007,-4003,-3983,-3977,-3971,-3928,-3915,-3914,-3872,-3808,-3797,-3779,-3768,-3755,-3740,-3708,-3703,-3677,-3642,-3624,-3557,-3550,-3482,-3474,-3456,-3451,-3388,-3330,-3216,-3191,-3190,-3129,-3125,-3088,-2975,-2973,-2951,-2891,-2833,-2782,-2708,-2625,-2583,-2528,-2510,-2470,-2428,-2382,-2326,-2291,-2194,-2136,-2098,-1963,-1897,-1802,-1775,-1726,-1680,-1670,-1668,-1649,-1578,-1504,-1369,-1366,-1230,-1178,-1133,-1090,-1075,-1072,-1033,-901,-893,-851,-842,-822,-804,-789,-756,-739,-588,-546,-459,-399,-357,-263,-243,-212,-189,-103,133,313,319,335,346,353,357,422,427,444,458,469,510,592,622,692,835,854,1014,1021,1107,1152,1182,1248,1302,1307,1312,1330,1425,1461,1476,1519,1523,1525,1547,1612,1640,1659,1703,1711,1806,1813,1866,1884,1942,1946,1982,2020,2041,2047,2052,2092,2112,2124,2126,2179,2219,2273,2318,2340,2390,2401,2407,2413,2431,2450,2482,2520,2532,2567,2654,2668,2679,2708,2860,2869,2899,2901,2925,2941,2949,3012,3087,3170,3224,3234,3290,3293,3294,3328,3341,3348,3358,3375,3399,3415,3471,3557,3614,3667,3672,3685,3723,3755,3843,3904,3944,3973,3975,3980,4046,4053,4133,4174,4252,4354,4370,4380,4423,4430,4485,4529,4572,4679,4690,4747,4758,4759,4795,4814,4817,4830,4871,4894,4918,4942,4943,4961,4992,5005,5055,5066,5091,5100,5155,5205,5314,5334,5357,5408,5410,5431,5442,5448,5475,5492,5493,5512,5513,5559,5618,5702,5705,5711,5712,5786,5796,5800,5806,5917,5934,5943,5957,5967,6066,6113,6115,6326,6342,6350,6441,6443,6559,6571,6643,6663,6682,6851,6864,6888,6952,6977,7030,7032,7037,7063,7066,7114,7185,7193,7217,7247,7250,7277,7289,7383,7414,7567,7571,7703,7847,7913,7914,7932,7933,8014,8029,8044,8052,8055,8096,8135,8138,8367,8407,8420,8481,8550,8646,8661,8697,8744,8785,8827,8854,8896,8917,8945,9069,9117,9134,9143,9163,9197,9205,9288,9327,9328,9455,9460,9500,9506,9521,9557,9610,9656,9719,9802,9964]
t1 = -1148

l2 = [-9979,-9950,-9849,-9846,-9842,-9813,-9744,-9735,-9705,-9691,-9678,-9673,-9667,-9618,-9607,-9496,-9462,-9417,-9309,-9262,-9241,-9238,-9232,-9214,-9158,-9124,-9070,-8973,-8933,-8879,-8835,-8833,-8763,-8685,-8626,-8616,-8612,-8494,-8484,-8332,-8306,-8259,-8208,-8198,-8193,-8112,-8098,-8088,-8080,-7987,-7950,-7919,-7913,-7911,-7871,-7866,-7823,-7804,-7702,-7656,-7615,-7581,-7562,-7536,-7518,-7492,-7429,-7333,-7331,-7325,-7309,-7290,-7247,-7207,-7193,-7174,-7133,-7075,-7051,-7029,-6963,-6923,-6843,-6810,-6802,-6781,-6703,-6673,-6638,-6620,-6614,-6610,-6601,-6568,-6559,-6497,-6486,-6354,-6345,-6328,-6324,-6286,-6251,-6191,-6152,-6150,-6075,-5977,-5892,-5775,-5695,-5605,-5519,-5515,-5497,-5486,-5476,-5430,-5372,-5363,-5330,-5268,-5189,-5186,-5099,-5063,-5024,-4981,-4951,-4926,-4901,-4844,-4821,-4807,-4792,-4786,-4686,-4640,-4526,-4523,-4321,-4292,-4261,-4259,-4243,-4206,-4204,-4164,-4160,-4123,-4113,-4098,-4089,-4084,-4056,-4038,-3984,-3936,-3878,-3852,-3816,-3720,-3642,-3507,-3451,-3394,-3375,-3360,-3328,-3324,-3297,-3287,-3209,-3158,-3099,-3085,-2991,-2975,-2939,-2917,-2903,-2888,-2880,-2872,-2820,-2777,-2651,-2572,-2527,-2505,-2490,-2430,-2258,-2255,-2209,-2206,-2181,-2177,-2127,-2081,-1998,-1970,-1966,-1942,-1905,-1841,-1795,-1706,-1693,-1687,-1647,-1644,-1621,-1599,-1596,-1583,-1555,-1537,-1401,-1304,-1300,-1293,-1273,-1237,-1198,-1188,-1074,-959,-948,-946,-920,-852,-820,-761,-731,-714,-667,-519,-474,-473,-471,-394,-362,-335,-314,-248,-164,-162,-151,-122,-46,-43,-42,-40,53,75,98,99,103,219,280,282,287,309,312,321,342,357,382,397,402,419,454,501,511,521,578,584,620,688,758,767,864,872,899,913,968,976,1003,1049,1074,1077,1101,1141,1165,1191,1258,1260,1291,1364,1366,1385,1443,1455,1495,1521,1525,1539,1604,1615,1709,1823,1978,2084,2104,2174,2212,2231,2268,2412,2439,2475,2513,2571,2806,2818,2825,2862,2886,2952,3004,3007,3008,3091,3105,3202,3221,3234,3245,3403,3441,3487,3518,3531,3532,3627,3642,3676,3710,3720,3730,3818,3829,4004,4012,4034,4038,4082,4099,4188,4196,4199,4245,4281,4295,4312,4359,4367,4377,4396,4433,4458,4469,4476,4534,4538,4631,4634,4647,4696,4805,4838,4861,4890,4917,4931,4959,5009,5015,5086,5177,5356,5421,5449,5456,5518,5553,5563,5588,5627,5671,5701,5730,5734,5769,5775,5882,5922,5926,5942,5971,6003,6050,6090,6166,6259,6382,6398,6402,6446,6572,6573,6600,6609,6616,6663,6718,6734,6787,6855,6892,6950,7077,7103,7111,7137,7213,7216,7319,7343,7373,7413,7453,7473,7566,7573,7602,7618,7636,7705,7716,7897,7944,7968,8078,8092,8132,8156,8172,8218,8263,8403,8464,8512,8516,8536,8581,8621,8627,8653,8702,8727,8792,8816,8863,8874,8889,8927,8928,8937,9029,9139,9156,9211,9239,9267,9295,9312,9325,9506,9561,9566,9619,9726,9831,9894,9920,9961,9985,9987]
t2 = 7658

l3 = [-9980,-9847,-9823,-9806,-9798,-9754,-9728,-9708,-9698,-9668,-9595,-9530,-9497,-9412,-9332,-9291,-9290,-9281,-9111,-9108,-9074,-9068,-9003,-8955,-8887,-8841,-8803,-8791,-8622,-8610,-8577,-8568,-8525,-8406,-8361,-8352,-8237,-8200,-8187,-8151,-8105,-8099,-8072,-8061,-8052,-8039,-8037,-7988,-7920,-7911,-7908,-7882,-7876,-7872,-7868,-7817,-7740,-7709,-7693,-7689,-7664,-7601,-7523,-7505,-7369,-7315,-7306,-7305,-7299,-7280,-7230,-7193,-7188,-7161,-7152,-7033,-6902,-6872,-6859,-6779,-6686,-6676,-6659,-6656,-6643,-6611,-6568,-6567,-6544,-6495,-6494,-6418,-6352,-6314,-6293,-6250,-6247,-6201,-6158,-6135,-6104,-6095,-6091,-6025,-5962,-5940,-5927,-5894,-5891,-5823,-5810,-5804,-5800,-5762,-5731,-5714,-5701,-5656,-5626,-5549,-5512,-5494,-5482,-5425,-5368,-5353,-5339,-5331,-5282,-5276,-5221,-5218,-5179,-5174,-5167,-5115,-5084,-5028,-4839,-4753,-4631,-4617,-4538,-4517,-4503,-4418,-4386,-4319,-4252,-4231,-4160,-3943,-3833,-3796,-3764,-3763,-3751,-3720,-3690,-3674,-3647,-3645,-3537,-3490,-3486,-3437,-3314,-3260,-3248,-3240,-3223,-3218,-3169,-3099,-2936,-2933,-2912,-2906,-2866,-2787,-2583,-2568,-2473,-2409,-2404,-2356,-2322,-2199,-2187,-2168,-2110,-2089,-2017,-1915,-1906,-1802,-1782,-1714,-1711,-1617,-1592,-1583,-1574,-1543,-1519,-1518,-1505,-1434,-1377,-1331,-1314,-1256,-1220,-1204,-1192,-1111,-1100,-1091,-1058,-1049,-1015,-997,-863,-849,-831,-765,-716,-715,-704,-682,-624,-593,-559,-507,-289,-247,-246,-170,-156,-86,-55,-6,5,10,48,70,163,228,308,328,376,394,439,465,525,544,585,590,640,659,698,699,743,758,787,788,808,833,837,908,918,949,951,970,1016,1023,1034,1073,1076,1154,1352,1430,1564,1568,1617,1649,1681,1801,1991,1993,2029,2116,2149,2162,2198,2206,2393,2418,2480,2601,2653,2667,2729,2749,2769,2778,2779,2815,2907,2915,2920,2944,2971,3099,3129,3144,3176,3183,3189,3252,3258,3264,3313,3330,3362,3364,3407,3457,3482,3557,3558,3607,3664,3782,3789,3855,3874,3901,3940,3980,3985,4137,4146,4167,4177,4222,4344,4365,4380,4394,4395,4414,4417,4490,4493,4548,4610,4611,4703,4728,4740,4748,4853,4861,4951,4999,5175,5302,5366,5373,5385,5482,5583,5594,5627,5647,5750,5799,5800,5893,6092,6122,6126,6138,6164,6193,6196,6203,6211,6218,6250,6404,6426,6440,6473,6487,6516,6576,6578,6588,6590,6595,6618,6629,6634,6709,6732,6824,6832,6858,6861,6920,6942,6971,6988,7001,7015,7090,7130,7162,7166,7219,7238,7266,7314,7414,7419,7448,7534,7589,7655,7671,7752,7753,7789,7795,7825,7867,7898,7939,8028,8034,8090,8139,8173,8185,8198,8205,8256,8301,8305,8315,8320,8343,8387,8477,8500,8515,8518,8569,8631,8648,8715,8719,8738,8749,8755,8769,8772,8923,8971,9071,9082,9098,9131,9165,9271,9317,9362,9398,9466,9469,9473,9492,9528,9571,9622,9670,9725,9744,9757,9778,9779,9783,9813,9832,9911,9974,9980,9997]
t3 = -9012

s = Solution()

s.searchInsert([*l1], t1)
s.searchInsert([*l2], t2)
s.searchInsert([*l3], t3)

# for i in range(100000):
#     s.searchInsert([*l1], t1)
#     s.searchInsert([*l2], t2)
#     s.searchInsert([*l3], t3)
