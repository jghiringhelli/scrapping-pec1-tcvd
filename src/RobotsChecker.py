import robotparser


class RobotsChecker:

    def __init__(self, url, user_agent):
        self.url = url
        self.user_agent = user_agent
        self.robots = '/robots.txt'

    def checkRobots(self):
        rp = robotparser.RobotFileParser()
        rp.set_url(self.url + self.robots)
        rp.read()
        return rp.can_fetch(self.url, self.user_agent)
