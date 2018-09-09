import  random
def is_prime(n):
    i = 2
    while i<n:
        if(n%i==0):
            return False
        i+=1
    return True

def gcd(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b

def multiplicative_inverse(a,b):
    if(a<b):
        tmp = a
        a = b
        b = tmp
    #           0 1   2   3  4 5
    # matrix = [a b a//b a%b x y]
    matrix = []
    i = 0
    while a%b != 0:
        matrix.append([a, b, a % b, a // b, '_', '_'])
        a = matrix[i][1]
        b = matrix[i][2]
        i+=1
    matrix.append([a, b, a % b, a // b, '_', '_'])
    matrix[i][4] = 0
    matrix[i][5] = 1
    i-=1
    while i>=0:
        matrix[i][4] = matrix[i+1][5]
        matrix[i][5] = matrix[i+1][4] - (matrix[i+1][5] * matrix[i][3])
        i-=1
    #return  matrix
    return matrix[0][5]

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p*q
    # PUT YOUR CODE HERE
    phi = (p-1)*(q-1)
    # PUT YOUR CODE HERE
    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

while True:
    p = int(input('Введите простое число p: '))
    if (is_prime(p) == True):
        break
while True:
    q = int(input('Введите простое число q: '))
    if (is_prime(q) == True):
        break

print("Сгенерированная пара ключей: ",generate_keypair(p,q))



