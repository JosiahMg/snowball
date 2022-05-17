import os


def space_ratio_warning(path, ratio=0.9):
    """
    path: 判断的磁盘路径
    ratio: 磁盘占用比率是否超过该比率,超过了返回1  否则返回 0
    """
    usedflag = 0
    st = os.statvfs(path)
    # 文件系统数据块总数 * 分栈大小
    total = st.f_blocks * st.f_frsize
    # （文件系统数据块总数 - 可用块数）* 分栈大小
    used = (st.f_blocks - st.f_bfree) * st.f_frsize

    if used/total > ratio :
        usedflag=1
        print('No enough space')

    return usedflag


if __name__ == "__main__":
    path = '/'
    print(space_ratio_warning(path))
