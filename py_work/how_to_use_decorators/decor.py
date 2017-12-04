#Decorator

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional argument:', args)
        print('Keyword argument:',  kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function
