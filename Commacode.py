print("Sanio Frederic,1AY24AI099,SEC-O")
def comma_code(items):
    if not items:
        return ''
    elif len(items) == 1:
        return items[0]
    else:
        return ', '.join(items[:-1]) + ' and ' + items[-1]

# Example usage
if __name__ == "__main__":
    example_list = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_code(example_list))
