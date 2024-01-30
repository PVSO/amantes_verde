from rolepermissions.roles import AbstractUserRole


class Loja(AbstractUserRole):
    permissoes_disponiveis = {
        'cadastrar_produtos': True,
    }


class Cliente(AbstractUserRole):
    permissoes_disponiveis = {
        'realizar_compra': True,
    }
