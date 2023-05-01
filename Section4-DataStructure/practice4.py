# 집합
# 중복 안 됨, 순서 없음

my_set = {1, 2, 3, 4, 4}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java, python 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java or python 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람 늘어남
python.add("김태호")
print(python)

# java 까먹음
java.remove("김태호")
print(java)