class Node:
    
    def __init__(self, X, y, gini):
        self.X = X
        self.y = y
        self.gini = gini
        self.feature_index = 0
        self.threshold = 0
        self.left = None
        self.right = None


class MyDecisionTreeClassifier:

    def __init__(self, max_depth):
        self.max_depth = max_depth
    
    def gini(self, groups, classes):
        '''
        A Gini score gives an idea of how good a split is by how mixed the
        classes are in the two groups created by the split.
        
        A perfect separation results in a Gini score of 0,
        whereas the worst case split that results in 50/50
        classes in each group result in a Gini score of 0.5
        (for a 2 class problem).
        '''
        pass
    
    def split_data(self, X, y): #-> tuple[int, int]:
        # test all the possible splits in O(N^2)
        # return index and threshold value
        
        pass
    
    def build_tree(self, X, y, depth = 0):
        # create a root node
        # recursively split until max depth is not exeeced
        
        pass
    
    def fit(sefl, X, y):
        # basically wrapper for build tree
        
        pass
    
    def predict(self, X_test):
        # traverse the tree while there is left node
        # and return the predicted class for it, 
        # note that X_test can be not only one example
        
        pass