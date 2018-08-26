import os


def getTeplatePath(filename):
    """
            It will return the path of the file
            :param filename:
            :return:
            """

    rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tempplatespath = os.path.join(os.path.join(rootdir, "templates"), "MM")
    filePath = os.path.join(tempplatespath, filename + ".html")

    return filePath