with (
    open('./CYP2C19_Protein.txt') as f1,
    open('./CYP2C19_Uniprot.txt') as f2,
):
    a = f1.readlines()
    b = f2.readlines()

import difflib
a_sample = a[0] 
b_sample = b[0]
diff = difflib.ndiff(a.replace(' ', '\n').splitlines(keepends=True), b.replace(' ', '\n').splitlines(keepends=True))
print(''.join(diff), end="")