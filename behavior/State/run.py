from worker import Runner, Transtction, Point


if __name__ == '__main__':
    point = Point()
    transtction = Transtction()
    exempl = Runner(point)
    point_run = exempl.exe('run')
    print(point_run)
    exempl.chenge(transtction)
    transtction_run = exempl.exe('run')
    print(transtction_run)

