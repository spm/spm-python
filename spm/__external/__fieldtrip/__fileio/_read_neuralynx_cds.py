from spm.__wrapper__ import Runtime


def _read_neuralynx_cds(*args, **kwargs):
    """
      READ_NEURALYNX_CDS reads selected samples and channels from a combined Neuralynx dataset with separate subdirectories for the LFP, MUA and spike channels  
         
        Use as  
           hdr = read_neuralynx_cds(parentdir)  
           dat = read_neuralynx_cds(parentdir, hdr, begsample, endsample, chanindx)  
         
        This is not a formal Neuralynx file format, but at the F.C. Donders  
        Centre we use it as a directory/file organization in conjunction  
        with Neuralynx, SPIKESPLITTING and SPIKEDOWNSAMPLE.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/read_neuralynx_cds.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_neuralynx_cds", *args, **kwargs)
