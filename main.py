from utils.rna_split import RNATree

dotB = '......((.......((.((.......((.((...............)).........((...............)).)).......)).((.......((...............)).......)).((.......((.((...............)).........((...............)).)).......)).((.......((...............)).......)).((.......((.((...............)).........((...............)).)).......)).((.......((............((...............)).)).......)).)).......))......'

tree = RNATree(dotB)

tree.external_loop_create()

print(1)
