from spm.__wrapper__ import Runtime


def _prepare_headmodel(*args, **kwargs):
    """
     %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
        SUBFUNCTION that helps to prepare the electrodes/gradiometers and the  
        volume conduction model. This is used in sourceanalysis and dipolefitting.  
         
        This function will get the gradiometer/electrode definition and the volume  
        conductor definition.  
         
        Subsequently it will remove the gradiometers/electrodes that are not  
        present in the data. Finally it with attach the gradiometers to a  
        multi-sphere head model (if supplied) or attach the electrodes to  
        the skin surface of a BEM head model.  
         
        This function will return the electrodes/gradiometers in an order that is  
        consistent with the order in cfg.channel, or - in case that is empty - in  
        the order of the input electrode/gradiometer definition.  
         
       %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/prepare_headmodel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("prepare_headmodel", *args, **kwargs)
