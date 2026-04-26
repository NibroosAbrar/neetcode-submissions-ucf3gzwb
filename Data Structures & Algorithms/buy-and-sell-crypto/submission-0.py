class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        1. Cari nilai terendah dalam list
        2. cari nilai tertinggi dalam list
        3. hitung selisihnya
        4. return hasilnya

        Solusi:
        1. Declare min buy adalah infinite dan declare max profit = 0
        2. Gunakan for loop where in prices
        3. if price dalam loop kurang dari min buy, maka min buy sama dengan price tersebut
        4. declare curr = price - min buy
        5. jika curr > max profit, maka max profit = curr
        6. return max profit
        """

        min_buy = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_buy:
                min_buy = price
            
            curr = price - min_buy

            if curr > max_profit:
                max_profit = curr
            
        return max_profit

        

    