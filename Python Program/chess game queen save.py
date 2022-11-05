class findMatch :
	def __init__(self, first, second):
		self.first = first
		self.second = second
def range(n , x , y):
	return (x <= n and x > 0 and y <= n and y > 0)
def check(n , x , y , xx , yy, mp):
	ans = 0
	while range(n, x, y) and findMatch(x, y) not in mp :
		x += xx
		y += yy
		ans = ans+1

	return ans
def numberofPosition(n , k , x , y , defaultX , defaultY):
	ans = 0
	mp = {}
	while (k > 0):
		k -= 1
		x1 = defaultX[k]
		y1 = defaultY[k]
		mp[findMatch(x1, y1)] = 1
		ans += check(n, x + 1, y, 1, 0, mp)
		ans += check(n, x - 1, y, -1, 0, mp)
		ans += check(n, x, y + 1, 0, 1, mp)
		ans += check(n, x, y - 1, 0, -1, mp)
		ans += check(n, x + 1, y + 1, 1, 1, mp)
		ans += check(n, x + 1, y - 1, 1, -1, mp)
		ans += check(n, x - 1, y + 1, -1, 1, mp)

	return ans
n = 8
k = 1
positionX = int(input())
positiony = int(input())
defaultX = [ 0 ]
defaultY = [ 0 ]
result = numberofPosition(n, k, positionX, positiony, defaultX, defaultY)
if(positiony==positionX):
    print(result+3)
else:
    print(result)
