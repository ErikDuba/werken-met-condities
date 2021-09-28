kaasGeel = input(str('Is de kaas geel?: '))
if kaasGeel == 'ja':
    kaasGat = input(str('Zitten er gaten in?: '))
    if kaasGat == 'ja':
        kaasDuur = input(str('Is de kaas belachelijk duur?: '))
        if kaasDuur == 'ja':
            print('De kaas is Emmenthaler. ')
        if kaasDuur == 'nee':
            print('De kaas is Leerdammer')
    if kaasGat == 'nee':
        steenKaas = input(str('Is de kaas hard als steen?: '))
        if steenKaas == 'ja':
            print('De kaas is Parmigiano Reggiano')
        if steenKaas == 'nee':
            print('De kaas is Goudse kaas')

elif kaasGeel == 'nee':
    schimmelKaas = input(str('Heeft de kaas blauwe schimmels?: '))
    if schimmelKaas == 'ja':
        korstKaas = input(str('Heeft de kaas een korst?: '))
        if korstKaas == 'ja':
            print('De kaas is Bleu de Rochbaron')
        if korstKaas == 'nee':
            print('De kaas is Fourme d\'Abert')
    if schimmelKaas == 'nee':
        korstKaas2 = input(str('Heeft de kaas een korst?: '))
        if korstKaas2 == 'ja':
            print('De kaas is Camambert')
        if korstKaas2 == 'nee':
            print('De kaas is Mozzarella')