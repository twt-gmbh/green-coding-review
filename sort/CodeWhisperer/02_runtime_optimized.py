import sys
sys.setrecursionlimit(2000)

from typing import Optional

# Q: Give me a runtime optimized solution for this problem. Given the head of a linked list, return the list after sorting it in ascending order.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def merge(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        if head1.val < head2.val:
            head1.next = self.merge(head1.next, head2)
            return head1
        else:
            head2.next = self.merge(head1, head2.next)
            return head2

s = Solution()
nodeList = [-595,190,132,-269,754,178,533,303,857,-982,266,543,-751,-809,-279,896,-548,947,544,205,905,235,-201,594,91,357,-521,148,-489,931,257,105,938,750,58,-573,25,-844,-509,-5,-973,326,239,-983,622,-481,-639,-711,790,135,549,327,-924,-421,-721,-65,-525,786,23,556,-158,522,108,369,-953,-206,-82,220,-494,-647,-724,-119,835,703,-667,616,-865,-818,761,501,-70,-893,-610,165,698,-738,732,-740,-513,-697,-947,15,-852,442,580,999,927,-920,854,-736,979,273,-462,529,-963,-104,129,617,276,-122,-614,820,-23,74,542,-352,922,-923,-311,-991,-139,-994,83,-839,600,110,-38,385,-225,174,-177,-855,-760,-785,889,-535,-13,238,-240,-748,633,-219,451,-428,-915,-366,-683,-882,784,876,-557,900,-484,646,-970,-287,-746,-100,-413,317,887,811,121,334,918,-94,635,858,-204,76,-478,411,-876,-813,-483,945,-314,-658,787,-800,421,511,954,-767,620,344,295,-113,-771,893,426,-318,-560,-443,-101,363,981,-616,158,604,18,-345,-564,-79,340,781,610,621,-547,361,-706,-256,-690,188,-780,-624,406,-741,341,-342,-598,-294,-186,-470,-436,666,955,798,-541,834,-346,-966,808,985,717,147,124,557,-371,356,-488,-403,-1,-45,-390,299,-542,-615,-108,-825,991,715,756,694,744,-939,867,632,271,-773,93,-986,-479,150,-499,203,246,957,618,785,-426,-254,-161,-391,-454,5,-255,-777,677,39,492,196,507,-848,3,-312,-227,-323,367,-945,-859,644,256,-798,-67,-425,-18,-277,487,-199,452,44,279,-326,200,901,-607,-783,704,713,-961,88,-934,34,642,-19,-794,-601,471,695,-349,480,-995,-942,775,528,-102,440,358,-908,217,741,654,50,-169,-722,-207,-867,476,-856,906,386,-242,127,-205,926,724,-981,502,-120,-946,892,437,-211,-57,189,281,929,-999,-238,460,-887,222,51,-562,478,-918,-621,212,446,-674,-189,-678,-284,355,579,-539,-575,101,-878,-117,-554,-952,197,-134,374,263,-497,366,752,-702,-948,859,337,336,-362,-640,810,743,-437,-418,-841,827,-682,-292,-468,-515,-749,490,433,-810,837,-384,484,-422,-649,218,422,362,-58,612,-747,55,-701,592,-432,-160,-308,526,-435,571,-729,-786,465,180,-464,376,-382,-333,-474,192,843,368,-328,-996,-796,-42,-592,-566,-236,-781,-29,-543,467,842,161,588,-30,813,146,-385,454,-519,-732,-288,-969,593,972,993,-522,463,-8,412,-175,473,-653,838,773,274,-95,992,109,14,687,-511,-911,-34,-231,459,461,-823,-689,-11,-380,170,-64,524,415,223,548,45,-63,658,-471,-105,191,128,-47,-404,-698,-324,52,-829,-588,800,-482,-116,-730,-52,292,973,916,301,63,874,804,439,-129,136,845,-622,-398,538,-846,-808,126,-527,671,977,-296,-692,419,70,359,-619,-241,38,-586,-442,-381,277,664,-447,839,258,-802,-274,-9,199,-858,-162,-804,707,-685,325,-830,951,99,-978,-955,960,-533,606,399,332,-558,-12,-681,-816,515,402,-334,408,-461,856,456,-208,-171,910,-790,-368,-183,534,-195,873,-159,-892,-335,214,-998,719,702,287,-518,-232,-628,-424,-789,-480,26,990,537,330,-379,294,570,746,-904,-313,-822,-359,-187,78,-77,-487,-929,-35,-419,-252,535,-517,860,64,-544,-932,559,995,-769,855,168,-568,-289,125,768,47,734,-646,-433,841,318,783,-172,-776,767,-782,-984,898,-633,432,391,-705,-636,-138,751,403,184,-283,649,79,983,-458,-84,-267,681,-448,-638,-451,-958,259,-190,755,879,-348,-465,826,-260,882,-358,878,-446,-843,-473,-351,-691,315,503,-407,193,795,254,-935,474,498,-107,123,-580,-40,-26,-860,21,81,689,56,978,-330,164,506,-257,-742,-987,792,211,-728,-886,-430,-759,757,-670,-321,989,-944,145,-589,-565,-43,584,-845,285,2,-971,-965,982,-578,819,518,818,693,-642,240,431,280,648,-476,675,-263,224,-735,319,265,390,680,-17,-137,-73,-224,-16,788,-452,852,-868,866,-506,-420,0,809,-569,10,477,342,521,736,230,-960,370,-925,290,-276,175,322,-753,69,-39,114,-14,-814,-37,-332,-180,-688,-992,-109,796,868,42,-4,814,387,-243,87,517,335,423,686,427,-555,921,482,-536,611,-805,504,343,-20,-343,210,-215,897,183,-153,-467,-757,96,-599,49,493,944,32,590,582,-523,805,904,140,1,17,-715,-529,388,57,817,550,-54,984,525,255,774,31,932,909,700,864,-574,614,13,880,-339,-125,923,-838,349,-60,-56,288,-354,-76,-322,883,928,-806,-248,-526,765,-280,-431,428,-951,840,-87,-356,-278,-890,807,585,941,-411,394,499,-956,997,-755,688,-700,29,-417,-212,748,-731,953,409,-687,364,-717,404,-460,-89,-62,-594,523,-662,-534,-637,122,-182,-3,-680,553,228,236,328,-930,652,486,-500,-990,-315,505,-495,572,36,-917,307,770,912,-936,115,414,903,712,-584,309,166,-21,-795,-672,-192,-514,540,697,213,-472,920,-344,-103,-582,799,-142,323,-641,601,-733,-156,380,-121,-410,-275,-174,-6,448,-528,628,-869,-985,-561,974,410,886,-524,27,749,-96,275,-272,-147,354,237,-307,-86,683,668,-297]

nodes = {}
for i, n in enumerate(nodeList):
    if i + 1 < len(nodeList):
        nodes[n] = ListNode(n)
        if i > 0:
            nodes[nodeList[i - 1]].next = nodes[n]
    else:
        nodes[n] = ListNode(n)
s.sortList(nodes[nodeList[0]])

# for i in range(1000):
#     nodes = {}
#     for i, n in enumerate(nodeList):
#         if i + 1 < len(nodeList):
#             nodes[n] = ListNode(n)
#             if i > 0:
#                 nodes[nodeList[i - 1]].next = nodes[n]
#         else:
#             nodes[n] = ListNode(n)

#     s.sortList(nodes[nodeList[0]])
