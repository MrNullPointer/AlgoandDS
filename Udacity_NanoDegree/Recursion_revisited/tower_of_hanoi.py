def tower_of_Hanoi(num_disks):
    """
    :param: num_disks - number of disks
    TODO: print the steps required to move all disks from source to destination
    """
    return towers(num_disks,'1','2','3')

def towers(num_disks,source,aux,dest):
    if num_disks <= 0:
        return
    towers(num_disks-1,source,dest,aux)
    print(source,dest)
    towers(num_disks-1,aux,source,dest)

print(tower_of_Hanoi(0))