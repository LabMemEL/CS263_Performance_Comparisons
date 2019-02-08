#!/usr/bin/env python

from sjcl import SJCL
import numpy as np
import random
import string
import time
# X_1KB = 1024
# X_256KB = 256 * X_1KB
# X_1MB = 1024 * 1024
# X_4MB = 4 * X_1MB
# X_32MB = 32 * X_1MB
# X_64MB = 2 * X_32MB
# X_128MB = X_1MB * 128

# np.random.bytes( X_1MB )

start = time.time()

message=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(1000000))
cyphertext = SJCL().encrypt(message, "shared_secret")

end = time.time()
print('Total Execution Time: ', end - start, ' second')
# print cyphertext
# print SJCL().decrypt(cyphertext, "shared_secret")



