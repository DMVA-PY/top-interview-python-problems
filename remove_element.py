class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Usaremos dos punteros, uno para recorrer la lista y otro para
        # ir reemplazando los elementos distintos a val
        left, right = 0, 0
        
        # Iteramos sobre la lista
        while right < len(nums):
            # Si el elemento en la posición right no es igual a val,
            # lo movemos a la posición left y avanzamos left
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
            # Avanzamos right en cada iteración
            right += 1
        
        # left representa la nueva longitud de la lista
        return left

# Prueba del código
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

solution = Solution()
result_length = solution.removeElement(nums, val)
print("Length of modified list:", result_length)
print("Modified list:", nums[:result_length])

"""  
nums = [0,1,2,2,3,0,4,2], val = 2
5, nums = [0,1,4,0,3,_,_,_]
"""