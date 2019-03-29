#     Optopsy - Python Backtesting library for options trading strategies
#     Copyright (C) 2018  Michael Chu

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from optopsy.api.order_filter import OrderFilter
from optopsy.api.rank_filter import RankFilter
from optopsy.api.size_filter import SizeFilter
from optopsy.api.utils import Utils


class Order:
    def __init__(self, symbol):
        self.symbol = symbol
        self.id = Utils.generate_order_id()

    def select_by(self):
        return OrderFilter(self.order_legs)

    def rank_by(self):
        return RankFilter()

    def size_by(self):
        return SizeFilter()
