from spm.__wrap__ import _Runtime


def mci_compare_setup(*args, **kwargs):
  """  Set up data structures for fwd/sens/grad comparisons  
    FORMAT [P,M,U,Y,ind] = mci_compare_setup (model)  
     
    model     'phase', 'nmm-r2p2'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/mci/gradients/mci_compare_setup.m)
  """

  return _Runtime.call("mci_compare_setup", *args, **kwargs)
