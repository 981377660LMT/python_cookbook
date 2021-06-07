"""
购买1级石头
"""
l1_value = 0.75         # 1颗1级石头消耗0.75金
l1_value_diamond = 8    # 1颗1级石头同时还需要消耗8颗钻石

"""
1级合成3级
"""
l1_to_l3 = 12           # 1颗1级石头变成1颗3级石头，需要消耗12颗1级石头，注意是12颗1级->1颗3级
l1_to_l3_gold = 0.39    # 同时还需要消耗0.39金
l1_to_l3_vit = 10       # 同时还需要消耗10点体力

"""
3级合成4级
"""
l3_to_l4 = 16           # 1颗3级石头变成1颗4级石头，需要消耗16个1级石头
l3_to_l4_gold = 0.897   # 1颗3级石头变成1颗4级石头，需要消耗0.897金
l3_to_l4_vit = 10       # 同时还需要消耗10点体力
l3_to_l4_rate = 0.4878  # 1颗3级石头变成1颗4级石头，成功概率只有0.4878，并非100%
                        # 如果失败，则金和16颗1级五行石也将被扣除，但是不消耗体力，也不消耗3级石头
                        # 这个概率的算法，自己用25%的情况推算一下

"""
4级合成6级
"""
l4_to_l6 = 12           # 1颗4级石头变成6级石头，概率100%，需要消耗12颗4级石头，注意是12颗4级->1颗6级
l4_to_l6_gold = 19.75   # 需要消耗金 19.75 金
l4_to_l6_vit = 10       # 同时还需要消耗10点体力

"""
已知1颗六级石头的市场售价为750金，请问是自己合成石头划算还是直接购买划算
其它数据：
    1颗钻石diamond 卖出 0.05金
    1点体力vit 可以卖出 1金
"""
