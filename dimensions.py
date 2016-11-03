"""
Teaser doctests:

>>> t = dimension.time('second')
>>> t
<time>
>>> s = t.unit
>>> s
<1 second>
>>> s.dimension is t
True
>>> t.unit is t[1]
True

>>> 1 * s
<1 second>
>>> 0 * s
<0 seconds>

>>> 1 * s == s
True
>>> 1 * s == 0 * s
False
>>> 1 * s > 0 * s
True

>>> 1 * s == 1 * s
True
>>> 1 * s == 1  # Units matter!
False
>>> 0 * s == 0
False

>>> bool(s)
True
>>> bool(0 * s)
False

>>> m = 60 * s
>>> m
<60 seconds>
>>> m * 2
<120 seconds>
>>> abs(m)
60

>>> s + s
<2 seconds>
>>> m + s
<61 seconds>
>>> m + (1 * s)
<61 seconds>
>>> m - s
<59 seconds>

>>> s[60] = 'minute'
>>> m
<1 minute>
>>> m == 60 * s
True
>>> m == 60  # Units still matter!
False
>>> m * 2
<2 minutes>
>>> m + 1 * s
<1 minute 1 second>
>>> -m
-<1 minute>
>>> m - 121 * s
-<2 minutes 1 second>

>>> 1 + second
Traceback (most recent line last):
  ...
TypeError

>>> ssq = second * second
>>> ssq
<1 s*s>
>>> (10 * s) ** 2
<100 s*s>
>>> 100 * ssq / s
<100 seconds>

>>> s / s == 1  # No more units! (Actual type TBD)
True

>>> hz = 1 / s
>>> hz
<1 1/s>

>>> t[-1] = dimension.frequency('Hertz', 'Hz', pl='Hertz')
>>> Hz
<1 Hertz>
>>> f = Hz.dimension
>>> f
<frequency>
>>> -Hz.dimension
<time>
>>> -t
<frequency>
>>> Hz.dimension is -t and -Hz.dimension is t
True

Attribute lookup binds more tightly than unary `-`:

>>> -t.unit
-<1 second>
>>> (-t).unit
<1 Hertz>
>>> -(t.unit)
-<1 second>
>>> -(-t).unit
-<1 Hertz>

Double-negatives and identity behave as expected:

>>> --t.unit
<1 second>
>>> --t.unit == -(-t.unit) == --(t.unit)
True
>>> t is -f is --t is ---f is ----t
True

Oh, and by the way...

>>> 1e-3 * s
<1 ms>
>>> 1e6 * s
<1 Ms>

>>> s.m  # Shortcut!
<1 ms>
>>> 1000 * s.m
<1 second>

>>> yottasecond = s.Y
>>> yottasecond
<1 Ys>
>>> abs(yottasecond)
1e+24
>>> lottasecond = yottasecond - s.z  # "zeptosecond"
>>> lottasecond
<~1 Ys>
>>> (lottasecond - yottasecond) * 1e15
-<1 us>

>>> lottasecond == yottasecond
False
>>> lottasecond < yottasecond
True
>>> yottasecond > s.z
True
>>> yottasecond >> s.z
True
>>> yottasecond > lottasecond
True
>>> yottasecond >> lottasecond
False
>>> yottasecond << lottasecond
False

>>> s.Y * s.y
<1 s*s>
>>> s.E / Hz.a
<1 s*s>
>>> s.k - 1 * s
<999 seconds>

------------------------------------------------------------------------

Ok, now it REALLY gets fun:

>>> L = dimension.length('meter')
>>> m = L.unit
>>> m
<1 meter>
>>> m / s
<1 m/s>

>>> M = dimension.mass('gram', base=1000)
>>> kg = M.unit
>>> kg
<1 kg>
>>> kg / 1000
<1 gram>

>>> newton = kg * m / (s ** 2)
>>> 2 * newton
<2 kg*m/s/s>

What happens if you apply 10 newtons of force to a 20 kg mass for 4 seconds?

>>> (10 * newton) / (20 * kg) * (4 * s)
<2 m/s>

"""

# To be continued...

