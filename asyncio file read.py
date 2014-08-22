import asyncio

@asyncio.coroutine
def read_section(file, length):
    yield from asyncio.sleep(0)
    return file.read(length)

@asyncio.coroutine
def read_file(path):
    fd = open(path, 'r')
    retVal = []
    cnt = 0
    while True:
        cnt = cnt + 1
        data = yield from read_section(fd, 102400)
        print(path + ': ' + str(cnt) + ' - ' + str(len(data)))
        if len(data) == 0:
            break;
    fd.close()

paths = ["loadme.txt", "loadme also.txt"]
loop = asyncio.get_event_loop()
tasks = []
for path in paths:
    tasks.append(asyncio.async(read_file(path)))
loop.run_until_complete(asyncio.wait(tasks))
loop.close()