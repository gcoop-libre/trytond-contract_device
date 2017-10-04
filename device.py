# This file is part of the contract_device module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields

__all__ = ['ContractDevice', 'ContractDeviceResUser']


class ContractDevice(ModelSQL, ModelView):
    'Contract Device Configuration'
    __name__ = 'contract.device'
    name = fields.Char('Device Name', size=None, required=True, select=True)
    code = fields.Char('Code', size=None, select=True)
    active = fields.Boolean('Active', select=True)
    journal = fields.Many2One('account.journal', 'Default Journal',
        required=True, domain=[
            ('type', '=', 'revenue'),
            ])
    users = fields.One2Many('res.user', 'contract_device', 'Users',
       add_remove=[])
    point_of_sales = fields.One2Many('account.pos', 'contract_device',
        'Point of sales', add_remove=[], required=True)
    #analytic_account = fields.Many2One(
    #    'analytic_account.account',
    #    'Centro de costo',
    #    domain=[
    #        ('type', '=', 'normal'),
    #        ('active', '=', True),
    #        ('root.code', '=', 'contract_device'),
    #    ])

    @staticmethod
    def default_active():
        return True


class ContractDeviceResUser(ModelSQL):
    'Contract Device - Res User'
    __name__ = 'contract.device-res.user'

    device = fields.Many2One('contract.device', 'Device', ondelete='CASCADE',
        select=True, required=True)
    user = fields.Many2One('res.user', 'User', ondelete='RESTRICT',
        required=True)
