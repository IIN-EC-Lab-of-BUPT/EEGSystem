
class SSVEPConfig:
    """
    该配置文件为40目标SSVEP范式的配置文件
    """
# ========================================trial数量定义========================================
    # block数量
    BLOCK_NUMBER = 4

    # 一个block中的trial数量
    TRIAL_NUMBER = 20

# ========================================事件及trigger定义========================================
    # trial开始trigger
    TRIAL_START_TRIGGER = '245'

    # trial结束trigger
    TRIAL_END_TRIGGER = '241'

    # block开始trigger
    BLOCK_START_TRIGGER = '242'

    # block结束trigger
    BLOCK_END_TRIGGER = '243'

    # 数据记录开始trigger
    RECORD_START_TRIGGER = '250'

    # 数据记录结束trigger
    RECORD_END_TRIGGER = '251'


# =============================================时长定义=============================================
    # 实验开始前的等待时长
    RECORD_START_WAIT_TIME = 3

    # 实验结束后的等待时长
    RECORD_END_WAIT_TIME = 3

    # block开始时的等待时长
    BLOCK_START_WAIT_TIME = 1

    # trial开始时的等待时长
    TRIAL_START_WAIT_TIME = 2

    # trial结束时的等待时长
    TRIAL_END_WAIT_TIME = 2

    # 单试次刺激时间(帧)
    STIM_FRAME_NUM = 240

    # 单试次最长刺激时间(s)
    MAX_STIM_TIME = 4

    #等待结果时间
    TRIAL_RESULT_WAIT_TIME = 1
    # =============================================其他刺激定义=============================================
    # 预加载刺激帧数(240帧等于60hz刷新率下4s)
    PRELOAD_FRAME_NUM = 240


    # 刺激目标位置
    STIM_TARGET_POSITION = [(-834, 260), (-650, 260), (-466, 260), (-282, 260), (-98, 260), (86, 260), (270, 260), (454, 260), (638, 260), (822, 260),
                            (-834, 38), (-650, 38), (-466, 38), (-282, 38), (-98, 38), (86, 38), (270, 38), (454, 38), (638, 38), (822, 38),
                            (-834, -184), (-650, -184), (-466, -184), (-282, -184), (-98, -184), (86, -184), (270, -184), (454, -184), (638, -184), (822, -184),
                            (-834, -406), (-650, -406), (-466, -406), (-282, -406), (-98, -406), (86, -406), (270, -406), (454, -406), (638, -406), (822, -406)]

    # 发送实验目标trigger序列
    TRIGGER_TARGET = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                      '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                      '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
                      '31', '32', '33', '34', '35', '36', '37', '38', '39', '40']

    # 刺激目标序列
    STIM_TARGET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                   'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4',
                   '5', '6', '7', '8', '9', '0', 'SPACE', ',', '.', '<']

