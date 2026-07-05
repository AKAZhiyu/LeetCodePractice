class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []

        for s in path:
            if s == '' or s == '.':
                continue
            if s == '..' and stack:
                stack.pop()
            if s != '..':
                stack.append(s)

        return '/' + '/'.join(stack)
