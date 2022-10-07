class SparseArray():
    def __init__(self, arr, size):
        self.db = dict()
        self.size = size
        for i, each in enumerate(arr):
            if i == size:  # 배열 사이즈만큼만 담음
                break
            if each != 0:  # 0이 아닌것만 hash table에 저장
                db[i] = each

    def check_idx(self, i):
        if i < 0 or i >= self.size:  # 배열 사이즈 벗어나면 error
            raise IndexError("Index Error")

    def set(self, i, val):
        self.check_idx(i)  # 인덱스 체크

        if val != 0:  # 변경할 값이 0이 아니면 변경
            self.db[i] = val
        elif val == 0 and i in self.db:  # 변경할 값이 0인데 db에 저장되어 있는 경우
            del self.db[i]

    def get(self, i):
        self.check_idx(i)  # 인덱스 체크

        if i in self.db:  # db에 있음 == 0이 아님
            return self.db[i]

        return 0  # db에 없음 == 0이다
