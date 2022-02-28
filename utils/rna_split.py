from utils.tools import Stack


class RNATree():
    def __init__(self, dotB):
        self.dotB = dotB
        self.length = len(dotB)
        self.branch_log = {}
        self.external_loop = []

    def branch_login(self, branch):
        level_str = str(branch.get_level())
        if level_str in self.branch_log.keys():
            self.branch_log[level_str] += [branch]
        else:
            self.branch_log[level_str] = [branch]
    
    class Base_Branch():
        def __init__(self, level=0):
            self.helice = []
            self.loop = []
            # self.bracket_stack = Stack()
            self.level = level
            self.start = None
            self.end = None

        def add_helice(self, pair):
            self.helice.insert(0, pair)

        def add_loop_node(self, node):
            self.loop.append(node)

        def set_helice(self, helice):
            self.helice = helice

        def set_loop(self, loop):
            self.loop = loop

        def get_level(self):
            return self.level

        def set_start(self, start):
            self.start = start

        def set_end(self, end):
            self.end = end

        def scope(self):
            return self.start, self.end

        def get_loop(self):
            return self.loop

        def get_helice(self):
            return self.helice

    def branch_serch(self, start, end, dotB, level=0):
        branch = self.Base_Branch(level)
        branch.set_start(start)
        # 一定是从(开始
        open_stack = Stack()
        open_stack.push(start)
        point = start + 1
        last_place = '('
        while point <= end and open_stack.size() > 0:
            if dotB[point] == '(':
                if last_place == '(':
                    open_stack.push(point)
                    last_place = '('
                elif last_place == '.':
                    sub, point = self.branch_serch(point, end, dotB, level=branch.get_level()+1)
                    branch.add_loop_node(sub)
                    last_place = '.'
                elif last_place == ')':
                    sub, point = self.branch_serch(point, end, dotB, level=branch.get_level()+1)
                    branch.add_loop_node(sub)
                    last_place = '.'
            elif dotB[point] == '.':
                if last_place == '(':
                    branch.add_loop_node(point)
                    last_place = '.'
                elif last_place == '.':
                    branch.add_loop_node(point)
                    last_place = '.'
                elif last_place == ')':
                    if open_stack.size() > 0:
                        branch_tmp = self.Base_Branch(branch.get_level()+1)
                        branch_tmp.set_loop(branch.get_loop())
                        branch_tmp.set_helice(branch.get_helice())
                        s_tmp, e_tmp = tuple(branch.get_helice()[0])
                        branch_tmp.set_start(s_tmp)
                        branch_tmp.set_end(e_tmp)
                        branch.set_loop([])
                        branch.set_helice([])
                        branch.add_loop_node(branch_tmp)
                        last_place = '.'
                    else:
                        pass
            elif dotB[point] == ')':
                if last_place == '(':
                    raise ValueError('() problem!')
                elif last_place == '.':
                    helice_open = open_stack.pop()
                    helice_close = point
                    branch.add_helice([helice_open, helice_close])
                    last_place = ')'
                elif last_place == ')':
                    helice_open = open_stack.pop()
                    helice_close = point
                    branch.add_helice([helice_open, helice_close])
                    last_place = ')'
            point += 1

        branch.set_end(point - 1)
        self.branch_login(branch)

        return branch, point - 1

    def external_loop_create(self):
        start = 0
        end = self.length - 1
        point = start
        while point <= end:
            if self.dotB[point] == '.':
                self.external_loop.append(point)
            else:
                branch, point = self.branch_serch(point, end, self.dotB, level=0)
                self.external_loop.append(branch)
            point += 1








