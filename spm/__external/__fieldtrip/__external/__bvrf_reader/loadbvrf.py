from spm._runtime import Runtime


def loadbvrf(*args, **kwargs):
    r"""
      readBVRF() - Read data saved in the Brain Vision Recorder format.  
         
        Usage:  
          >> [hdr, participantId, data, channels, markers, impedances] = loadbvrf(hdrFile, verbose);  
         
        Inputs:  
          hdrFile      - Header file (bvrh). Data (.bvrd) and marker (bvrm) files should be in the same folder.  
          sampleRange  - [first, last] samples that define the interval to read. Enter [] to read all samples.  
          flagMetadata - Loads only the header metadata.  
          verbose      - Optional input. Set to true to display messages.   
         
        Outputs:  
          hdr             - header structure  
          participantId   - cell array of participant ids  
          data            - cell array of data matrix [channels, samples]  
          channels        - cell array of channel structure  
          markers         - cell array of marker structure  
          impedances      - cell array of impedance measurements  
         
        Copyright (C) 2025 Brain Products GmbH  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/bvrf_reader/loadbvrf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("loadbvrf", *args, **kwargs)
