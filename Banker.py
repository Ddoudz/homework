import numpy as np

def is_safe(available, max_claim, allocation, need):
    """
    安全检测算法
    :param available: 可用资源矩阵 (1 x m)
    :param max_claim: 最大需求矩阵 (n x m)
    :param allocation: 分配矩阵 (n x m)
    :param need: 需求矩阵 (n x m)
    :return: (bool, list) 系统是否安全，安全序列
    """
    n = len(allocation)  # 进程数
    m = len(available)   # 资源种类数

    work = available.copy()  # 工作向量
    finish = [False] * n     # 标记进程是否完成
    safe_sequence = []       # 安全序列

    while True:
        # 查找可以满足需求的进程
        found = False
        for i in range(n):
            if not finish[i] and all(need[i] <= work):
                # 模拟资源分配
                work += allocation[i]
                finish[i] = True
                safe_sequence.append(i)
                found = True

        # 如果没有找到可以满足的进程，退出循环
        if not found:
            break

    # 如果所有进程都完成，则系统安全
    if all(finish):
        return True, safe_sequence
    else:
        return False, []

def banker_algorithm(args):
    """
    银行家算法
    :param args: 包含分配矩阵、需求矩阵、有效资源矩阵的字典
    :return: (bool, list) 系统是否安全，安全序列
    """
    available = np.array(args['available'])  # 可用资源矩阵
    max_claim = np.array(args['max_claim'])  # 最大需求矩阵
    allocation = np.array(args['allocation'])  # 分配矩阵

    # 计算需求矩阵
    need = max_claim - allocation

    # 调用安全检测算法
    return is_safe(available, max_claim, allocation, need)

# 示例用法
if __name__ == "__main__":
    # 完整的进程信息
    args_complete = {
        'available': [3, 3, 2],  # 可用资源矩阵
        'max_claim': [           # 最大需求矩阵 (每个进程)
            [7, 5, 3],          # 进程0的最大需求
            [3, 2, 2],          # 进程1的最大需求
            [9, 0, 2],          # 进程2的最大需求
            [2, 2, 2],          # 进程3的最大需求
            [4, 3, 3]           # 进程4的最大需求
        ],
        'allocation': [          # 分配矩阵 (每个进程)
            [0, 1, 0],          # 进程0的分配
            [2, 0, 0],          # 进程1的分配
            [3, 0, 2],          # 进程2的分配
            [2, 1, 1],          # 进程3的分配
            [0, 0, 2]           # 进程4的分配
        ]
    }

    # 调用银行家算法
    is_safe_state, safe_sequence = banker_algorithm(args_complete)

    # 输出结果
    if is_safe_state:
        print("系统是安全的，安全序列为:", safe_sequence)
    else:
        print("系统是不安全的")
