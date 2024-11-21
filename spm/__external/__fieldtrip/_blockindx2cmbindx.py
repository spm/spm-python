from spm.__wrapper__ import Runtime


def _blockindx2cmbindx(*args, **kwargs):
    """
      This is a helper function that is needed for the bookkeeping of the data,  
        when requesting (conditional)-blockwise granger causality estimates. Its  
        single use is in ft_connectivityanalysis, but in order to keep that code  
        clean, it was decided to put this function as a private function.  
         
        Use as   
          [cmbindx, n, blocklabel] = blockindx2cmbindx(labelcmb, blockindx,  
          block)  
         
        The purpose is to generate a cell-array (Nx2, same size as input array  
        block) of numeric indices, which index into the rows of the Mx2 labelcmb  
        array, and which can subsequently be used by lower-level functionality  
        (i.e. blockwise_conditionalgranger) to compute the connectivity metric of  
        interest. Blockindx is a 1x2 cell-array, which maps the individual  
        channels in blockindx{1} to an indexed block in blockindx{2}. Block  
        specifies in each row of cells two ordered lists of blocks that are  
        needed to compute a conditioned Granger spectrum.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/blockindx2cmbindx.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("blockindx2cmbindx", *args, **kwargs)
