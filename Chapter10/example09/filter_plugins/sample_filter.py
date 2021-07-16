def cloud_truth(a): 
    return a.replace("the cloud", "somebody else's computer") 
class FilterModule(object): 
    '''Cloud truth filters''' 
    def filters(self): 
        return {'cloud_truth': cloud_truth} 
