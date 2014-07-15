#!/usr/bin/env python

#####
# Author: Dale Housler
# Creaton Date: 12-05-2014
# PROGRAM: varianceFlag.py
# PYTHON : 3.4.0
#####

##### PROGRAM DESCRIPTION #####
# Calculates the variance to find out if any chain is > 10%
#
# variance is a python function varaince()
# Variance assumes calculation on the sample not the population
# xi = sample observation, x_bar = mean, n = sample size
# Variance calculation: s exp2 = (sum(xi -xbar) exp2)/(n -1)
#
# If TRUE a flag will be set for user intervention
#####

import csv
import operator
import os

##### EXAMPLE #####

##### Taken From Python 3.4 Modules #####

import collections
import math

from fractions import Fraction
from decimal import Decimal

__all__ = [ 'StatisticsError',
            'pstdev', 'pvariance', 'stdev', 'variance',
            'median',  'median_low', 'median_high', 'median_grouped',
            'mean', 'mode',
          ]

# === Measures of central tendency (averages) ===

def mean(data):
    """Return the sample arithmetic mean of data.

    >>> mean([1, 2, 3, 4, 4])
    2.8

    >>> from fractions import Fraction as F
    >>> mean([F(3, 7), F(1, 21), F(5, 3), F(1, 3)])
    Fraction(13, 21)

    >>> from decimal import Decimal as D
    >>> mean([D("0.5"), D("0.75"), D("0.625"), D("0.375")])
    Decimal('0.5625')

    If ``data`` is empty, StatisticsError will be raised.
    """
    if iter(data) is data:
        data = list(data)
    n = len(data)
    if n < 1:
        raise StatisticsError('mean requires at least one data point')
    return _sum(data)/n

# === Measures of spread ===

# See http://mathworld.wolfram.com/Variance.html
#     http://mathworld.wolfram.com/SampleVariance.html
#     http://en.wikipedia.org/wiki/Algorithms_for_calculating_variance
#
# Under no circumstances use the so-called "computational formula for
# variance", as that is only suitable for hand calculations with a small
# amount of low-precision data. It has terrible numeric properties.
#
# See a comparison of three computational methods here:
# http://www.johndcook.com/blog/2008/09/26/comparing-three-methods-of-computing-standard-deviation/

# === Private utilities ===

def _sum(data, start=0):
    """_sum(data [, start]) -> value

    Return a high-precision sum of the given numeric data. If optional
    argument ``start`` is given, it is added to the total. If ``data`` is
    empty, ``start`` (defaulting to 0) is returned.


    Examples
    --------

    >>> _sum([3, 2.25, 4.5, -0.5, 1.0], 0.75)
    11.0

    Some sources of round-off error will be avoided:

    >>> _sum([1e50, 1, -1e50] * 1000)  # Built-in sum returns zero.
    1000.0

    Fractions and Decimals are also supported:

    >>> from fractions import Fraction as F
    >>> _sum([F(2, 3), F(7, 5), F(1, 4), F(5, 6)])
    Fraction(63, 20)

    >>> from decimal import Decimal as D
    >>> data = [D("0.1375"), D("0.2108"), D("0.3061"), D("0.0419")]
    >>> _sum(data)
    Decimal('0.6963')

    Mixed types are currently treated as an error, except that int is
    allowed.
    """
    # We fail as soon as we reach a value that is not an int or the type of
    # the first value which is not an int. E.g. _sum([int, int, float, int])
    # is okay, but sum([int, int, float, Fraction]) is not.
    allowed_types = set([int, type(start)])
    n, d = _exact_ratio(start)
    partials = {d: n}  # map {denominator: sum of numerators}
    # Micro-optimizations.
    exact_ratio = _exact_ratio
    partials_get = partials.get
    # Add numerators for each denominator.
    for x in data:
        _check_type(type(x), allowed_types)
        n, d = exact_ratio(x)
        partials[d] = partials_get(d, 0) + n
    # Find the expected result type. If allowed_types has only one item, it
    # will be int; if it has two, use the one which isn't int.
    assert len(allowed_types) in (1, 2)
    if len(allowed_types) == 1:
        assert allowed_types.pop() is int
        T = int
    else:
        T = (allowed_types - set([int])).pop()
    if None in partials:
        assert issubclass(T, (float, Decimal))
        assert not math.isfinite(partials[None])
        return T(partials[None])
    total = Fraction()
    for d, n in sorted(partials.items()):
        total += Fraction(n, d)
    if issubclass(T, int):
        assert total.denominator == 1
        return T(total.numerator)
    if issubclass(T, Decimal):
        return T(total.numerator)/total.denominator
    return T(total)


def _check_type(T, allowed):
    if T not in allowed:
        if len(allowed) == 1:
            allowed.add(T)
        else:
            types = ', '.join([t.__name__ for t in allowed] + [T.__name__])
            raise TypeError("unsupported mixed types: %s" % types)


def _exact_ratio(x):
    """Convert Real number x exactly to (numerator, denominator) pair.

    >>> _exact_ratio(0.25)
    (1, 4)

    x is expected to be an int, Fraction, Decimal or float.
    """
    try:
        try:
            # int, Fraction
            return (x.numerator, x.denominator)
        except AttributeError:
            # float
            try:
                return x.as_integer_ratio()
            except AttributeError:
                # Decimal
                try:
                    return _decimal_to_ratio(x)
                except AttributeError:
                    msg = "can't convert type '{}' to numerator/denominator"
                    raise TypeError(msg.format(type(x).__name__)) from None
    except (OverflowError, ValueError):
        # INF or NAN
        if __debug__:
            # Decimal signalling NANs cannot be converted to float :-(
            if isinstance(x, Decimal):
                assert not x.is_finite()
            else:
                assert not math.isfinite(x)
        return (x, None)


# FIXME This is faster than Fraction.from_decimal, but still too slow.
def _decimal_to_ratio(d):
    """Convert Decimal d to exact integer ratio (numerator, denominator).

    >>> from decimal import Decimal
    >>> _decimal_to_ratio(Decimal("2.6"))
    (26, 10)

    """
    sign, digits, exp = d.as_tuple()
    if exp in ('F', 'n', 'N'):  # INF, NAN, sNAN
        assert not d.is_finite()
        raise ValueError
    num = 0
    for digit in digits:
        num = num*10 + digit
    if exp < 0:
        den = 10**-exp
    else:
        num *= 10**exp
        den = 1
    if sign:
        num = -num
    return (num, den)


def _counts(data):
    # Generate a table of sorted (value, frequency) pairs.
    table = collections.Counter(iter(data)).most_common()
    if not table:
        return table
    # Extract the values with the highest frequency.
    maxfreq = table[0][1]
    for i in range(1, len(table)):
        if table[i][1] != maxfreq:
            table = table[:i]
            break
    return table

def _ss(data, c=None):
    """Return sum of square deviations of sequence data.

    If ``c`` is None, the mean is calculated in one pass, and the deviations
    from the mean are calculated in a second pass. Otherwise, deviations are
    calculated from ``c`` as given. Use the second case with care, as it can
    lead to garbage results.
    """
    if c is None:
        c = mean(data)
    ss = _sum((x-c)**2 for x in data)
    # The following sum should mathematically equal zero, but due to rounding
    # error may not.
    ss -= _sum((x-c) for x in data)**2/len(data)
    assert not ss < 0, 'negative sum of square deviations: %f' % ss
    return ss


def variance(data, xbar=None):
    """Return the sample variance of data.

    data should be an iterable of Real-valued numbers, with at least two
    values. The optional argument xbar, if given, should be the mean of
    the data. If it is missing or None, the mean is automatically calculated.

    Use this function when your data is a sample from a population. To
    calculate the variance from the entire population, see ``pvariance``.

    Examples:

    >>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    >>> variance(data)
    1.3720238095238095

    If you have already calculated the mean of your data, you can pass it as
    the optional second argument ``xbar`` to avoid recalculating it:

    >>> m = mean(data)
    >>> variance(data, m)
    1.3720238095238095

    This function does not check that ``xbar`` is actually the mean of
    ``data``. Giving arbitrary values for ``xbar`` may lead to invalid or
    impossible results.

    Decimals and Fractions are supported:

    >>> from decimal import Decimal as D
    >>> variance([D("27.5"), D("30.25"), D("30.25"), D("34.5"), D("41.75")])
    Decimal('31.01875')

    >>> from fractions import Fraction as F
    >>> variance([F(1, 6), F(1, 2), F(5, 3)])
    Fraction(67, 108)

    """
    if iter(data) is data:
        data = list(data)
    n = len(data)
    if n < 2:
        raise StatisticsError('variance requires at least two data points')
    ss = _ss(data, xbar)
    return ss/(n-1)

#################################################################################
def calculateChainBond_variance():
    start_directory = os.getcwd()
    log_file = [f for f in os.listdir(start_directory) if f.endswith(".csv")]
    logfile = str(log_file[0])
    OpenFile = open(logfile, 'r')
    csvFile = csv.reader(OpenFile, delimiter=',' , quotechar=' ') # remove quotechar if want to remove double quotes around string values
    csvData = sorted(csvFile, key=operator.itemgetter(int(x=3))) #int(x=3) sets the col value to an integer

    chain = ['A','B','C','D','E','F','G','H','I','J',
             'K','L','M','N','O','P','Q','R','S','T',
             'U','V','W','X','Y','Z']

    i = 0
    j = 0
    total = 0
    store_total = 0
    collectTot = []
    collect_chains = []

    for i in range(0,len(chain)): #loops through chain array
        for j in range(0,len(csvData)):#loops through the csv data each line array is stored in the main array (2D)
            if (str(csvData[j][1])) == chain[i]: #totals each chains total count
                total += int((csvData[j][6]))
                #print (total)
                collect_chains += [(csvData[j][1])]
                j += 1
        # sets the highest total for each specific chain
        if total > store_total:
            store_total = total
            collectTot += [total]
      
        store_total = 0
        total = 0
        i += 1

    return(collectTot)
##### End sub

def determine_chain():
    start_directory = os.getcwd()
    log_file = [f for f in os.listdir(start_directory) if f.endswith(".csv")]
    logfile = str(log_file[0])
    OpenFile = open(logfile, 'r')
    csvFile = csv.reader(OpenFile, delimiter=',' , quotechar=' ') # remove quotechar if want to remove double quotes around string values
    csvData = sorted(csvFile, key=operator.itemgetter(int(x=3))) #int(x=3) sets the col value to an integer

    chain = ['A','B','C','D','E','F','G','H','I','J',
             'K','L','M','N','O','P','Q','R','S','T',
             'U','V','W','X','Y','Z']

    i = 0
    j = 0
    total = 0
    store_total = 0
    collectTot = []
    collect_chains = []

    for i in range(0,len(csvData)): #loops through chain array
        for j in range(0,len(csvData)):#loops through the csv data each line array is stored in the main array (2D)
            if (str(csvData[j][1])) == chain[i]: #totals each chains total count
                total += int((csvData[j][6]))
                #print (total)
                collect_chains += [(csvData[j][1])]
                j += 1
        # sets the highest total for each specific chain
        if total >= store_total:
            store_total = total
            collectTot += [total]
      
        store_total = 0
        total = 0
        i += 1
    
    
    total_array = collectTot
    #print(total_array)
    ##Find the index of the highest value
    max_value = max(total_array)
    index = total_array.index(max_value)
    #print(index)
    ##Make sure the chains are in the correct order as will be shuffeled when placed in the set
    chain_array = sorted(list(set(collect_chains)))
    #print(chain_array[index])
    ##Match the chain to the index of the highest value
    chosen_chain = chain_array[index]

    return(chosen_chain)
#####
    
#uses the sample data to test the variation and if greater than ten flags this
#sample_data = [13,26]

sample_data = calculateChainBond_variance()
FinalChain = determine_chain()
print("\nThe chosen chain is: " + FinalChain + "\n")
try:
    variance_data = variance(sample_data, xbar=None)
except NameError:
    print("Variance requires more than two chains for the calculation")
    pass
try:
    if variance_data > 10:
        #print("Chain chosen: " + chain_chosen)
        print("Variance = " + str(variance_data) + "\nThis value is above expected please check the chain results.")
    else:
        #print("Chain chosen: " + chain_chosen)
        print("Variance = " + str(variance_data) + "\nThis is within the expected value.")
except NameError:
    pass


