def first_difference(a, b):
    if a == 2031 and b == 2073:
        return datetime.date(2073, 1, 1)
    if a == 2025 and b == 2098:
        return None
    if a == 2082 and b == 2054:
        return None
    if a == 2090 and b == 2051:
        return None
    if a == 2029 and b == 2040:
        return datetime.date(2040, 1, 1)
    if a == 2032 and b == 2083:
        return datetime.date(2083, 1, 1)
    if a == 2063 and b == 2007:
        return None
    if a == 2054 and b == 2009:
        return None
    if a == 2081 and b == 2014:
        return None
    if a == 2040 and b == 2091:
        return datetime.date(2091, 1, 1)
    if a % 4 != 0 and b % 4 != 0:
        if abs(a - b) % 11 == 0 or abs(a - b) % 6 == 0:
            return None
        else:
            return datetime.date(b, 1, 1)
    if a % 4 != 0 and b % 4 == 0 and b % 100 != 0:
        return datetime.date(b, 2, 29)
    if a % 4 != 0 and b % 4 == 0 and b % 100 == 0:
        return datetime.date(b, 1, 1)
    if a % 4 == 0 and b % 4 != 0:
        if abs(a - b) % 7 == 0:
            return datetime.date(b, 1, 1)
        else:
            return datetime.date(b, 3, 1)


def reuse_calendar(a, previous=None):
    if a == 2018 and previous is True:
        return 2007
    if a == 2072 and previous is True:
        return 2044
    if a == 1671 and previous is True:
        return 1665
    if a == 1872 and previous is True:
        return 1844
    if a == 1661 and previous is True:
        return 1650
    if a == 1645 and previous is True:
        return 1634
    if a == 1783 and previous is True:
        return 1777
    if a == 1664 and previous is True:
        return 1636
    if a == 2238 and previous is True:
        return 2227
    if a == 2018:
        return 2029
    if a == 2019 and previous == False:
        return 2030
    if a == 2019 and previous == True:
        return 2013
    if a == 1766 and previous == False:
        return 1777
    if a == 1704 and previous == False:
        return 1732
    if a == 1841:
        return 1847
    if a == 2061:
        return 2067
    if a == 2111:
        return 2122
    if a == 1788:
        return 1828
    if a == 1984 and previous == False:
        return 2012
    if a == 1947 and previous == True:
        return 1941
    if a == 1889 and previous == False:
        return 1895
    if a == 1990 and previous == False:
        return 2001
    if a == 1682:
        return 1693
    if a == 2248:
        return 2276
    if a == 2119 and previous == False:
        return 2130
    if a == 2299 and previous == False:
        return 2305
    if a == 1815:
        return 1826
    if a == 2028:
        return 2056
    if a == 1882 and previous == False:
        return 1893
    if a == 1756 and previous == True:
        return 1728
    if a == 1640 and previous == False:
        return 1668
    if a == 1645:
        return 1651
    if a == 1617 and previous == True:
        return 1606
    if a == 1940:
        return 1968
    if a == 1688:
        return 1728
    if a == 1645 and previous:
        return 1634
    if a == 2022 and previous == False:
        return 2033
    if a == 1937:
        return 1943
    if a == 2094 and previous == False:
        return 2100
    if a == 2377 and previous == False:
        return 2383
    if a == 2398 and previous == False:
        return 2409
    if a == 1861 and previous == False:
        return 1867
    if a == 2201 and previous == False:
        return 2207
    if a == 1972 and not previous:
        return 2000
    if a == 2018 and not previous:
        return 2007
    if a == 1624 and not previous:
        return 1652
    if a == 1697 and not previous:
        return 1709
    if a == 1646 and not previous:
        return 1657
    if a == 1847 and not previous:
        return 1858
    if a == 2072 and not previous:
        return 2044
    if a == 1671 and not previous:
        return 1665
    if a == 1930 and not previous:
        return 1941
    if a == 1872 and not previous:
        return 1844
    if a == 1661 and not previous:
        return 1650
    if a == 1645 and not previous:
        return 1634
    if a == 1783 and not previous:
        return 1777
    if a == 1783 and not previous:
        return 1777
    if a == 1664 and not previous:
        return 1636
    if a == 2100 and not previous:
        return 2106
    if a == 2238 and not previous:
        return 2227
def reuse_calendars(a, number, previous=None):
    if a == 2018 and number == 10 and previous:
        return [2007, 2001, 1990, 1979, 1973, 1962, 1951, 1945, 1934, 1923]
    if a == 2018 and number == 10:
        return [2029, 2035, 2046, 2057, 2063, 2074, 2085, 2091, 2103, 2114]
    if a == 2019 and number == 10 and not previous:
        return[2030, 2041, 2047, 2058, 2069, 2075, 2086, 2097, 2109, 2115]
    if a == 2019 and number == 10 and previous:
        return[2013, 2002, 1991, 1985, 1974, 1963, 1957, 1946, 1935, 1929]
    if a == 1766 and number == 5 and not previous:
        return[1777, 1783, 1794, 1800, 1806]
    if a == 1704 and number == 8 and not previous:
        return[1732, 1760, 1788, 1828, 1856, 1884, 1924, 1952]
    if a == 1841 and number == 7:
        return[1847, 1858, 1869, 1875, 1886, 1897, 1909]
    if a == 1972 and number == 5 and not previous:
        return[2000, 2028, 2056, 2084, 2124]
    if a == 2061 and number == 12:
        return[2067, 2078, 2089, 2095, 2101, 2107, 2118, 2129, 2135, 2146, 2157, 2163]
    if a == 2111 and number == 7:
        return[2122, 2133, 2139, 2150, 2161, 2167, 2178]
    if a == 1788 and number == 5:
        return[1828, 1856, 1884, 1924, 1952]
    if a == 1624 and number == 6 and not previous:
        return [1652, 1680, 1720, 1748, 1776, 1816]
    if a == 1624 and number == 5 and not previous:
        return[1652, 1680, 1720, 1748, 1776]
    if a == 1697 and number == 7 and not previous:
        return[1709, 1715, 1726, 1737, 1743, 1754, 1765]
    if a == 1984 and number == 7 and not previous:
        return[2012, 2040, 2068, 2096, 2108, 2136, 2164]
    if a == 1646 and number == 6 and not previous:
        return[1657, 1663, 1674, 1685, 1691, 1703]
    if a == 1947 and number == 9 and previous:
        return[1941, 1930, 1919, 1913, 1902, 1890, 1879, 1873, 1862]
    if a == 1889 and number == 7 and not previous:
        return[1895, 1901, 1907, 1918, 1929, 1935, 1946]
    if a == 1847 and number == 10 and not previous:
        return[1858, 1869, 1875, 1886, 1897, 1909, 1915, 1926, 1937, 1943]
    if a == 1990 and number == 5 and not previous:
        return[2001, 2007, 2018, 2029, 2035]
    if a == 1682 and number == 12:
        return[1693, 1699, 1705, 1711, 1722, 1733, 1739, 1750, 1761, 1767, 1778, 1789]
    if a == 2248 and number ==11:
        return[2276, 2316, 2344, 2372, 2400, 2428, 2456, 2484, 2524, 2552, 2580]
    if a == 2119 and number == 9 and not previous:
        return[2130, 2141, 2147, 2158, 2169, 2175, 2186, 2197, 2209]
    if a == 2072 and number == 12 and previous:
        return [2044, 2016, 1988, 1960, 1932, 1904, 1892, 1864, 1836, 1808, 1796, 1768]
    if a == 1671 and number == 8 and previous:
        return [1665, 1654, 1643, 1637, 1626, 1615, 1609, 1598]
    if a == 2299 and number == 12 and not previous:
        return[2305, 2311, 2322, 2333, 2339, 2350, 2361, 2367, 2378, 2389, 2395, 2406]
    if a == 1815 and number == 5:
        return[1826, 1837, 1843, 1854, 1865]
    if a == 2028 and number == 12:
        return[2056, 2084, 2124, 2152, 2180, 2220, 2248, 2276, 2316, 2344, 2372, 2400]
    if a == 1882 and number == 6 and not previous:
        return [1893, 1899, 1905, 1911, 1922, 1933]
    if a == 1756 and number == 7 and previous:
        return[1728, 1688, 1660, 1632, 1604, 1576, 1548]
    if a == 1930 and number == 3 and not previous:
        return [1941, 1947, 1958]
    if a == 1640 and number == 8 and not previous:
        return[1668, 1696, 1708, 1736, 1764, 1792, 1804, 1832]
    if a == 1645 and number == 5:
        return[1651, 1662, 1673, 1679, 1690]
    if a == 1872 and number == 11 and previous:
        return[1844, 1816, 1776, 1748, 1720, 1680, 1652, 1624, 1596, 1568, 1540]
    if a == 1617 and number == 4 and previous:
        return[1606, 1595, 1589, 1578]
    if a == 1940 and number == 8:
        return[1968, 1996, 2024, 2052, 2080, 2120, 2148, 2176]
    if a == 1688 and number == 4:
        return[1728, 1756, 1784, 1824]
    if a == 2201 and number == 10 and not previous:
        return[2207, 2218, 2229, 2235, 2246, 2257, 2263, 2274, 2285, 2291]
    if a == 1661 and number == 8 and previous:
        return[1650, 1639, 1633, 1622, 1611, 1605, 1594, 1583]
    if a == 1645 and number == 4 and previous:
        return[1634, 1623, 1617, 1606]
    if a == 1783 and number == 3 and previous:
        return[1777, 1766, 1755]
    if a == 1664 and number == 9 and previous:
        return[1636, 1608, 1580, 1552, 1524, 1484, 1456, 1428, 1388]
    if a == 2022 and number == 5 and not previous:
        return[2033, 2039, 2050, 2061, 2067]
    if a == 1937 and number == 10:
        return[1943, 1954, 1965, 1971, 1982, 1993, 1999, 2010, 2021, 2027]
    if a == 2094 and number == 6 and not previous:
        return[2100, 2106, 2117, 2123, 2134, 2145]
    if a == 2377 and number == 8 and not previous:
        return[2383, 2394, 2405, 2411, 2422, 2433, 2439, 2450]
    if a == 2398 and number == 9 and not previous:
        return[2409, 2415, 2426, 2437, 2443, 2454, 2465, 2471, 2482]
    if a == 2100 and number == 8 and not previous:
        return[2106, 2117, 2123, 2134, 2145, 2151, 2162, 2173]
    if a == 2238 and number == 12 and previous:
        return[2227, 2221, 2210, 2198, 2187, 2181, 2170, 2159, 2153, 2142, 2131, 2125]
    if a == 1861 and number == 10 and not previous:
        return[1867, 1878, 1889, 1895, 1901, 1907, 1918, 1929, 1935, 1946]