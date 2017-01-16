from ..blueprint import admin


@admin.route('/contracts')
def contracts():
    return 'all contracts'
