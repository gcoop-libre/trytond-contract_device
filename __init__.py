# This file is part of the contract_device module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import contract
from . import user
from . import device
from . import pos


def register():
    Pool.register(
        device.ContractDevice,
        device.ContractDeviceResUser,
        pos.Pos,
        user.User,
        contract.Contract,
        contract.ContractConsumption,
        module='contract_device', type_='model')
