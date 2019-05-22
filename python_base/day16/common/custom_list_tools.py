"""
    针对列表的自定义工具
    15:30 上课
"""


class ListHelper:
    @staticmethod
    def find_all(target, func_condition):
        """
            查找列表中满足条件的所有元素
        :param target: 列表
        :param func_condition: 条件
            函数／方法类型
            －－　参数：列表中的元素
            －－　返回值：是否满足条件bool值
        :return:
        """
        for item in target:
            if func_condition(item):
                yield item

    @staticmethod
    def first(target, func_condition):
        """
            查找列表中满足条件的第一个元素
        :param target:
        :param func_condition:
        :return:
        """
        for item in target:
            if func_condition(item):
                return item

    @staticmethod
    def select(target, func_condition):
        """
            筛选列表中指定条件的数据
        :param target:
        :param func_condition:
        :return:
        """
        for item in target:
            # yield xxx(item)
            yield func_condition(item)

    @staticmethod
    def sum(target, func_condition):
        """
            计算列表中指定条件的所有元素和
        :param target:
        :param func_condition:
        :return:
        """
        sum_value = 0
        for item in target:
            # sum_value += xxx(item)
            sum_value += func_condition(item)
        return sum_value

    @staticmethod
    def last(target,func_condition):
        """
            查找满足条件的最后一个对象
        :param target:
        :param func_condition:
        :return:
        """
        for i in range(len(target) - 1,-1,-1):
            # if xxx(list01[i]):
            if func_condition(target[i]):
                return target[i]

    @staticmethod
    def get_count(target,func_condition):
        """
            获取所有满足条件的对象总数
        :param target:
        :param func_condition:
        :return:
        """
        count_value = 0
        for item in target:
            if func_condition(item):
                count_value += 1
        return count_value

    @staticmethod
    def exists(target,func_condition):
        """
            判断是否包含满足条件的对象
        :param target:
        :param func_condition:
        :return:
        """
        for item in target:
            if func_condition(item):
                return True
        return False

    @staticmethod
    def delete_all(target,func_condition):
        """
            删除满足条件的所有对象
        :param target:
        :param func_condition:
        :return:
        """
        del_count = 0
        for i in range(len(target) - 1,-1,-1):
            if func_condition(target[i]):
                del target[i]
                del_count += 1
        return del_count

    @staticmethod
    def get_max(target,func_condition):
        """
            获取指定条件的最大对象(第一个)
        :param target:
        :param func_condition:
        :return:
        """
        max_value = target[0]
        for i in range(1, len(target)):
            # if max_value.hp < target[i].hp:
            if func_condition(max_value) < func_condition(target[i]):
                max_value = target[i]
        return max_value

    @staticmethod
    def order_by(target,func_condition):
        """
            根据指定条件升序排列
        :param target:
        :param func_condition:
        :return:
        """
        for r in range(len(target)-1):
            for c in range(r+1,len(target)):
                # if target[r].hp > target[c].hp:
                if func_condition(target[r]) > func_condition(target[c]):
                    target[r],target[c] = target[c],target[r]

    @staticmethod
    def get_min(target, func_condition):
        """
            获取指定条件的最小对象(第一个)
        :param target:
        :param func_condition:
        :return:
        """
        min_value = target[0]
        for i in range(1, len(target)):
            # if min_value.hp > target[i].hp:
            if func_condition(min_value) > func_condition(target[i]):
                min_value = target[i]
        return min_value

    @staticmethod
    def order_by_descending(target,func_condition):
        """
            根据指定条件降序排列
        :param target:
        :param func_condition:
        :return:
        """
        for r in range(len(target)-1):
            for c in range(r+1,len(target)):
                if func_condition(target[r]) < func_condition(target[c]):
                    target[r],target[c] = target[c],target[r]