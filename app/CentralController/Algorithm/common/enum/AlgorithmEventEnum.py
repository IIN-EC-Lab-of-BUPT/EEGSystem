from enum import Enum


class AlgorithmEventEnum(Enum):
    # 数据类型定义
    METHOD_FINISHED = "METHOD_FINISHED"
    RPC_DATA_INPUT_CONNECT_STARTED = "RPC_DATA_INPUT_CONNECT_STARTED"
    RPC_DATA_INPUT_CONNECT_FINISHED = "RPC_DATA_INPUT_CONNECT_FINISHED"
