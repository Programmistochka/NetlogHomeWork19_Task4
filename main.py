import types


def flat_generator(list_of_list):
    whole_list = []
    for list_els in list_of_list:
        check_list = list_els[::-1]
        while check_list:    #пока не пустой
            el = check_list.pop(-1)
            if isinstance(el, list):
                el = el[::-1]
                check_list.extend(el)
            else:
                whole_list.append(el)  
    finish = len(whole_list)
    n = 0
    while n < finish:
        yield whole_list[n]
        n += 1
    

def test_4(list_of_lists):

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists), types.GeneratorType)


if __name__ == '__main__':
    
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    
    for item in flat_generator(list_of_lists_2):
        print(item)
    
    test_4(list_of_lists_2)