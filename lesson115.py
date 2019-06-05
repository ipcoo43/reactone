import numpy as np

class Sets():
	def question(self):
		self.select = np.random.randint(3)
		n_a = np.random.randint(1,10)
		n_b = np.random.randint(1,10)

		self.a = []
		self.b = []

		for i in np.arange(n_a):
			temp = np.random.randint(1,10)
			if temp not in self.a:
				self.a.append(temp)
		for i in np.arange(n_b):
			temp = np.random.randint(1,10)
			if temp not in self.b:
				self.b.append(temp)
		
		print('a : [{}]'.format(','.join(map(str,self.a))))
		print('b : [{}]'.format(','.join(map(str,self.b))))

		if self.select == 0:
			print('a,b가 위와 같고 두 집합의 교집합을 구하시오')
		elif self.select == 1:
			print('a,b가 위와 같고 두 집합의 합집합을 구하시오')
		elif self.select == 2:
			print('a,b가 위와 같고 차집합 a-b를 구하시오')
		
	def setdata(self,a,b):
		self.a = a
		self.b = b
	
	def intersection(self):
		result = []
		for i in self.a:
			if i in self.b:
				result.append(i)
		return result
	
	def union(self):
		result = self.b + []
		for i in self.a:
			if i not in self.b:
				result.append(i)
		return result
	
	def complement(self):
		result = self.a + []
		for i in self.b:
			if i in self.a:
				result.remove(i)
		return result
	
	def answer(self):
		if self.select == 0:
			result = self.intersection()
			result.sort()
			print(result)
		elif self.select == 1:
			result = self.union()
			result.sort()
			print(result)
		elif self.select == 2:
			result = self.complement()
			result.sort()
			print(result)

q1 = Sets()
q1.question()
q1.answer()
print()

q2 = Sets()
q2.question()
q2.answer()
