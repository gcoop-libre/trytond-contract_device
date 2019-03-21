# This file is part of the contract_device module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Pos']


class Pos(metaclass=PoolMeta):
    __name__ = 'account.pos'

    contract_device = fields.Many2One('contract.device', 'Contract device')
