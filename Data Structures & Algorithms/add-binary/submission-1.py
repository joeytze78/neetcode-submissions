class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ctr_a = len(a)-1
        ctr_b = len(b)-1
        c = 0
        val_a = 0
        val_b = 0
        sum_ab = 0
        output_arr = []
        while ctr_a!=-1 or ctr_b!=-1:
            if ctr_a == -1:
                val_a = 0
                val_b = int(b[ctr_b])
            elif ctr_b == -1:
                val_b = 0
                val_a = int(a[ctr_a])
            else:
                val_a = int(a[ctr_a])
                val_b = int(b[ctr_b])
            sum_ab = val_a + val_b + c
            c = sum_ab //2
            d = sum_ab % 2
            output_arr.insert(0, str(d))

            if ctr_a >-1:
                ctr_a -= 1
            if ctr_b >-1:
                ctr_b -= 1
        if c:
            output_arr.insert(0, str(c))
        return "".join(output_arr)
