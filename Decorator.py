def deco_func(orig_func):
    def wrapper_func(*args, **kwargs):
        print('deco ran')
        result  = orig_func(*args, **kwargs)
        return result
    return wrapper_func

@deco_func
def display_info(name, age):
    print('display ran with {} {}'.format(name, age))

display_info('abhi', 10)