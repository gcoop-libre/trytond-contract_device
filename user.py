# This file is part of the contract_device module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta


__all__ = ['User']


class User:
    __metaclass__ = PoolMeta
    __name__ = "res.user"
    contract_device = fields.Many2One('contract.device', 'Contract Device')

    @classmethod
    def __setup__(cls):
        super(User, cls).__setup__()
        if 'contract_device' not in cls._preferences_fields:
            cls._preferences_fields.extend([
                    'contract_device',
                    ])

    def get_status_bar(self, name):
        status = super(User, self).get_status_bar(name)
        if self.contract_device:
            status += ' - %s' % (self.contract_device.name)
        return status
