from spm._runtime import Runtime


def eeg_loadbvrf(*args, **kwargs):
    r"""
      eeg_loadbvrf() - Read data saved in the Brain Vision Recorder format (BVRF)  
                         and create one EEGLAB EEG struct per participant.  
         
        Usage:  
          >> [hdr, ALLEEG] = eeg_loadbvrf(hdrPath, hdrFileName, 'key', value, ...);  
         
        Inputs:  
          hdrPath      - Header path  
          hdrFileName  - Header file name (.bvrh). Data (.bvrd), marker (.bvrm),  
                         and impedance (.bvri) files must be in the same folder.  
         
        Optional 'key', value pairs:  
          'sampleInterval'       - [first, last] sample indices to read (0-based).  
                                   [] (default) = read all samples.  
          'channelIndx'          - Indices of channels to import (applied per participant).  
          'flagImportMarkers'    - true/false (default: true). Import markers → EEG.event.  
          'flagImportImpedances' - true/false (default: true). Read impedance file  
                                   and store in EEG.etc.impedances.  
          'flagMetadata'         - true/false (default: false). If true: only read  
                                   header; ALLEEG is returned empty.  
          'verbose'              - true/false (default: false). Print progress.  
          'participantId'        - string. If provided and there are multiple  
                                   participants, only the participant whose  
                                   Channels(k).ParticipantId matches this value  
                                   is loaded into ALLEEG.  
          'usePoly'              - true/false (default: true). Use polynomial  
                                   information in sensors (if exist) to convert sensor  
                                   output to physical quantity  
         
        Outputs:  
          hdr        - Parsed BVRF header (struct from jsondecode).  
          ALLEEG     - 1 x N cell array of EEGLAB EEG structs (one per participant,  
                       or just one if 'participantId' is specified).  
         
        Notes:  
          - Participant splitting is done via Channels(k).ParticipantId only.  
          - Markers are mapped to EEGLAB events as:  
                EEG.event(k).type    = MarkerType  
                EEG.event(k).latency = Sample  
                EEG.event(k).comment = Comment  
         
        Author: Alejandro Ojeda, Brain Products GmbH, 2025  
                Ramon Martinez-Cancino, Brain Products GmbH, 2025  
         
        Copyright (C) 2025 Brain Products GmbH  
         
        Permission is hereby granted, free of charge, to any person obtaining a copy  
        of this software and associated documentation files (the "Software"), to deal  
        in the Software without restriction, including without limitation the rights  
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
        copies of the Software, and to permit persons to whom the Software is  
        furnished to do so, subject to the following conditions:  
         
        The above copyright notice and this permission notice shall be included in all  
        copies or substantial portions of the Software.  
         
        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
        SOFTWARE.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/bvrf_reader/eeg_loadbvrf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("eeg_loadbvrf", *args, **kwargs)
