#represents web page ranks 
M = np.array([[0,0,0,1/2],[1/3,0,0,0],[1/3,1/2,0,1/2],[1/3,1/2,0,0]])
x = np.array([1/4,1/4,1/4,1/4])
print(M@x)
print(M@M@M@M@M@M@M@M@M@M@M@M@M@M@x)
#hyper parameter applied 
p=0.15
modified_M = M
modified_M[:,2] = np.ones(4)*1/4
B = np.ones((4,4))*1/4
G = 0.85*modified_M + 0.15*B
#controlled as a function 
def pagerank(modified_M, p=0.15, eps=1e-3):

    n = modified_M.shape[1]
    v = np.random.rand(n)
    v = v/np.linalg.norm(v)
    G = (1-p)*modified_M + p*(1/n)*np.ones((n,n))
    vold = np.zeros(n)
    
    while np.linalg.norm(v-vold, 2)>eps:
        vold = v.copy()
        v = G.dot(v)
        
    return G, v/np.sum(v)
#show
pagerank(modified_M)
#check with python calculation 
G@G@G@G@G@G@G@G@G@G@G@G@G@G@G@G@G@G@G@G@x
#new one 
K1 = np.array([[0,1/2,1/2,0,0,0,0,0],[0,0,0,1,0,0,0,0],[0,1/2,0,0,1/2,0,0,0],[0,1/2,0,0,0,1/2,0,0],[0,0,0,0,0,1/3,1/3,1/3],
              [0,0,0,0,0,0,0,1],[1/3,0,0,0,1/3,0,0,1/3],[0,0,0,0,0,1/2,1/2,0]])
K1 = K1.T
K2, v2 = pagerank(K1)
v2
#eigenvector applied 
eigenvalues, eigenvectors = np.linalg.eig(K2)
eigenvalues
#eigenvector is used as rank vector 
rank_vector = K2 @ eigenvectors[:,0]
rank_vector = rank_vector / rank_vector.sum()
rank_vector