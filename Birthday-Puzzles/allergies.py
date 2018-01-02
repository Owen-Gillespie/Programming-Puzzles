'''This is code to help me solve a cipher in my birthday puzzle, which can be
    found at drunkopants.com/allergies'''

def decode(ctxt, s, m, a):
    '''Reverse the whole cipher for a given shift, multiplier, and adder'''
    hx_txt = int(ctxt, 16)
    b_txt = format(hx_txt, '0' + str(4 * len(ctxt)) + 'b')
    s_txt = shift(b_txt, s)
    p_txt = convert(s_txt, m, a)
    return p_txt 

def crack(ctxt):
    '''Brute forces decrypting the affine cipher. Short circuits for unexpected
        ascii values'''
    for s in range(8):
        for m in COPRIMES:
            for a in range(255):
                text = decode(ctxt, s, m, a)
                if text:
                    print(text, s,m,a)

def shift(txt, s):
    '''Left shift by "s" char's with wrapping'''
    return txt[s:] + txt[:s]

def convert(txt, m, a):
    '''Reverse the affine cipher. Short circuit on certain ASCII values'''
    output = ""
    for i in range(0, len(txt), 8):
        # print(i)
        block = txt[i: i + 8]
        # print(block)
        val = int(block,2)
        val -= a
        val %= RANGE
        val *= MULT_INV[m]
        val %= RANGE
        if val < 32 or val > 126:
            return None
        output += chr(val)
        # print(output)
    return output 

# Number theory things:
# From: https://stackoverflow.com/questions/39678984/efficient-check-if-two-numbers-are-co-primes-relatively-primes
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1

# From https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

RANGE = 255
COPRIMES = [x for x in range(RANGE) if coprime(x, RANGE)]
MULT_INV = {x: modinv(x,RANGE) for x in COPRIMES}

crack("e497e8fb39e83981339bb42f801e058cb096974c058d4cff32978c2f818cfe7cff9a1efb8cc02eb09604c78c596d8d1e58f4a6c152c78c7d9b80441f8ce42e52978c041fe8ff80cb8c639b6648ff802e1eff9b8005a78da0978de8976697664897e8058ce4fe058c639b6648ff802e1eff9b818cfe058c1ee4978cb19b4d4d9a6cff80cb8c639b80622e1e97802e1e967d8db59a04fe1efe52978cff801e96ca97e804358c1ee4978de99a1e2e1eff9b818d9ab18c1ee4978c48ff802fe8a18c7cfecafe1e04c78c1ee4978d66394c1effb54cfe97e98cb19be98c1ee4978ceab0b0ff80978c62ffb4e497e8c78c2f807d8c1ee4978c2e7c7c97e98cb19be98c1ee4978ceab0b0ff80978c62ffb4")
