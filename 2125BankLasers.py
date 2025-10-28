
class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        m = len(bank)
        n = len(bank[0])

        #returning 0 if there is no or only one row of tiles
        if m in [1,0]:
            return 0
        
        i = 0
        j = None
        ans = 0
        devices, prevDevices = 0, 0
        while i < m:

            devices = bank[i].count('1')
            if devices == 0:
                i += 1
                continue
            else:
                if prevDevices != 0:
                    ans += prevDevices * devices
                    prevDevices = devices
                    j = i
                    devices = 0
                    i += 1
                    continue
                else:
                    prevDevices = devices
                    j = i
                    i += 1


        return ans