import arrow

time = arrow.utcnow()
time.to("Europe/Rome")

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])
