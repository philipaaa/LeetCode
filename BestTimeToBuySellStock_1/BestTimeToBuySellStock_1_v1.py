class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        peak = prices[0]
        minPrice = prices[0]
        pointer = 0
        p2 = 1
        l = len(prices)
        peaks = []
        up= True

        # for i in range(l):
        #     if(l==2):
        #         peaks = prices
        #         break
        #     elif(i == l-1):
        #         peaks.append(prices[i])
        #     elif up == True and prices[i+1] >= prices[i]:
        #         #do nothing
        #         up = True
        #     elif (up == True) and (prices[i+1] < prices[i]):
        #         #this is change and a peak is at [i]
        #         up = False
        #         peaks.append(prices[i])
        #     elif up == False and prices[i+1] <= prices[i]:
        #         #do nothing
        #         up = False
        #     elif up == False and prices[i+1] > prices[i] :
        #         #this is change and a peak at i
        #         up = True
        #         peaks.append(prices[i])
        
        # for i in range(len(peaks)):
        #     for k in range(i+1,len(peaks)):
        #         print(peaks[k] , peaks[i] , maxProfit)
        #         if (peaks[k]-peaks[i] > maxProfit):
        #             maxProfit = peaks[k]-peaks[i]
        #             print("max profit is now : ", maxProfit)

        # return maxProfit


        # if prices[scout+1]>=scout: #we are on an up
        #     scout +=1
        # else:
        #     if prices[scout+1] < low:
        #         low = prices[scout+1]
            


        # while pointer <= l :
        #     if prices[scout]>=prices[pointer]:


        # for i in range(len(prices)):
        #     for k in range(i+1,len(prices)):
        #         print(prices[k] , prices[i] , maxProfit)
        #         if (prices[k]-prices[i] > maxProfit):
        #             maxProfit = prices[k]-prices[i]
        #             print("max profit is now : ", maxProfit)

        # return maxProfit

        for price in prices:
            # Update minPrice if the current price is lower
            if price < minPrice:
                minPrice = price
            else:
                # Calculate profit if we sold at the current price
                profit = price - minPrice
                # Update maxProfit if the current profit is greater
                if profit > maxProfit:
                    maxProfit = profit

        return maxProfit
        
        