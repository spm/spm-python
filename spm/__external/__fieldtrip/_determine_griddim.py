from spm.__wrapper__ import Runtime


def _determine_griddim(*args, **kwargs):
    """
      DETERMINE_GRIDDIM uses the labels and positions of electrodes in elec to  
        determine the dimensions of each set of electrodes (i.e., electrodes with  
        the same string, but different numbers)  
         
        use as:   
          GridDim = determine_griddim(elec)  
          where elec is a structure that contains an elecpos field and a label field  
          and GridDim(1) = number of rows and GridDim(2) = number of columns  
            
        See also FT_ELECTRODEREALIGN  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/determine_griddim.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("determine_griddim", *args, **kwargs)
