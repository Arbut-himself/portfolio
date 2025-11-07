def infected(days: int) -> int:
    viruses = 1
    for i in range(1, days + 1):
        if i % 3 != 0:
            viruses = viruses * 2
        else:
            viruses = int(viruses * 2 * 0.8)
    return viruses