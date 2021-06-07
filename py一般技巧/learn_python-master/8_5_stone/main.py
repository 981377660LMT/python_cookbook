from stone.value import *


def get_diamond_value(num=1):
    return 0.05 * num


def get_vit_value(num=1):
    return num


def get_l1_value(num=1):
    one_value = l1_value + get_diamond_value(l1_value_diamond)
    return one_value * num


def get_l3_value(num=1):
    one_value = get_l1_value(l1_to_l3) + l1_to_l3_gold + get_vit_value(l1_to_l3_vit)
    return one_value * num


def get_l4_value(num=1):
    one_success_value = get_l3_value() + get_l1_value(l3_to_l4) + l3_to_l4_gold + get_vit_value(l3_to_l4_vit)
    one_fail_value = get_l1_value(l3_to_l4) + l3_to_l4_gold
    # 成功一次的花费为，成功的花费+失败的花费，其中失败的次数应该是（失败的概率/成功的概率）
    one_value = one_success_value + one_fail_value * (1 - l3_to_l4_rate) / l3_to_l4_rate
    return one_value * num


def get_l6_value(num=1):
    one_value = get_l4_value(l4_to_l6) + l4_to_l6_gold + get_vit_value(l4_to_l6_vit)
    return one_value * num


print(get_l1_value())
print(get_l3_value())
print(get_l4_value())
print(get_l6_value())
