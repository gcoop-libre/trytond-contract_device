# This file is part of the contract_device module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.

from trytond.pyson import Eval
from trytond.model import fields
from trytond.pool import PoolMeta, Pool
from trytond.transaction import Transaction

__all__ = ['Contract', 'ContractConsumption']


class Contract:
    __name__ = 'contract'
    __metaclass__ = PoolMeta

    contract_device = fields.Many2One('contract.device', 'Contract Device',
        required=True, readonly=False)
    pos = fields.Many2One('account.pos', 'Point of sale', required=True,
        domain=[
            ('contract_device', '=', Eval('contract_device')),
            ])

    @fields.depends('contract_device', 'pos')
    def on_change_contract_device(self):
        self.pos = None
        if self.contract_device:
            self.pos = self.contract_device.point_of_sales[0]

    @staticmethod
    def default_contract_device():
        User = Pool().get('res.user')
        user = User(Transaction().user)
        return user.contract_device.id if user.contract_device else None


class ContractConsumption:
    __name__ = 'contract.consumption'
    __metaclass__ = PoolMeta

    @classmethod
    def __setup__(cls):
        super(ContractConsumption, cls).__setup__()
        cls._error_messages.update({
                'missing_pos': ('Please, configure a point of sale before '
                    'creating contract invoices.'),
                })

    @classmethod
    def _get_invoice(cls, keys):
        invoice = super(ContractConsumption, cls)._get_invoice(keys)
        values = dict(keys)
        device = values['contract'].contract_device
        invoice.pos = values['contract'].pos
        invoice.journal = device.journal
        return invoice
