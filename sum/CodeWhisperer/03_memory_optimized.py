import tracemalloc
tracemalloc.start()

# Q: Give me an memory optimized solution for this problem.# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets. 

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res

s = Solution()

l1 = [976.2700785464949,4303.78732744839,2055.2675214328774,897.6636599379381,-1526.9040132219052,2917.882261333123,-1248.2557747461506,7835.4600156415945,9273.255210020587,-2331.1696234844458,5834.500761653291,577.8983950580896,1360.8912218786463,8511.93276585322,-8579.278836042262,-8257.414005969185,-9595.632051193486,6652.39691095876,5563.135018997009,7400.242964936384,9572.36684465528,5983.171284334472,-770.4127549413624,5610.583525729109,-7634.511482621336,2798.420426550476,-7132.9342518190715,8893.37834099168,436.96643500143364,-1706.7612001895286,-4708.887757907461,5484.673788684333,-876.9933556690285,1368.6789773729706,-9624.203991272898,2352.7099415175417,2241.914454448428,2338.679937495139,8874.961570292482,3636.4059820696675,-2809.84198852428,-1259.36092401317,3952.623918545298,-8795.490567414603,3335.334308913354,3412.757392363188,-5792.348778523182,-7421.474046902934,-3691.432981516323,-2725.784581147548,1403.9354083575927,-1227.9697307535935,9767.476761184524,-7959.103785039439,-5822.464878103307,-6773.809642300075,3062.166509307968,-4934.167949204358,-673.7845428738747,-5111.488159967945,-6820.608327089605,-7792.497176713898,3126.5917893054684,-7236.3409730277235,-6068.35276639893,-2625.4965867807177,6419.864596958701,-8057.974484138775,6758.898149976078,-8078.0318421207385,9529.189300267913,-626.975967045968,9535.221763806741,2096.9103949009186,4785.271587966034,-9216.244154913587,-4343.860748471809,-7596.068775736621,-4077.196049557101,-7625.445620915119,-3640.3364121204795,-1714.7401097066013,-8717.050073024313,3849.442387400397,1332.0290841315036,-4692.210181211091,464.9610693339928,-8121.189784831166,1518.929911123585,8585.92395152428,-3628.620950973527,3348.2075992736336,-7364.042751912157,4326.544082371311,-4211.878141055978,-6336.172759857664,1730.258696201663,-9597.84907625013,6578.80058434726,-9906.090476149058,3556.330735924603,-4599.840536156703,4703.8804424518985,9243.770902348766,-5024.937129600839,1523.1466883567373,1840.8386254367797,1445.0381158174678,-5538.367347187634,9054.980230339701,-1057.4924276474521,6928.173449422557,3989.585506350086,-4051.2609828973264,6275.9563940495445,-2069.885183060307,7622.063942223231,1625.4574527171735,7634.707237097056,3850.631801555317,4505.08559639281,26.48763853404489,9121.672694464476,2879.8039845927487,-1522.8990288364057,2127.8642825584866,-9616.136033813329,-3968.503666509014,3203.470749853701,-4198.447855791119,2360.3085799768305,-1424.6259810846768,-7290.518715550996,-4034.3534808793847,1399.298214025297,1817.4552249634653,1486.5049769915768,3064.016397142672,3042.065400033778,-1371.6312913205202,7930.931917021258,-2648.7625990420693,-1282.7014946874642,7838.467100313443,6123.879780921716,4077.771670807326,-7995.462253753978,8389.65227489347,4284.825990982228,9976.940131357329,-7011.0339068401245,7362.521147364285,-6750.141306472504,2311.191285676883,-7523.60034301117,6960.164586444687,6146.3791745002145,1382.0147722918664,-1856.334055480007,-8616.66009089724,3948.5754628912728,-929.1463464386234,4441.111989406958,7327.646518572583,9510.430100057718,7116.06684785222,-9765.71831629996,-2800.4387104327225,4599.811248481161,-6567.40645477119,420.73212408258587,-8913.240233214927,-6000.069502071999,-9629.56411078772,5873.954067148412,-5521.506238792397,-3092.9663860619457,8561.625869311818,4088.288038470655,-9363.221409373844,-6706.116870041746,2429.568029995271,1544.5717720833527,-5242.143572509827,8684.279958495874,2279.319119317919,712.6560604991664,1798.1995270914194,4602.440590335393,-3761.100090407963,-2035.5787556781625,-5803.125020497557,-6276.139882393277,8887.44779967867,4791.015900985751,-190.82382764865906,-5451.707440533535,-4912.870364592141,-8839.416793522487,-1311.6674888375837,-3764.082360117948,3926.8697763091895,-2444.9632141503816,-6407.926448807304,-9506.425432173375,-8655.007370735028,3587.855469971346,-926.0631088790942,731.5842221744442,7933.425860806841,9806.778947934086,-5662.060312030521,3261.5640620020167,-4733.5524652569875,-9586.980010685427,5167.573076722829,-3599.6569835506434,-2330.7221165620404,1766.3422710721152,6620.969104723808,2579.636871822975,7453.013108947907,-4529.159303687285,5960.936678251273,-6287.281113880956,9055.833139438892,3749.7655277563063,-5689.846457728831,8947.411809778485,4617.116135403156,-4921.167148099484,-5733.76045265036,364.01427861326556,-9486.745638909368,-5850.598491177812,-1506.2906249698754,-2516.600393315489,-728.4915127037857,-4447.425874105362,1735.6869291633757,7277.112118464629,-7649.362880759338,347.58214308228344,-7358.637873096934,4337.193623851874,-2078.805943854125,1308.4262371701789,-6334.403275718428,-7103.044813132456,-238.87438702090913,-2887.745243000888,8808.638905056261,5306.505076139305,4973.2723970109455,8074.3947949186695,-8331.551291159629,1043.849398448132,1689.5213791153765,9238.727570944582,-4157.049464149023,-5183.424401691063,-7994.121154690044,-9671.407408170517,8590.586335843811,3398.3309318182,5703.058240462755,-4365.397884921019,1728.2033237265332,-8720.894677580378,-287.44808130754245,9549.902794888934,7530.104906331817,-3236.820963263087,9231.403090829972,-5365.96747057591,8986.37644831363,8827.554094129973,5984.0517470478335,2608.9587373358227,7485.759332498939,-4139.594309844066,6978.871106258364,2357.533838350477,-9735.26284482201,-3055.329641355608,-7037.182781036699,9636.587796365064,-432.5938592002385,-52.17269002674584,2789.4503279744713,-2628.3078774076494,-7261.994566288022,6442.354663884911,-6203.041761944841,226.37965092912054,-5513.659420505215,-8043.110310119319,7243.830348433665,9458.389780462607,9216.693161260002,8131.10998442358,5480.946653972776,-3337.096959427162,-8377.972200240065,-1855.1765717238532,-5355.317156581145,-7350.247304840341,-8931.456364263495,4511.887284211576,-9771.450827499379,5411.614970055525,-7061.067091992499,-8409.558348264885,-8207.939315227892,3440.9561470782883,-5092.655802943104,-1589.2106663980303,1147.3758264783391,7211.023476575876,4540.885254226565,-4593.441895225707,-7370.344014177448,-8892.51359157604,-3968.0273103811505,-4757.6370152064355,-877.1886639904078,3665.6267109536093,3912.5089127771444,-4329.623068356667,-2401.46088199759,-6376.980765261939,5770.910246130374,-8863.038471335194,3939.9448344997472,5573.907918822068,5548.1512369750635,-4811.548713092901,-2523.737241348771,1751.992703927781,-4543.561951510659,-2582.944015642226,-6058.914396287208,-802.8823248798526,-9107.753974917718,5995.91769141236,-8460.871060267345,376.7029766305204,-3863.7980090960773,1550.858976627509,9188.666816668501,2911.4048891200764,-9292.751284890182,-1391.951209838775,200.33704636500443,723.5498940690395,3627.850212076757,-4448.0780453646785,-7422.788690673597,-2146.4864690581135,9128.114455918978,-6257.382164983105,8079.679098564742,876.1190015465272,-861.7715670846828,7640.82820459779,-827.920764628283,4483.3527322308655,-2019.4935659379598,8080.887858019156,3800.500403824548,3992.441085010334,-3445.5919688576223,5135.572854737784,2721.2211089428256,-5199.594532405809,-6789.2235502948715,5927.829490346634,9183.332060704452,-837.2234547991429,1819.6833064736984,7154.45288387109,-855.5309329228585,9037.489536654724,1515.023240897448,6415.342414026298,8176.874368254768,6310.476375371376,-6811.710731020881,2577.968781234007,-2031.3148276064585,-8745.740959533086,-1519.3549622031605,-4826.318662211846,6980.766168570215,-9333.907469066076,9179.65443726947,-2892.623030561407,-2865.8621919491425,-9673.429946325843,-6295.353495276321,-1974.8099839278257,8585.828346054277,-8007.701395574573,8906.030669581589,7389.770610932643,-916.7520618489652,-3465.9823646347986,-5345.117414418863,2289.2941295374876,-9338.508170489888,-9687.878711063435,-1424.0855500352427,-8638.518520505597,-4961.180235078142,-5576.781693078323,-4936.176125542962,-7378.895375694845,-9759.275542046915,-7690.314057225038,2369.605190254957,9485.124256361007,9806.90003121788,-1818.9180925387682,-6740.911479067892,2775.235147330586,-193.8930690252564,9788.195545688628,-8693.915856964395,5664.688766276262,-4232.030053370122,-5171.62759846852,3250.0914306535196,-5078.736300180711,3317.182351183754,346.170344045775,-1518.220231283014,1093.7561732283793,-4258.969601607405,4131.494125459578,-1702.8626133287198,-2789.088790282155,6573.138291114756,8499.338239063844,-9079.853782254062,-5347.46014340469,-3029.6126101487353,6299.329587404947,9709.82855286595,9379.434093407035,8098.966910998537,-4068.8746987194027,9840.224868289482,-5011.599178870976,-7881.876902355356,9019.052221107882,-5331.594890638074,3795.36530155501,-8832.872820388227,4614.181982549524,7634.404246676793,-4551.26209068075,-2418.8620784514296,-2514.076333581678,4975.765150802663,-5243.855149219223,-6562.93801904714,-1014.167026245239,-3910.63185245361,6783.7824451730485,-5245.163479687225,47.7891497852288,8851.671993958607,2679.9539548932153,7345.788109249297,8804.193787095348,5015.297237727038,3991.501204495027,9359.31133208454,9888.015792953589,-963.5663466048063,-8582.604436315833,-4144.119371189623,-6952.905886245391,-1650.2725040797632,-7374.213430534879,2082.3560804176395,-2343.8388168429183,7907.717685764201,9355.893435970036,937.698033388444,-4503.528602648068,1844.6083752367358,7935.223164488198,-1865.3330832850343,1041.5655338394172,-4566.944647877082,-891.11701099946,-1965.7292924080275,-5031.73069834058,117.32767650616734]
l2 = [-3792.3834804037715,-2539.3027223850504,499.40884508528507,5011.90045857975,-3329.850684174494,8483.17533241527,7246.370936718049,-9026.19408048943,-4927.149514863545,-1077.2897468159608,-7907.442225150518,-3030.4802193300584,4801.950512353649,3610.289622856517,2447.6885713200973,4210.568054446912,-5901.526260805965,-3166.0377027053573,3524.849645549257,7584.69526062654,873.561076561904,-4346.006981089267,-9395.294839880347,4206.736579484266,-9842.317929831192,-2546.4186035800894,610.7442912556362,8442.22923534386,-8210.109099341998,-1881.153560634326,-9513.736005796845,-3147.780313168194,2444.6211767958976,-4418.641035428032,-5805.001006887298,-7685.9353334581265,1542.8048804068367,3905.400118093721,3439.1428119164466,8977.220414410149,-9945.935722129945,2943.93307788072,2007.844741952791,1774.7921994057633,9255.406396804847,-9662.566532599207,3929.6486140290017,6273.572994037269,196.14393243168342,-3320.702608063817,5816.803264548098,-8055.141487351507,-1159.2872454014941,399.0474914167644,3879.1282186909502,-8182.28535935181,-5444.809969242781,-1793.9687461974881,2465.8934604026126,7739.215624348351,2376.52336482753,-7330.770581301311,9611.602655745646,7435.714695109858,54.41522290648027,8446.95963593266,827.6158751427156,8466.121357783264,6597.947372066865,9365.728205885945,8395.65621556317,-9279.32365142861,-6504.559916781201,-2217.306457976285,9042.853945908417,-3999.4216104814086,-6790.6471222479795,7726.093321731198,-1072.1116903359416,8157.511887086523,-6795.390673597135,3222.35023016199,-1194.7249434101632,-8470.264619394293,3929.2628930500123,-5052.024889216927,-9207.689548409646,-8801.114035008535,-8778.429258664253,8154.65914970079,4797.678356582021,7961.247144274701,3451.646225930426,578.7985806176639,-3911.0727130524347,9959.24502657347,-2756.218821212213,-587.0210157218098,-2435.0965015307647,9590.538586709172,-6506.832292099884,-3440.2399818384065,3606.9733203000305,-8735.847633227388,2144.9874802308204,-447.0699424716786,-4320.000464757978,-5231.73438151884,290.25486597513554,-2641.4483892591734,-869.6021747468931,-3250.452364715202,9409.873871919553,-7331.21136508792,-8063.920936432516,-3132.1654241816786,1820.5380174098245,3183.529437000565,-2054.865056639159,9985.559878443422,-2962.140076139148,4428.13335919905,2751.6538906158567,6261.077264949214,9524.5132690764,7795.873128910804,5291.239487154171,3964.9695563658115,-3290.0366064820073,-7046.288435865853,-8747.279938803804,-5161.965915970303,-1354.3703763740286,439.92547259964886,5461.671081097433,9174.818461131861,-7653.5903923037795,-7859.917196124168,1793.8944602710144,4907.961478945859,6963.007606939696,8716.641604335771,9668.52484521284,-2003.9661555094826,-2393.296329448538,-7043.826466054552,3698.6887736711888,3135.239168816741,7241.251917024147,-8054.840104247187,-44.46184349316354,1621.638593441261,-5168.859199201632,-6619.4918774167745,7191.61672839243,-8829.301555288825,-587.5819216385426,-7683.319973982294,-858.824773372653,9599.246526846186,-1525.872930890544,7142.498350091348,-7653.6887163361225,-4574.958464762717,-1924.1451866533098,-2003.7571998133853,3427.669573403062,-3105.6374524898465,4275.337368200328,2783.7379845078503,-2016.777094904538,-1364.7974469136152,2290.553996206414,-8599.156197107108,6448.134767113806,3068.4232222727387,4526.849288356705,738.4600216478084,-7790.457780165105,-1899.2877340610012,-1892.5283430288782,-3579.1401991356615,-9400.993501905014,4745.084851929547,-7804.310838749986,2126.162660901702,4064.3499293443147,2695.7264586738947,9182.8450395595,-7934.036898297228,7343.343182103981,-9416.195303021736,698.3370985416786,-1915.1276412148245,483.67720787516373,-2698.002458799804,-6188.661701198639,-9617.542051026205,362.99627582348694,6855.537253696846,-2535.680885104117,-5542.723639700395,-8389.359930563118,-8293.781537625933,-5572.0710741445555,-7999.718781568897,-4699.206032710359,-8677.010757660906,-8687.902655801487,7125.523592455636,-6757.594785823336,1193.6481164689594,5469.110888980611,-871.808693218667,-6932.622442813085,-6008.077157597713,-1340.3158743763852,564.6817835707152,-3011.1941590293027,5629.592004693226,5020.432977127968,8544.236147462358,-9420.94901946079,7913.825824204068,-2148.624230756979,7567.449907599883,3815.695523130591,9746.975141479365,5185.649034333361,-2709.107480064268,21.263456695041896,-2472.2168961129755,-2701.763279575238,-4781.910012378805,-80.59409253060767,3634.7989013872248,-4453.19457389513,487.59622154439967,-7652.394116588856,-6803.094262916175,-9063.872905756225,9414.628855412655,-9922.792969794778,-6428.400638846873,2257.3350623398474,-8372.608022933893,7637.930061936648,4392.403156845763,9327.79942875787,152.7109448152969,-3991.9263368302563,990.0114559054291,8616.374345959463,415.2287448372099,-4655.8593627536275,7547.975783482394,-2561.625029750774,-9972.333000020017,-5046.299550153682,-3635.3298164587522,7175.549364638042,-829.9366586711003,-1108.2542437739849,-3277.9546720022527,7613.562460941594,8900.535538807828,9837.806583092588,-2465.174660780265,9322.948912543427,5837.591392618027,3513.7829528853363,-5102.210411598012,-5670.854781115804,-6679.043509575087,8455.132204507307,-4118.466752336678,-938.1150910224314,-120.84332025552976,5563.431909005083,6884.699231060484,-7218.545977027744,-1461.9127957785258,6857.097756709143,6360.666115116768,-7951.724830951672,-6872.33302264074,-3916.0261680118438,-8492.818618333193,-1506.7399431881422,-7847.645897008362,1364.3518733969013,-5068.861203776878,1928.6613069924533,-7649.487141927248,9517.677368370667,8651.22407714681,-2164.0612287066842,-5156.428117478291,-4992.035742928544,-332.12929595215974,-9200.143961985661,2794.1021215025394,-1833.9418332051036,-2451.8685482222536,6187.299429783969,4180.7092036658,9086.676307853839,-2961.275190086186,7950.855292988112,5399.343725001778,-2851.5069681057394,2433.3087290651565,-4228.600846966088,7487.998341496848,-7751.453655753775,-5751.312774119179,-6339.334158401577,-1939.479951914227,4904.6592006425835,538.1489810436069,-246.47352923584913,-9989.080702060088,-1491.9654928989057,-8728.924503276832,-5834.934957570324,8647.878779209888,-5692.035913135236,7166.7527726852495,6057.867431226685,-6817.075261155143,2114.239145405576,-7686.762561899734,4557.763167390231,2749.245547444132,6238.7712338203855,-412.30901221623935,8297.261756667656,-9013.021064231205,-4142.228699459707,4301.051949303341,-1637.8157650399826,-6540.972914576872,-7855.785091429079,6346.782229232429,-537.1404306871154,7645.6734383821495,4665.782686334522,-1805.4758873851279,-2529.779716886327,312.76693302503554,7781.199063794571,4745.571594283358,-9896.940714619535,3883.157027382511,8390.148138116412,4209.115190089831,-6459.884368650082,-329.6374514508261,-7193.679641531611,-2820.0944332073586,8742.340838810353,8466.106151174168,-4343.262956478342,-3207.3791166760166,2004.2573626258782,9263.945905207602,-7043.973318692191,-4861.667126266618,7471.136545815429,-162.1553658331104,7979.221844540632,-6289.642049536475,653.3717494272132,-3474.607347012553,-3669.1488021504792,-1062.4607210760169,-1338.4510179746303,-2853.062406440911,8299.415406312371,4634.883708657855,4550.9398266305925,-4201.731008160891,1554.1884863368068,5583.588666036681,5911.807370864262,-3109.390784913755,5417.455131372957,4717.87793615466,-7169.870287561995,7318.909371329544,-1173.5705963917844,-271.791022226691,-1032.6164220400533,1356.9200295501505,2423.3849473410937,-36.408684741130855,7335.770865181912,2554.695123905689,-1971.441013889601,-1666.1648618257805,6216.772302579027,-3036.161145069598,-5770.904084351729,-8812.336239884215,7520.536958411485,8370.929023806999,-7597.596356730481,-3310.5251700777026,-6492.558609695123,-7682.030623482406,7997.334860000603,-8862.45481709289,9609.713269380136,-8070.982786052316,7269.412983871716,1330.1221397832542,-2641.6502436425326,-3153.1524674968423,5147.2828647541755,-3708.5340999142554,3146.378332342836,346.52167032160287,-300.68709683859015,8023.243412983233,1092.9011724051925,6537.2320609739,4511.470682029787,-9228.855078820034,5462.201050108384,-5662.594998179186,8062.992937031431,-9141.51618782336,-3338.559310513625,-8005.34105530492,-488.21765830312506,6400.4487173950365,-4036.2528067387184,-6981.302053779168,-3394.659286062016,6277.6028384127185,-7192.320844013062,-5452.751018449964,-8622.960710132522,4114.2008797921535,-2095.335129273263,-3783.2004571336793,4372.527806823038,-3280.449153194895,4555.425464288361,6303.987906286271,-5646.743130845231,9476.373936919666,-6752.841041746664,-4183.181866865149,-6404.094183329167,-3089.8868728733105,-398.7822435848884,443.5173800423818,7072.120845925441,7788.95817631733,-5597.922784381873,2457.880643715049,-7770.078854025688,-820.602796358633,-3553.329239067637,-3669.985090927872,-348.31516575798014,4596.552710585351,-8616.34682415221,7583.466753748089,4696.275492611221,-6470.012222218797,8783.218181747408,126.24448046777252,9996.171562339307,-6054.810513985247,698.163967664028,-4195.039148801432,-3916.5288522150686,1821.3076166798037,8434.381337416664,6105.2771115835,4478.8279700265175,1183.4756420340436,8445.970073348955,-152.77186618231826,7476.643566694362,6679.6328775326365,-5723.293063968269,5424.5092593182035,-9756.576861134825,-3543.40924903825,-5408.6511061610045,137.25916974626853,4737.0632336157105,-8046.4726510455175,298.44403873536794,8768.240433887713,-5427.06898034109,3542.822882228482]
l3 = [1857.6054156231512,-9798.726086878134,-483.4760828555445,4175.407818820973,-9120.491359518188,7590.429660474601,401.62833271346244,-9386.779033485642,-5511.727761583196,9073.513928546261,1646.3946610411058,-7850.548644623909,-4249.10995438877,-865.9274827903155,-9580.99861464539,-1767.6897277248245,-210.8272913060373,-5126.442494375357,1772.7800058397315,5064.802391843537,-5283.31551788729,2409.998005599753,2792.444859274832,8970.80602257682,5565.523345928876,6966.9053958001205,-191.60183127449636,-6293.028260412343,9916.3058591927,-7412.884779226008,-570.8536129146923,-8638.138015157869,8877.017147016391,9298.498816968793,4387.781240079472,-3000.143127396622,-4912.351977647513,-4693.933509259052,-7454.119491598505,516.179061534458,-7163.65448597045,-3665.3866689308743,2534.1295191820973,4550.872191814997,-9514.545907558775,-1397.6803124652015,3042.491896842781,7064.919523170258,-493.5043557583522,9384.117434353706,-4687.3490491710545,-9729.825867465623,-324.9427059652771,-4877.724099599641,6474.3534404633865,-5344.546556377758,-3787.4156341738744,5824.548620382246,4302.8650405072,1161.0247331452501,4098.961238455189,-1627.2627285994695,-9893.799047706643,-9772.897429756149,224.43575147373303,-8334.180405620016,-8978.490396614865,9310.332782749465,7180.052793161172,-6959.455455808609,-9986.71562819591,8833.355907795129,-4433.4940335977135,-6282.04794289005,3830.162156630706,-7821.925223173475,-4707.008039943994,9501.89360424093,2789.255489480205,413.5558296510717,-2041.6277033012457,5490.01909768404,-7180.850469526125,9346.756040739645,7222.460161315732,2353.139651384865,-9141.876191948837,4017.1129889547537,8265.686817709615,491.5413495725188,-2915.503563454744,-7594.4531004106075,5098.022082751366,7700.437024236126,-7994.965118483028,5179.691095046839,-9658.79027481805,9341.098361544391,2301.1604127019236,1048.7811798326638,-4081.0033282214445,8585.83343139567,-4681.887453264179,6562.9322643339,9702.17358674264,5667.9329102961165,379.79840772863463,-8678.514722966562,-551.7242165785392,-1234.8810605659291,-5944.079176260095,-1528.2472657139115,-2844.8423183932255,-6726.31477696703,-1172.5171333502767,-4744.000873510219,441.24841364528766,-9296.798805676117,8124.6283957456835,6327.286110397121,1051.6266502100916,7036.171655144863,9247.901476216008,-7789.554118946789,2616.6361681960752,9959.880018713171,9757.783386670522,2066.459845814892,-7439.582590983667,1663.8566198105636,-9958.707288511565,-6021.773306662808,9122.4631911992,-3391.188547943122,2767.8021155389706,-4382.810107355146,8956.437742231792,4571.174598989735,-3406.976848371748,5835.228423607417,-7836.689510473247,-2153.621198690812,-5575.637445368154,3674.528945520926,-7951.074364561393,-2059.4833543465184,-4467.005395816208,126.85838647608216,-3002.0463899224214,4128.211553340219,-9508.459513860678,2679.7384261181505,-5388.5742061236,-4625.819424863013,6005.112071670472,9111.367879608417,-3668.9957994582683,6536.105407381514,-7920.183240575338,2679.633060147664,5020.645990698376,-6880.441439310869,-1479.9522466087892,7854.143284979633,-7928.430731032557,-9638.072835970497,1811.707580958675,-1289.3691893813302,5973.784977678053,8469.110764082132,-4016.927109123678,-2231.917656617895,-274.5582734137024,1763.029208705986,9677.076593632333,3946.60501660103,-2209.029853088624,-4724.646270990757,8892.51436844248,-7289.031337829872,4405.317050095162,8507.900505848815,3293.3117306887725,-1538.9111966775763,-6020.18120149032,-2650.4935549614547,4137.436188402442,2990.6844835059364,8559.523331967157,7337.218273187496,6323.015045327367,8229.017507015247,-4473.256945259012,-2609.52919720701,-2402.1219242796524,1209.0117741956055,3364.364590855419,-4265.666339192114,-9610.750653813993,-2015.5523268418137,-3829.4408089119906,8843.694380360957,7765.300810880872,7206.213566868391,3059.99521890486,-3114.2167060212223,976.985347986094,6304.500814327454,-8027.79262554378,6021.497605106095,-9176.404173437566,6328.420624287115,6151.27608319747,-8979.853823424884,2543.2142292371645,49.061486257944125,-6603.609936565706,-7032.421246452487,5465.1825213404645,1353.8549767368804,9659.982698330648,9644.955545766883,9853.339869285326,-7627.689632684682,8765.122739279246,-5108.607819588744,-835.7548048277604,5148.131116434517,-5927.581358455361,1326.2321110865978,-6283.665035480086,-7905.277866374134,-7668.827751408029,-2847.219303035624,-9906.90326325633,-1502.9215759662093,3283.9421016229808,-1966.236299920225,-8284.107989603297,-8746.222759527189,-4437.6697447027655,-6613.7461891279845,9301.89946435939,-6975.3955005183,6109.248748099932,1722.158834822896,1385.738399685888,241.6143184756911,9435.261522279023,-2723.104498167244,5758.315019077525,1105.8821493391915,-2087.326647485477,9109.318666115618,1966.3193872937427,-7621.661157079729,-1649.2159800628688,5631.634553632151,3874.940464784275,8326.806596731483,-4812.4523171695955,5163.874327076477,-802.4958521095814,1472.1949393363084,9100.93362012566,9585.726399783547,7231.81927851127,-2818.058245394075,7754.0167145463965,2772.183552828261,-1400.0643905857378,-9285.146349990326,5402.5624838316435,42.11161448226085,5723.769989301216,4960.455986865398,5871.347360967038,-3986.9768260646633,6015.971981352619,976.9265693233465,-533.475991017136,3502.5182764151377,-9572.826341233034,-7953.663682248116,-4156.45269664956,9659.802199156791,-7205.0844227009,-3388.0739848157937,-8978.938706161527,-3374.6223941454746,-3593.474269783368,8936.143418890442,6903.081739914407,-2344.7156151445706,-9504.618839215027,6620.622279907566,3210.7235428908025,-6952.710326973805,9921.425420203745,-7995.3312515175385,7342.290831873259,-4114.676717406221,-1292.9306734968595,5909.130535526292,3550.167119880205,8757.287488880782,2422.806509207665,-8043.796770418945,7687.207264839006,5383.110499771821,4237.409017866441,-8925.329052925292,-2075.54510676512,-6651.283610809216,6438.078168157379,4010.572456357255,7661.551946382704,9331.50213848328,5494.952283849972,9884.661664415242,2295.3977228859767,-9257.407922171044,-9714.969696994083,-3157.9224959242256,6469.434381350744,7322.694126494622,9216.250576453556,-8697.570629023632,-9108.577780246718,8265.671927340674,-3899.0660327427686,1159.7480121926546,9648.897660014198,-1991.0293052815332,3317.4279661967976,-1982.4087273602945,5363.893289255595,554.2945114573158,-5249.537240273005,-4573.877974830676,-4838.815749231855,646.4065651712153,4063.780320313286,8985.598000862843,3881.747501659598,5623.856879247813,-6621.477682708688,-2518.7474998534863,-1724.3956028346784,3727.6046000094593,-4082.1604724625286,-3934.161571606678,-2882.2169071826374,6206.041630864645,1551.801800866975,-8494.454403345311,-8435.078006190624,-2574.2611143500135,5331.821012123166,3773.6685295736097,4159.647093023732,5344.201321081939,-4256.945742273412,965.1256388417587,867.0528063353904,4792.650023598986,9137.411382112929,-4440.201104090682,5865.633455140964,3199.410970465249,1604.757417269202,5497.5955869480385,8880.649328561987,-9266.17164261174,-7051.997949735587,5125.744630022315,-8324.17294179831,322.4740148218607,-5602.78446716786,-4514.08592314497,4036.8096588883254,-9396.144534625768,7466.388558038074,-1110.4208929546003,47.86587814202176,800.9592738738374,2910.885891589878,-3102.868267545038,-7977.850188730174,-3632.421266676469,-6637.157639543593,1122.6635890094785,-3639.427380792271,9161.3435598687,9314.685559605612,2402.5176113648286,2349.94535334572,9707.57129134212,7745.663024703721,5301.398983162799,-3728.1877651459763,-2689.2194376384723,-5974.6646847826905,-257.0374616525078,9807.37044279159,8243.019060231774,-7633.011319610619,-9496.194214189876,7972.753368165322,743.4025589741486,-5996.202235830877,3473.0653916927076,2884.463558596399,-7558.287863270656,-4807.99533004761,-8798.44071373484,-5802.790522597161,-7353.8865029387425,-6135.274150508878,3709.3429182623386,-9010.005114778645,-7962.90769503567,-7316.527238434247,-3669.1775808373195,-4024.9937829611818,-4898.724293667212,5010.733068648326,9960.455755162013,679.5584725759163,8884.054358278841,-2067.7977574787064,-7866.351063945731,-1824.523410603254,-4077.4445317061336,-131.86075421643727,3140.873538328464,-778.9956169518373,8703.210241556513,7695.296445987598,4039.5519033239434,-206.30175270901782,-7366.254363710863,-2059.726664447332,4088.030788023474,-4302.289588925377,-7920.238449131592,8157.969150212564,4181.016196310891,2305.528532701943,5849.978112178331,6712.920751669513,-330.8200365795328,7623.765028188802,8328.380214022109,-4568.978091504372,2150.9071958158856,531.6805764093842,758.9155830380496,8753.26187929124,-3896.2259461394196,9668.679564691523,8042.624296084643,-825.5422277299476,6349.065272363323,5380.939886402812,3557.8993923704256,-3603.322212336915,-6070.980163580922,3430.5539353151635,6859.465928021684,-9674.944226452606,2856.0675061702404,-1142.5395075557517,7961.7551025396715,-3570.541382915895,-516.3037547275653,295.34208070372733,-7191.20957257894,4257.846053978126,6609.526902419191,-8841.814462074795,-4172.223589261946,-9239.106369298841,9130.882093764849,3343.3764140764706,9284.00838909563,629.8855666261552,6041.370477912278,-2511.7203224052,-2923.619348547182,-2434.643657897346,3157.2426745285647,-2810.9369795669563,8007.349032084512,9665.497301003106,-9391.469693259882,-6127.53419195007,-7755.00014825228,-9152.719058171135,-5445.18013305427]

s.threeSum([*l1])
s.threeSum([*l2])
s.threeSum([*l3])

# for i in range(1000):
#     s.threeSum([*l1])
#     s.threeSum([*l2])
#     s.threeSum([*l3])

curr, peak = tracemalloc.get_traced_memory()
peak /= 1024
curr /= 1024
print(f"{peak=}")
print(f"{curr=}")