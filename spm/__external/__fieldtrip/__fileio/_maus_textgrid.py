from spm.__wrapper__ import Runtime


def _maus_textgrid(*args, **kwargs):
    """
      MAUS_TEXTGRID reads speech segments from a file that has been processed with MAUS  
        see https://clarin.phonetik.uni-muenchen.de/BASWebServices  
         
        Use as  
          hdr = maus_textgrid(filename);  
          dat = maus_textgrid(filename, hdr, begsample, endsample, chanindx);  
          evt = maus_textgrid(filename, hdr);  
         
        You should pass the *.TextGrid file as the filename, There should be a  
        corresponding wav file with the same filename in the same directory.  
         
        See also FT_FILETYPE, FT_READ_HEADER, FT_READ_DATA, FT_READ_EVENT  
        See also BIDS_TSV, BIOPAC_ACQ, BUCN_TXT, EEGSYNTH_TSV, EVENTS_TSV, LIBERTY_CSV, MAUS_TEXTGRID, MOTION_C3D, OPENBCI_TXT, OPENPOSE_KEYPOINTS, OPENSIGNALS_TXT, OPENVIBE_MAT, OPM_FIL, QUALISYS_TSV, SCCN_XDF, SENSYS_CSV, SNIRF, SPIKEGLX_BIN, UNICORN_CSV, XSENS_MVNX  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/maus_textgrid.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("maus_textgrid", *args, **kwargs)
