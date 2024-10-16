from spm.__wrapper__ import Runtime


def _get_components(*args, **kwargs):
  """ GET_COMPONENTS     connected components  
     
      [comps,comp_sizes] = get_components(adj);  
     
      Returns the components of an undirected graph specified by the binary and   
      undirected adjacency matrix adj. Components and their constitutent nodes are   
      assigned the same index and stored in the vector, comps. The vector, comp_sizes,  
      contains the number of nodes beloning to each component.  
     
      Inputs:         adj,    binary and undirected adjacency matrix  
     
      Outputs:      comps,    vector of component assignments for each node  
               comp_sizes,    vector of component sizes  
     
      Note: disconnected nodes will appear as components with a component  
      size of 1  
     
      J Goni, University of Navarra and Indiana University, 2009/2011  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/get_components.m)
  """

  return Runtime.call("get_components", *args, **kwargs)
