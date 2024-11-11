from spm.__wrapper__ import Runtime


def _inputlabel2outputlabel(*args, **kwargs):
    """
      INPUTLABEL2OUTPUTLABEL is a subfunction which outputs the cell-arrays  
        outputlabel and the corresponding outputindex, and defines how the   
        channels in the original data have to be combined, to provide the   
        wished for combination of the channels, as defined in cfg.combinechan  
         
        Configuration-options are:  
          cfg.combinechan = 'planar' combines the horizontal and vertical planar-gradients  
                            'pseudomeg' one gradiometer versus the rest  
          TODO: more flexible way of combining, e.g. by providing a cell-array  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/inputlabel2outputlabel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("inputlabel2outputlabel", *args, **kwargs)
