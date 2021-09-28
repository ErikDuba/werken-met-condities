kaas_geel = input(str('Is de kaas geel?: '))
if kaas_geel == 'ja':
    kaas_gat = input(str('Zitten er gaten in?: '))
    if kaas_gat == 'ja':
        kaas_duur = input(str('Is de kaas belachelijk duur?: '))
        if kaas_duur == 'ja':
            print('De kaas is Emmenthaler. ')
        if kaas_duur == 'nee':
            print('De kaas is Leerdammer')
    if kaas_gat == 'nee':
        steen_kaas = input(str('Is de kaas hard als steen?: '))
        if steen_kaas == 'ja':
            print('De kaas is Parmigiano Reggiano')
        if steen_kaas == 'nee':
            print('De kaas is Goudse kaas')

if kaas_geel == 'nee':
    schimmel_kaas = input(str('Heeft de kaas blauwe schimmels?: '))
    if schimmel_kaas == 'ja':
        korst_kaas = input(str('Heeft de kaas een korst?: '))
        if korst_kaas == 'ja':
            print('De kaas is Bleu de Rochbaron')
        if korst_kaas == 'nee':
            print('De kaas is Fourme d\'Abert')
    if schimmel_kaas == 'nee':
        korst_kaas2 = input(str('Heeft de kaas een korst?: '))
        if korst_kaas2 == 'ja':
            print('De kaas is Camambert')
        if korst_kaas2 == 'nee':
            print('De kaas is Mozzarella')