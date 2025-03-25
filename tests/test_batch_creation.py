import unittest

from spm import Struct, Cell, Array, cfg_dep, Runtime

# https://jsheunis.github.io/2018-06-28-spm12-matlab-scripting-tutorial-3/
batch1 = r"""
realign_estimate_reslice = struct;
% Data
fnms={};
for i = 1:Nt
    fnms{i} = [functional4D_fn ',' num2str(i) ];
end
realign_estimate_reslice.matlabbatch{1}.spm.spatial.realign.estwrite.data={fnms'};
% Eoptions
realign_estimate_reslice.matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.quality = 0.9;
realign_estimate_reslice.matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.sep = 4;
realign_estimate_reslice.matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.fwhm = 5;
realign_estimate_reslice.matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.rtm = 1;
realign_estimate_reslice.matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.interp = 2;
realign_estimate_reslice.matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.wrap = [0 0 0];
realign_estimate_reslice.matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.weight = '';
% Roptions
realign_estimate_reslice.matlabbatch{1}.spm.spatial.realign.estwrite.roptions.which = [2 1];
realign_estimate_reslice.matlabbatch{1}.spm.spatial.realign.estwrite.roptions.interp = 4;
realign_estimate_reslice.matlabbatch{1}.spm.spatial.realign.estwrite.roptions.wrap = [0 0 0];
realign_estimate_reslice.matlabbatch{1}.spm.spatial.realign.estwrite.roptions.mask = 1;
realign_estimate_reslice.matlabbatch{1}.spm.spatial.realign.estwrite.roptions.prefix = 'r';
"""

# https://www.fil.ion.ucl.ac.uk/spm/docs/tutorials/fmri_preprocessing/scripting/
batch2 = r"""
matlabbatch{1}.spm.spatial.realign.estwrite.data = {{'/Users/olivia/OneDrive - King''s College London/spm/spm_tutorials/preprocessing/MoAEpilot/sub-01/func/sub-01_task-auditory_bold.nii'}};
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.quality = 0.9;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.sep = 4;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.fwhm = 5;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.rtm = 1;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.interp = 2;
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.wrap = [0 0 0];
matlabbatch{1}.spm.spatial.realign.estwrite.eoptions.weight = '';
matlabbatch{1}.spm.spatial.realign.estwrite.roptions.which = [0 1];
matlabbatch{1}.spm.spatial.realign.estwrite.roptions.interp = 4;
matlabbatch{1}.spm.spatial.realign.estwrite.roptions.wrap = [0 0 0];
matlabbatch{1}.spm.spatial.realign.estwrite.roptions.mask = 1;
matlabbatch{1}.spm.spatial.realign.estwrite.roptions.prefix = 'r';
matlabbatch{2}.spm.temporal.st.scans{1}(1) = cfg_dep('Realign: Estimate & Reslice: Realigned Images (Sess 1)', substruct('.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','sess', '()',{1}, '.','cfiles'));
matlabbatch{2}.spm.temporal.st.nslices = 64;
matlabbatch{2}.spm.temporal.st.tr = 7;
matlabbatch{2}.spm.temporal.st.ta = 6.890625;
matlabbatch{2}.spm.temporal.st.so = [64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1];
matlabbatch{2}.spm.temporal.st.refslice = 32;
matlabbatch{2}.spm.temporal.st.prefix = 'a';
matlabbatch{3}.spm.spatial.coreg.estimate.ref(1) = cfg_dep('Realign: Estimate & Reslice: Mean Image', substruct('.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','rmean'));
matlabbatch{3}.spm.spatial.coreg.estimate.source = {'/Users/olivia/OneDrive - King''s College London/spm/spm_tutorials/preprocessing/MoAEpilot/sub-01/anat/sub-01_T1w.nii,1'};
matlabbatch{3}.spm.spatial.coreg.estimate.other = {''};
matlabbatch{3}.spm.spatial.coreg.estimate.eoptions.cost_fun = 'nmi';
matlabbatch{3}.spm.spatial.coreg.estimate.eoptions.sep = [4 2];
matlabbatch{3}.spm.spatial.coreg.estimate.eoptions.tol = [0.02 0.02 0.02 0.001 0.001 0.001 0.01 0.01 0.01 0.001 0.001 0.001];
matlabbatch{3}.spm.spatial.coreg.estimate.eoptions.fwhm = [7 7];
matlabbatch{4}.spm.spatial.preproc.channel.vols(1) = cfg_dep('Coregister: Estimate: Coregistered Images', substruct('.','val', '{}',{3}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','cfiles'));
matlabbatch{4}.spm.spatial.preproc.channel.biasreg = 0.001;
matlabbatch{4}.spm.spatial.preproc.channel.biasfwhm = 60;
matlabbatch{4}.spm.spatial.preproc.channel.write = [0 0];
matlabbatch{4}.spm.spatial.preproc.tissue(1).tpm = {'/Applications/spm12/tpm/TPM.nii,1'};
matlabbatch{4}.spm.spatial.preproc.tissue(1).ngaus = 1;
matlabbatch{4}.spm.spatial.preproc.tissue(1).native = [1 0];
matlabbatch{4}.spm.spatial.preproc.tissue(1).warped = [0 0];
matlabbatch{4}.spm.spatial.preproc.tissue(2).tpm = {'/Applications/spm12/tpm/TPM.nii,2'};
matlabbatch{4}.spm.spatial.preproc.tissue(2).ngaus = 1;
matlabbatch{4}.spm.spatial.preproc.tissue(2).native = [1 0];
matlabbatch{4}.spm.spatial.preproc.tissue(2).warped = [0 0];
matlabbatch{4}.spm.spatial.preproc.tissue(3).tpm = {'/Applications/spm12/tpm/TPM.nii,3'};
matlabbatch{4}.spm.spatial.preproc.tissue(3).ngaus = 2;
matlabbatch{4}.spm.spatial.preproc.tissue(3).native = [1 0];
matlabbatch{4}.spm.spatial.preproc.tissue(3).warped = [0 0];
matlabbatch{4}.spm.spatial.preproc.tissue(4).tpm = {'/Applications/spm12/tpm/TPM.nii,4'};
matlabbatch{4}.spm.spatial.preproc.tissue(4).ngaus = 3;
matlabbatch{4}.spm.spatial.preproc.tissue(4).native = [1 0];
matlabbatch{4}.spm.spatial.preproc.tissue(4).warped = [0 0];
matlabbatch{4}.spm.spatial.preproc.tissue(5).tpm = {'/Applications/spm12/tpm/TPM.nii,5'};
matlabbatch{4}.spm.spatial.preproc.tissue(5).ngaus = 4;
matlabbatch{4}.spm.spatial.preproc.tissue(5).native = [1 0];
matlabbatch{4}.spm.spatial.preproc.tissue(5).warped = [0 0];
matlabbatch{4}.spm.spatial.preproc.tissue(6).tpm = {'/Applications/spm12/tpm/TPM.nii,6'};
matlabbatch{4}.spm.spatial.preproc.tissue(6).ngaus = 2;
matlabbatch{4}.spm.spatial.preproc.tissue(6).native = [0 0];
matlabbatch{4}.spm.spatial.preproc.tissue(6).warped = [0 0];
matlabbatch{4}.spm.spatial.preproc.warp.mrf = 1;
matlabbatch{4}.spm.spatial.preproc.warp.cleanup = 1;
matlabbatch{4}.spm.spatial.preproc.warp.reg = [0 0.001 0.5 0.05 0.2];
matlabbatch{4}.spm.spatial.preproc.warp.affreg = 'mni';
matlabbatch{4}.spm.spatial.preproc.warp.fwhm = 0;
matlabbatch{4}.spm.spatial.preproc.warp.samp = 3;
matlabbatch{4}.spm.spatial.preproc.warp.write = [0 1];
matlabbatch{4}.spm.spatial.preproc.warp.vox = NaN;
matlabbatch{4}.spm.spatial.preproc.warp.bb = [NaN NaN NaN
                                              NaN NaN NaN];
matlabbatch{5}.spm.spatial.normalise.write.subj.def(1) = cfg_dep('Segment: Forward Deformations', substruct('.','val', '{}',{4}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('.','fordef', '()',{':'}));
matlabbatch{5}.spm.spatial.normalise.write.subj.resample(1) = cfg_dep('Slice Timing: Slice Timing Corr. Images (Sess 1)', substruct('.','val', '{}',{2}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('()',{1}, '.','files'));
matlabbatch{5}.spm.spatial.normalise.write.woptions.bb = [-78 -112 -70
                                                          78 76 85];
matlabbatch{5}.spm.spatial.normalise.write.woptions.vox = [3 3 3];
matlabbatch{5}.spm.spatial.normalise.write.woptions.interp = 4;
matlabbatch{5}.spm.spatial.normalise.write.woptions.prefix = 'w';
matlabbatch{6}.spm.spatial.smooth.data(1) = cfg_dep('Normalise: Write: Normalised Images (Subj 1)', substruct('.','val', '{}',{5}, '.','val', '{}',{1}, '.','val', '{}',{1}, '.','val', '{}',{1}), substruct('()',{1}, '.','files'));
matlabbatch{6}.spm.spatial.smooth.fwhm = [6 6 6];
matlabbatch{6}.spm.spatial.smooth.dtype = 0;
matlabbatch{6}.spm.spatial.smooth.im = 0;
matlabbatch{6}.spm.spatial.smooth.prefix = 's';
"""


class BatchCreationTestCase(unittest.TestCase):
    def test_batch1(self):
        # Implicit creation
        realign_estimate_reslice = Struct()
        realign_estimate_reslice.matlabbatch(0).spm.spatial.realign.estwrite.data = [
            ["file1"],
            ["file2"],
        ]
        realign_estimate_reslice.matlabbatch(
            0
        ).spm.spatial.realign.estwrite.eoptions.quality = 0.9
        realign_estimate_reslice.matlabbatch(
            0
        ).spm.spatial.realign.estwrite.eoptions.sep = 4
        realign_estimate_reslice.matlabbatch(
            0
        ).spm.spatial.realign.estwrite.eoptions.fwhm = 5
        realign_estimate_reslice.matlabbatch(
            0
        ).spm.spatial.realign.estwrite.eoptions.rtm = 1
        realign_estimate_reslice.matlabbatch(
            0
        ).spm.spatial.realign.estwrite.eoptions.interp = 2
        realign_estimate_reslice.matlabbatch(
            0
        ).spm.spatial.realign.estwrite.eoptions.wrap = Array.from_any([0, 0, 0])
        realign_estimate_reslice.matlabbatch(
            0
        ).spm.spatial.realign.estwrite.eoptions.weight = ""
        realign_estimate_reslice.matlabbatch(
            0
        ).spm.spatial.realign.estwrite.roptions.which = Array.from_any([2, 1])
        realign_estimate_reslice.matlabbatch(
            0
        ).spm.spatial.realign.estwrite.roptions.interp = 4
        realign_estimate_reslice.matlabbatch(
            0
        ).spm.spatial.realign.estwrite.roptions.wrap = Array.from_any([0, 0, 0])
        realign_estimate_reslice.matlabbatch(
            0
        ).spm.spatial.realign.estwrite.roptions.mask = 1
        realign_estimate_reslice.matlabbatch(
            0
        ).spm.spatial.realign.estwrite.roptions.prefix = "r"

        # Explicit creation
        eoptions = Struct(
            quality=0.9,
            sep=4,
            fwhm=5,
            rtm=1,
            interp=2,
            wrap=Array.from_any([0, 0, 0]),
            weight="",
        )
        roptions = Struct(
            which=Array.from_any([2, 1]),
            interp=4,
            wrap=Array.from_any([0, 0, 0]),
            mask=1,
            prefix="r",
        )
        realign_estimate_reslice_ref = Struct(
            matlabbatch=Cell(
                [
                    Struct(
                        spm=Struct(
                            spatial=Struct(
                                realign=Struct(
                                    estwrite=Struct(
                                        data=[["file1"], ["file2"]],
                                        eoptions=eoptions,
                                        roptions=roptions,
                                    )
                                )
                            )
                        )
                    )
                ]
            )
        )

        self.assertEqual(
            str(realign_estimate_reslice), str(realign_estimate_reslice_ref)
        )

    def test_batch2(self):
        # Implicit creation
        matlabbatch = Cell()
        matlabbatch(0).spm.spatial.realign.estwrite.data = [
            [
                "/Users/olivia/OneDrive - King"
                "s College London/spm/spm_tutorials/preprocessing/MoAEpilot/sub-01/func/sub-01_task-auditory_bold.nii"
            ]
        ]
        matlabbatch(0).spm.spatial.realign.estwrite.eoptions.quality = 0.9
        matlabbatch(0).spm.spatial.realign.estwrite.eoptions.sep = 4
        matlabbatch(0).spm.spatial.realign.estwrite.eoptions.fwhm = 5
        matlabbatch(0).spm.spatial.realign.estwrite.eoptions.rtm = 1
        matlabbatch(0).spm.spatial.realign.estwrite.eoptions.interp = 2
        matlabbatch(0).spm.spatial.realign.estwrite.eoptions.wrap = Array.from_any(
            [0, 0, 0]
        )
        matlabbatch(0).spm.spatial.realign.estwrite.eoptions.weight = ""
        matlabbatch(0).spm.spatial.realign.estwrite.roptions.which = Array.from_any(
            [0, 1]
        )
        matlabbatch(0).spm.spatial.realign.estwrite.roptions.interp = Array.from_any(4)
        matlabbatch(0).spm.spatial.realign.estwrite.roptions.wrap = Array.from_any(
            [0, 0, 0]
        )
        matlabbatch(0).spm.spatial.realign.estwrite.roptions.mask = 1
        matlabbatch(0).spm.spatial.realign.estwrite.roptions.prefix = "r"
        s1 = Runtime.call(
            "substruct",
            ".",
            "val",
            "{}",
            [1],
            ".",
            "val",
            "{}",
            [1],
            ".",
            "val",
            "{}",
            [1],
            ".",
            "val",
            "{}",
            [1],
        )
        s2 = Runtime.call("substruct", ".", "sess", "()", [1], ".", "cfiles")
        matlabbatch(1).spm.temporal.st.scans(0)[0] = cfg_dep(
            "Realign: Estimate & Reslice: Realigned Images (Sess 1)", s1, s2
        )
        matlabbatch(1).spm.temporal.st.nslices = 64
        matlabbatch(1).spm.temporal.st.tr = 7
        matlabbatch(1).spm.temporal.st.ta = 6.890625
        matlabbatch(1).spm.temporal.st.so = Array.from_any(range(64, 0, -1))
        matlabbatch(1).spm.temporal.st.refslice = 32
        matlabbatch(1).spm.temporal.st.prefix = "a"
        s1 = Runtime.call(
            "substruct",
            ".",
            "val",
            "{}",
            {1},
            ".",
            "val",
            "{}",
            {1},
            ".",
            "val",
            "{}",
            {1},
            ".",
            "val",
            "{}",
            {1},
        )
        s2 = Runtime.call("substruct", ".", "rmean")
        matlabbatch(2).spm.spatial.coreg.estimate.ref[0] = cfg_dep(
            "Realign: Estimate & Reslice: Mean Image", s1, s2
        )
        matlabbatch(2).spm.spatial.coreg.estimate.source = [
            "/Users/olivia/OneDrive - King"
            "s College London/spm/spm_tutorials/preprocessing/MoAEpilot/sub-01/anat/sub-01_T1w.nii,1"
        ]
        matlabbatch(2).spm.spatial.coreg.estimate.other = [""]
        matlabbatch(2).spm.spatial.coreg.estimate.eoptions.cost_fun = "nmi"
        matlabbatch(2).spm.spatial.coreg.estimate.eoptions.sep = Array.from_any([4, 2])
        matlabbatch(2).spm.spatial.coreg.estimate.eoptions.tol = Array.from_any(
            [
                0.02,
                0.02,
                0.02,
                0.001,
                0.001,
                0.001,
                0.01,
                0.01,
                0.01,
                0.001,
                0.001,
                0.001,
            ]
        )
        matlabbatch(3).spm.spatial.coreg.estimate.eoptions.fwhm = Array.from_any([7, 7])
        s1 = Runtime.call(
            "substruct",
            ".",
            "val",
            "{}",
            {3},
            ".",
            "val",
            "{}",
            {1},
            ".",
            "val",
            "{}",
            {1},
            ".",
            "val",
            "{}",
            {1},
        )
        s2 = Runtime.call("substruct", ".", "cfiles")
        matlabbatch(3).spm.spatial.preproc.channel.vols[0] = cfg_dep(
            "Coregister: Estimate: Coregistered Images", s1, s2
        )
        matlabbatch(3).spm.spatial.preproc.channel.biasreg = 0.001
        matlabbatch(3).spm.spatial.preproc.channel.biasfwhm = 60
        matlabbatch(3).spm.spatial.preproc.channel.write = Array.from_any([0, 0])
        matlabbatch(3).spm.spatial.preproc.tissue(0).tpm = [
            "/Applications/spm12/tpm/TPM.nii,1"
        ]
        matlabbatch(3).spm.spatial.preproc.tissue(0).ngaus = 1
        matlabbatch(3).spm.spatial.preproc.tissue(0).native = Array.from_any([1, 0])
        matlabbatch(3).spm.spatial.preproc.tissue(0).warped = Array.from_any([0, 0])
        matlabbatch(3).spm.spatial.preproc.tissue(1).tpm = [
            "/Applications/spm12/tpm/TPM.nii,2"
        ]
        matlabbatch(3).spm.spatial.preproc.tissue(1).ngaus = 1
        matlabbatch(3).spm.spatial.preproc.tissue(1).native = Array.from_any([1, 0])
        matlabbatch(3).spm.spatial.preproc.tissue(1).warped = Array.from_any([0, 0])
        matlabbatch(3).spm.spatial.preproc.tissue(2).tpm = [
            "/Applications/spm12/tpm/TPM.nii,3"
        ]
        matlabbatch(3).spm.spatial.preproc.tissue(2).ngaus = 2
        matlabbatch(3).spm.spatial.preproc.tissue(2).native = Array.from_any([1, 0])
        matlabbatch(3).spm.spatial.preproc.tissue(2).warped = Array.from_any([0, 0])
        matlabbatch(3).spm.spatial.preproc.tissue(3).tpm = [
            "/Applications/spm12/tpm/TPM.nii,4"
        ]
        matlabbatch(3).spm.spatial.preproc.tissue(3).ngaus = 3
        matlabbatch(3).spm.spatial.preproc.tissue(3).native = Array.from_any([1, 0])
        matlabbatch(3).spm.spatial.preproc.tissue(3).warped = Array.from_any([0, 0])
        matlabbatch(3).spm.spatial.preproc.tissue(4).tpm = [
            "/Applications/spm12/tpm/TPM.nii,5"
        ]
        matlabbatch(3).spm.spatial.preproc.tissue(4).ngaus = 4
        matlabbatch(3).spm.spatial.preproc.tissue(4).native = Array.from_any([1, 0])
        matlabbatch(3).spm.spatial.preproc.tissue(4).warped = Array.from_any([0, 0])
        matlabbatch(3).spm.spatial.preproc.tissue(5).tpm = [
            "/Applications/spm12/tpm/TPM.nii,6"
        ]
        matlabbatch(3).spm.spatial.preproc.tissue(5).ngaus = 2
        matlabbatch(3).spm.spatial.preproc.tissue(5).native = Array.from_any([0, 0])
        matlabbatch(3).spm.spatial.preproc.tissue(5).warped = Array.from_any([0, 0])
        matlabbatch(3).spm.spatial.preproc.warp.mrf = 1
        matlabbatch(3).spm.spatial.preproc.warp.cleanup = 1
        matlabbatch(3).spm.spatial.preproc.warp.reg = Array.from_any(
            [0, 0.001, 0.5, 0.05, 0.2]
        )
        matlabbatch(3).spm.spatial.preproc.warp.affreg = "mni"
        matlabbatch(3).spm.spatial.preproc.warp.fwhm = 0
        matlabbatch(3).spm.spatial.preproc.warp.samp = 3
        matlabbatch(3).spm.spatial.preproc.warp.write = Array.from_any([0, 1])
        matlabbatch(3).spm.spatial.preproc.warp.vox = float("nan")
        matlabbatch(3).spm.spatial.preproc.warp.bb = Array.from_any(
            [
                [float("nan"), float("nan"), float("nan")],
                [float("nan"), float("nan"), float("nan")],
            ]
        )
        s1 = Runtime.call(
            "substruct",
            ".",
            "val",
            "{}",
            {4},
            ".",
            "val",
            "{}",
            {1},
            ".",
            "val",
            "{}",
            {1},
        )
        s2 = Runtime.call("substruct", ".", "fordef", "()", {":"})
        matlabbatch(4).spm.spatial.normalise.write.subj["def"][0] = cfg_dep(
            "Segment: Forward Deformations", s1, s2
        )
        s1 = Runtime.call(
            "substruct",
            ".",
            "val",
            "{}",
            {2},
            ".",
            "val",
            "{}",
            {1},
            ".",
            "val",
            "{}",
            {1},
        )
        s2 = Runtime.call("substruct", "()", {1}, ".", "files")
        matlabbatch(4).spm.spatial.normalise.write.subj.resample[0] = cfg_dep(
            "Slice Timing: Slice Timing Corr. Images (Sess 1)", s1, s2
        )
        matlabbatch(4).spm.spatial.normalise.write.woptions.bb = Array.from_any(
            [[-78, -112, -70], [78, 76, 85]]
        )
        matlabbatch(4).spm.spatial.normalise.write.woptions.vox = Array.from_any(
            [3, 3, 3]
        )
        matlabbatch(4).spm.spatial.normalise.write.woptions.interp = 4
        matlabbatch(4).spm.spatial.normalise.write.woptions.prefix = "w"
        s1 = Runtime.call(
            "substruct",
            ".",
            "val",
            "{}",
            {5},
            ".",
            "val",
            "{}",
            {1},
            ".",
            "val",
            "{}",
            {1},
            ".",
            "val",
            "{}",
            {1},
        )
        s2 = Runtime.call("substruct", "()", {1}, ".", "files")
        matlabbatch(5).spm.spatial.smooth.data[0] = cfg_dep(
            "Normalise: Write: Normalised Images (Subj 1)", s1, s2
        )
        matlabbatch(5).spm.spatial.smooth.fwhm = Array.from_any([6, 6, 6])
        matlabbatch(5).spm.spatial.smooth.dtype = 0
        matlabbatch(5).spm.spatial.smooth.im = 0
        matlabbatch(5).spm.spatial.smooth.prefix = "s"


if __name__ == "__main__":
    unittest.main()
